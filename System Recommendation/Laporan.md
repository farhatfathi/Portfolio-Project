# Laporan Proyek Machine Learning - Muhammad Fathi Farhat

## Project Overview

Sistem rekomendasi telah menjadi salah satu teknologi penting dalam industri hiburan, terutama dalam menyajikan konten yang relevan bagi pengguna di platform seperti Netflix, Amazon Prime, atau Disney+. Pada proyek ini, saya membangun **sistem rekomendasi film berbasis hybrid** yang menggabungkan pendekatan **content-based filtering** dan **text similarity** untuk menghasilkan rekomendasi yang lebih akurat.

Masalah utama yang dihadapi oleh pengguna layanan streaming adalah terlalu banyaknya pilihan film yang tersedia tanpa kejelasan mana yang relevan dengan preferensi mereka. Oleh karena itu, sistem rekomendasi bertujuan untuk mempersonalisasi pengalaman menonton setiap pengguna berdasarkan kesamaan konten dan preferensi sebelumnya.

Referensi:
- Ricci, F., Rokach, L., & Shapira, B. (2011). *Introduction to Recommender Systems Handbook*. Springer.
- Gómez-Uribe, C. A., & Hunt, N. (2016). The Netflix Recommender System: *Algorithms, Business Value, and Innovation*. *ACM Transactions on Management Information Systems*, 6(4).

---

## Business Understanding

### Problem Statements
1. Bagaimana memberikan rekomendasi film yang relevan berdasarkan konten seperti genre, bintang film, dan deskripsi?
2. Bagaimana menggabungkan beberapa metode rekomendasi untuk meningkatkan relevansi dan personalisasi?

### Goals
1. Menghasilkan daftar film yang mirip berdasarkan genre, pemeran utama, dan deskripsi cerita.
2. Menggabungkan hasil dari pendekatan content-based (genre & cast) dan TF-IDF (description) menggunakan weighted hybrid model untuk meningkatkan akurasi.

### Solution Approach
- **Solution 1**: Menggunakan *CountVectorizer* untuk memproses gabungan kolom `stars` dan `genre`, lalu menghitung kemiripan menggunakan *cosine similarity*.
- **Solution 2**: Menggunakan *TF-IDF Vectorizer* pada kolom `description` dan menghitung kemiripan teks menggunakan *linear kernel*.
- **Solution 3 (Hybrid)**: Menggabungkan kedua kemiripan (content-based dan TF-IDF) dengan pembobotan proporsional untuk menghasilkan skor akhir.

---

## Data Understanding

Dalam proyek ini, digunakan **tiga dataset utama** yang diperoleh dari Kaggle:

1. **n_movies.csv**  
   Dataset ini merupakan hasil penggabungan dan seleksi film dari platform netflix.  
   - URL/Tautan Sumber Data: https://www.kaggle.com/datasets/narayan63/netflix-popular-movies-dataset
   - Jumlah data: 9957 baris  
   - Jumlah kolom: 9 
   - Kondisi Data: Terdapat missing value pada kolom selain `title`, `description`, `stars`, dan beberapa data duplikat.
   - Fitur-fitur:
     - `title`: judul film
     - `year`: tahun rilis
     - `certificate`: rating umur
     - `genre`: genre film, dapat berisi lebih dari satu kategori dalam satu string
     - `rating`: rating (skor) film
     - `description`: sinopsis atau ringkasan cerita film
     - `duration`: durasi film dalam menit (beberapa data memiliki nilai “min” tanpa angka)
     - `stars`: daftar pemeran utama, dalam bentuk string list
     - `votes`: jumlah vote penonton terhadap film (tipe awal: string)

2. **Netflix_Dataset_Movie.csv**  
   Dataset ini berisi metadata film dari platform Netflix.  
   - URL/Tautan Sumber Data: https://www.kaggle.com/datasets/rishitjavia/netflix-movie-rating-dataset
   - Jumlah data: 17,8rb baris  
   - Jumlah kolom: 3  
   - Kondisi Data: Tidak terdapat null values dan duplicate.
   - Fitur-fitur:
     - `Movie_Id`: ID film 
     - `Year`: tahun rilis
     - `Name`: nama film

