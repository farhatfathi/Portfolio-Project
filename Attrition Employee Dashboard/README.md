# Proyek Akhir: Menyelesaikan Permasalahan Perusahaan Edutech

## Business Understanding
Perusahaan Edutech menghadapi tantangan besar terkait tingginya tingkat attrition (pengunduran diri) karyawan. Hal ini berdampak langsung terhadap stabilitas tim, biaya rekrutmen ulang, serta menurunnya produktivitas. Untuk menciptakan strategi retensi yang lebih baik, perusahaan perlu memahami faktor-faktor penyebab attrition secara data-driven.

## Permasalahan Bisnis
1. Tingkat pengunduran diri karyawan melebihi ambang batas (>10%).
2. Tidak diketahui dengan jelas faktor-faktor yang berkontribusi terhadap keputusan resign karyawan.
3. Tidak adanya alat monitoring visual yang dapat membantu manajemen dalam menganalisis pola dan tren terkait kepuasan kerja, promosi, dan attrition.
4. Perlu adanya sistem prediksi untuk mengidentifikasi karyawan berisiko tinggi agar dapat dilakukan tindakan preventif.

## Cakupan Proyek
- Membuat model machine learning untuk memprediksi kemungkinan attrition.
- Membuat business dashboard interaktif menggunakan Tableau untuk visualisasi data HR dan insight-insight penting.
- Memberikan insight dari data HR yang relevan terhadap attrition.
- Menyusun rekomendasi strategis berdasarkan hasil analisis data.

## Persiapan

### Sumber data  
Dataset yang digunakan adalah dataset yang dikumpulkan oleh HR berisi informasi karyawan seperti umur, penghasilan, jabatan, kepuasan kerja, hingga riwayat promosi, dan status attrition nya. Data diperoleh melalui link berikut: 
https://github.com/dicodingacademy/dicoding_dataset/tree/main/employee

### Setup Environment
**Setup Environment - Shell/Terminal**
pip install pipenv
pipenv install
pipenv shell
pip install -r requirements.txt

### Menjalankan File Prediksi

**Struktur Folder**
Pastikan file berikut berada dalam satu folder:

```
├── app.py
├── logreg_model.pkl
├── robust_scaler.pkl
├── minmax_scaler.pkl
├── README.md
├── (venv/)
```

**Cara Menjalankan Aplikasi**

1. Aktifkan virtual environment (jika belum aktif):

```bash
source venv/bin/activate   # Untuk Mac/Linux
venv\Scripts\activate      # Untuk Windows
```

2. Jalankan Streamlit

```bash
streamlit run app.py
```

Jika berhasil, Streamlit akan membuka browser secara otomatis atau menampilkan URL lokal seperti:

```
Local URL: http://localhost:8501
```

## Business Dashboard

Business dashboard dibuat menggunakan **Tableau** dan berfungsi sebagai alat visualisasi untuk memahami pola-pola dalam data HR terkait employee attrition. Dashboard ini menyajikan data dalam bentuk grafik interaktif, KPI card, dan filter yang dapat membantu manajemen dalam mengambil keputusan strategis. Link Dashboard bisa diakses melalui: 

https://public.tableau.com/app/profile/muhammad.fathi.farhat/viz/EmployeeAttritionOverview_17473666306570/Dashboard1

**Fitur-fitur utama dalam dashboard:**
Fitur yang ditampilkan pada dashboard adalah fitur yang berkorelasi besar terhadap attrition rate. Info tersebut diperoleh dari feature importance yang sudah dilakukan sebelumnya. Berikut fitur-fitur yang digunakan:
- **Attrition Overview:**  
  - Attrition Rate
  - Attrition Percentage
  - Attrition Count.
- **Attrition by Demographic:** 
  - Age Range
  - Marital Status
- **Attrition by Tenure & Experience:** 
  - Years with Current Manager
  - Years Since Last Promotion
- **Attrition by Job & Work:** 
  - Number of Companies Worked
  - Department
  - Job Involvement
  - Over Time

Dashboard ini memungkinkan stakeholder untuk:
- Memantau kondisi organisasi
- Menemukan potensi penyebab attrition
- Melakukan drill-down pada kelompok karyawan tertentu yang berisiko tinggi

## Conclusion

Telah dilakukan pembuatan sistem prediksi employee attrition di perusahaan dengan menggunakan model Linear Regression untuk meninjau feature importance yang sangat mempengaruhi tingginya attrition rate. Di samping itu, dashboard dibuat dengan Tableau Public untuk menunjukkan korelasi attrition karyawan terhadap beberapa fitur yang paling mempengaruhi.

Berdasarkan analisis visual dari **Employee Attrition Dashboard**, berikut adalah insight utama dan rekomendasi action items yang dapat dilakukan untuk **menurunkan attrition rate**.

### Insight Utama
1. **Rentang Usia Rentan (25–34 tahun)**
   - Usia 25–29: 41 orang
   - Usia 30–34: 44 orang
   - Kelompok usia ini paling banyak mengalami attrition.
2. **Status Pernikahan**
   - Single: 52,51% dari total attrition
   - Menikah: 34,64%
   - Bercerai: 12,85%
3. **Promosi dan Hubungan dengan Manajer**
   - 83 orang belum pernah dipromosikan dalam 1 tahun terakhir.
   - 59 orang baru 0 tahun dengan manajer saat ini.
   - Terdapat hubungan antara kurangnya promosi & hubungan manajer dengan attrition.
4. **Jumlah Perusahaan Sebelumnya**
   - Attrition tertinggi pada karyawan yang telah bekerja di >1 perusahaan sebelumnya.
5. **Departemen**
   - Sales: 36,87% dari total attrition.
   - R&D: 59,78%
   - HR: 3,35%
6. **Job Involvement**
   - Level 2 (Medium Low): 30,73%
   - Level 3 (Medium High): 51,40%
   - Job involvement yang kurang maksimal menjadi penyebab potensial.
7. **Overtime**
   - 54,75% dari karyawan yang keluar mengalami lembur.
   - Korelasi kuat antara beban kerja dan attrition.

---

### Rekomendasi Action Items

1. Program Retensi Usia Produktif (25–34)
    - Buat jalur karier jelas dan transparan.
    - Tawarkan mentoring dan pelatihan skill baru.
    - Tambahkan tunjangan untuk mendukung fase hidup (subsidi pernikahan, perumahan, kesehatan mental).

2. Engagement untuk Karyawan Single
    - Buat kegiatan komunitas internal dan klub hobi.
    - Perkuat keterikatan emosional terhadap perusahaan.

3. Evaluasi dan Tingkatkan Proses Promosi
    - Tetapkan indikator kinerja untuk promosi secara transparan.
    - Lakukan review karier setiap 6–12 bulan.

4. Pelatihan dan Retensi Manajer
    - Latih manajer baru dalam komunikasi dan coaching.
    - Karyawan baru atau dengan manajer baru perlu onboarding khusus.

5. Penanganan Khusus untuk Departemen Sales
    - Audit beban kerja dan target penjualan.
    - Tambahkan insentif jangka panjang dan work-life balance.

6. Tingkatkan Job Involvement
    - Libatkan karyawan dalam pengambilan keputusan.
    - Berikan tanggung jawab yang menantang dan bermakna.

7. Kontrol Lembur dan Workload
    - Tetapkan batas maksimal overtime mingguan.
    - Terapkan fleksibilitas kerja (WFH/hybrid/flexible hours).

8. Onboarding untuk Karyawan dengan Riwayat Frequent Switching
    - Perjelas role dan ekspektasi sejak awal.
    - Fokus pada integrasi kultural dan kepuasan awal kerja.