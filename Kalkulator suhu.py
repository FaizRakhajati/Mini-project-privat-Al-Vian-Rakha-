Satuan = input("Pilih satuan suhu awal : \nA. Celsius \nB. Reamur \nC. Fahrenheit \nD. Kelvin \n").upper()
Awal = float(input("Masukkan nominal Suhu Awal: "))
Akhir = input("Pilih satuan suhu awal : \nA. Celsius \nB. Reamur \nC. Fahrenheit \nD. Kelvin \n").upper()

if Satuan == "A" and Akhir == "D" : 
    hasil = Awal + 273.15
    print(f"{hasil} Kelvin")
elif Satuan == "A" and Akhir == "C" :
    hasil = Awal * 9/5 + 32
    print(f"{hasil} Celsius")
elif Satuan == "A" and Akhir == "B" :
    hasil = Awal * 4/5
    print(f"{hasil} Reamur")
elif Satuan == "B" and "A" :
    hasil = Awal * 5/4 
    print(f"{hasil} Celsius")
elif Satuan == "B" and "C" :
    hasil = (Awal*9/4) + 32
    print(f"{hasil} Fahrenheit")
elif Satuan == "B" and "D" :
    hasil = 5/4 * Awal + 273
    print(f"{hasil} Kelvin")
elif Satuan == "C" and "A" :
    hasil = (Awal - 32) * 5
    print(f"{hasil} Celsius")
elif Satuan == "C" and "B" :
    hasil = (Awal - 32) * 4/9
    print(f"{hasil} Reamur")
elif Satuan == "C" and "D" :
    hasil = (Awal - 32) * 5/9 + 273,15
    print(f"{hasil} Kelvin")
elif Satuan == "D" and "A" :
    hasil = Awal - 273.15
    print(f"{hasil} Celsius")
elif Satuan == "D" and "B" :
    hasil = 4/5 * (Awal - 273.15)
    print(f"{hasil} Reamur")
elif Satuan == "D" and "C" :
    hasil = 1.8 * (Awal - 273.15) + 32
    print(f"{hasil} Fahrenheit")
elif Satuan == "A" and "A" :
    print("tidak valid")
elif Satuan == "B" and "B" :
    print("tidak valid")
elif Satuan == "C" and "C" :
    print("tidak valid")
elif Satuan == "D" and "D" :
    print("tidak valid")
else :
    print("Tidak ada")