3. **Netflix_Dataset_Rating.csv**  
   Dataset ini merupakan rating dari user terhadap film di Netflix.  
   - URL/Tautan Sumber Data: https://www.kaggle.com/datasets/rishitjavia/netflix-movie-rating-dataset
   - Jumlah data: 17,3jt baris 
   - Jumlah kolom: 3  
   - Kondisi Data: Tidak ditemukan missing value maupun duplikat.
   - Fitur-fitur:
     - `User_ID`: ID pengguna
     - `Rating`: rating (skor) film
     - `Movie_Id`: ID film

---

### Penjelasan Tambahan

Untuk memahami data secara lebih mendalam, dilakukan eksplorasi awal dengan analisis statistik sederhana dan visualisasi frekuensi genre serta distribusi jumlah pemeran utama per film.  

Hasilnya menunjukkan variasi genre yang cukup luas dengan beberapa genre populer seperti Action, Drama, dan Comedy mendominasi dataset. Terdapat null values dengan jumlah yg cukup besar, sehingga perlu berhati-hati dalam penanganannya pada tahap persiapan data.

---

## Data Preparation

Tahapan data preparation dilakukan secara berurutan untuk mempersiapkan data agar siap digunakan pada tahap modeling untuk masing-masing dataset:

### Preparating Metadata Film 

Pada tahap ini, dilakukan pembersihan dataset `n_movies.csv` sebagai metadata film.

1. **Pengecekan Data Duplikat**  
   Melakukan cek baris yang memiliki judul film sama. Hasilnya menunjukkan data tidak memiliki data duplikat.

2. **Mengganti Tipe Data `votes` menjadi Integer**  
   Nilai pada kolom `votes` yang sebelumnya bertipe string dibersihkan (menghapus tanda koma) dan dikonversi ke integer.

3. **Menghapus kolom yang tidak relevan**
   Kolom `year`, `certificate`, `duration` dihapus karena tidak relevan dengan sistem rekomendasi yang akan dibuat dan mengandung jumlah missing value yang tinggi.

4. **Menangani Missing Value**  
   melakukan dropna() untuk seluruh missing value.

5. **Melakukan Reset Index dan Fillna('')**  
   melakukan reset index pada dataset agar tidak mengganggu analisis dan memastikan kekosongan data pada kolom `description` terisi.

### Preprocessing untuk Persiapan Modelling

1. **Eksrtraksi Fitur dengan TF-IDF Vectorization pada `description`**  
   Menggunakan `TfidfVectorizer(stop_words='english')` untuk menangkap informasi semantik dari deskripsi film.

2. **Parsing `stars`**  
   Kolom `stars` yang berupa string list dikonversi menggunakan `literal_eval`.

3. **Memperbaiki Kolom `stars`**  
   Memperbaiki entri pada kolom `stars` dengan asumsi jika merupakan list maka menggabung entri serta membuang spasi dan koma berlebih jika ada.

### Preparating Ground Truth 

Pada tahap ini, dilakukan merge dan preparation data `Netflix_Dataset_Movie.csv` dan` Netflix_Dataset_Rating.csv` sebagai ground truth / data user untuk melakukan evaluasi model.

1. **Merge Antar Dataset**  
   Menggabungkan kedua dataset `Netflix_Dataset_Movie.csv` dan `Netflix_Dataset_Rating.csv` berdasarkan `Movie_ID` secara *right join* sebagai `Merged_df`.

2. **Seleksi dan Mengubah Nama Kolom**  
   Memilih kolom tertentu pada `Merged_df` dan mengubah nama kolom agar sama dengan metadata film (dataset awal) untuk proses merge selanjutnya.

3. **Transformasi nilai `rating`**  
   Pada kolom `rating`, dilakukan transformasi penggantian skala rating menjadi 1-10 agar sesuai dengan metadata film.

3. **Merge Terakhir dengan Metadata Film.**  
   Merge final metadata film dan ground truth berdasarkan `title` secara *inner join*.

