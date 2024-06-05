# Laporan Proyek Machine Learning - Hairul Yasin

## *Sistem Rekomendasi Buku*

## Project Overview
Membaca buku adalah salah satu cara utama untuk memperoleh pengetahuan dan wawasan baru. Buku merupakan sumber informasi yang kaya dan membantu memperluas cakrawala kita. Pepatah "Buku adalah jendela dunia" menekankan pentingnya membaca. Meskipun informasi tentang berbagai buku mudah diakses di internet, minat baca di Indonesia masih rendah . Salah satu alasan utamanya adalah kesulitan menemukan buku yang sesuai dengan preferensi pembaca karena banyaknya pilihan yang tersedia.
Untuk meningkatkan minat baca, kita dapat membangun sistem rekomendasi buku yang memudahkan pembaca menemukan buku yang sesuai dengan preferensi mereka. Sistem ini akan menggunakan metode Content-Based Filtering dan Collaborative Filtering. Diharapkan dengan mendapatkan rekomendasi yang tepat, pembaca akan lebih tertarik untuk membaca lebih banyak buku.

## Business Understanding
Tujuan utama dari penelitian ini adalah membangun sistem rekomendasi buku yang sesuai dengan preferensi pembaca menggunakan metode content-based filtering dan collaborative filtering.

### Problem Statements
1. Bagaimana cara membangun sistem rekomendasi buku berdasarkan kriteria pembaca menggunakan content-based filtering?
2. Bagaimana cara membangun sistem rekomendasi buku yang disukai berdasarkan rating menggunakan collaborative filtering?

### Goals
1. Menyediakan rekomendasi buku yang sesuai dengan kriteria pembaca atau buku serupa menggunakan content-based filtering.
2. Menyediakan rekomendasi buku yang belum dibaca atau mungkin disukai pembaca menggunakan collaborative filtering.

#### Solution Statements
1. Menerapkan content-based filtering dengan menggunakan TF-IDF dan cosine similarity untuk menemukan top 5 buku serupa berdasarkan judul dan penulis.
2. Menerapkan collaborative filtering menggunakan class RecommenderNet untuk mendapatkan rekomendasi top 10 buku dengan rating tinggi.

### Data Understanding

Dataset yang digunakan diambil dari situs **Kaggle** yang berjudul [_"goodbooks-10k"_](https://www.kaggle.com/datasets/zygmunt/goodbooks-10k?select=books.csv). Dataset ini berisi 5 file dengan ekstensi csv, yaitu:
1. **'book_tags.csv'**, file ini berisi data tag buku (label), diurutkan berdasarkan ascending goodreadsbookid dan count descending.
   - goodreads_id : ID dari goodreads
   - tag_id : ID tag (genre)
   - count : Jumlah goodreads

  Untuk mengetahui jumlah genre digunakan fungsi `len()` dengan menambah fungsi `unique`. Sehingga outputnya: 
  ```sh
    Jumlah genre buku:  34252
  ```
2. **'books.csv'**, berisi informasi mengenai buku.
   - id : ID dari file books
   - book_id : ID buku
   - best_book_id : ID dari buku populer
   - work_id : ID karya
   - books_count : jumlah edisi buku tertentu
   - isbn : nomor isbn
   - authors : nama penulis
   - original_publication_year : tahun terbit buku
   - original_title : judul asli buku
   
   Untuk melihat jumlah buku dan jumlah nama penulis menggunakan fungsi `len()` dan`unique()`. Sehingga outputnya:
   ```sh
     Jumlah buku:  10000
     Jumlah author:  4664
   ```
4. **'ratings.csv'**, berisi rating buku sesuai id pengguna.
   - book_id : ID buku
   - user_id : ID Pengguna
   - rating : rating buku
   
    ![image](https://github.com/hairulysin/streamlitDashboard/assets/90087096/110e667b-14c4-45bc-8590-e6568bfdcfde)
   > Gambar 1. Visualisasi Jumlah Rating Buku dari Pengguna
5. **'tag.csv'**, berisi tentang pemetaan id-nama tag.
   - tag_id : ID tag (genre)
   - tag_name : Nama tag (genre)

   Untuk mengetahui jumlah genre menggunakan fungsi `len()` dan `unique()`. Outputnya:
    ```sh
      Jumlah jenis genre buku:  34252
    ```
6. **'to_read.csv'**, daftar buku yang ditandai oleh pengguna "untuk dibaca". Diurutkan berdasarkan user_id dan book_id.
   - user_id : ID pengguna/pembaca
   - book_id : ID buku
   
    Dari data didapatkan Jumlah User = 48871.

### Data Preparation

Langkah-langkah persiapan data meliputi:

1. Mengatasi Missing Value: Pengecekan dan penghapusan data kosong menggunakan isnull().sum() dan dropna().
   ![image](https://github.com/hairulysin/streamlitDashboard/assets/90087096/9c181be2-b78e-42a3-b505-b6781c658a5d)
3. Encoding Data: Melakukan encoding fitur 'user_id' dan book_id ke dalam indeks integer.
4. Membagi Dataset: Membagi dataset menjadi data train dan test dengan rasio 80:20 setelah melakukan pengacakan dataset.

### Pemodelan
Content-Based Filtering: Menggunakan TF-IDF untuk mengubah fitur teks menjadi numerik dan menghitung kemiripan menggunakan cosine similarity. Model ini menghasilkan rekomendasi top 5 buku serupa berdasarkan judul yang dimasukkan.

Collaborative Filtering: Menggunakan embedding untuk menghitung skor kecocokan antara pengguna dan buku. Model ini menerapkan class RecommenderNet dari Keras dan menghasilkan rekomendasi top 10 buku berdasarkan rating tinggi.

### Evaluasi
Metrik evaluasi yang digunakan adalah Precision dan Root Mean Squared Error (RMSE).

-  Precision: Mengukur jumlah prediksi positif yang benar dibagi dengan jumlah item yang direkomendasikan. Dalam contoh ini, precision untuk model content-based filtering adalah 60%.
- RMSE: Mengukur tingkat akurasi prediksi model dengan rumus berikut:
  Nilai RMSE rendah menunjukkan prediksi yang mendekati nilai observasi. Visualisasi RMSE selama pelatihan model collaborative filtering menunjukkan nilai error yang menurun hingga 0.2138, yang menunjukkan performa model yang baik.

### Kesimpulan
1. Sistem rekomendasi buku menggunakan content-based filtering berhasil memberikan rekomendasi buku berdasarkan penulis.
2. Sistem rekomendasi buku menggunakan collaborative filtering berhasil memberikan rekomendasi buku berdasarkan rating tertinggi.
3. Evaluasi model content-based filtering dengan precision mencapai 60%.
4. Evaluasi model collaborative filtering dengan RMSE mencapai 0.2161.


