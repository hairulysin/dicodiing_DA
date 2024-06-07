# Laporan Proyek Machine Learning - Hairul Yasin

## *Sistem Rekomendasi Buku*

## Project Overview
Membaca buku adalah kunci penting untuk meningkatkan literasi dan pengetahuan, namun di Indonesia, minat baca masih sangat rendah, dengan indeks hanya sekitar 0,001 menurut UNESCO. Salah satu tantangan utamanya adalah kesulitan menemukan buku yang sesuai dengan preferensi individu karena banyaknya pilihan yang tersedia. Dataset goodbooks-10k dari Kaggle, yang mencakup 10.000 buku beserta rating dan ulasan pengguna, digunakan untuk membangun sistem rekomendasi berbasis machine learning. Sistem ini menggunakan metode Content-Based dan Collaborative Filtering untuk membantu pembaca menemukan buku yang relevan dan menarik, sehingga diharapkan dapat mendorong peningkatan minat baca dan literasi. Dengan menggunakan model rekomendasi yang tepat, diharapkan dapat mempermudah pembaca dalam menemukan buku yang sesuai dengan minat mereka, menjadikan proses pencarian lebih cepat dan efisien, serta memberikan kontribusi positif terhadap budaya membaca di masyarakat.

## Business Understanding
Proyek ini bertujuan untuk membangun sistem rekomendasi buku yang dapat meningkatkan minat baca dengan menyediakan rekomendasi buku yang sesuai dengan preferensi dan kebutuhan pembaca.

### Problem Statements
1. Bagaimana cara membangun sistem rekomendasi buku berdasarkan kriteria pembaca menggunakan content-based filtering?
2. Bagaimana cara membangun sistem rekomendasi buku yang disukai berdasarkan rating menggunakan collaborative filtering?

### Goals
1. Menyediakan rekomendasi buku yang sesuai dengan kriteria pembaca atau buku serupa menggunakan content-based filtering.
2. Menyediakan rekomendasi buku yang belum dibaca atau mungkin disukai pembaca menggunakan collaborative filtering.

#### Solution Statements
1. **Content-Based Filtering:**
- **Metode**: Sistem akan menggunakan teknik Term Frequency-Inverse Document Frequency (TF-IDF) dan cosine similarity untuk mengukur kemiripan antara deskripsi buku, genre, dan metadata lainnya.
- **Output**: Sistem ini akan merekomendasikan top 5 buku yang memiliki kemiripan konten paling tinggi dengan buku yang diinput oleh pengguna.
- **Detail Rekomendasi**: Buku-buku yang direkomendasikan akan memiliki skor kemiripan minimal 0.7 pada skala 0 hingga 1, yang menunjukkan bahwa buku-buku tersebut memiliki konten yang sangat relevan dengan preferensi pembaca.

2. **Collaborative Filtering:**
- **Metode**: Menggunakan model embedding seperti RecommenderNet yang diimplementasikan dengan Keras, sistem ini akan memprediksi buku yang akan disukai pengguna berdasarkan pola rating pengguna lain yang memiliki preferensi serupa.
Output: Sistem akan merekomendasikan top 10 buku yang memiliki rating tinggi yang belum pernah dibaca oleh pengguna.
- **Detail Rekomendasi**: Buku yang direkomendasikan memiliki rating rata-rata minimal 4.0 dari skala 5 berdasarkan ulasan pengguna di dataset. Buku-buku ini juga akan diprioritaskan jika telah menerima lebih dari 50 ulasan, untuk memastikan bahwa rekomendasi didasarkan pada data yang cukup signifikan dan representatif.
- **Kriteria Nilai Tinggi**: “Rating tinggi” didefinisikan sebagai buku dengan skor 4.0 atau lebih, yang menandakan bahwa buku tersebut sangat direkomendasikan oleh mayoritas pengguna lain dan dianggap berkualitas tinggi.

Solusi ini dirancang untuk memberikan rekomendasi buku yang relevan dan berkualitas tinggi, sehingga dapat membantu pembaca menemukan buku yang sesuai dengan preferensi mereka dengan lebih mudah dan cepat. Dengan meningkatkan kualitas rekomendasi, diharapkan pembaca akan lebih termotivasi untuk membaca lebih banyak buku, yang pada akhirnya dapat berkontribusi pada peningkatan minat baca dan literasi di masyarakat.

### Data Understanding

