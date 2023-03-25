f = open(r"C:\Users\kaczb\Desktop\Physics of space and upper atmosphere\SOHO_CELIAS-PM_5MIN_13387 - Copie.txt","r")
Lines = f.readlines()
for l in range(len(Lines)):
    Lines[l] = Lines[l].split()

#print(Lines[0])

#%%
jour = Lines[0][0]
dernier = Lines[-1][0]

compteur = 0

file = open(r"C:\Users\kaczb\Desktop\Physics of space and upper atmosphere\SOHO_final.txt", "w")

for l in Lines:
    compteur += 1
    if compteur%286==0:
        for i in range(len(l)):
            file.writelines(l[i])
            file.writelines(" ")
        file.writelines("\n")
        
#la dernière ligne est vide, à effacer        

#%%
"""
jour = Lines[0][0]
#286 données par jour

file = xxx

for i in range(len(Lines[0])):
    file.writelines(Lines[0][i])
    file.writelines(" ")
file.writelines("\n")

count = 0

for l in Lines:
    if l[0] != jour :
        for i in range(len(l)):
            file.writelines(l[i])
            file.writelines(" ")
        file.writelines("\n")
        jour = l[0]
"""