---

## Modelling

### Model 1: Content-Based Filtering (CountVectorizer)

**Cara kerja:**  
- Membentuk representasi teks dari `genre` + `stars`  
- Menyiapkan kolom 'stars' dan 'genre' menjadi soup
- Vectorizer akan menghasilkan vektor fitur dari kata-kata unik  
- Kemiripan dihitung menggunakan cosine similarity antar film  
- Film yang paling mirip (dalam skor tertinggi) dengan input film akan direkomendasikan

**Contoh Output:**  

Input:

    recommender = cast_genre_recommender(df)
    recommender("The Crown")

Output:

|     | title                             | genre                        | stars                                                                 |
|-----|-----------------------------------|------------------------------|-----------------------------------------------------------------------|
| 0   | The Crown                         | Biography, Drama, History    | Claire Foy, Olivia Colman, Imelda Staunton, Matt Smith                |
| 1   | Victoria & Abdul                  | Biography, Drama, History    | Stephen Frears, |, Stars:, Judi Dench, Ali Fazal                     |
| 2   | The Most Hated Woman in America   | Biography, Drama, History    | Tommy O'Haver, |, Stars:, Melissa Leo, Brandon Mychal Smith       |
| 3   | Answer for Heaven                 | Drama                        |                                                                       |
| 4   | Black Heart                       | Drama                        |                                                                       |
| 5   | Broadchurch                       | Crime, Drama, Mystery        | David Tennant, Olivia Colman, Jodie Whittaker, Arthur Darvill         |
| 6   | Medici                            | Biography, Drama, History    | Daniel Sharman, Alessandra Mastronardi, Synnøve Karlsen               |
| 7   | Versailles                        | Biography, Drama, History    | George Blagden, Alexander Vlahos, Tygh Runyan, Evan Williams          |
| 8   | Borgia                            | Biography, Drama, History    | Mark Ryder, Isolda Dychauk, Diarmuid Noyes, John Doman                |
| 9   | Flowers                           | Comedy, Drama                | Sophia Di Martino, Olivia Colman, Julian Barratt                      |

---
### Model 2: Hybrid Model (Content-Based + TF-IDF)

**Cara kerja:**  
- Skor kemiripan dihitung dari dua sumber: metadata dan deskripsi film  
- Menyiapkan kolom 'stars' dan 'genre' menjadi soup
- Cosine similarity dari `soup` dan `description` digabungkan dengan bobot seimbang  
- Memberikan hasil rekomendasi yang mempertimbangkan aspek teks cerita dan fitur utama film

**Contoh Output:**  

Input:

    get_hybrid = hybrid_recommender(df)    
    get_hybrid("The Crown", top_n=10)

Output:

|     | title                             | genre                        | stars                                                                 |
|-----|-----------------------------------|------------------------------|-----------------------------------------------------------------------|
| 0   | The Crown                         | Biography, Drama, History    | Claire Foy, Olivia Colman, Imelda Staunton, Matt Smith                |
| 1   | Victoria & Abdul                  | Biography, Drama, History    | Stephen Frears, |, Stars:, Judi Dench, Ali Fazal                     |
| 2   | Medici                            | Biography, Drama, History    | Daniel Sharman, Alessandra Mastronardi, Synnøve Karlsen               |
| 3   | Versailles                        | Biography, Drama, History    | George Blagden, Alexander Vlahos, Tygh Runyan, Evan Williams          |
| 4   | The Most Hated Woman in America   | Biography, Drama, History    | Tommy O'Haver, |, Stars:, Melissa Leo, Brandon Mychal Smith       |
| 5   | Answer for Heaven                 | Drama                        |                                                                       |
| 6   | Black Heart                       | Drama                        |                                                                       |
| 7   | Munich: The Edge of War           | Biography, Drama, History    | Christian Schwochow, |, Stars:, George MacKay, Jannis Niewöhner        |
| 8   | Stavisky                          | Biography, Crime, Drama      | Alain Resnais, |, Stars:, Jean-Paul Belmondo, Charles Boyer       |
| 9   | The Tudors                        | Drama, History, Romance      | Jonathan Rhys Meyers, Henry Cavill, Anthony Brophy                   |

