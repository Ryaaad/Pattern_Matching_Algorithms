def hachage_Base_10(motif):
  m=len(motif)
  hached=0
  coef=1
  i=m-1
  while i>=0 :
     hached=hached+ ord(motif[i])*coef
     coef=coef*10
     i=i-1

  return hached

def hachageroulent(text,c):
   
   hached=(hachage_Base_10(text) - ord(text[0])*(10 ** (len(text)-1)) )*10 + hachage_Base_10(c)*1
   return hached

def hashed_motifs(motifs):
 hashedmotifs=[]
 for motif in motifs : 
   hashedmotifs.append([motif,hachage_Base_10(motif)])
 return  hashedmotifs

def tester(text,index,motif):
   m=len(motif)-1
   for i in range(m+1):
      if text[index+i]!=motif[i]:
         return False
   return True  

motifs=[
   "aba",
   "aaa",
   "zbc"
]
hashedmotifs=hashed_motifs(motifs)

def Rabin_Karp(text,hashedmotifs):
    n=len(text) ; k=len(hashedmotifs)
    m=len(hashedmotifs[0][0]) # come et un tableau des tableau ...
    occ={motif[0]:[] for motif in hashedmotifs }
    i=0
    while i<n-m : 
      print(f"i : {i}")
      ht=hachage_Base_10(text[i:i+m])  
      j=0
      while j<k:
       hm=hashedmotifs[j][1] 
       print(hm,ht)
       if hm==ht:
         motif=hashedmotifs[j][0]
         found=tester(text,i,motif)
         if found==True :
            occ[motif].append(i)
       j=j+1   
      i=i+1
    return occ  



occ=Rabin_Karp("aaaabaaacdbarzbc",hashedmotifs)
print(occ)