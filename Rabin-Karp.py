import time 

def hachage(motif):  # Fonction de hachage
    m = len(motif)
    hached = 0
    coef = 1
    i = m - 1
    while i >= 0:
        hached = hached + ord(motif[i]) * coef 
        coef = coef * 10 
        i = i - 1
    return hached

def hachageroulent(text, c):  # Fonction de hachage roulent
    hached = (hachage(text) - ord(text[0]) * (10 ** (len(text) - 1))) * 10 + hachage(c) * 1
    hached = hached % 100  # Calcule le hachage final en modulo 100
    return hached

def hashed_motifs(motifs):  # Fonction qui applique la fonction de hachage sur tout les motifs et les stocke dans un dictionnaire
    hashedmotifs = []  # Initialise le tableau de dictionnaires pour assigner à chaque motif sa valeur de hachage
    for motif in motifs:
        hashedmotifs.append([motif, hachage(motif) % 100])    # Pour le hachage, j'ai utilisé une logique similaire à la base 10, mais au lieu de modulo 10, j'utilise modulo 100 pour limiter les faux positifs
    return hashedmotifs

def tester(text, index, motif, nbr_combarison):
    m = len(motif) - 1
    for i in range(m + 1):
        nbr_combarison = nbr_combarison + 1 
        if text[index + i] != motif[i]:
            return False, nbr_combarison
    return True, nbr_combarison

def Rabin_Karp(text, hashedmotifs):
    n = len(text)
    k = len(hashedmotifs)
    m = len(hashedmotifs[0][0])
    nbr_combarison = 0
    faux_vrai = 0
    occ = {motif[0]: [] for motif in hashedmotifs}  # Initialise la table des occurrences
    i = 0
    while i < n - m:
        ht = hachage(text[i:i + m]) % 100  # Hacher la fenetre courante
        j = 0
        while j < k:
            hm = hashedmotifs[j][1]
            if hm == ht:
                motif = hashedmotifs[j][0]
                found, nbr_combarison = tester(text, i, motif, nbr_combarison)  # Verifie si le motif et la fenêtre sont vraiment égaux
                if found == True:
                    occ[motif].append(i)
                else:
                    faux_vrai = faux_vrai + 1
            j = j + 1
        i = i + 1
    return occ, faux_vrai, nbr_combarison

motifs = ["cat", "dog","rab","bit"]
hashedmotifs = hashed_motifs(motifs)
text = "a cat and a dog were walking when they saw some birds that were eating fish mais ils didnt see any rabits maybe the rabbits were killed"
debutTemps = time.time()
occ, faux_vrai, nbr_combarison = Rabin_Karp(text, hashedmotifs)
TempsFin = time.time() 
Temps = TempsFin - debutTemps  # Calcul du temps d'exécution

print(f"---------------------------------------")
print(f"Motifs : {motifs} ")
print(f"Text : {text} ")
print(f"Table des occurrences : {occ} ")
print(f"Nombre de comparaisons : {nbr_combarison}")
print(f"faux_vrai: {faux_vrai} ")
print(f"Temps d'execution: {Temps * 1000 } ms ")

print(f"---------------------------------------")
