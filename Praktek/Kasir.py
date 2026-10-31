list_menu = [["Nasi Goreng",2000],["Bakmi Goreng",14000],["Kwetiaw Goreng",14000],["Capcay Goreng / Kuah",15000],["Es Teh / Panas",3000],["Es Teh Kampul / Panas",3000]]

print("+-"+"-"*3+"---"+"-"*25+"---"+"-"*10+"-+")
print("| "+"No. |"+" Menu"+" "*22+"| Harga"+" "*5+" |")
print("+-"+"-"*3+"---"+"-"*25+"---"+"-"*10+"-+")
menu = 0
while menu < len (list_menu):
    nomor = str(menu + 1)
    makanan = list_menu[menu][0]
    harga = str(list_menu[menu][1])
    print("| "+" "*(3-len(nomor))+(nomor) + " | " + makanan+" "*(25-len(makanan))+" | Rp"+" "*(8-len(harga))+harga+" | ")
    menu +=1
print("+-"+"-"*3+"---"+"-"*25+"---"+"-"*10+"-+")
menu = input("Mau makan apa hari ini? \nA.nasi goreng \nB.Bakmie Goreng \nC.Kwetiaw Goreng \nD.Capcay goreng \nE.Capcay kuah \nF.Es teh \nG.Teh panas \nH.Es teh Kampul \nI.Teh Kampul \n")
jumlah = int(input("Berapa porsi? "))



