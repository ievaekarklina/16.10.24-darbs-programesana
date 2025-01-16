 #1. uzdevums

saraksts = []

for i in range(5):
    skaitlis = int(input("Ievadi skaitli: "))
    saraksts.append(skaitlis)

saraksts = saraksts[1:-1]

print("Atlikusī saraksts:", saraksts)


#2.uzdevums

saraksts = []


for i in range(5):
    skaitlis = int(input("Ievadi skaitli: "))
    saraksts.append(skaitlis)

summa = sum(saraksts)  # izvada skaitļus un aprēkina
print("Saraksta elementu summa ir:")


#3.uzdevums

saraksts = []

for i in range(10):
    skaitlis = int(input("Ievadi skaitli: "))
    saraksts.append(skaitlis)

para_skaitli = 0
nepara_skaitli = 0
for skaitlis in saraksts:
    if skaitlis % 2 == 0:
        para_skaitli += 1
    else:
        nepara_skaitli += 1

print("Pāra skaitļu skaits:", para_skaitli)
print("Nepāra skaitļu skaits:", nepara_skaitli)


#4.uzdevums

saraksts = []

for i in range(10):
    skaitlis = int(input("Ievadi skaitli: "))
    saraksts.append(skaitlis)


meklejams_skaitlis = int(input("Ievadi skaitli, kuru vēlies atrast: "))

if meklejams_skaitlis in saraksts:
    print("Skaitlis ir sarakstā.")
else:
    print("Skaitlis nav sarakstā.")
    
    
    #6.uzdevums

print("Ievadiet 7 vārdus:")


vardi = []


for i in range(7):
    vards = input(f"Ievadiet vārdu {i + 1}: ") 
    vardi.append(vards)  

garakais_vards = vardi[0]  

for vards in vardi:
    if len(vards) > len(garakais_vards): 
        garakais_vards = vards 
        
