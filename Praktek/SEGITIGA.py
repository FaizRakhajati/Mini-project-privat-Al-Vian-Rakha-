tinggi = int(input("masukkan tinggi: "))
counter = 1
while counter <= tinggi :
    print(" " + "Dewdudu "*(counter))
    counter += 1
tinggi = int(input("Masukkan tinggi: "))
panjang = int(input("Masukkan lebar: "))
counter2 = 1
while counter2 <= tinggi: 

    counter1 = 1
    while counter1 <= panjang :
        print("* ",end="")
        counter1 += 1
        counter2 += 1
        print("") 

panjang = int(input("Masukkan panjang : "))
counter1 = 1
tinggikali2 = panjang*2
while counter1 <= tinggikali2:
    if counter1 == tinggikali2:
        print("* " * panjang) 
    else:
        print("* ")
    counter1 += 1
panjang = int(input("Masukkan panjang yg diinginkan : ")) 
lebar = int(input("Masukkan Lebar yg diinginkan  : "))

counter_panjang = 1
while counter_panjang <= panjang:
    counter_lebar = 1
    titik = ""
    while counter_lebar <= lebar:
        
        if counter_panjang == 1 or counter_panjang == panjang or counter_lebar == 1 or counter_lebar == lebar:
            titik += ". "
        else:
          
            titik += "  " 
        counter_lebar += 1
    print(titik)
    counter_panjang += 1
