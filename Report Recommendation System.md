# Laporan Proyek Machine Learning - Hairul Yasin

## *Sistem Rekomendasi Buku*

## Project Overview
Membaca buku adalah kunci penting untuk meningkatkan literasi dan pengetahuan, namun di Indonesia, minat baca masih sangat rendah, dengan indeks hanya sekitar 0,001 menurut UNESCO. Salah satu tantangan utamanya adalah kesulitan menemukan buku yang sesuai dengan preferensi individu karena banyaknya pilihan yang tersedia. Dataset _goodbooks-10k_ dari Kaggle, yang mencakup 10.000 buku beserta rating dan ulasan pengguna, digunakan untuk membangun sistem rekomendasi berbasis _machine learning_. Sistem ini menggunakan metode _Content-Based_ dan _Collaborative Filtering_ untuk membantu pembaca menemukan buku yang relevan dan menarik, sehingga diharapkan dapat mendorong peningkatan minat baca dan literasi. Dengan menggunakan model rekomendasi yang tepat, diharapkan dapat mempermudah pembaca dalam menemukan buku yang sesuai dengan minat mereka, menjadikan proses pencarian lebih cepat dan efisien, serta memberikan kontribusi positif terhadap budaya membaca di masyarakat.

## Business Understanding
Proyek ini bertujuan untuk membangun sistem rekomendasi buku yang dapat meningkatkan minat baca dengan menyediakan rekomendasi buku yang sesuai dengan preferensi dan kebutuhan pembaca.

### Problem Statements
1. Bagaimana cara membangun sistem rekomendasi buku berdasarkan kriteria pembaca menggunakan _Content-Based Filtering_?
2. Bagaimana cara membangun sistem rekomendasi buku yang disukai berdasarkan rating menggunakan _Collaborative Filtering_?

### Goals
1. Menyediakan rekomendasi buku yang sesuai dengan kriteria pembaca atau buku serupa menggunakan _Content-Based Filtering_.
2. Menyediakan rekomendasi buku yang belum dibaca atau mungkin disukai pembaca menggunakan _Collaborative Filtering_.

#### Solution Statements
1. **_Content-Based Filtering_:**
- **Metode**: Sistem akan menggunakan teknik _Term Frequency-Inverse Document Frequency (TF-IDF)_ dan _cosine similarity_ untuk mengukur kemiripan antara deskripsi buku, genre, dan metadata lainnya.
- **Output**: Sistem ini akan merekomendasikan top 5 buku yang memiliki kemiripan konten paling tinggi dengan buku yang diinput oleh pengguna.
- **Detail Rekomendasi**: Buku-buku yang direkomendasikan akan memiliki skor kemiripan minimal 0.7 pada skala 0 hingga 1, yang menunjukkan bahwa buku-buku tersebut memiliki konten yang sangat relevan dengan preferensi pembaca.

2. **_Collaborative Filtering_:**
- **Metode**: Menggunakan _model embedding_ seperti _RecommenderNet_ yang diimplementasikan dengan Keras, sistem ini akan memprediksi buku yang akan disukai pengguna berdasarkan pola rating pengguna lain yang memiliki preferensi serupa.
_Output_: Sistem akan merekomendasikan top 10 buku yang memiliki rating tinggi yang belum pernah dibaca oleh pengguna.
- **Detail Rekomendasi**: Buku yang direkomendasikan memiliki rating rata-rata minimal 4.0 dari skala 5 berdasarkan ulasan pengguna di dataset. Buku-buku ini juga akan diprioritaskan jika telah menerima lebih dari 50 ulasan, untuk memastikan bahwa rekomendasi didasarkan pada data yang cukup signifikan dan representatif.
- **Kriteria Nilai Tinggi**: “Rating tinggi” didefinisikan sebagai buku dengan skor 4.0 atau lebih, yang menandakan bahwa buku tersebut sangat direkomendasikan oleh mayoritas pengguna lain dan dianggap berkualitas tinggi.

