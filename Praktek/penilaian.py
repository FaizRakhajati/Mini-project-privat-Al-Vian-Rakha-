# nama = input("Masukkan nama \t: ")
# prodi = input("Masukkan prodi \t: ")

# benda = input("Masukkan nama benda \t: ")
# stok = int(input("Masukkan stok barang \t: "))
# harga = int(input("Masukkan harga \t: "))
# Rating = float(input("Masukkan rating \t: "))
# print(f"="*20)
# print(f"{benda:^20}")
# print(f"-"*20)
# print(f"Stok \t: {stok} \nharga \t: Rp {harga:,.2f} \nrating \t: {Rating:,.2f}")
# print("="*20)

# nilai = int(input("Masukkan nilai : "))

# if nilai >= 75 :
#     print("Lulus")
# else:
#     print("Remidi")

# barang = input("Masukkan nama barang \t: ")
# harga = int(input("Masukkan harga barang \t: "))
# jumlah = int(input("Masukkan jumlah barang \t: "))
# total = harga*jumlah
# print("="*50)
# if total > 150000:
#     total2 = total*0.1
#     total3 = total - total2
#     print(f"{barang:<12}: Rp{harga:<11}")
#     print(f"Diskon(10%) : Rp{total2:<11}")
#     print("-"*50)
#     print(f"total : Rp{total3:<11}")
# else:
#     print(f"{barang:<10} : {total:<10}")
#     print(f"Diskon(0%) : Rp{0:<10}")
#     print("-"*50)
#     print(f"total : Rp{total:<10}")

# usia = int(input("Masukkan usia : "))

# if usia < 0:
#     print("tidak valid")
# elif  usia < 5 :
#     print("Balita")
# elif usia <13 :
#     print("Anak anak")
# elif usia < 18 :
#     print("Remaja")
# elif usia < 60:
#     print("Dewasa")
# elif usia > 60:
#     print("lansia")
# else:
#     print("tidak valid")

# opsi = input("Pilih jenis operasi : \nA. Pertambahan \nB. Pengunrangan \nC. Perkalian \nD. perbagian \n").upper()
# angka1 = int(input("Masukkan angka pertama: "))
# angka2 = int(input("Masukkan angka kedua: "))

# if opsi == "A":
#     total = angka1 + angka2
#     print(total)
# elif opsi == "B":
#     total = angka1 - angka2
#     print(total)
# elif opsi == "C":
#     total = angka1 * angka2
#     print(total)
# elif opsi == "D":
#     total = angka1 / angka2
#     print(total)
# angka = int(input("Masukkan angka: "))

# if angka < 0 and angka % 2 == 0 :
#     print("Bilangan negatif genap")
# elif angka < 0 and angka % 2 == 1 :
#     print("Bilangan negatif ganjil")
# elif angka > 0 and angka % 2 == 0 :
#     print("Bilangan positif genap")
# elif angka > 0 and angka % 2 == 1 :
#     print("Bilangan positif ganjil")
# elif angka == 0:
#     print("Netral")

# angka1 = int(input("Masukkan angka: "))
# angka2 = int(input("Masukkan angka: "))

# if angka1 % 2 == 0 and angka2 % 2 == 0:
#     print("sama")
# elif angka1 % 2 == 1 and angka2 % 2 == 1:
#     print("sama")
# elif angka1 % 2 == 1 and angka2 % 2 == 0:
#     print("beda")
# elif angka1 % 2 == 0 and angka2 % 2 == 1:
#     print("beda")
# --- INPUT DATA BARANG ---
# # Aturan 1: User dapat input 2 nama barang, 2 harga, dan 2 jumlah beli
# nama_barang1 = input("Masukkan nama barang 1: ")
# harga_barang1 = int(input(f"Masukkan harga satuan {nama_barang1}: "))
# jumlah_barang1 = int(input(f"Masukkan jumlah beli {nama_barang1}: "))

# nama_barang2 = input("Masukkan nama barang 2: ")
# harga_barang2 = int(input(f"Masukkan harga satuan {nama_barang2}: "))
# jumlah_barang2 = int(input(f"Masukkan jumlah beli {nama_barang2}: "))

# # --- INPUT KUPON & MEMBERSHIP ---
# # Aturan 2 & 3: User dapat input status kupon hemat dan membership
# kupon = input("Apakah memiliki kupon hemat? (y/n): ").lower()
# membership = input("Apakah memiliki membership? (y/n): ").lower()

