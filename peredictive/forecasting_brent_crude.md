# Laporan Proyek Machine Learning - Hairul Yasin
## Domain Proyek

Beberapa perusahaan aspal curah menghadapi tantangan fluktuasi harga minyak yang kompleks. Fluktuasi ini langsung memengaruhi biaya produksi aspal, yang pada gilirannya menentukan harga jual yang optimal. Saat ini, perusahaan bergantung pada data historis harga Argus (melalui berlangganan) dan tren harga minyak untuk memprediksi harga aspal. Namun, keterbatasan data Argus hanya mencakup gambaran masa lalu tanpa kemampuan untuk memproyeksikan masa depan, menyulitkan perusahaan dalam pengambilan keputusan strategis yang tepat. Solusi inovatif datang dalam bentuk Machine Learning (ML). ML mampu menganalisis data historis harga minyak dan aspal, serta mempertimbangkan faktor-faktor lain seperti kondisi ekonomi global dan permintaan pasar. Hasilnya adalah prediksi harga aspal yang lebih akurat dan terarah. Diharapkan, dengan prediksi ini, perusahaan dapat menetapkan harga jual yang kompetitif, mengelola stok dengan lebih efisien, dan meminimalkan risiko keuangan.

## Business Understanding

### Problem Statements
Fluktuasi harga minyak dunia yang tak terduga menjadi momok bagi industri aspal. Hal ini menyebabkan perusahaan kesulitan dalam memprediksi biaya produksi dan penetapan harga yang tepat. Penelitian ini hadir untuk membawa solusi inovatif dengan model machine learning (ML) akan membantu perusahaan dalamm pengambilan keputusan

**Goals** :
Penelitian ini bertujuan membantu industri aspal menghadapi masalah fluktuasi harga minyak dunia. Dengan membuat model prediksi menggunakan machine learning untuk membantu perusahaan memprediksi biaya produksi dan menetapkan harga dengan lebih tepat. Dengan prediksi yang lebih baik, diharapkan perusahaan dapat mengambil keputusan yang lebih baik pula.

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

1. Pengubahan dtype pada variabel
   -  Pengubahan dtype pada variabel mengacu pada proses mengubah tipe data dari suatu variabel menjadi tipe data yang berbeda, agar datanya konsisten.
   -  Kegunaannya adalah untuk mempermudah analisis data time series, dan memungkinkan model untuk memproses data secara akurat dalam konteks data
   -  Teknik ini dilakukan pada kolom Date
2. Memilih variabel target
   - Menentukan kolom dalam dataset yang akan diprediksi oleh model (Variabel y)
   - Kegunaanya ialah untuk mengarahkan model untuk fokus pada prediksi harga minyak, yang merupakan tujuan utama dari analisis
   - Dilakukan pada kolom Close data, karena analisis ini untuk memprediksi harga penuutupan minyak.
3. Menganalisis Statistik Deskriptif Awal
   - Deskrispi Statistik ialah metode analisis data yang menggunakan konsep statistik untuk menjelaskan pola, tren, dan distribusi data tanpa analisis mendalam.
   - Kegunaannya adalah untuk pemahaman awal tentang data sebelum analisis lebih lanjut, ini membantu dalam identifikasi pola atau anomali dalam data.
   - Tahapan ini dilakukan pada seluruh dataset harga minyak.
4. Visualiasi time series 
   - Visualisasi time series ialah tahapan melihat tren dan pola harga selama periode waktu tertentu.
   - Kegunaannya ialah untuk mengidentifikasi tren dan pola harga secara visual, kemudian untuk melihat potensi musiman dalam data harga aspal
   - Dilakukan pada kolom Close dan kolom Date dalam dataset
5. Melakukan differencing data
   - Differencing ialah proses untuk mengurai nilai-nilai dalam data time series dengan nilai sebelumnya.
   - Kegunaannya ialah untuk memenuhi asumsi stasioneritas dalam model ARIMA, sehingga model bekerja lebih baik. kemudian untuk menghilangkan trend dan pola musiman dalam data.
   - Dilakukan pada kolom Close, target variabelnya.
