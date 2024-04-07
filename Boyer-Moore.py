def dTable(motif):
 m = len(motif)  
 d = {}
 for j in range(m + 1):  
    d[j] = {chr(i): -1 for i in range(ord('a'), ord('z') + 1)}
    for k in range(j):  
        d[j][motif[k]] = k  # Assign k as the value for motif[k] in d[j]
 return d       

def decalage(c,d,j):
  if d[j][c]==-1:
    k=j+1
  else :
    k=j-d[j][c]  
  return k  
def BoyerMoore(motif,text,d):
 n=len(text) ; m=len(motif); i=0 ; j=m-1;
 occ=[] # var avec les index des occurences
 nbr_comp=0 # var pour calculer nbr de comparaisons
 while(i<n-m+1):
  k=0
  j=m-1
  while j>=0 :
   nbr_comp+=1 # a chaque fois en rentre dans cette boulce il y'aura une combaraison 
   if motif[j]==text[i+j]:
    j=j-1
   else:
    k=decalage(c=text[i+j],d=d,j=j)
    break; 
  if k==0:
   occ.append(i)
   i=i+1
  else:
   i=i+k 
 return occ,nbr_comp

motif = "aada"
d=dTable(motif)  # table d du motif
text = "azcdzzddaddddzddlxgsdzxdzamddzfdzxdzz"

n=len(text) 
m=(len(motif))
occurrences,nbr_comp = BoyerMoore(motif, text,d)
print(occurrences,nbr_comp)