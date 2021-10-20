ValidationMac = ["A", "B", "C", "D", "E",":", "F","0","1","2","3","4","5","6","7","8","9"]
listNewMac = []
mac = input("Mac:").upper()

def validation(mac):
   if(len(mac) < 17):
    print("invalido")
   else:
       print("Valido")

for i in ValidationMac:
    for j in mac:
        if(i == j):
            listNewMac.append(j)

validation(listNewMac)

