import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import warnings
from flask import jsonify
warnings.filterwarnings('ignore')
import base64
import io

def get_exact_value_of_questions(df):

    # Analisis Pertanyaan
    # EXT
    df['EXT1'] = df['EXT1'] * 1
    df['EXT2'] = df['EXT2'] * -1
    df['EXT3'] = df['EXT3'] * 1
    df['EXT4'] = df['EXT4'] * -1
    df['EXT5'] = df['EXT5'] * 1
    df['EXT6'] = df['EXT6'] * -1
    df['EXT7'] = df['EXT7'] * 1
    df['EXT8'] = df['EXT8'] * -1
    df['EXT9'] = df['EXT9'] * 1
    df['EXT10'] = df['EXT10'] * -1

    # ESP
    df['EST1'] = df['EST1'] * 1
    df['EST2'] = df['EST2'] * -1
    df['EST3'] = df['EST3'] * 1
    df['EST4'] = df['EST4'] * -1
    df['EST5'] = df['EST5'] * 1
    df['EST6'] = df['EST6'] * 1
    df['EST7'] = df['EST7'] * 1
    df['EST8'] = df['EST8'] * 1
    df['EST9'] = df['EST9'] * 1
    df['EST10'] = df['EST10'] * 1

    # AGR
    df['AGR1'] = df['AGR1'] * -1
    df['AGR2'] = df['AGR2'] * 1
    df['AGR3'] = df['AGR3'] * -1
    df['AGR4'] = df['AGR4'] * 1
    df['AGR5'] = df['AGR5'] * -1
    df['AGR6'] = df['AGR6'] * -1
    df['AGR7'] = df['AGR7'] * 1
    df['AGR8'] = df['AGR8'] * -1
    df['AGR9'] = df['AGR9'] * 1
    df['AGR10'] = df['AGR10'] * 1

    # CSN
    df['CSN1'] = df['CSN1'] * 1
    df['CSN2'] = df['CSN2'] * -1
    df['CSN3'] = df['CSN3'] * 1
    df['CSN4'] = df['CSN4'] * -1
    df['CSN5'] = df['CSN5'] * 1
    df['CSN6'] = df['CSN6'] * -1
    df['CSN7'] = df['CSN7'] * 1
    df['CSN8'] = df['CSN8'] * -1
    df['CSN9'] = df['CSN9'] * 1
    df['CSN10'] = df['CSN10'] * 1

    # OPN
    df['OPN1'] = df['OPN1'] * 1
    df['OPN2'] = df['OPN2'] * -1
    df['OPN3'] = df['OPN3'] * 1
    df['OPN4'] = df['OPN4'] * -1
    df['OPN5'] = df['OPN5'] * 1
    df['OPN6'] = df['OPN6'] * -1
    df['OPN7'] = df['OPN7'] * 1
    df['OPN8'] = df['OPN8'] * 1
    df['OPN9'] = df['OPN9'] * 1
    df['OPN10'] = df['OPN10'] * 1
    return df

def calculate_total_type(df):
    # Model
    col_list = list(df)
    ext = col_list[0:10]
    est = col_list[10:20]
    agr = col_list[20:30]
    csn = col_list[30:40]
    opn = col_list[40:50]

    # Classify --> Tambah 3 biar nilainya rentang 1-5
    df_total = pd.DataFrame()
    df_total['openness'] = (df[opn].sum(axis=1)/10) + 3
    df_total['conscientiousness'] = (df[csn].sum(axis=1)/10) + 3
    df_total['extroversion'] = (df[ext].sum(axis=1)/10) + 3
    df_total['agreeableness'] = (df[agr].sum(axis=1)/10) + 3
    df_total['neuroticism'] = (df[est].sum(axis=1)/10) + 3

    return df_total

def get_mbti(df_total):
    mbti = []

    if df_total['extroversion'].values >= 2.5:
        mbti.append('E')
    else:
        mbti.append('I')

    if df_total['openness'].values >= 2.5:
        mbti.append('N')
    else:
        mbti.append('S')

    if df_total['conscientiousness'].values >= 2.5:
        mbti.append('F')
    else:
        mbti.append('T')

    if df_total['agreeableness'].values >= 2.5:
        mbti.append('J')
    else:
        mbti.append('P')

    if df_total['neuroticism'].values >= 2.5:
        mbti.append('-A')
    else:
        mbti.append('-T')

    return "".join(mbti)

