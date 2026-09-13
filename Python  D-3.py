nilai = 40

match nilai :
    case x if x == 100 :
        print("Nilai sempurna lulus")
    case x if x >= 90 :
        print("Lulus, nilai sudah bagus")
    case x if x >= 75 :
        print("Lulus belum maksimal tingkatkan lagi")
    case _ :
        print("Remed lu lawak")

print("Program selesai")
