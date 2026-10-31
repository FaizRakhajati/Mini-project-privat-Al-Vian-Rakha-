class rekord :
    def __init__(self,tanggal, keterangan,nominal) :
        self.tan = tanggal
        self.ket = keterangan
        self.nom = nominal


anggaran = 3400000

bulan = None
tahun = None
 
data = [
    rekord("01", "sambal krecek", 3000)
]

def tabel() :
    global data
    global anggaran
    anggaran_sisa = anggaran
    judul = f"Catatan Pengeluaran Bulan {bulan} Tahun {tahun}"
    print(f"{judul:^75}")
    print(f"Anggaran Bulan ini = Rp {anggaran,}")
    print ("="*75)
    print(f"| {"No.":^3} | {"Tanggal":^7} | {"Keterangan":^40} | {"Nominal":^12} |")
    print("="*75)
    for i in range(len(data)) :
        print(f"| {i+1:^3} | {data[i].tan:^7} | {data[i].ket:<40} | Rp {data[i].nom:>9,} |")
        anggaran_sisa -= data[i].nom
        print("="*75)
        print(f"Sisa anggaran = Rp {anggaran_sisa:,}")
        print("="*75)
tabel()

def input_bulan_tahun ():
    global bulan, tahun
    while True:
        bulan = input("Masukkan Bulan : ").capitalize()
        if bulan not in ["Januari","Februari","Maret","April","Mei","Juni","Juli","Agustus","September","Oktober","November","Desember"] :
            print("Bulan wajib menggunakan Bahasa Indonesia")
        else:
            break

    while True:
        try:
            tahun = int(input("Masukkan Tahun : "))
            break
        except ValueError :
            print("Tahun wajib menggunakan Bilangan Bulat")
