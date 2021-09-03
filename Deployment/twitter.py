from flask import Blueprint, json, render_template, jsonify, request
import pickle
from get_tweet import *
import re

twitter = Blueprint('twitter',__name__)

# graduation page
@twitter.route("/twitter")
def twitter_index():
    data = {
        "title": "Prediksi lewat username twitter"
    }
    return render_template("twitter/index.html", data=data)

@twitter.route("/twitter/predict", methods=["POST"])
def twitter_predict():
    username = request.form["username"]

    if re.match('^[a-zA-Z0-9_]+$', username): 

        try:
            result = search_trait(username)
        except:
            data = {
                "title": "Prediksi lewat username twitter",
                "prediction": "Username tidak ditemukan",
                "is_found": False
            }
            return render_template("twitter/predict.html", data=data)
        data = {
            "title": "Prediksi lewat username twitter",
            "prediction": result,
            "is_found": True,
            "advice": getAdvice(result),
            "friendship": getFriendshipAdvice(result),
            "image_url": getImageUrl(result)
        }
    else:
        data = {
                "title": "Prediksi lewat username twitter",
                "prediction": "Username tidak ditemukan",
                "is_found": False
            }
    return render_template("twitter/predict.html", data=data)

@twitter.route("/api/v1/twitter/predict", methods=["POST"])
def api_twitter_predict():
    try:
        if request.get_json() is None or request.get_json()['username'] is None:
            data = {
                "status": False,
                "response_code": 400,
                "message": "Bad Request"
            }

            return jsonify(data)
        
        if re.match('^[a-zA-Z0-9_]+$', request.get_json()['username']):

            username = request.get_json()['username']
            try:
                result = search_trait(username)
            except:
                data = {
                    "status": False,
                    "response_code": 404,
                    "message": "Username Not Found",
                    "is_found": False,
                    "personality": ""
                }

                return jsonify(data)

            data = {
                    "status": True,
                    "response_code": 200,
                    "message": "Success Predict Personality by username twitter",
                    "is_found": True,
                    "advice": getAdvice(result),
                    "friendship": getFriendshipAdvice(result),
                    "image_url": getImageUrl(result)
                }

            return jsonify(data)
        
        data = {
            "status": False,
            "response_code": 400,
            "message": "Bad Request"
        }
        return jsonify(data)
    except KeyError:
        data = {
                "status": False,
                "response_code": 400,
                "message": "Bad Request"
            }
        return jsonify(data)


