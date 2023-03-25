f = open(r"C:\Users\kaczb\Desktop\Physics of space and upper atmosphere\SOHO_CELIAS-PM_5MIN_13387 - Copie.txt","r")
Lines = f.readlines()
for l in range(len(Lines)):
    Lines[l] = Lines[l].split()

#print(Lines[0])

#%%

compteur = 0

file = open(r"C:\Users\kaczb\Desktop\Physics of space and upper atmosphere\SOHO_several_per_day.txt", "w")

for l in Lines:
    compteur += 1
    if compteur%26==0:   #286
        for i in range(len(l)):
            file.writelines(l[i])
            file.writelines(" ")
        file.writelines("\n")
        
#la dernière ligne est vide, à effacer