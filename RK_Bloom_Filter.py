import time  

def hachBase101(motif): # 1ere Fonction de hachage : base 101
    hash = 0  
    coef = 1  
    for i in motif:
        hash = hash + ord(i) * coef 
        coef = coef * 101  
    hash = hash % 101 
    return hash

def hachBase202(motif): # 2eme Fonction de hachage : base 202, mais j'ajoute 101 pour garantir des valeurs distinctes de celles de la première fonction de hachage.
    hash = 0  
    coef = 1 
    for i in motif:
        hash = hash + ord(i) * coef  
    hash = hash % 202 + 101  # Calcule hachage modulo 202 et ajoute 101
    return hash

def hachBase298(motif): # 3eme Fonction de hachage : base 298 mais j'ajoute 202 pour garantir des valeurs distinctes de celles de la première fonction de hachage.
    hash = 0  
    for i in motif:
        hash = hash + ord(i)  
    hash = hash % 298 + 202  # Calcule hachage modulo 298 et ajoute 202
    return hash

def create_Bloom_Filter(motifs):  # Crée un filtre de Bloom à partir des motifs donnés
    bm = [0] * 500  # Initialise le filtre de Bloom à un tableau de 500 éléments ( pourquoi 500 car la valure la plus grande des 3 fonction de hachage sera 499)
    for motif in motifs:
        for index in [hachBase101(motif), hachBase202(motif), hachBase298(motif)]:
            bm[index] = 1  
    return bm

def Rabin_Karp(text, bm, motifs):
    n = len(text) 
    m = len(motifs[0])
    nbr_combarison = 0  
    faux_vrai = 0 
    occ = {motif: [] for motif in motifs}  # Initialise la table des occurrences
    i = 0 
    while i < n - m + 1:
        found = True  
        for index in hachBase101(text[i:i+m]), hachBase202(text[i:i+m]), hachBase298(text[i:i+m]):
            if bm[index] == 0:  
                found = False 
                break
        if not found:
            i = i + 1 
        else:
            found = False # pour verifier faut positive
            for motif in motifs:
                j = 0
                while j < m:
                    nbr_combarison = nbr_combarison + 1 
                    if motif[j] == text[i + j]:
                        j = j + 1  
                    else:
                        break  # Sortire de la boucle quand un caractères ne correspondent pas
                if j == m:
                    occ[motif[0:m]].append(i) 
                    found = True
            i = i + 1
            if not found:
                faux_vrai = faux_vrai + 1
    return occ, faux_vrai, nbr_combarison 



# 6 &  &  verymotifBig motifveryBig & 34 & 0.8ms & 10   \\ \hline


# Définition des motifs et création du filtre de Bloom
motifs = ["veryBigmotif", "verymotifBig","motifveryBig"]
bm = create_Bloom_Filter(motifs)
text = "those Big motif was veryBigmotif but not as big as the motifveryBig so it was small but not small as verymotifBig"
debutTemps = time.time()
occ, faux_vrai, nbrcmb = Rabin_Karp(text, bm, motifs)
TempsFin = time.time()
Temps = TempsFin - debutTemps  # Calcul du temps d'exécution

print(f"---------------------------------------")
print(f"Motifs : {motifs} ")
print(f"Texte : {text} ")
print(f"Table des occurrences : {occ} ")
print(f"Nombre de comparaisons : {nbrcmb}")
print(f"Faux positifs : {faux_vrai} ")
print(f"Temps d'exécution: {Temps * 1000} ")

print(f"---------------------------------------")
