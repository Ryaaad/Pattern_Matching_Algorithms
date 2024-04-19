import timeit

# Fonction qui crée la table d (table d du motif)
def dTable(motif):
    m = len(motif)  
    d = {} 
    for j in range(m + 1):  
        d[j] = {} # initialise la case j de la table d     
        for k in range(j):  
          d[j].setdefault(motif[k], k) 
    return d       

def decalage(c, d, j):
    if c not in d[j]: # vérifie si c n'est pas une clé dans d[j]
        k = j + 1
    else :
        k = j - d[j][c]  
    return k  

def BoyerMoore(motif, text, d):
    n = len(text); m = len(motif); i = 0; j = m - 1 
    occ = [] # variable avec les index des occurrences
    nbr_comp = 0 # variable pour calculer le nombre de comparaisons
    while(i < n - m + 1):
        k = 0 # variable qui vas indiquer la quantité de décalage
        j = m - 1
        while j >= 0:
            nbr_comp += 1 # à chaque fois que nous entrons dans cette boucle, il y aura une comparaison
            if motif[j] == text[i + j]:
                j = j - 1
            else: 
                k = decalage(c=text[i + j], d=d, j=j)
                break  # Sortie de la 1ere boucle (j) pour déterminer le décalage de la fenêtre 
        if k == 0:
            occ.append(i)
            i = i + 1 
        else:
            i = i + k 
    return occ, nbr_comp

motif = "oui"
d = dTable(motif) 
text = "no_no_n__"
n = len(text) 
m = len(motif)

occurrences, nbr_comp = BoyerMoore(motif, text, d)

print(f"---------------------------------------")
print(f"Motif : {motif} ")
print(f"Text : {text} ")
print(f"Table des occurrences : {occurrences} ")
print(f"Nombre de combarison : {nbr_comp}")
print(f"---------------------------------------")



