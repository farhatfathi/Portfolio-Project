# Employee Attrition Prediction App

Aplikasi ini menggunakan model machine learning untuk memprediksi apakah seorang karyawan berpotensi mengalami **attrition** (berhenti bekerja) berdasarkan beberapa input fitur. Aplikasi dibangun menggunakan **Streamlit**.

## Struktur Folder

Pastikan file berikut berada dalam satu folder:

```
├── app.py
├── logreg_model.pkl
├── robust_scaler.pkl
├── minmax_scaler.pkl
├── README.md
├── (venv/)
```

## Cara Menjalankan Aplikasi

### 1. **Aktifkan virtual environment** (jika belum aktif):

```bash
source venv/bin/activate   # Untuk Mac/Linux
venv\Scripts\activate      # Untuk Windows
```

### 2. **Jalankan Streamlit**

```bash
streamlit run app.py
```

Jika berhasil, Streamlit akan membuka browser secara otomatis atau menampilkan URL lokal seperti:

```
Local URL: http://localhost:8501
```

## Cara Menggunakan Aplikasi

Setelah aplikasi terbuka:

1. **Masukkan nilai untuk fitur berikut:**
   - `Age`: Usia karyawan (18–65 tahun)
   - `Job Satisfaction`: Skor kepuasan kerja (1–4)
   - `Monthly Income`: Pendapatan bulanan (1.000–20.000)
   - `OverTime`: Apakah bekerja lembur? (Yes/No)

2. Klik tombol **Predict**.

3. Hasil prediksi akan muncul:
   - **Attrition** → kemungkinan tinggi berhenti kerja
   - **Not Attrition** → kemungkinan bertahan kerja

## Tentang Model

Model yang digunakan adalah **Logistic Regression** yang telah dilatih sebelumnya, dengan preprocessing dua tahap:

- **Robust Scaler** untuk menangani outlier
- **MinMax Scaler** untuk normalisasi

## Catatan

- Fitur lain yang dibutuhkan model (total 34 fitur) diisi dengan default `0`, kecuali fitur input yang tersedia di UI.
- Untuk hasil yang lebih akurat, disarankan menambahkan input untuk fitur penting lainnya di masa mendatang.

---