def get_advice_from_ocean(df_total):
    advice = []
    if df_total.openness.values >= 2.5:
        advice.append("Berdasarkan nilai opennessmu, kamu cenderung memiliki sifat \
yang terbuka terhadap cara berpikir baru dan mau \
menerima konsep-konsep baru. Umumnya keputusan yang kamu \
ambil tidak konservatif")
    else:
        advice.append("Berdasarkan nilai opennessmu, kamu cenderung memiliki sifat \
yang kurang inovatif, tetapi kelebihan dirimu terletak pada \
kekonsistenanmu. Kamu cenderung bersikap praktis dan cenderung \
tertutup")

    # conscientiousness
    if df_total.conscientiousness.values >= 2.5:
        advice.append("Berdasarkan nilai conscientiousnessmu, kamu cenderung memiliki sifat \
suka bekerja keras dan memiliki tenggat target yang terencana, kamu cenderung \
rajin dan cermat dalam melakukan segala hal")
    else:
        advice.append("Berdasarkan nilai conscientiousnessmu, kamu cenderung memiliki sifat \
yang kurang rajin dan terkesan ceroboh, jika kamu masih memiliki sifat ini \
mungkin ada baiknya kamu melakukan introspeksi diri supaya menjadi pribadi \
lebih baik di masyarakat")

    #  extroversion
    if df_total.extroversion.values >= 2.5:
        advice.append("Berdasarkan nilai extroversionmu kamu cenderung masuk ke dalam \
karakter extrovert, dimana kamu lebih suka berkumpul dengan orang lain untuk \
melakukan interaksi ataupun aktivitas lainnya")
    else:
        advice.append("Berdasarkan nilai extroversionmu kamu cenderung masuk ke dalam \
karakter introvert, dimana kamu lebih cenderung tertutup dan hanya memiliki \
hubungan terbatas pada beberapa orang saja")

    # agreeableness
    if df_total.agreeableness.values >= 2.5:
        advice.append("Berdasarkan nilai agreeableness yang kamu miliki, dirimu \
cenderung bersifat bersifat positif dan menghargai nilai orang lain, \
dirimu juga suka menolong orang lain")
    else:
        advice.append("Berdasarkan nilai agreeableness yang kamu miliki, dirimu \
cenderung bersifat teguh pada pendirian dan lebih mementingkan diri sendiri \
hal ini tidak selalu buruk, tetapi sebagai pemilik sifat ini kamu mungkin perlu \
untuk mulai memperbaiki diri dengan mendengarkan orang lain")

    # neuroticism
    if df_total.neuroticism.values >= 2.5:
        advice.append("Berdasarkan nilai neuroticism yang kamu miliki, dirimu \
mungkin sering merasa tidak beruntung apabila dibandingkan terhadap \
dunia luar, hal ini dikarenakan sifat neuroticism yang kamu miliki\
membuat kondisi emosimu kurang stabil")
    else:
        advice.append("Berdasarkan nilai neuroticism yang kamu miliki, dirimu \
cenderung memiliki kestabilan emosi yang baik sehingga tidak mudah stres")
    
    return advice

