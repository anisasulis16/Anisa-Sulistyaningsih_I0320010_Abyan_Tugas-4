#Rencana Kualifikasi Kursus Online
#aplikasi operator logika


print("PENDAFTARAN KURSUS ONLINE")
print(".........................")
print("Pengujian Calon Siswa")

#Menginputkan semua data
nama_calon = input("Siapa nama kamu: ")
usia_calon = input("Berapa usia kamu?: ")
kualifikasi = input("Apakah Anda sudah lulus kualifikasi (Y/T)? : ")

#Syarat
usia_calon = 21

if usia_calon >= 21:
    usia_calon = True
else:
    usia_calon = False

Y = True

print(".....................")
print("HASIL : ")
if usia_calon >= 21 and Y:
    print(nama_calon,",","Anda dapat mendaftar di kursus.")
else:
    print(nama_calon,",","Anda tidak dapat mendaftar di kursus.")