Dataset yang digunakan diambil dari situs **Kaggle** yang berjudul [_"goodbooks-10k"_](https://www.kaggle.com/datasets/zygmunt/goodbooks-10k?select=books.csv). Dataset ini berisi 5 file dengan ekstensi csv, yaitu:
1. **'book_tags.csv'**
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

3. **'ratings.csv'**
- Konten: File ini berisi 5.973.270 entri rating yang diberikan oleh pengguna untuk berbagai buku.
- Analisis:
   - Jumlah pengguna unik: 53.424
   - Distribusi rating dari 1 hingga 5, dengan mayoritas rating berada pada skala 4 dan 5 (Gambar 1).
   
    ![image](https://github.com/hairulysin/streamlitDashboard/assets/90087096/110e667b-14c4-45bc-8590-e6568bfdcfde)
   > Gambar 1: Distribusi rating buku dari pengguna, menunjukkan sebagian besar buku mendapatkan rating tinggi.
   
4. **'tag.csv'**
- Konten: File ini berisi pemetaan antara ID tag dan nama tag yang digunakan untuk buku-buku.
- Analisis:
   - Jumlah jenis genre atau tag buku: 34.252
   - Beberapa tag seperti 'fiction', 'fantasy', dan 'young-adult' adalah yang paling sering digunakan.

5. **To_Read.csv**:
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

| **Fitur**                    | **Jumlah Missing Values** |
|------------------------------|---------------------------|
| book_id                      | 0                         |
| user_id                      | 0                         |
| rating                       | 0                         |
| authors                      | 88.860.317                |
| title                        | 88.860.317                |
| original_publication_year    | 88.870.317                |

  
**2. Encoding Data**:
**Deskripsi**: Proses mengubah fitur kategorikal menjadi format numerik agar bisa digunakan oleh algoritma pembelajaran mesin.
**Teknik yang Digunakan:**
   1. One Hot Encoding:
      - Digunakan untuk mengubah fitur kategorikal seperti genre buku menjadi format biner.
      - Kegunaan: Menyediakan representasi yang tidak memiliki urutan atau hierarki, yang penting untuk fitur seperti genre buku.
   2. Label Encoding:
      - Digunakan untuk mengubah fitur kategorikal seperti penulis menjadi label numerik.
      - Kegunaan: Menyediakan cara sederhana dan cepat untuk mengkonversi fitur kategorikal menjadi numerik.
   3. Drop Dummy:
      - Digunakan untuk mengurangi redundansi setelah One Hot Encoding dengan menghapus satu kolom dummy.
      - Kegunaan: Mencegah masalah collinearity dalam model regresi atau klasifikasi.
        
**Alasan**: Encoding fitur kategorikal menjadi numerik sangat penting agar dapat digunakan oleh algoritma pembelajaran mesin, yang hanya bisa bekerja dengan data numerik. One Hot Encoding dipilih untuk fitur tanpa urutan (seperti genre), sementara Label Encoding digunakan untuk fitur dengan jumlah kategori yang banyak (seperti penulis).

3. **Pembagian Data**
- **Deskripsi**: Membagi dataset menjadi data pelatihan (training) dan pengujian (testing) untuk memvalidasi model.
Metode: Menggunakan train_test_split dengan rasio 80:20 untuk membagi data.
- **Alasan**: Membagi data menjadi bagian training dan testing penting untuk mengevaluasi performa model dengan data yang belum pernah dilihat sebelumnya, sehingga memberikan indikasi yang lebih baik tentang bagaimana model akan bekerja pada data yang baru.

### Modelling:

Dalam proyek ini, digunakan dua pendekatan utama untuk membangun sistem rekomendasi buku: Content-Based Filtering dan Collaborative Filtering. Kedua metode ini dipilih untuk memberikan rekomendasi yang lebih akurat dan personal kepada pengguna.

**1. Content-Based Filtering**
**Deskripsi**:
Content-Based Filtering adalah teknik rekomendasi yang mendasarkan rekomendasi pada kesamaan antara konten dari item yang berbeda. Metode ini menggunakan informasi fitur dari item (misalnya, buku) untuk menemukan item yang serupa dengan preferensi pengguna sebelumnya.

**Algoritma yang Digunakan:**
Pendekatan ini menggunakan algoritma TF-IDF (Term Frequency-Inverse Document Frequency) untuk mengubah teks (misalnya, deskripsi buku, genre) menjadi vektor numerik. Setelah itu, dihitung kesamaan antara buku menggunakan cosine similarity untuk menemukan buku yang paling mirip dengan buku yang sudah disukai atau dilihat oleh pengguna.

**Cara Kerja:**
1. TF-IDF Vectorization: Mengubah teks (misalnya, deskripsi buku) menjadi representasi numerik yang menangkap relevansi kata dalam konteks koleksi dokumen (buku).
2. Cosine Similarity: Menghitung kesamaan antara vektor buku berdasarkan sudut antara vektor. Nilai cosine similarity berkisar antara 0 dan 1, di mana 1 menunjukkan kesamaan sempurna.

**Alasan Pemilihan:**
- **Relevansi Kontekstual**: TF-IDF cocok untuk menangkap konteks dan relevansi kata dalam deskripsi buku, sehingga bisa memberikan rekomendasi buku yang relevan berdasarkan isi kontennya.
- **Efektif untuk Data Teks**: Pendekatan ini sangat baik dalam menangani data teks seperti deskripsi buku, genre, dan lainnya.
- **Tidak Memerlukan Data Pengguna Lain:** Content-Based Filtering tidak memerlukan data dari pengguna lain, sehingga cocok untuk memberikan rekomendasi awal untuk pengguna baru.

**Top 5 Rekomendasi Buku (Contoh):**

Berikut adalah tabel hasil rekomendasi buku berdasarkan buku yang dicari ("The Door Into Summer") dengan menggunakan Content-Based Filtering

## Hasil Rekomendasi Buku Berdasarkan Buku yang Dicari ("The Door Into Summer")

| **Judul Buku**                                            | **Penulis**              |
|-----------------------------------------------------------|--------------------------|
| Time Enough for Love                                      | Robert A. Heinlein       |
| Stranger in a Strange Land                                | Robert A. Heinlein       |
| Job: A Comedy of Justice                                  | Robert A. Heinlein       |
| Mrs. Frisby and the Rats of NIMH (Rats of NIMH #1)        | Robert C. O'Brien        |
| Shadow Divers                                             | Robert Kurson            |


**2. Collaborative Filtering**
**Deskripsi**:
Collaborative Filtering adalah teknik yang menggunakan informasi dari banyak pengguna untuk memberikan rekomendasi. Metode ini berfokus pada pola preferensi di antara pengguna untuk merekomendasikan item yang mungkin disukai pengguna lain dengan preferensi yang sama.

**Algoritma yang Digunakan:**
Menggunakan algoritma embedding yang diterapkan dalam class RecommenderNet dari Keras. Algoritma ini mempelajari representasi numerik (embedding) dari pengguna dan buku sehingga bisa memprediksi kesukaan pengguna terhadap buku tertentu berdasarkan pola preferensi pengguna lainnya.

**Cara Kerja:**
1. **Embedding Layer**: Mempelajari representasi numerik untuk pengguna dan buku dalam dimensi rendah.
2.** Dot Product**: Menghitung kecocokan antara pengguna dan buku berdasarkan dot product dari embedding mereka.
3. **Optimisasi**: Menggunakan optimisasi backpropagation untuk meminimalkan kesalahan prediksi rating buku.

**Alasan Pemilihan:**
- **Memanfaatkan Preferensi Pengguna Lain**: Collaborative Filtering efektif dalam memanfaatkan data dari banyak pengguna untuk menemukan pola preferensi, sehingga bisa memberikan rekomendasi yang lebih personal.
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
Metrik evaluasi yang digunakan dalam proyek ini adalah Root Mean Squared Error (RMSE), yang memberikan gambaran tentang seberapa baik model dalam memprediksi rating buku oleh pengguna. Nilai RMSE digunakan untuk mengukur tingkat akurasi prediksi model, di mana nilai yang lebih rendah menunjukkan prediksi yang lebih dekat dengan nilai observasi.

![image](https://github.com/hairulysin/streamlitDashboard/assets/90087096/20f50a42-6fac-4cab-8a85-f6aa7a2f75e1)
> **Gambar 2: Plot History RMSE**

**Interpretasi RMSE:**
Dalam konteks proyek ini, nilai RMSE sebesar 0.2136 menunjukkan performa yang baik dari model Collaborative Filtering. RMSE yang rendah menandakan bahwa model mampu memberikan prediksi rating yang mendekati nilai sebenarnya. Dengan demikian, hasil evaluasi menunjukkan bahwa model memiliki kemampuan yang baik dalam memprediksi preferensi pengguna terhadap buku. Hal ini sesuai dengan tujuan proyek untuk menyediakan rekomendasi buku yang sesuai dengan preferensi pengguna.

### Kesimpulan
1. Sistem rekomendasi buku menggunakan content-based filtering berhasil memberikan rekomendasi buku berdasarkan penulis.
2. Sistem rekomendasi buku menggunakan collaborative filtering berhasil memberikan rekomendasi buku berdasarkan rating tertinggi.
4. Evaluasi model collaborative filtering dengan RMSE mencapai 0.2136.




