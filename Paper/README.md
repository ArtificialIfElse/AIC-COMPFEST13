## Periksa Topic Paper
---

Paper merupakan salah satu jenis karya ilmiah yang membahas topik tertentu dengan didukung data dan argumen yang valid dan kuat. Paper dapat diartikan sebagai ringkasan suatu penelitian. Secara umum, paper dituliskan sebanyak 6 halaman. [PenerbitBukuDeepPublish](https://penerbitbukudeepublish.com/pengertian-paper/)

Terdapat banyak sekali jenis paper. Pemodelan pada situs ini mengambil dataset utama dari [ARXIV data from 24,000+ papers](https://www.kaggle.com/neelshah18/arxivdataset) yang terdiri dari paper yang diterbitkan dalam rentang 1992 hingga 2017. Pelabelan paper ini kemudian diperkecil ke dalam enam kelas saja yaitu
    
    1. AI/ML
    2. Computer Vision
    3. Computer Science
    4. Math & Stats
    5. Physics
    6. Others

<p align="center">
  <img src="https://github.com/ArtificialIfElse/AIC-COMPFEST13/blob/main/Paper/res/paper.png" />
</p>

Untuk topik paper others karena jumlahnya yang terlalu tidak sebanding dengan data lain maka dilakukan droping sehingga menyisakan nomor 1 sampai 5 saja untuk mencegah terjadinya overfitting. 

Tujuan utama dari model ini yaitu membantu mahasiswa atau para peneliti yang kesulitan dalam menerka topik yang hendak dibawa oleh suatu paper. Inputan yang diperlukan untuk melakukan prediksi topik yaitu berupa abstraksi dari paper. Masih terdapat banyak kelemahan pada model ini, yaitu data paper hanya dapat melakukan klasifikasi seputar ilmu komputer