6. Membagi data training dan testing 
   - Membagi dataset mebnjadi set training untuk melatih model, sedangkan set test digunakan untuk mengevaluasi performa model.
   - Kegunaanya untuk mencegah model overfitting, dimana model terlalu terfokus pada set training dan tidak dapat menghasilkan prediksi yang akurat pada data baru.
   - Dilakukan pada kolom Close dan Date.
7. Menyiapkan data dalam format yang sesuai untuk model ARIMA dan LSTM
   - Mengubah format data agar sesuai dengan kebutuhan model ARIMA dan LSTM. Model ARIMA membutuhkan data yang stasioner, sedangkan model LSTM membutuhkan data yang diubah menjadi time steps dan feature vectors. Time steps adalah representasi data time series dalam bentuk urutan data pada interval waktu tertentu. Feature vectors adalah representasi data dalam bentuk vektor yang berisi nilai numerik untuk setiap fitur atau variabel.
   - Tahapan ini berguna untuk membantu model dalam memahami struktur dan karakteristik data
   - Dilakukan pada:
      a. ARIMA: Kolom Close dalam dataset harga aspal setelah differencing.
      b. LSTM: Kolom Close dan kolom Date dalam dataset harga aspal, diubah menjadi time steps dan feature vectors.
     
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

Metrik evaluasi untuk model time series seperti ARIMA dan LSTM memberikan wawasan tentang keakuratan prediksi model. 

1. Mean Absolute Error (MAE) mengukur rata-rata perbedaan absolut antara nilai aktual dan prediksi, menunjukkan rata-rata kesalahan prediksi.
   
   **MAE = \frac{1}{n} \sum_{i=1}^{n} |y_i - \hat{y}_i|**
   
   di mana:
      - n adalah jumlah data
      - y_i adalah nilai aktual pada data ke-i
      - \hat{y}_i adalah prediksi model pada data ke-i

3. Mean Squared Error (MSE) mengukur rata-rata kuadrat perbedaan, memberikan bobot lebih besar pada kesalahan besar.
   
   **MSE = \frac{1}{n} \sum_{i=1}^{n} (y_i - \hat{y}_i)^2**
   
   di mana:
      - n adalah jumlah data
      - y_i adalah nilai aktual pada data ke-i
      - \hat{y}_i adalah prediksi model pada data ke-i
  
4. Root Mean Squared Error (RMSE) adalah akar kuadrat MSE, memberikan skala kesalahan dalam unit data asli.
   
   **RMSE = \sqrt{MSE}**
   
   di mana:
      - MSE adalah Mean Squared Error

5. R-squared (R²) menunjukkan seberapa baik model menjelaskan varians data, dengan nilai mendekati 1 menunjukkan penjelasan yang baik.
   
   **R^2 = 1 - \frac{\sum_{i=1}^{n} (y_i - \hat{y}_i)^2}{\sum_{i=1}^{n} (y_i - \bar{y})^2}**
   
   di mana:
      - n adalah jumlah data
      - y_i adalah nilai aktual pada data ke-i
      - \hat{y}_i adalah prediksi model pada data ke-i
      - \bar{y} adalah rata-rata nilai aktual

![image](https://github.com/hairulysin/streamlitDashboard/assets/90087096/11a47918-1f82-4436-9fa8-c9ef780e3bae)

Metrik evaluasi untuk model time series seperti ARIMA dan LSTM memberikan wawasan tentang keakuratan prediksi model. Mean Absolute Error (MAE) mengukur rata-rata perbedaan absolut antara nilai aktual dan prediksi, menunjukkan rata-rata kesalahan prediksi. Mean Squared Error (MSE) mengukur rata-rata kuadrat perbedaan, memberikan bobot lebih besar pada kesalahan besar. Root Mean Squared Error (RMSE) adalah akar kuadrat MSE, memberikan skala kesalahan dalam unit data asli. R-squared (R²) menunjukkan seberapa baik model menjelaskan varians data, dengan nilai mendekati 1 menunjukkan penjelasan yang baik.

**Kesimpulan:**

Pengembangan model LSTM untuk prediksi harga minyak Brent Crude memberikan solusi yang efektif untuk menjawab kompleksitas dan dinamika data harga minyak. Model ini terbukti mampu menghasilkan prediksi yang akurat dan dapat diandalkan, sehingga dapat digunakan untuk mendukung berbagai kepentingan yang terkait dengan harga minyak.
