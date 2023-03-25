import matplotlib.pyplot as plt

#format :densité distance latitude

#f = open(r"C:\Users\kaczb\Desktop\Physics of space and upper atmosphere\SOHO_true_final_several.txt", "r")


f = open(r"C:\Users\kaczb\Desktop\Physics of space and upper atmosphere\SOHO_final_le_vrai.txt", "r")
Lines = f.readlines()
for l in range(len(Lines)):
    Lines[l] = Lines[l].split()
    
density = []
distance = []
latitude = []

for l in Lines:
    density.append(float(l[0]))
    distance.append(float(l[1]))
    latitude.append(float(l[2]))
    
print(len(density))
#%%

plt.plot(distance,density)
plt.title("Corrélation entre la densité des protons et la distance Soleil-satellite")
plt.xlabel("Distance ($10^{6}km$)")
plt.ylabel("Densité des protons en $cm^{-3}$")

#%%
plt.plot(latitude,density) #[:165]
plt.title("Corrélation entre la densité des protons et la latitude héliographique du satellite")
plt.xlabel("Latitude (degrés)")
plt.ylabel("Densité des protons en $cm^{-3}$")
