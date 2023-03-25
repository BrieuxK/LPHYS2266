#format : jour heure densité distance latitude
f = open(r"C:\Users\kaczb\Desktop\Physics of space and upper atmosphere\SOHO_CELIAS-PM_5MIN_13387 - Copie.txt","r")
Lines = f.readlines()
for l in range(len(Lines)):
    Lines[l] = Lines[l].split()
    
new = open(r"C:\Users\kaczb\Desktop\Physics of space and upper atmosphere\SOHO_final.txt", "w")

for i in range(len(Lines)):
    new.writelines(Lines[i][2])
    new.writelines(" ")
    new.writelines(Lines[i][3])
    new.writelines(" ")
    new.writelines(Lines[i][4])
    new.writelines(" ")
    new.writelines("\n")