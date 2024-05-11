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
Date: Tanggal pencatatan data.
Open: Harga pembukaan perdagangan.
High: Harga tertinggi dalam satu hari perdagangan.
Low: Harga terendah dalam satu hari perdagangan.
Close: Harga penutupan perdagangan.
Volume: Volume perdagangan dalam barel.

![image](https://github.com/hairulysin/streamlitDashboard/assets/90087096/85e9a047-af49-4961-94ca-4a6f0ad32acf)

Statistik deskriptif Awal:
                                Date       Close  chg.close.         Low  \
count                            759  759.000000  759.000000  759.000000   
mean   2022-07-06 09:29:10.197628672   80.307971    0.099987   79.184269   
min              2021-01-04 00:00:00   50.230000  -17.140000   49.970000   
25%              2021-10-04 12:00:00   72.445000   -0.800000   71.480000   
50%              2022-07-07 00:00:00   79.820000    0.210000   78.760000   
75%              2023-04-08 00:00:00   88.200000    1.080000   87.230000   
max              2024-01-10 00:00:00  114.190000   50.230000  113.390000   
std                              NaN   12.323786    2.721369   12.051838   

         chg.low.        High   chg.high.  
count  759.000000  759.000000  759.000000  
mean     0.099776   81.372266    0.102385  
min    -13.990000   51.880000  -18.050000  
25%     -0.680000   73.435000   -0.575000  
50%      0.140000   80.750000    0.160000  
75%      0.995000   90.335000    0.850000  
max     49.970000  115.060000   51.880000  
std      2.562347   12.661389    2.641597  

**💡 Insight :**
Analisis mendalam menguak fluktuasi harga penutupan yang signifikan (kisaran 50.23-114.19) dan perubahannya yang dinamis (rata-rata 0.1). Hal ini menunjukkan volatilitas pasar yang perlu diwaspadai. Harga terendah (kisaran 49.97-113.39) dan perubahannya (rata-rata 0.10) mencerminkan potensi risiko penurunan harga, sedangkan harga tertinggi (kisaran 51.88-115.06) dan perubahannya (rata-rata 0.10) membuka peluang keuntungan dari kenaikan harga. Volatilitas pasar minyak Brent Crude yang kompleks ini menjadi landasan bagi perusahaan untuk mengambil keputusan strategis yang tepat dan terukur. 

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