# # Hitung subtotal awal untuk masing-masing barang dan total keseluruhan
# subtotal1 = harga_barang1 * jumlah_barang1
# subtotal2 = harga_barang2 * jumlah_barang2
# total_belanja = subtotal1 + subtotal2

# # --- PERHITUNGAN DISKON ---
# persen_diskon = 0

# # Aturan 4: Jika total belanja melebihi 500.000, mendapat diskon 10%
# if total_belanja > 500000:
#     persen_diskon += 10

# # Aturan 5: Kupon hemat memotong 5%, berefek 2x lipat (10%) jika memiliki membership
# if kupon == 'y':
#     if membership == 'y':
#         persen_diskon += 10
#     else:
#         persen_diskon += 5

# # Aturan 6: Membership memotong 10% dari total harga
# if membership == 'y':
#     persen_diskon += 10

# # Perhitungan potongan diskon dan total akhir tiap barang (Aturan 7)
# potongan1 = subtotal1 * (persen_diskon / 100)
# total_akhir1 = subtotal1 - potongan1

# potongan2 = subtotal2 * (persen_diskon / 100)
# total_akhir2 = subtotal2 - potongan2

# # --- OUTPUT / STRUK BELANJA ---
# # Tips 2: Menggunakan f-string untuk alignment justify agar tampilan rapi dan lurus
# print("\n" + "="*60)
# print(f"{'STRUK PEMBAYARAN TOKO':^60}")
# print("="*60)
# print(f"{'Nama Barang':<15}{'Harga':<12}{'Jumlah':<8}{'Diskon':<12}{'Total':<13}")
# print("-"*60)
# print(f"{nama_barang1:<15}{harga_barang1:<12,}{jumlah_barang1:<8}{potongan1:<12,}{total_akhir1:<13,}")
# print(f"{nama_barang2:<15}{harga_barang2:<12,}{jumlah_barang2:<8}{potongan2:<12,}{total_akhir2:<13,}")
# print("-"*60)

# # Aturan 8 (Opsional): Menampilkan total persenan diskon akumulasi
# print(f"{'Total Sebelum Diskon':<35}: Rp {total_belanja:,}")
# print(f"{'Total Persenan Diskon':<35}: {persen_diskon}%")
# print(f"{'Total Potongan Diskon':<35}: Rp {(potongan1 + potongan2):,}")
# print(f"{'Total Akhir yang Dibayar':<35}: Rp {(total_akhir1 + total_akhir2):,}")
# print(("="*60),f"\n Harga 1 : {harga_barang1} \n Harga 2 : {harga_barang2} \n Total : Rp{total_akhir2 + total_akhir1}")

# while True:
#     angka = int(input("Masukkan angka: "))
 
#     if angka % 2 == 0:
#         print("genap") 
#     elif angka % 2 == 1:
#         print("ganjil")

#     ulang = input("Apakah mau di ulang [Y/N]: ").upper()
#     if ulang == "Y":
#         continue
#     elif ulang == "N":
#         break

# hasil = 0
# while True:
#     angka = int(input("Masukkan angka: "))
#     hasil += angka
#     if angka == 0:
#         break
#     else:
#         continue
# print(hasil)

# hasil = 0
# counter = 0
# while True:
#     angka = int(input("Masukkan angka: "))
#     counter += 1
#     if angka == 0:
#         break
#     elif counter % 3 == 0:
#         continue
#     hasil += angka
# print(hasil)

# bintang = int(input("Masukkan jumlah bintang: "))
# for i in range (bintang):
#     print ("* ", end="")


# panjang = int(input("Masukkan panjang: "))
# lebar = int(input("Masukkan lebar: "))
# for i in range (lebar):
#     for j in range (panjang):
#         print ("* ", end = " ")
#     print()

# angka = int(input("Masukkan angka: "))
# for i in range (1,11):
#     perkalian = angka * i
#     print(f"{angka} * {i} = {perkalian}")

# buah = ["Pisang","Nanas","Jambu","Pepaya","Mangga","Kelapa"]
# buah.append("melon")
# buah.pop(1)
# buah [0] = "Leci"
# buah.insert(2,"Semangka")
# buahbaru = ["apel","ceri","alpukat"]
# buah.extend(buahbaru)
# print(buah[2:7])