def getAdvice(result):
    mappingAdvice = {
        "ISTJ": "ISTJ adalah seorang perencana, suka merencanakan segala hal dengan hati-hati sebelum melakukan sesuatu. \
Seseorang dengan karakteristik ini umumnya memiliki sikap bertanggung jawab dan realistis. Hal lain \
yang menjadi ciri dari kepribadian ini yaitu kepatuhannya pada \
tradisi dan hukum yang berlaku.",
        "ISTP": "ISTP adalah orang yang berorientasi pada hasil, ketika muncul permasalahan, orang bertipe ini ingin cepat \
memahami permasalahan tersebut dan memahami penyebab yang mendasarinya untuk kemudian menerapkan beberapa jenis solusi. \
Orang bertipe ini juga menikmati pengalaman baru yang menantang serta berisiko. Hal lain dari orang bertipe ini yaitu sering \
digambarkan pendiam tetapi santai terhadap orang lain.  ISTP tidak terbiasa dengan keadaan emosional orang lain dan kadang \
terlihat tidak peka.  Kelebihan yang dimiliki orang bertipe ini yaitu pandai menjaga kepala tetap dingin dan bersifat objektif \
dalam mengatasi suatu krisis.",
        "ISFJ": "ISFJ adalah orang yang memiliki kemampuan yang baik dalam memahami perasaan orang lain. \
Orang bertipe ini pandai dalam memahami perasaan dirinya juga tetapi cenderung untuk memendamnya karena tidak suka membebani \
orang lain. Seorang ISFJ umumnya lebih menyukai praktik daripada penjelasan teori untuk itu mereka lebih senang \
bekerja sambil belajar. Sebagai tambahan, orang bertipe ini cenderung untuk bersifat konsisten dan menikmati kehidupan \
yang terstruktur. ",
        "ISFP": "ISFP adalah orang yang cenderung mempertahankan opsi sebanyak-banyaknya terbuka sehingga seringkali \
membuat mereka menunda-nunda hingga pilihan terbaru yang menurutnya terbaik muncul. Sesuai dengan sifatnya yang \
introvert orang bertipe ini cenderung lebih memilih berbaur dengan kelompok kecil. Meskipun pendiam ISFP sering dikenal \
sebagai orang yang suka berdamai, peduli, dan perhatian. ISFP juga fokus pada detail, orang bertipe ini jarang mengkhawatirkan \
masa depan karena lebih fokus pada hal yang ada sekarang dan saat ini. Karakteristik terakhir, orang ini lebih menyukai kerja \
praktik daripada teori abstrak.",
        "INTJ": "INTJ adalah orang yang cenderung bersifat introvert dan memilih untuk bekerja sendiri. INTJ suka melihat gambaran \
besar dan suka berfokus pada informasi secara abstrak daripada detail. Orang bertipe ini cenderung bersifat objektif daripada \
subjektif serta orang bertipe ini lebih menyukai kehidupan yang dilaluinya teratur sehingga mereka lebih suka melakukan perencanaan \
dengan sungguh-sungguh.",
        "INTP": "INTP adalah orang yang cenderung pendiam, bijaksana, dan lebih memilih bergaul dalam kelompok kecil. Orang \
bertipe ini senang memikirkan konsep teoritis dan cenderung menghargai kecerdasan daripada perasaan. Dalam melakukan analisis \
dan membuat keputusan, orang bertipe ini cenderung sangat logis dan objektif. Karakteristik lain yang dimiliki yaitu sifatnya \
yang fleksibel dan pandai berfikir ‘out of the box’. INTP lebih memilih memikirkan gambaran besar daripada fokus pada detail kecil. \
Orang bertipe ini cenderung mempertahankan pilihan tetap terbuka dan merasa dibatasi oleh struktur dan perencanaan.",
        "INFJ": "INFJ adalah seseorang yang cenderung bersikap welas asih, suka menolong, idealis, terorganisir, dan memiliki \
sikap emosional dan logis yang baik. Orang bertipe ini dapat bersikap lembut tetapi bukan penurut dan juga dapat bersikap \
tegas untuk memperoleh yang diinginkan. Meskipun bersifat introvert, orang bertipe ini cenderung suka menolong tetapi memerlukan \
waktu untuk sendiri. Orang INFJ tidak hanya berbicara tentang impian mereka mewujudkan impiannya. Orang bertipe ini cenderung suka \
merencanakan segala sesuatu sedini mungkin dimana keputusannya lebih ditekankan pada perasaan mereka tetapi tidak menutup kemungkinan \
untuk bersifat objektif pada hal yang dipilihnya.",
        "INFP": "INFP adalah orang yang cenderung memiliki kepribadian pendiam, tertutup, dan cenderung memilih berbaur \
pada grup yang berupa teman dekat. Orang bertipe ini memiliki fokus pada gambaran besar daripada detail kecil. Kecenderungan \
orang bertipe ini yaitu lebih memfokuskan pada perasaan dibandingkan objektivitas. Dalam hal pengambilan keputusan, INFP lebih \
memilih untuk memiliki opsi terbanyak dan ketika harus memutuskan, lebih menekankan pada perasaan dibandingkan logika.",
        "ESTP": "ESTP adalah orang yang memiliki kecenderungan untuk mengambil keputusan dengan cepat baru kemudian melakukan \
improvisasi daripada melakukan perencanaan yang terlalu lama. ESTP lebih menyukai kerja praktik daripada pemahaman abstrak, \
selain itu juga memiliki kemampuan yang baik dalam kehidupan sosial. Terkadang, orang berkepribadian ini bersikap impulsif yang \
kadang dapat membuatnya kecewa.",
        "ESTJ": "ESTJ adalah orang yang memiliki kecenderungan untuk menjaga nilai yang tinggi pada tradisi, aturan, dan \
keamanan. Orang bertipe ini cenderung berhasil meraih posisi kepemimpinan yang baik. Kepercayaan diri yang dimiliki orang \
ini tinggi, tetapidapat menjadi terlalu kritis ketika orang lain gagal memenuhi standar tinggi mereka. Secara umum, orang bertipe \
ini sangat terbuka dan dan jujur dalam berbagi pendapat tetapi terkadang terlihat kasar atau terlalu kritis.",
        "ESFP": "ESFP adalah orang yang memiliki kecenderungan sangat praktis dan penuh ide. Orang bertipe ini tidak suka pembelajaran \
berbasis buku dan diskusi teori untuk itu dalam hal pendidikan tradisional orang bertipe ini tidak ahli, tetapi ketika \
perlu interaksi dengan orang lain, ESFP adalah ahlinya. Orang bertipe ESFP cenderung tidak menyukai rutinitas dan lebih \
menikmati pengalaman baru. Karakteristik lain orang bertipe ini yaitu kemampuannya untuk merasakan hal yang dirasakan oleh orang \
lain dan pintar dalam memberikan tanggapan, oleh karenanya ESFP sering dikenal sebagai orang yang hangat, simpatik, dan santai.",
        "ESFJ": "ESFJ adalah orang yang memiliki kecenderungan untuk membantu orang lain, tetapi disisi lain mereka \
memerlukan adanya pengakuan dan apresiasi orang lain dalam kebaikannya. Memiliki kepekaan yang baik terhadap kebutuhan dan perasaan \
orang lain. Orang bertipe ini mudah terluka pada ketidakbaikan dan sikap apatis. ESFJ dalam melakukan kebaikan berdasarkan sumber yang \
diakui oleh masyarakat luas dibandingkan dengan pedoman instrinsik, etika, dan moral.",
        "ENFP": "ENFP adalah orang yang memiliki keterampilan yang sangat baik, selain memiliki antusiasme yang tinggi, \
orang bertipe ini juga peduli dengan orang lain dan pandai dalam memahami hal yang dirasakan orang lain. Orang bertipe ini memiliki \
semangat, karisma, dan kreativitas yang baik. Sifat mereka menjadikan dirinya sebagai pemimpin yang hebat. Sifat lain yang dimiliki orang \
bertipe ini yaitu mudah terganggu pada hal yang tidak menarik baginya selain itu suka membiarkan pilihan terbuka supaya tetap fleksibel dan \
juga orang dengan karakteristik ini tidak menyukai rutinitas tetapi sering menunda tugas penting hingga mendekati deadline.",
        "ENFJ": "ENFJ adalah orang yang memiliki kecenderungan extrovert dengan bahagia menikmati waktu dengan orang lain. \
Orang bertipe ini sering dikenal sebagai orang yang hangat, penyayang, dan suportif. ENFJ hebat dalam mendorong orang lain memperoleh \
kepuasan pribadi. Orang bertipe ENFJ memiliki kemampuan yang baik dalam memahami perasaan orang lain, tetapi sering kali menyalahkan diri \
sendiri ketika terjadi ketidaksesuaian. Kemampuan ENFJ yang dapat menghubungkan jenis orang yang beragam dapat menjadikannya pemimpin yang mampu \
memberikan semangat dan inspirasi bagi kelompok.",
        "ENTP": "ENTP adalah orang yang memiliki kecenderungan berinteraksi pada banyak orang. Mereka adalah pembicara hebat \
yang suka mengajak orang lain ke dalam perdebatan. Orang bertipe ini berfokus pada masa depan dan sering kali projek yang dimulainya \
tidak pernah selesai karena fokusnya pada gambaran besar. Orang bertipe ENTP cenderung menunggu daripada mengambil keputusan. Orang bertipe \
ini mudah memahami hal baru dengan cukup cepat.",
        "ENTJ": "ENTJ adalah orang yang cenderung bahagia bersama dengan orang lain. Memiliki kemampuan verbal yang tinggi dan \
menjadi bersemangat dengan berinteraksi dengan orang lain. Orang bertipe ini lebih memikirkan masa depan daripada pada waktu saat ini \
dan sekarang. Dalam pengambilan keputusan orang ENTJ cenderung bersifat objektif dan logis, perasaan tidak terlalu mempengaruhi pilihan mereka. \
ENTJ secara alami adalah seoarang perencana yang membuat keputusan dan melakukan perencanaan yang baik. Sifat yang dimilikinya menjadikannya sebagai seorang \
pemimpin yang mampu berfokus pada pemecahan masalah secara efisien.",
    }

    return mappingAdvice[result]

