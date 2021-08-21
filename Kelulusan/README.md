# Model Prediksi Predikat Kelulusan

Pada model ini dilakukan pembuatan model untuk melakukan prediksi predikat kelulusan seorang mahasiswa. Prediksi predikat kelulusan ini dapat digunakan baik mahasiswa yang menjalani pendidikan diploma maupun sarjana. 

## Rujukan

Dasar yang digunakan mengacu pada [Keputusan Rektor Universitas Indonesia](http://repository.ui.ac.id/dokumen/lihat/4236.pdf), pada pasal 23 ayat 1 sampai 4. Rujukan ini tidak ada kaitannya terhadap suatu universitas tertentu, tetapi hanya dijadikan dasar sebab kampus Universitas Indonesia merupakan salah satu perguruan tinggi terbaik di [Indonesia](https://www.kompas.com/edu/read/2021/06/05/082452171/ui-peringkat-atas-kampus-terbaik-indonesia-versi-the-2021?page=all)

<p align="center">
  <img src="https://github.com/ArtificialIfElse/AIC-COMPFEST13/blob/main/Kelulusan/Rujukan/dasar.png" />
</p>

Pemilihan standar yang tinggi ini diharapkan menjadi pacuan bagi mahasiswa lain untuk memperoleh nilai IPK terbaik disetiap semesternya. Sehingga kelak dapat bersaing baik dalam kancah nasional maupun internasional.

## Step 1 - Mencari Algoritma Terbaik

Pada langkah ini dilakukan pemilihan algoritma machine learning yang paling sesuai untuk kasus ini. Pada tahap ini dilakukan perbandingan empat algoritma standar machine learning yaitu `Decision Tree`, `KNN`, `SVM`, dan `Random Forest`. Dari perbandingan ini diperoleh bahwa algoritma SVM memiliki nilai akurasi terbaik dibanding tiga algoritma lainnya.

1. Perbandingan Alogritma Pada Model Diploma
<p align="center">
  <img src="https://github.com/ArtificialIfElse/AIC-COMPFEST13/blob/main/Kelulusan/Step%201%20-%20Mencari%20Algoritma%20Terbaik/Gambar%20Perbandingan%20Model/Perbandingan%20Model%20Diploma.png" />
</p>

2. Perbandingan Alogritma Pada Model Sarjana
<p align="center">
  <img src="https://github.com/ArtificialIfElse/AIC-COMPFEST13/blob/main/Kelulusan/Step%201%20-%20Mencari%20Algoritma%20Terbaik/Gambar%20Perbandingan%20Model/Perbandingan%20Model%20Sarjana.png" />
</p>

Setelah mengetahui algoritma SVM adalah yang terbaik, maka dalam pembuatan model ini dipergunakan algoritma SVM

## Step 2 - Prediksi SVM untuk Sarjana

Pada langkah ini dilakukan pembuatan model untuk prediksi predikat kelulusan sarjana. Tahap ini menghasilkan 3 buah model prediksi untuk melakukan prediksi dengan input 5, 6, dan 7 nilai.


## Step 3 - Prediksi SVM untuk Diploma

Pada langkah ini dilakukan pembuatan model untuk prediksi predikat kelulusan diploma. Tahap ini menghasilkan 3 buah model prediksi untuk melakukan prediksi dengan input 3, 4, dan 5 nilai.

---

Demikian penyusunan laporan untuk model pertama, selanjutnya model yang dihasilkan akan dialihkan pada bagian [deployment](https://github.com/ArtificialIfElse/AIC-COMPFEST13/tree/main/Deployment) untuk diproses.
