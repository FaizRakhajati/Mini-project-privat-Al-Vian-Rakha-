Satuan = input("Pilih satuan suhu awal : \nA. Celsius \nB. Reamur \nC. Fahrenheit \nD. Kelvin \n").upper()
Awal = float(input("Masukkan nominal Suhu Awal: "))
Akhir = input("Pilih satuan suhu awal : \nA. Celsius \nB. Reamur \nC. Fahrenheit \nD. Kelvin \n").upper()
# match (Satuan,Akhir) :
#     case (x,y) if x == "A" and y == "B" :
#         hasil = 4/5 * Awal
#     case (x,y) if x == "A" and y == "C" :
#         hasil = Awal * 9/5 + 32
#         print(f"{hasil}")
#     case (x,y) 
#     case _ :
#         print("tidak valid")
match Satuan :
    case "A" :
        match Akhir :
            case "A" :
                hasil = Awal
            case "B" :
                hasil = 4/5 * Awal
            case "C" :
                hasil = Awal * 9/5 + 32
            case "D" :
                hasil =  Awal + 273.15
    case "B" :
        match Akhir :
            case "A" :
                hasil = Awal * 5/4 
            case "B" :
                hasil = Awal
            case "C" :
                hasil = (Awal*9/4) + 32
            case "D" :
                hasil = 5/4 * Awal + 273
    case "C" :
        match Akhir :
            case "A" :
                hasil = (Awal - 32) * 5
            case "B" :
                hasil = (Awal - 32) * 4/9
            case "C" :
                hasil = Awal
            case "D" :
                 hasil = (Awal - 32) * 5/9 + 273,15
    case "D" :
        match Akhir :
            case "A" :
                hasil = Awal - 273.15
            case "B" :
                hasil = 4/5 * (Awal - 273.15)
            case "C" :
                 hasil = 1.8 * (Awal - 273.15) + 32
            case "D" :
                hasil = Awal
    case _ :
        print("tidak valid")

print(f"{hasil}")




