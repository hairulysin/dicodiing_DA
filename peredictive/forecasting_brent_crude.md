# Laporan Proyek Machine Learning - Hairul Yasin
## Domain Proyek
Beberapa perusahaan aspal curah dihadapkan pada fluktuasi harga minyak yang rumit. Harga minyak yang naik turun langsung berimbas pada biaya produksi aspal, sehingga menentukan harga jual yang tepat menjadi tantangan besar. Saat ini, perusahaan mengandalkan data historis harga Argus (berlangganan) dan tren harga minyak untuk memprediksi harga aspal.  Sayangnya, data Argus hanya memberikan gambaran masa lalu, tanpa kemampuan memprediksi masa depan. Hal ini membuat perusahaan kesulitan dalam mengambil keputusan strategis yang tepat.

**Terobosan Baru: Machine Learning (ML)!**

Alasannya : ML mampu menganalisis data historis harga minyak dan aspal, serta faktor-faktor lain yang mempengaruhi harga, seperti kondisi ekonomi global dan permintaan pasar. Hasilnya, prediksi harga aspal yang lebih akurat dan terarah. Dengan hasil preediksi ini, diharapkan perusahaan dapat menetapkan harga jual yang kompetitif, mengelola stock dengan baik, dan meminimalisir resiko keuangan

## Business Understanding

### Problem Statements

**Bagaimana model ML dapat membantu perusahaan aspal dalam memprediksi harga minyak?**

Fluktuasi harga minyak dunia yang tak terduga menjadi momok bagi industri aspal. Hal ini menyebabkan perusahaan kesulitan dalam memprediksi biaya produksi dan penetapan harga yang tepat. Penelitian ini hadir untuk membawa solusi inovatif dengan model machine learning (ML) akan membantu perusahaan dalam:
1. Meningkatkan Efisiensi dan Profitabilitas
2. Meningkatkan daya saing
3. Mendukung pengambilan keputusan

**Goals** :
- Mengembangkan model prediksi harga minyak dunia yang akurat dan mudah diakses.
- Memberikan informasi prediksi harga minyak kepada perusahaan aspal untuk membantu mereka dalam pengambilan keputusan strategis.

## Data Understanding

Data yang digunakan dalam proyek ini adalah data harga minyak Brent Crude harian dari tahun 2021 hingga 2024. Data tersebut diperoleh dari Google Finance.

Data dapat diakses secara gratis melalui situs web Google Finance. Berikut adalah tautannya: _https://www.google.com/finance/quote/BZW00:NYMEX?hl=en_

### Dataset ini memiliki beberapa kolom, yaitu:
1. Date: Tanggal pencatatan data.
2. Open: Harga pembukaan perdagangan.
3. High: Harga tertinggi dalam satu hari perdagangan.
4. Low: Harga terendah dalam satu hari perdagangan.
5. Close: Harga penutupan perdagangan.
6. Volume: Volume perdagangan dalam barel.

