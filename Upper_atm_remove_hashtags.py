import pandas

f = open(r"C:\Users\kaczb\Desktop\Physics of space and upper atmosphere\SOHO_CELIAS-PM_5MIN_13387.txt","r")
new = open(r"C:\Users\kaczb\Desktop\Physics of space and upper atmosphere\SOHO_CELIAS-PM_5MIN_13387 - Copie.txt","w")

Lines = f.readlines()
count=0

for l in Lines:
    if (l[0] != '#') and not l[0].isalpha():
        new.writelines(l)