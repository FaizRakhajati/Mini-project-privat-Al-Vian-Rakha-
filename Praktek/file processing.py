# data = [
#     ["01","Sarapan Nasi Kuning",5000],
#     ["01","Beli Galon",20000],
#     ["01","Mie Ayam TinTon",15000],
#     ["02","Cilor",2000],
#     ["03","Paket Data",50000]
# ]

# with open("FileMaterikingprabsss.csv","w",encoding="utf-8") as ffile :
#     for i in range(len(data)) :
#         print(data[i][0] , data[i][1] , data[i][2], sep="," , file=ffile)
data = []
with open("FileMaterikingprabsss.csv","r",encoding="utf-8") as ffile :
    for baris in ffile :
        baris.strip()
        tanggal , nama , harga = baris.split(",")
        
        harga = int(harga)
        nama = (nama)
         
        data.append([ tanggal , nama, harga ])

print(data)