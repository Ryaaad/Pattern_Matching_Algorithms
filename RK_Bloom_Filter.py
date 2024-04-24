def hachBase101(motif):
    hash=0
    for i in motif:
     hash=hash + ord(i)
    hash = hash % 101
    return hash
    
def hachBase202(motif):
    hash=0
    for i in motif:
     hash=hash + ord(i)
    hash = hash % 202 + 101
    return hash

def hachBase298(motif):
    hash=0
    for i in motif:
     hash=hash + ord(i)
    hash = hash % 298 + 202
    return hash


def create_Bloom_Filter(motifs):
   bm=[0]*500
   for motif in motifs : 
       for index in [hachBase101(motif),hachBase202(motif),hachBase298(motif)]:
         bm[index]=1
   return bm

def Rabin_Karp(text,bm,motifs):
    n=len(text) ; m=len(motifs[0])
    nbr_combarison=0; faux_vrai=0
    occ={motif:[] for motif in motifs }
    i=0
    while i<n-m : 
      found=True
      for index in hachBase101(text[i:i+m]),hachBase202(text[i:i+m]),hachBase298(text[i:i+m]):
         if bm[index]==0 : 
            found=False
            break
      if not found:
         i=i+1
      else:
         found=False 
         for motif in motifs:
          if motif[0:m] == text[i:i+m]:
             found=True
             occ[motif[0:m]].append(i)
         i=i+1    
         if found : 
          faux_vrai=faux_vrai+1
    return occ ,faux_vrai

motifs=["xzr","axa","aaa","daa","cdx"]
bm=create_Bloom_Filter(motifs)
text="axaabdaafgddikjhnkcdczkaaaaabd"
occ,faux_vrai=Rabin_Karp(text,bm,motifs)

print(occ,faux_vrai)
