# Best Meeting Time Finder
Script ini membantu menemukan waktu terbaik untuk ketemuan di antara orang-orang sibuk dengan jadwal padat. Cukup masukkan jadwal dalam format JSON yang sudah ditentukan, dan program akan menghitung waktu kosong yang sesuai untuk semua pihak yang terlibat.

## Fitur
- Menemukan waktu kosong pada hari dan jam tertentu di antara jadwal berbagai orang.
- Memungkinkan konfigurasi jam kerja harian, sehingga dapat disesuaikan dengan kebutuhan (default: jam 7:00 hingga 23:00).
- Hasil output menunjukkan waktu kosong per hari.

## Struktur Proyek
template.json: Template jadwal yang harus diisi dengan jadwal orang-orang yang terlibat.
possibility.py: Script utama untuk memproses jadwal dan menentukan waktu ketemuan terbaik.

## Prasyarat
Python 3.x
Pastikan pustaka json dan datetime sudah tersedia (kedua pustaka ini adalah pustaka standar Python).

## Cara Menggunakan
Isi Jadwal di template.json dengan format sebagai berikut:
```bash
{
  "person1": [
    {"hari": "Senin", "jam": "09:00 - 10:30", "kegiatan":"-"},
    {"hari": "Selasa", "jam": "13:00 - 14:30", "kegiatan":"-"}
  ],
  "person2": [
    {"hari": "Senin", "jam": "10:00 - 11:00", "kegiatan":"-"},
    {"hari": "Rabu", "jam": "15:00 - 16:30", "kegiatan":"-"}
  ]
}
```
- hari: Hari dalam seminggu (gunakan format Indonesia: Senin, Selasa, Rabu, dst.)
- jam: Waktu mulai dan berakhir dalam format HH:MM - HH:MM.

## Jalankan Script
Setelah mengisi jadwal di template.json, jalankan script possibility.py dengan perintah berikut:

```bash
python possibility.py
```

## Contoh Output
Jadwal kosong pada hari Senin:
09:00 - 09:30
10:30 - 11:00
Jadwal kosong pada hari Selasa:
07:00 - 09:00
11:00 - 13:00
...

## Catatan
Slot waktu "12:00 - 12:30" akan otomatis diabaikan sebagai waktu kosong, sehingga waktu istirahat standar terhindarkan.
Jika tidak ada jadwal kosong yang cocok untuk suatu hari, pesan yang sesuai akan ditampilkan.

## Penyesuaian
Range Jam: Anda dapat mengatur jam kerja dengan mengubah nilai start_hour dan end_hour dalam fungsi find_free_slots.
Interval Waktu: Default interval waktu adalah 30 menit, tetapi Anda dapat mengubahnya di fungsi time_range.

## Kontribusi
Jika Anda memiliki ide untuk meningkatkan proyek ini, jangan ragu untuk membuat pull request atau mengirimkan masukan.