def getFriendshipAdvice(result):
    mappingFriendshipAdvice = {
        "ISTJ": "Orang dengan kepribadian ISTJ senang bersama teman yang memiliki kemiripan dengannya. Meskipun terkadang orang tipe ini \
terlihat serius, mereka sebenarnya juga suka bersenang-senang. ISTJ jarang suka mengeksplorasi hal baru, untuk menjadi teman yang baik dengan \
menemaninya melakukan hobby atau aktivitas yang disukainya.",
        "ISTP": "Orang dengan kepribadian ISTP cenderung bersifat ingin tahu dan suka bertualang. Tetapi, terkadang orang berkepribadian \
ini memiliki keinginan untuk menyendiri. Untuk menjadi teman yang baik dengan orang seperti ini yaitu dengan mengajaknya untuk mencoba petualangan \
baru tetapi ketika orang tersebut enggan tetap menghormatinya karena dirinya butuh kesendirian.",
        "ISFJ": "Orang bertipe ISFJ sering bersikap mudah bergaul dan berbaur dengan orang lain, tetapi untuk membuka diri, orang ini perlu \
benar-benar tahu karakteristik orang lain. Untuk menjadi teman baik dapat didukung dengan menerima diri mereka dan memahami kapan waktu mereka \
ingin sendiri.",
        "ISFP": "Orang bertipe ISFP mudah dikenali dengan sifatnya yang hangat dan tidak terlalu mengutamakan ego diri mereka. Meskipun \
demikian, mereka sering kesulitan dalam mengekspresikan hal yang dirasakannya untuk itu untuk menjadi teman yang baik dapat dilakukan dengan \
mengajaknya bersikap terbuka dalam berbagi perasaan dan berusaha untuk memahami kebutuhannya serta memahami kapan waktu mereka ingin sendiri karena \
jika dilanggar sering orang bertipe ini lebih menutup diri.",
        "INTJ": "Orang bertipe INTJ cenderung suka menyendiri dan bersifat mandiri. Jadi untuk menjalin pertemanan dengan orang bertipe ini \
terkadang memang sulit karena orang ini sangat berorientasi pada masa depan dan menganggap persahabatan jangka panjang tidak bermanfaat. Hal baik \
dari sifat ini, INTJ hanya memiliki sedikit teman yang mana pertemanan tersebut akan sangat dekat. Untuk menjadi teman yang baik yaitu dengan bersabar \
dalam menghadapi sikapnya.",
        "INTP": "Orang bertipe INTP sangat terlihat dalam pembicaraannya yang lebih menyukai berbagi kesamaan. Mereka cenderung menghargai \
pengetahuan dari hal lainnya, hal ini yang menjadi penyebab sulitnya dalam membentuk pertemanan dengan orang bertipe ini. Untuk menjadi teman yang \
baik, orang bertipe ini bukanlah orang yang pandai dalam mengatasi emosi berlebihan tetapi mudah terjalin dalam topik pembicaraan yang mendalam dan \
berbagi perasaan.",
        "INFJ": "Orang bertipe INFJ cenderung tertutup dan terkadang sulit untuk dipahami. Mereka menempatkan nilai yang tinggi pada hubungan \
yang dekat dan mudah terluka, meskipun demikian orang bertipe ini cenderung memilih untuk menyembunyikan perasaannya.  Untuk menjadi teman yang baik \
dapat dilakukan dengan meluangkan waktu untuk memahami perspektif dan kekuatan mereka.",
        "INFP": "Orang bertipe INFP hanya memiliki hubungan dengan orang yang sedikit, tetapi hubungan tersebut bertahan lama. Orang bertipe \
ini mahir dalam memahami emosi orang lain tetapi terkadang sulit untuk berbagi perasaan. Untuk menjadi teman yang baik umumnya memerlukan waktu dan \
usaha yang banyak, tetapi apabila berhasil dapat menjalin hubungan yang bertahan lama.",
        "ESTP": "Orang bertipe ESTP sangat menyukai petualangan, untuk menjadi teman yang baik salah satunya dengan selalu siap ketika diajak \
mencoba pengalaman baru. Selain itu, juga dapat dengan memberikan ide melakukan suatu hal yang baru bersama orang bertipe ini.",
        "ESTJ": "Orang bertipe ESTJ memiliki kemampuan sosial yang baik dan suka mengajak orang lain beraktivitas sesuai yang dia sukai. Untuk \
menjadi teman yang baik dapat dilakukan dengan bersikap stabil stabil yang berpegang teguh pada komitmen bersama. Dari hal tersebut, dapat membangun \
persahabatan yang baik dengan orang bertipe ini.",
        "ESFP": "Orang bertipe ESFP cenderung tidak menyukai hal yang bersikap rutinitas, mereka lebih menyukai petualangan baru. Untuk menjadi \
teman yang baik dapat dilakukan dengan selalu siap ketika diajak mencoba pengalaman baru seperti mengeksplorasi tempat baru atau bertemu dengan \
orang baru. Kunci pertemanan dengan orang bertipe ini yaitu dengan menjaga segala sesuatu menarik.",
        "ESFJ": "Orang bertipe ESFJ mampu bersikap tanpa pamrih untuk membuat orang lain bahagia. Orang bertipe ini memiliki kemampuan bergaul \
paling baik dengan orang-orang yang menghargai mereka. Untuk menjadi teman yang baik dengan orang bertipe ini dapat dilakukan dengan mengungkapkan \
penghargaan atas sifat mereka yang memberi dan memastikan bahwa kita membalas kebaikan mereka",
        "ENFP": "Orang bertipe ENFP sering digambarkan sebagai orang yang menyenangkan dan mengasyikan. Orang bertipe ini sering melakukan hal \
yang baru dan biasanya memiliki banyak kenalan. Kelebihan ENFP yaitu peka terhadap perasaan orang lain dengan lebih cepat. Untuk menjadi teman yang \
baik orang bertipe ini dengan memberikan dukungan orang ini dalam mencapai tujuannya.",
        "ENFJ": "Orang bertipe ENFJ sering digambarkan sebagai orang yang menyenangkan dan mengasyikan. Orang bertipe ini sering melakukan hal \
yang baru dan biasanya memiliki banyak kenalan. Kelebihan ENFP yaitu peka terhadap perasaan orang lain dengan lebih cepat. Untuk menjadi teman yang \
baik orang bertipe ini dengan memberikan dukungan orang ini dalam mencapai tujuannya.",
        "ENTP": "Orang bertipe ENTP memiliki kemampuan dalam bergaul dalam setiap tipe kepribadian, meskipun umumnya bersikap santai, orang bertipe \
ini dapat sangat kompetitif. Untuk menjadi teman yang baik, perlu untuk berhati-hati dan tidak berusaha untuk saling mengalahkan. Menyadari kecintaan \
mereka pada perdebatan, tetapi berhati-hati untuk tidak meningkatkan diskusi menjadi argumen yang agresif.",
        "ENTJ": "Orang bertipe ENTJ secara umum menyukai percakapan yang menarik, terkadang orang ini terlihat argumentative dan konfrontatif tetapi \
hal itu merupakan bagian dari  gaya komunikasi mereka. Orang bertipe ini cenderung mudah menjalin persahabatan dengan orang yang memiliki minat dan \
pandangan yang sama. Orang bertipe ini tidak mudah dalam memahami orang yang sangat tertutup, sensitive, atau emosional. Untuk dapat berteman baik dengan \
orang bertipe ini dapat dilakukan dengan berusaha untuk terbuka dan bersikap santai terhadap ucapan dari ENTJ yang kadang terdengar agresif.",
    }

    return mappingFriendshipAdvice[result]