# buku = [["Nabil"],
#         ["King prabs"],
#         ["Matdas"]]
# while True:
#     print("+-" + "-"*3 +"---"+"-"*25 + "-+" )
#     print(f"{"| No. | Nama Buku  ":<25} {"|":>9}")
#     print("+-" + "-"*3 +"---"+"-"*25 + "-+" )

#     counter = 0
#     while counter < len(buku):
#         nomor = str(counter + 1)
#         judul = buku[counter][0]
#         print("| " + " "*(3-len(nomor)) + nomor + " | " + judul + " "*(25 - len(judul)) + " | ")
#         counter += 1
#     print("+-" + "-"*3 +"---"+"-"*25 + "-+" )

#     opsi = input("A. Tambah B. Hapus C. Edit : ").upper()
#     if opsi == "A":
#          nabilzz = [input("Masukkan buku yg kw maw: ")]
#          buku.append(nabilzz)   
#     elif opsi == "B":
#         prabs = int(input("Mau hapus buku berapa: "))
#         buku.pop(prabs - 1)
#     elif opsi == "C":
#         nabils = int(input("Mau edit buku berapa: ")) -1
#         prabz = [input("Masukkan buku baru: ")]
#         buku[nabils] = (prabz)
#     else:
#         exit()
 

# tambah_buku = []
# counter = 0
# while True :
#     print("="*50)
#     print(f"{"| No. | Nama Buku  ":<25} {"|":>24}")
#     print("="*50)
#     buku = input("Masukkan buku: ")
#     tambah_buku.append(buku)
#     counter += 1
#     print(f"{"| . | {tambah_buku}  ":<25} {"|":>24}")
#     continue
#     break

# string1 = "Artificial Neural Network Multi Layer Perceptron" # Pecah Berdasarkan Spasi
# string2 = "Saltcheese,2000,1.345,Rating saya kasih satu karena udah bosan" # Pecah Berdasarkan Koma
# string3 = "RTX 5090\t100000000\t10.00\tBonus CPU Intel Celeron untuk paket Gaming Turbo" # Pecah berdasarkan Tab

# str1 = string1.split(" ")
# print(str1)
# str2 = string2.split(",")
# print(str2)
# str3 = string3.split("\t")
# print(str3)

# data = [
#     ["01","Sarapan Nasi Kuning",5000],
#     ["01","Beli Galon",20000],
#     ["01","Mie Ayam TinTon",15000],
#     ["02","Cilor",2000],
#     ["03","Paket Data",50000]
# ]
# for i in data :
#     tanggal = i[0]
#     makanan = i[1]
#     harga = i[2]

#     print((tanggal),(makanan),(harga),sep=",")


# bulan = ["Januari","Februari","Maret","April","Mei","Juni","Juli","Agustus","September","Oktober","November","Desember"]
# buln = input("Masukkan bulan: ").capitalize()
# if buln in bulan:
#     thn = int(input("Masukkan tahun: "))
#     print(f"Pengeluarag {buln} {thn}.csv")
# else :
#     print("Bulan tidak valid")

nilai_siswa = {"Andre" : 78, "Hana" : 90, "Tono" : 67}
while True :
    print("="*20)
    print(f"| {"nama":<7} | {"nilai":^7} |")
    print("="*20)
    for i in nilai_siswa:
        print(f"| {i:<7} | {nilai_siswa[i]:^7} |")
    print("="*20)

    print("Mw apa? ")
    print("A. Tambah \nB. Hapus \nC. Edit")
    pilihan = input(">> ").upper()

    if pilihan == "A":
        tambah_nama = input("Masukkan nama : ").capitalize()
        tambah_nilai = int(input("masukkan nilai : "))
        if tambah_nilai not in nilai_siswa :
            nilai_siswa[tambah_nama] = tambah_nilai
        else:
            print("sudah ada")
    elif pilihan == "B":
        key_hapus = input("masukkan nama : ").capitalize()
        if key_hapus in nilai_siswa :
            nilai_siswa.pop(key_hapus)
        else :
            print("DATA TIDAK DITEMUKAN")
    elif pilihan == "C":
        edit_nama = input("Masukkan nama : ").capitalize()
        edit_nilai = int(input("Masukkan nilai : "))
        if edit_nama in nilai_siswa : 
            nilai_siswa[edit_nama] = edit_nilai
        else:
            print("Data tidak ditemukan")
    else:
        exit()