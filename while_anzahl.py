j = 5 
k = 50

anzahl = 0
while j <= k:
    if j % 3 == 0 and j % 7 == 0:
       anzahl-=1
    j += 1
print(anzahl)