Output model berupa daftar rekomendasi film teratas (top-N) berdasarkan kemiripan skor hybrid tersebut terhadap film input.

### Penjelasan Tambahan
- Project ini menyajikan dua solusi utama (content-based dan text similarity) yang kemudian digabung menjadi solusi hybrid.  
- Kelebihan hybrid model adalah menggabungkan keunggulan masing-masing metode, tetapi penentuan bobot masih dapat dioptimalkan lebih lanjut.  
- Kekurangan pendekatan saat ini adalah belum mempertimbangkan data rating pengguna secara eksplisit untuk rekomendasi berbasis collaborative filtering.

---

## Evaluation

Pada tahap ini dilakukan evaluasi terhadap kedua model yang telah dibuat sebagai komparasi dalam menentukan model dengan kinerja terbaik.

### Teknik Evaluasi yang Digunakan

Evaluasi dilakukan dengan membandingkan hasil rekomendasi model dengan data rating pengguna sebagai ground truth. Fokus evaluasi adalah untuk mengetahui seberapa baik sistem dapat merekomendasikan film yang benar-benar disukai oleh pengguna.

Dua metrik utama yang digunakan adalah:

- **Precision@10**
- **Recall@10**

Nilai dari kedua metrik tersebut dirata-rata ke seluruh pengguna untuk menghasilkan:

- **Average Precision@10 (AP@10)**
- **Average Recall@10**

---

### Metrik yang Digunakan

#### 1. **Average Precision@10 (AP@10)**

Mengukur seberapa akurat rekomendasi model, yaitu proporsi dari 10 film teratas yang benar-benar relevan atau disukai oleh pengguna.

**Cara kerja:**

- Untuk setiap user, ambil 10 rekomendasi teratas dari model.
- Bandingkan dengan daftar film yang pernah diberi rating tinggi (≥ 4) oleh user.
- Hitung precision per user, lalu ambil rata-rata seluruh user.

#### 2. **Average Recall@10**

Mengukur seberapa banyak item relevan (film yang disukai) berhasil direkomendasikan dari semua item relevan yang tersedia.

**Cara kerja:**

- Identifikasi semua film yang disukai user (rating ≥ 4).
- Lihat dari 10 rekomendasi, berapa banyak yang termasuk film relevan tersebut.
- Hitung recall per user, lalu ambil rata-rata semua user.

---

### Hasil Evaluasi

**1. Model Content-Based Recommender**

Input:

    evaluate_content_based_recommender(merged_df_final, get_recommendations, top_n=10)

Output:

```text
Content-Based Evaluation  
Average Precision@10: 0.0000  
Average Recall@10: 0.0000
```

**2. Model Hybrid Recommender**

Input:

    evaluate_hybrid_recommender(merged_df_final=merged_df_final, get_hybrid_recommendations_fn=get_hybrid_recommendations, top_n=10, n_users=100)

Output:

```text
Content-Based Evaluation  
Average Precision@10: 0.0071  
Average Recall@10: 0.0533
```

---

### Kesimpulan

Sistem rekomendasi ini dibangun berdasarkan problem statement:  
**"Bagaimana merekomendasikan film yang relevan kepada pengguna berdasarkan preferensi film yang telah mereka tonton?"**

Berdasarkan eksperimen, hybrid model yang menggabungkan informasi genre-pemeran (metadata) dan deskripsi cerita (semantik teks) memberikan performa yang lebih baik. Namun, nilai AP dan Recall masih rendah, menunjukkan bahwa model belum sepenuhnya menangkap preferensi pengguna secara akurat. Hal ini diduga karena kurangnya data film yang ada.

**Saran pengembangan ke depan:**
- Integrasi data interaksi pengguna secara eksplisit (collaborative filtering)
- Optimasi bobot pada model hybrid
- Meningkatkan kualitas fitur dengan embedding teks atau metadata enrichment
- Mencari dataset rating film yang lebih luas.

---