![image](https://github.com/hairulysin/streamlitDashboard/assets/90087096/85e9a047-af49-4961-94ca-4a6f0ad32acf)

**💡 Insight :**
Analisis mendalam menguak fluktuasi harga penutupan yang signifikan (kisaran 50.23-114.19) dan perubahannya yang dinamis (rata-rata 0.1). Hal ini menunjukkan volatilitas pasar yang perlu diwaspadai. Harga terendah (kisaran 49.97-113.39) dan perubahannya (rata-rata 0.10) mencerminkan potensi risiko penurunan harga, sedangkan harga tertinggi (kisaran 51.88-115.06) dan perubahannya (rata-rata 0.10) membuka peluang keuntungan dari kenaikan harga. Volatilitas pasar minyak Brent Crude yang kompleks ini menjadi landasan bagi perusahaan untuk mengambil keputusan strategis yang tepat dan terukur. 

## Data Preparation

Langkah-langkah persiapan data yang dilakukan:

1. Mengubah format kolom Date menjadi datetime
2. Memilih kolom Close sebagai variabel target
3. Menganalisis statistik deskriptif awal untuk memahami distribusi data
4. Memvisualisasikan time series data harga close
5. Melakukan differencing data untuk mencapai stasioneritas
6. Membagi data training dan testing untuk melatih model
7. Menyiapkan data dalam format yang sesuai untuk model ARIMA dan LSTM

## Modeling
Proyek ini bertujuan untuk membangun model prediksi harga minyak Brent Crude yang akurat dan menyediakan informasi prediksi harga minyak secara real-time. Permasalahan utama yang dihadapi adalah kompleksitas dan dinamika data harga minyak yang dipengaruhi oleh berbagai faktor ekonomi dan non-ekonomi. Dalam proyek ini, dua algoritma machine learning digunakan untuk memprediksi harga minyak, yaitu ARIMA dan LSTM.

### ARIMA
Model ARIMA (Autoregressive Integrated Moving Average)  ARIMA merupakan model statistik yang umum digunakan untuk memprediksi data time series yang stabil dan menunjukkan tren yang jelas. Algoritma ini bekerja dengan mengidentifikasi pola ketergantungan antara nilai-nilai masa lalu dalam data. Model ARIMA yang digunakan dalam proyek ini adalah ARIMA(0, 1, 3).

### LSTM
Model LSTM (Long Short-Term Memory) merupakan model deep learning yang mampu menangkap pola dan hubungan kompleks dalam data time series, termasuk pola non-linear dan jangka panjang. Algoritma ini menggunakan jaringan saraf tiruan untuk mempelajari hubungan temporal dan spasial dalam data.

### Tahapan Pemodelan

a. Pra-pemrosesan Data:
Data dibersihkan dan diubah formatnya menjadi sesuai dengan kebutuhan model.
Data dibagi menjadi set pelatihan dan pengujian.

b. Pelatihan Model:
ARIMA: Model ARIMA dilatih dengan menggunakan paket pmdarima di Python.
LSTM: Model LSTM dilatih dengan menggunakan framework TensorFlow di Python.

c. Evaluasi Model:
Metrik evaluasi seperti Mean Absolute Error (MAE), Mean Squared Error (MSE), Root Mean Squared Error (RMSE), dan R-squared digunakan untuk menilai kinerja model.
Prediksi model dibandingkan dengan data aktual untuk memverifikasi keakuratan model.

d. Visualisasi Hasil:
Grafik time series digunakan untuk memvisualisasikan prediksi model dan membandingkannya dengan data aktual.

## Evaluation

Metrik evaluasi untuk model time series seperti ARIMA dan LSTM memberikan wawasan tentang keakuratan prediksi model. Mean Absolute Error (MAE) mengukur rata-rata perbedaan absolut antara nilai aktual dan prediksi, menunjukkan rata-rata kesalahan prediksi. Mean Squared Error (MSE) mengukur rata-rata kuadrat perbedaan, memberikan bobot lebih besar pada kesalahan besar. Root Mean Squared Error (RMSE) adalah akar kuadrat MSE, memberikan skala kesalahan dalam unit data asli. R-squared (R²) menunjukkan seberapa baik model menjelaskan varians data, dengan nilai mendekati 1 menunjukkan penjelasan yang baik.

![image](https://github.com/hairulysin/streamlitDashboard/assets/90087096/11a47918-1f82-4436-9fa8-c9ef780e3bae)

Metrik evaluasi untuk model time series seperti ARIMA dan LSTM memberikan wawasan tentang keakuratan prediksi model. Mean Absolute Error (MAE) mengukur rata-rata perbedaan absolut antara nilai aktual dan prediksi, menunjukkan rata-rata kesalahan prediksi. Mean Squared Error (MSE) mengukur rata-rata kuadrat perbedaan, memberikan bobot lebih besar pada kesalahan besar. Root Mean Squared Error (RMSE) adalah akar kuadrat MSE, memberikan skala kesalahan dalam unit data asli. R-squared (R²) menunjukkan seberapa baik model menjelaskan varians data, dengan nilai mendekati 1 menunjukkan penjelasan yang baik.

Kesimpulan:

Pengembangan model LSTM untuk prediksi harga minyak Brent Crude memberikan solusi yang efektif untuk menjawab kompleksitas dan dinamika data harga minyak. Model ini terbukti mampu menghasilkan prediksi yang akurat dan dapat diandalkan, sehingga dapat digunakan untuk mendukung berbagai kepentingan yang terkait dengan harga minyak.