def get_recommendation_major(mbti):
    mbti_split = mbti.split('-')[0]
    mapping_mbti = {
        "ISTJ": "Program studi yang sesuai denganmu ialah Manajemen, Pendidikan Kepolisian, Ilmu Hukum, Kedokteran, Akuntansi  dan Sistem Informasi (Manajemen Informatika).",
        "ISFJ": "Program studi yang sesuai denganmu ialah Arsitektur , Ilmu Keperawatan, Administrasi Perkantoran (Kesekretariatan), Pendidikan Bimbingan Konseling dan Ilmu Perpustakaan.",
        "ESTJ": "Program studi yang sesuai denganmu ialah Pendidikan Militer, akademi polisi, ilmu hukum, akuntansi dan Ekonomi.",
        "ESFJ": "Program studi yang sesuai denganmu ialah finance, Ilmu Keperawatan, Pendidikan Bimbingan Konseling dan kesekretariatan.",
        "ISTP": "Program studi yang sesuai denganmu ialah Kriminologi, Teknik Informatika, teknik, Penerbang (Pendidikan Pilot) dan Ilmu Keolahragaan.",
        "ISFP": "Program studi yang sesuai denganmu ialah desain, Seni Rupa (Creative Arts), Psikologi, bimbingan konseling dan pendidikan guru.",
        "ESTP": "Program studi yang sesuai denganmu ialah Manajemen Pemasaran (Marketing), bisnis dan ilmu ekonomi.",
        "ESFP": "Program studi yang sesuai denganmu ialah Manajemen Perhotelan, Pariwisata, seni rupa dan desain.",
        "INTJ": "Program studi yang sesuai denganmu ialah ilmu-ilmu eksak seperti matematika, fisika, kimia dan sebagainya. Selain itu, kamu juga cocok dalam program studi Arsitektur, teknik dan Statistika.",
        "ENTJ": "Program studi yang sesuai untukmu ialah Ilmu Hukum, Ilmu Komunikasi , Manajemen  dan bisnis.",
        "INTP": "Program studi yang sesuai untukmu ialah ilmu sains, Filsafat, Ilmu Hukum, Psikologi dan juga Arsitektur.",
        "ENTP": "Program studi yang sesuai untukmu ialah Ilmu Hukum, Manajemen Pemasaran (Marketing) dan konsultan.",
        "INFJ": "Program studi yang sesuai untukmu ialah pendidikan guru, Psikologi, Pendidikan Dokter dan juga Pendidikan Bimbingan Konseling.",
        "INFP": "Program studi yang sesuai untukmu ialah Jurnalistik, sastra, pendidikan, Seni Rupa (Creative Arts) dan agama.",
        "ENFJ": "Program studi yang sesuai denganmu ialah Akuntansi, Ilmu Keperawatan, Pendidikan Bimbingan Konseling  dan Administrasi Perkantoran (Kesekretariatan)",
        "ENFP": "Program studi yang sesuai dengan kepribadianmu adalah Ilmu Komunikasi, Psikologi, Pendidilkan, Hubungan Internasional, Jurnalistik  dan Hubungan Masyarakat."
    }

    return mapping_mbti[mbti_split]


def extract_personality_model(data):
    soal = ['EXT1', 'EXT2', 'EXT3', 'EXT4', 'EXT5', 'EXT6', 'EXT7', 'EXT8', 'EXT9', 'EXT10', 'EST1', 'EST2', 'EST3', 'EST4', 'EST5', 'EST6', 'EST7', 'EST8', 'EST9', 'EST10', 'AGR1', 'AGR2', 'AGR3', 'AGR4', 'AGR5',
            'AGR6', 'AGR7', 'AGR8', 'AGR9', 'AGR10', 'CSN1', 'CSN2', 'CSN3', 'CSN4', 'CSN5', 'CSN6', 'CSN7', 'CSN8', 'CSN9', 'CSN10', 'OPN1', 'OPN2', 'OPN3', 'OPN4', 'OPN5', 'OPN6', 'OPN7', 'OPN8', 'OPN9', 'OPN10']

    # Pertanyaan rentang 1-5 (diganti -2, -1, 0, 1, 2)
    for i in range(0, len(data)):
        data[i] = int(data[i])
    answer = data

    df = pd.DataFrame(answer, index=soal)
    df = df.T

    df = get_exact_value_of_questions(df)

    df_total = calculate_total_type(df)

    mbti = get_mbti(df_total)

    advice = get_advice_from_ocean(df_total)

    recommendation_major = get_recommendation_major(mbti)
    data = {
        'mbti': mbti,
        'advice': advice,
        'recommendation_major': recommendation_major,
        'graph_plot': {
            'agreeableness': df_total['agreeableness'][0],
            'extroversion': df_total['extroversion'][0],
            'conscientiousness': df_total['conscientiousness'][0],
            'neuroticism': df_total['neuroticism'][0],
            'openness': df_total['openness'][0],
        }
    }

    return data