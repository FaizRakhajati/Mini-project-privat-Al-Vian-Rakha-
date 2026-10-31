menu_makanan = [["Nasi Goreng",     12000],
                ["Bakmi Goreng",    14000],
                ["Kwetiaw Goreng",  14000],
                ["Es Teh",           3000]]
pesanan = []
def tabel_makanan(x) :
    header1 = "No."
    header2 = "Menu makanan"
    header3 = "Harga"
    print(f"{header1:3} {header2:25} {header3:10}")
    counter = 1
    for i in x : 
        print(f"{counter:3} {i[0]:25} Rp{i[1]:8}")
        counter += 1

def tabel_pesanan(x):
    print(f"List pesanan :")
    if not (x):
        print("1.")
    counter = 1
    for i in x :
        print(f"{counter:2}. {i[0]:20} {i[1]:8}")
        counter += 1

def tambah_pesanan(x,y) :
    tabel_makanan(x)
    print()
    tabel_pesanan(y)
    print("---------------------------------")
    pilihan = int(input("Masukan Nomor Menu Makanan :"))
    jumlah = int(input("Masukan Jumlah yang Dipesan : "))
    total = jumlah * x[pilihan -1][1]
    y.append([x[pilihan-1][0],jumlah,total])
    return y
while True :
    tabel_makanan(menu_makanan)
    print()
    tabel_pesanan(pesanan)
    print("--------------------")
    print("Mau makan apa?")
    print("A. Tambah Pesanan")
    print("B. Edit Pesanan")
    print("C. Hapus Pesanan")
    print("D. Bayar Pesanan")
    print("E. Keluar")
    pilihan = input(">> ").upper()

    match pilihan :
        case "A":
            pesanan = tambah_pesanan(menu_makanan,pesanan)
        case "B" :
            pass
        case "C" :
            pass
        case "D" :
            pass
        case "E" :
            exit()
        case _ :
            print("Tidak valid \n\n\nTekan Enter untuk melanjutkan")
            input