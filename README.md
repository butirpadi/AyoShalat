# AyoShalat
Aplikasi Pengingat Waktu Shalat yang di bangun menggunakan Python. Aplikasi Sederhana ini, masih dalam pengembangan, Sudah dapat digunakan, dengan beberapa toleransi ketepatan waktu.

![ayo-shalat](https://user-images.githubusercontent.com/3039273/110239515-d4a0a400-7f79-11eb-8709-161a03af465f.png)


## Instalasi

Untuk saat ini, pengembangan masih hanya di khususkan untuk pengguna Linux (khususnya ubuntu). Sebelum menggunakan aplikasi ini, perlu di install beberapa module. Lakukan langkah-langkah berikut, lewati jika ada module yang telah terinstall.

```
sudo apt install python3 python3-pip
```

setelah module python telah terinstall jalankan perintah berikut ini:

```
pip3 install pyside6 pathlib
```

## Running
Untuk menjalankan aplikasi ini cukup dengan men-double click pada file start.py, atau melalui terminal pada directory aplikasi ini dengan perintah:

```
python start.py
```

agar aplikasi dapat di running secara global, maka perlu dibuatkan link, ketikkan perintah berikut :

```
sudo ln -s /path-ke-folder/start.py /usr/bin/ayoshalat
```

maka cukup dengan perintah berikut, aplikasi dapat di running secara global.

```
ayoshalat
```



