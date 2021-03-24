#Soal no 3 Operator Comparison

#berat Bagasi Pada Maskapai dalam lbs
massa = 50
#konversi lbs ke dalam kg
a = massa * 0.45    #Berat maksimal bagasi dalam kg
x = 110     #Kondisi Benda 1 dalam kg
y = 49      #Kondisi Benda 2 dalam kg

#memproses program berupa syarat berat maksimum yang diperbolehkan adalah a
programpengecekan1 = x <= a
programpengecekan2 = y <= a

#menampilkan Hasil
print('Hasil Bagasi X adalah', x, '<=', a, '=', programpengecekan1)
print('Hasil Bagasi y adalah', y, '<=', a, '=', programpengecekan2)






