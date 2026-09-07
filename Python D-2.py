pilihan = input("Pilih jenis Operasi: \nA. Pertambahan \nB. Pengurangan \nC. Perkalian \nD. Pembagian \nE. Modulus \nF. Perpangkatan \n=").upper()
var1 = float(input("Masukkan Angka Pertama: "))
var2 = float(input("Masukkan Angka Kedua: "))

if pilihan == "A" : 
    nilai_akhir = var1+var2
    print("nilai akhir :", nilai_akhir)
elif pilihan == "B" :
    nilai_akhir = var1-var2
    print("nilai akhir :", nilai_akhir)
elif pilihan == "C" :
    nilai_akhir = var1*var2
    print("nilai akhir :", nilai_akhir)
elif pilihan == "D" :
    nilai_akhir = var1/var2
    print("nilai akhir :", nilai_akhir)
elif pilihan == "E" :
    nilai_akhir = var1%var2
    print("nilai akhir :", nilai_akhir)
elif pilihan == "F" :
    nilai_akhir = var1**var2
    print("nilai akhir: ", nilai_akhir)
else :
    print("pilihan tidak valid")