def getImageUrl(result):
    mappingImage = {
        "ENFJ" : "https://raw.githubusercontent.com/ArtificialIfElse/AIC-COMPFEST13/main/Kepribadian/res/ENFJ.png",
        "ENFP" : "https://raw.githubusercontent.com/ArtificialIfElse/AIC-COMPFEST13/main/Kepribadian/res/ENFP.png",
        "ENTJ" : "https://raw.githubusercontent.com/ArtificialIfElse/AIC-COMPFEST13/main/Kepribadian/res/ENTJ.png",
        "ENTP" : "https://raw.githubusercontent.com/ArtificialIfElse/AIC-COMPFEST13/main/Kepribadian/res/ENTP.png",
        "ESFJ" : "https://raw.githubusercontent.com/ArtificialIfElse/AIC-COMPFEST13/main/Kepribadian/res/ESFJ.png",
        "ESFP" : "https://raw.githubusercontent.com/ArtificialIfElse/AIC-COMPFEST13/main/Kepribadian/res/ESFP.png",
        "ESTJ" : "https://raw.githubusercontent.com/ArtificialIfElse/AIC-COMPFEST13/main/Kepribadian/res/ESTJ.png",
        "ESTP" : "https://raw.githubusercontent.com/ArtificialIfElse/AIC-COMPFEST13/main/Kepribadian/res/ESTP.png",
        "INFJ" : "https://raw.githubusercontent.com/ArtificialIfElse/AIC-COMPFEST13/main/Kepribadian/res/INFJ.png",
        "INFP" : "https://raw.githubusercontent.com/ArtificialIfElse/AIC-COMPFEST13/main/Kepribadian/res/INFP.png",
        "INTJ" : "https://raw.githubusercontent.com/ArtificialIfElse/AIC-COMPFEST13/main/Kepribadian/res/INTJ.png",
        "INTP" : "https://raw.githubusercontent.com/ArtificialIfElse/AIC-COMPFEST13/main/Kepribadian/res/INTP.png",
        "ISFJ" : "https://raw.githubusercontent.com/ArtificialIfElse/AIC-COMPFEST13/main/Kepribadian/res/ISFJ.png",
        "ISFP" : "https://raw.githubusercontent.com/ArtificialIfElse/AIC-COMPFEST13/main/Kepribadian/res/ISFP.png",
        "ISTJ" : "https://raw.githubusercontent.com/ArtificialIfElse/AIC-COMPFEST13/main/Kepribadian/res/ISTJ.png",
        "ISTP" : "https://raw.githubusercontent.com/ArtificialIfElse/AIC-COMPFEST13/main/Kepribadian/res/ISTP.png",
    }

    return mappingImage[result]