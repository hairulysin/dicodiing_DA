# Laporan Proyek Machine Learning - Hairul Yasin
## Domain Proyek

Fluktuasi harga minyak dunia secara langsung mempengaruhi biaya produksi aspal, yang pada akhirnya berdampak pada harga jual aspal di pasaran. Bagi perusahaan Aspal, prediksi harga minyak dunia menjadi informasi penting untuk:

- Membuat strategi penetapan harga
- Memanajemen biaya produksi
- Membuat keputusan investasi
- Meningkatkan daya saing


## Business Understanding

### Problem Statements

- Harga minyak dunia sering mengalami fluktuasi yang tidak terduga, sehingga sulit bagi perusahaan aspal untuk memprediksi biaya produksi dan penetapan harga.
- Kurangnya informasi akurat tentang tren harga minyak di masa depan dapat menyebabkan pengambilan keputusan yang tidak tepat oleh perusahaan aspal.


### Goals

- Mengembangkan model prediksi harga minyak dunia yang akurat dan mudah diakses.
- Memberikan informasi prediksi harga minyak kepada perusahaan aspal untuk membantu mereka dalam pengambilan keputusan strategis.


## Data Understanding

Data yang digunakan dalam proyek ini adalah data harga minyak Brent Crude dari tahun 2011 hingga 2024. Data tersebut diperoleh dari Google Finance. Data ini memiliki beberapa variabel, yaitu:

### Variabel-variabel pada Restaurant UCI dataset adalah sebagai berikut:
Date: Tanggal observasi
Close: Harga penutupan minyak pada tanggal observasi
chg.close: Perubahan harga penutupan minyak dibandingkan hari sebelumnya
Low: Harga terendah minyak pada tanggal observasi
chg.low. : Perubahan harga terendah minyak dibandingkan hari sebelumnya
High: Harga tertinggi minyak pada tanggal observasi
chg.high. :  Perubahan harga tertinggi minyak dibandingkan hari sebelumnya


## Data Preparation

Sebelum digunakan untuk pemodelan, data perlu dipreparasi terlebih dahulu. Tahapan data preparation yang dilakukan adalah:

- Pemeriksaan data: Memeriksa apakah terdapat nilai yang hilang dalam data.
- Transformasi data: Melakukan transformasi data jika diperlukan, seperti normalisasi (pada model LSTM)

## Modeling
Dalam proyek ini, dua algoritma machine learning digunakan untuk memprediksi harga minyak dunia, yaitu ARIMA dan LSTM.

### ARIMA
Model ARIMA (Autoregressive Integrated Moving Average) adalah model statistik yang umum digunakan untuk memprediksi data time series. Model ARIMA dipilih karena cocok untuk data time series yang stabil dan memiliki tren. Model ARIMA yang digunakan dalam proyek ini adalah ARIMA(0, 1, 3).

### LSTM
Model LSTM (Long Short-Term Memory) adalah model neural network yang efektif dalam menangani data time series dengan pola yang kompleks dan non-linear. Model LSTM dipilih karena kemampuannya dalam menangkap pola non-linear dan kompleks dalam data harga minyak.

## Evaluation

Metrik evaluasi untuk model time series seperti ARIMA dan LSTM memberikan wawasan tentang keakuratan prediksi model. Mean Absolute Error (MAE) mengukur rata-rata perbedaan absolut antara nilai aktual dan prediksi, menunjukkan rata-rata kesalahan prediksi. Mean Squared Error (MSE) mengukur rata-rata kuadrat perbedaan, memberikan bobot lebih besar pada kesalahan besar. Root Mean Squared Error (RMSE) adalah akar kuadrat MSE, memberikan skala kesalahan dalam unit data asli. R-squared (R²) menunjukkan seberapa baik model menjelaskan varians data, dengan nilai mendekati 1 menunjukkan penjelasan yang baik.

Metrik evaluasi untuk model time series seperti ARIMA dan LSTM memberikan wawasan tentang keakuratan prediksi model. Mean Absolute Error (MAE) mengukur rata-rata perbedaan absolut antara nilai aktual dan prediksi, menunjukkan rata-rata kesalahan prediksi. Mean Squared Error (MSE) mengukur rata-rata kuadrat perbedaan, memberikan bobot lebih besar pada kesalahan besar. Root Mean Squared Error (RMSE) adalah akar kuadrat MSE, memberikan skala kesalahan dalam unit data asli. R-squared (R²) menunjukkan seberapa baik model menjelaskan varians data, dengan nilai mendekati 1 menunjukkan penjelasan yang baik.

Kesimpulan:

Model LSTM direkomendasikan untuk memprediksi harga minyak dunia karena akurasinya yang lebih tinggi dan kemampuannya untuk menjelaskan varians data dengan lebih baik. Namun, penting untuk dicatat bahwa performa model dapat bervariasi tergantung pada karakteristik data dan pilihan hyperparameter