Solusi ini dirancang untuk memberikan rekomendasi buku yang relevan dan berkualitas tinggi, sehingga dapat membantu pembaca menemukan buku yang sesuai dengan preferensi mereka dengan lebih mudah dan cepat. Dengan meningkatkan kualitas rekomendasi, diharapkan pembaca akan lebih termotivasi untuk membaca lebih banyak buku, yang pada akhirnya dapat berkontribusi pada peningkatan minat baca dan literasi di masyarakat.

### Data Understanding

Dataset yang digunakan diambil dari situs **Kaggle** yang berjudul [_"goodbooks-10k"_](https://www.kaggle.com/datasets/zygmunt/goodbooks-10k?select=books.csv). Dataset ini berisi 5 file dengan ekstensi csv, yaitu:
1. **'genre.csv'**
- Metadata :
   - goodreads_book_id: ID buku Goodreads.
   - tag_id: ID tag (genre).
   - count: Jumlah buku yang terkait dengan tag tertentu.
- Konten: File ini mencakup data tag (label) untuk buku-buku, yang memungkinkan klasifikasi berdasarkan genre atau tema tertentu.
- Analisis:
   - Jumlah tag unik: 34.252
   - Tag paling populer digunakan untuk buku dengan genre fiksi dan non-fiksi.
     
2. **'books.csv'**
- Metadata :
   - id: ID unik untuk setiap baris data.
   - book_id: ID unik untuk buku.
   - best_book_id: ID buku terbaik (jika ada).
   - work_id: ID karya terkait buku.
   - books_count: Jumlah edisi buku tertentu.
   - isbn: Nomor ISBN buku.
   - isbn13: Nomor ISBN-13 buku.
   - authors: Nama penulis buku.
   - original_publication_year: Tahun terbitnya buku.
   - original_title: Judul asli buku.
   - title: Judul buku.
   - language_code: Kode bahasa buku.
   - average_rating: Rating rata-rata buku.
   - ratings_count: Jumlah rating yang diberikan untuk buku.
   - work_ratings_count: Jumlah rating yang diterima oleh karya.
   - work_text_reviews_count: Jumlah ulasan teks yang diterima oleh karya.
   - ratings_1, ratings_2, ratings_3, ratings_4, ratings_5: Jumlah rating dengan nilai tertentu.
- Konten: File ini berisi informasi mendetail tentang 10.000 buku, termasuk ID buku, penulis, judul, dan tahun terbit.
- Analisis:
   - Jumlah buku unik: 10.000
   - Jumlah penulis unik: 4.664
   - Distribusi tahun terbit menunjukkan mayoritas buku berasal dari periode setelah tahun 2000.
   - Penulis yang memiliki buku paling banyak ialah _John Grisham_, hal ini memberikan insight tentang produktivitas penulis.
     ![image](https://github.com/hairulysin/streamlitDashboard/assets/90087096/f6b32720-acca-4248-aec1-7a66f9e3a1d9)
    - Mayoritas buku memiliki rating tinggi, sehingga distribusi condong ke kanan.
     ![image](https://github.com/hairulysin/streamlitDashboard/assets/90087096/2f9abfe3-48fe-4d08-9823-47b54157f841)
     Insight:
      - Genre yang paling populer memberikan gambaran tentang preferensi umum pembaca.
      - Tag populer seperti '_fiction_', '_fantasy_', dan '_young-adult_' dapat digunakan untuk menyegmentasikan pembaca berdasarkan minat genre.


3. **'ratings.csv'**
- Metadata :
   - book_id: ID buku yang diberi rating.
   - user_id: ID pengguna yang memberi rating.
   - rating: Nilai rating yang diberikan oleh pengguna untuk buku tertentu.
- Konten: File ini berisi 5.973.270 entri rating yang diberikan oleh pengguna untuk berbagai buku.
- Analisis:
   - Jumlah pengguna unik: 53.424
   - Distribusi rating dari 1 hingga 5, dengan mayoritas rating berada pada skala 4 dan 5 (Gambar 1).
    ![image](https://github.com/hairulysin/streamlitDashboard/assets/90087096/110e667b-14c4-45bc-8590-e6568bfdcfde)
   > Gambar 1: Distribusi rating buku dari pengguna, menunjukkan sebagian besar buku mendapatkan rating tinggi.
   
  ** Insight:**
   - Distribusi rating yang cenderung tinggi menunjukkan banyak pengguna memberikan rating positif.
   - Pola rating ini dapat membantu dalam menyusun rekomendasi yang lebih akurat berdasarkan preferensi pengguna.
   
4. **'jenis_genre.csv'**
- Metadata :
   - book_id: ID buku yang diberi rating.
   - user_id: ID pengguna yang memberi rating.
   - rating: Nilai rating yang diberikan oleh pengguna untuk buku tertentu.
- Konten: File ini berisi pemetaan antara ID tag dan nama tag yang digunakan untuk buku-buku.
- Analisis:
   - Jumlah jenis genre atau tag buku: 34.252
   - Beberapa tag seperti '_fiction_', '_fantasy_', dan '_young-adult_' adalah yang paling sering digunakan.

5. **Users.csv**:
- Metadata :
   - user_id: ID unik untuk setiap pengguna.
   - book_id: ID buku yang telah dilihat atau diinteraksi oleh pengguna.
- Konten: File ini berisi daftar buku yang ditandai pengguna untuk dibaca.
- Analisis:
   - Jumlah pengguna unik: 48.871
   - Distribusi menunjukkan bahwa banyak pengguna memiliki daftar buku yang ingin mereka baca, yang dapat digunakan untuk memperkirakan minat baca.

### Data Preparation

**Langkah-langkah persiapan data meliputi:**

**1. Mengatasi Missing Value:** 
- **Deskripsi**: Pengecekan dan penghapusan data kosong dilakukan untuk memastikan integritas dataset.
- **Metode**: Digunakan metode isnull().sum() untuk menghitung jumlah nilai kosong dan dropna() untuk menghapusnya.
- **Alasan**: Menghapus data kosong penting untuk menghindari bias atau error pada model. Data yang lengkap dan konsisten membantu dalam meningkatkan akurasi prediksi.

**Tabel Missing Value:**
| **Fitur**                    | **Jumlah Missing Values** |
|------------------------------|---------------------------|
| book_id                      | 0                         |
| user_id                      | 0                         |
| rating                       | 0                         |
| authors                      | 88.860.317                |
| title                        | 88.860.317                |
| original_publication_year    | 88.870.317                |

**Insight** : Kolom book_id, user_id, dan rating tidak memiliki missing values, yang menunjukkan bahwa data utama terkait identifikasi buku, pengguna, dan rating diberikan secara lengkap. Ini penting karena data ini menjadi dasar dalam membangun sistem rekomendasi.


**2. _Encoding_ Data**:
**Deskripsi**: Proses mengubah fitur kategorikal menjadi format numerik agar bisa digunakan oleh algoritma pembelajaran mesin.
**Teknik yang Digunakan:**
   1. _One Hot Encoding_:
      - Digunakan untuk mengubah fitur kategorikal seperti genre buku menjadi format biner.
      - Kegunaan: Menyediakan representasi yang tidak memiliki urutan atau hierarki, yang penting untuk fitur seperti genre buku.
   2. Label _Encoding_:
      - Digunakan untuk mengubah fitur kategorikal seperti penulis menjadi label numerik.
      - Kegunaan: Menyediakan cara sederhana dan cepat untuk mengkonversi fitur kategorikal menjadi numerik.
   3. _Drop Dummy_:
      - Digunakan untuk mengurangi redundansi setelah _One Hot Encoding_ dengan menghapus satu kolom _dummy_.
      - Kegunaan: Mencegah masalah _collinearity_ dalam model regresi atau klasifikasi.
        
**Alasan**: _Encoding_ fitur kategorikal menjadi numerik sangat penting agar dapat digunakan oleh algoritma pembelajaran mesin, yang hanya bisa bekerja dengan data numerik. _One Hot Encoding_ dipilih untuk fitur tanpa urutan (seperti genre), sementara Label _Encoding_ digunakan untuk fitur dengan jumlah kategori yang banyak (seperti penulis).

3. **Pembagian Data**
- **Deskripsi**: Membagi dataset menjadi data pelatihan (_training_) dan pengujian (_testing_) untuk memvalidasi model.
Metode: Menggunakan _train_test_split_ dengan rasio 80:20 untuk membagi data.
- **Alasan**: Membagi data menjadi bagian training dan testing penting untuk mengevaluasi performa model dengan data yang belum pernah dilihat sebelumnya, sehingga memberikan indikasi yang lebih baik tentang bagaimana model akan bekerja pada data yang baru.

### Modelling:
Dalam proyek ini, digunakan dua pendekatan utama untuk membangun sistem rekomendasi buku: _Content-Based Filtering_ dan _Collaborative Filtering_. Kedua metode ini dipilih untuk memberikan rekomendasi yang lebih akurat dan personal kepada pengguna.

**1. _Content-Based Filtering_**
**Deskripsi**:
_Content-Based Filtering_ adalah teknik rekomendasi yang mendasarkan rekomendasi pada kesamaan antara konten dari item yang berbeda. Metode ini menggunakan informasi fitur dari item untuk menemukan item yang serupa dengan preferensi pengguna sebelumnya.

**Algoritma yang Digunakan:**
Pendekatan ini menggunakan algoritma _TF-IDF (Term Frequency-Inverse Document Frequency)_ untuk mengubah teks (misalnya, deskripsi buku, genre) menjadi vektor numerik. Setelah itu, dihitung kesamaan antara buku menggunakan _cosine similarity_ untuk menemukan buku yang paling mirip dengan buku yang sudah disukai atau dilihat oleh pengguna.

**Cara Kerja:**
1. _TF-IDF Vectorization_: Mengubah teks (misalnya, deskripsi buku) menjadi representasi numerik yang menangkap relevansi kata dalam konteks koleksi dokumen (buku).
2. Cosine Similarity: Menghitung kesamaan antara vektor buku berdasarkan sudut antara vektor. Nilai _cosine similarity_ berkisar antara 0 dan 1, di mana 1 menunjukkan kesamaan sempurna.

**Alasan Pemilihan:**
- **Relevansi Kontekstual**: _TF-IDF_ cocok untuk menangkap konteks dan relevansi kata dalam deskripsi buku, sehingga bisa memberikan rekomendasi buku yang relevan berdasarkan isi kontennya.
- **Efektif untuk Data Teks**: Pendekatan ini sangat baik dalam menangani data teks seperti deskripsi buku, genre, dan lainnya.
- **Tidak Memerlukan Data Pengguna Lain:** _Content-Based Filtering_ tidak memerlukan data dari pengguna lain, sehingga cocok untuk memberikan rekomendasi awal untuk pengguna baru.

**Top 5 Rekomendasi Buku (Contoh):**

Berikut adalah tabel hasil rekomendasi buku berdasarkan buku yang dicari ("_The Door Into Summer_") dengan menggunakan _Content-Based Filtering_

## Hasil Rekomendasi Buku Berdasarkan Buku yang Dicari ("The Door Into Summer")

| **Judul Buku**                                            | **Penulis**              |
|-----------------------------------------------------------|--------------------------|
| Time Enough for Love                                      | Robert A. Heinlein       |
| Stranger in a Strange Land                                | Robert A. Heinlein       |
| Job: A Comedy of Justice                                  | Robert A. Heinlein       |
| Mrs. Frisby and the Rats of NIMH (Rats of NIMH #1)        | Robert C. O'Brien        |
| Shadow Divers                                             | Robert Kurson            |

**Insight**: Tiga dari lima buku yang direkomendasikan ditulis oleh Robert A. Heinlein, yang juga penulis dari buku yang dicari, "_The Door Into Summer_". Ini menunjukkan bahwa sistem rekomendasi cenderung merekomendasikan buku-buku lain dari penulis yang sama, dengan begini pembaca yang menyukai satu karya dari seorang penulis kemungkinan besar akan menikmati karya-karya lainnya dari penulis tersebut. _Robert A. Heinlein_ dikenal dengan genre fiksi ilmiah (_science fiction_). Buku-buku seperti "_Time Enough for Love", "Stranger in a Strange Land"_, dan _"Job: A Comedy of Justice"_ semua berada dalam genre yang sama.

**2. _Collaborative Filtering_**
**Deskripsi**:
_Collaborative Filtering_ adalah teknik yang menggunakan informasi dari banyak pengguna untuk memberikan rekomendasi. Metode ini berfokus pada pola preferensi di antara pengguna untuk merekomendasikan item yang mungkin disukai pengguna lain dengan preferensi yang sama.

**Algoritma yang Digunakan:**
Menggunakan algoritma embedding yang diterapkan dalam class _RecommenderNet_ dari Keras. Algoritma ini mempelajari representasi numerik (_embedding_) dari pengguna dan buku sehingga bisa memprediksi kesukaan pengguna terhadap buku tertentu berdasarkan pola preferensi pengguna lainnya.

**Cara Kerja:**
1. _**Embedding Layer**_: Mempelajari representasi numerik untuk pengguna dan buku dalam dimensi rendah.
2. _**Dot Product**_: Menghitung kecocokan antara pengguna dan buku berdasarkan dot product dari embedding mereka.
3. _**Optimisasi**_: Menggunakan optimisasi backpropagation untuk meminimalkan kesalahan prediksi rating buku.

**Alasan Pemilihan:**
- **Memanfaatkan Preferensi Pengguna Lain**: _Collaborative Filtering_ efektif dalam memanfaatkan data dari banyak pengguna untuk menemukan pola preferensi, sehingga bisa memberikan rekomendasi yang lebih personal.
- **Menangani Skala Besar**: Pendekatan ini mampu menangani data dalam skala besar dan memberikan rekomendasi yang relevan dengan memanfaatkan kesamaan pola preferensi.
- **Cocok untuk Rating:** Algoritma ini dirancang khusus untuk prediksi rating, sehingga cocok untuk memberikan rekomendasi buku dengan rating tinggi.

## Top 10 Rekomendasi Buku untuk User ID: 11468

| **Judul Buku**                                         | **Penulis**                                                    |
|--------------------------------------------------------|----------------------------------------------------------------|
| Beloved                                                | Toni Morrison                                                  |
| The Curious Incident of the Dog in the Night-Time      | Mark Haddon                                                    |
| A People's History of the United States                | Howard Zinn                                                    |
| The Taste of Home Cookbook                             | Janet Briggs, Beth Wittlinger                                  |
| The Beautiful and Damned                               | F. Scott Fitzgerald                                            |
| Hard Times                                             | Charles Dickens                                                |
| Amsterdam                                              | Ian McEwan                                                     |
| Superman: Birthright                                   | Mark Waid, Alfred Gough, Miles Millar, Dave McCaig, Gerry Alanguilan, Leinil Francis Yu |
| Still Life with Woodpecker                             | Tom Robbins                                                    |
| Love in the Time of Cholera                            | Gabriel García Márquez, Edith Grossman                         |


### Evaluasi
Metrik evaluasi yang digunakan dalam proyek ini adalah _Root Mean Squared Error (RMSE)_, yang memberikan gambaran tentang seberapa baik model dalam memprediksi rating buku oleh pengguna. Nilai RMSE digunakan untuk mengukur tingkat akurasi prediksi model, di mana nilai yang lebih rendah menunjukkan prediksi yang lebih dekat dengan nilai observasi.

![image](https://github.com/hairulysin/streamlitDashboard/assets/90087096/20f50a42-6fac-4cab-8a85-f6aa7a2f75e1)
   > **Gambar 2: Plot History RMSE**

**Insight**:
- Penurunan RMSE: Nilai RMSE menurun seiring bertambahnya iterasi, menunjukkan peningkatan akurasi model selama pelatihan.
- Konvergensi Model: Setelah beberapa iterasi, nilai RMSE mendekati konstan, menandakan bahwa model mencapai konvergensi dan tidak banyak peningkatan lebih lanjut.
- Stabilitas: Stabilitas nilai RMSE di akhir pelatihan menunjukkan bahwa model belajar dengan baik tanpa tanda-tanda _overfitting_.

**Interpretasi RMSE:**
Dalam konteks proyek ini, nilai RMSE sebesar 0.2133 menunjukkan performa yang baik dari model _Collaborative Filtering_. RMSE yang rendah menandakan bahwa model mampu memberikan prediksi rating yang mendekati nilai sebenarnya. Dengan demikian, hasil evaluasi menunjukkan bahwa model memiliki kemampuan yang baik dalam memprediksi preferensi pengguna terhadap buku. Hal ini sesuai dengan tujuan proyek untuk menyediakan rekomendasi buku yang sesuai dengan preferensi pengguna.

Untuk content-based filtering, metrik evaluasi yang digunakan adalah _Precision_. _Precision_ mengukur proporsi rekomendasi yang relevan dari keseluruhan rekomendasi yang diberikan oleh sistem.

**Insight Precision:**
- Relevansi Rekomendasi: Precision tinggi menunjukkan bahwa sistem content-based filtering memberikan rekomendasi buku yang sesuai dengan minat dan preferensi pengguna berdasarkan konten buku (seperti genre, penulis, dan kata kunci). Dengan precision 0.60, ini berarti bahwa 60% dari buku yang direkomendasikan adalah relevan dengan minat pengguna. Misalnya, dari 5 buku yang direkomendasikan, 3 di antaranya benar-benar sesuai dengan preferensi pengguna, menunjukkan bahwa sistem berhasil mengidentifikasi dan merekomendasikan buku-buku yang relevan.
- Kualitas Rekomendasi: Dengan menggunakan precision, dapat dipastikan bahwa rekomendasi yang diberikan tidak hanya banyak tetapi juga berkualitas tinggi dan relevan bagi pengguna. Precision sebesar 0.60 menunjukkan bahwa dari setiap lima rekomendasi buku yang diberikan, tiga buku relevan dan berkualitas tinggi berdasarkan penulis yang sama atau hampir sama, yang menjadi dasar rekomendasi dari model content-based filtering ini. Ini menegaskan bahwa sistem ini cukup efisien dalam memahami dan memetakan preferensi pengguna ke dalam rekomendasi yang akurat.
- Kekuatan Content-Based Filtering: Precision yang dicapai (0.60) menunjukkan bahwa sistem mampu memberikan rekomendasi yang bermanfaat bagi pengguna, terutama bagi mereka yang tertarik untuk mengeksplorasi karya dari penulis yang sama atau genre yang mirip. Ini menunjukkan bahwa sistem ini bekerja dengan baik untuk menemukan buku-buku yang serupa berdasarkan fitur-fitur konten yang telah diidentifikasi sebelumnya.

**Kesimpulan Evaluasi**
- _Collaborative Filtering:_ RMSE digunakan untuk mengukur akurasi prediksi rating, dengan hasil menunjukkan bahwa model memiliki kemampuan yang baik dalam memprediksi preferensi pengguna.
- _Content-Based Filtering:_ Precision digunakan untuk mengevaluasi relevansi rekomendasi, memastikan bahwa rekomendasi yang diberikan sesuai dengan preferensi pengguna.

### Kesimpulan
1. Sistem rekomendasi buku menggunakan _Content-Based Filtering_ berhasil memberikan rekomendasi buku berdasarkan penulis.
2. Sistem rekomendasi buku menggunakan _Collaborative Filtering_ berhasil memberikan rekomendasi buku berdasarkan rating tertinggi.
4. Evaluasi model _Collaborative Filtering_ dengan RMSE mencapai 0.2133.




