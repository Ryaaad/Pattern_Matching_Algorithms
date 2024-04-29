# Pattern Matching Algorithms

## Single Pattern Matching

### Boyer-Moore:
**Principle:** We start by comparing the last index (j) of the pattern with the index i + j of the text. If these two elements are equal, we step back one position by comparing index (j - 1) of the pattern with i + (j - 1) of the text. We repeat this process until we reach a difference or index 0 of the pattern. If these elements are equal, we have found an occurrence of the pattern; otherwise, we calculate how far we should move using Boyer-Moore to calculate the shift in case of failure, using a dictionary table that contains all the last occurrences of all characters at each index.

**Example** : motif = "abbcab" text="abcfvabbcablmùdxeggse"
step 1 : creating the dictionary table (let's name it d): 
| index | dictionary            |
|-------|-----------------------|
| 0     | /                     |
| 1     | {"a":0}               |
| 2     | {"a":0,"b":1}         |
| 3     | {"a":0,"b":2}  .      |
| 4     | {"a":0,"b":2,"c":3}   |
| 5     | {"a":4,"b":2,"c":3}   |

step 2 : search : 
abcfvabbcablmùdxeggse        i=0
abbcab                       j=5

text[i+j]!=motif[j] so we calculate shift we have d[5]["a"]=4 so i=1

abcfvabbcablmùdxeggse        i=1
 abbcab                      j=5
text[i+j]==motif[j]

abcfvabbcablmùdxeggse        i=1
 abbcab                      j=4
 
text[i+j]==motif[j]

abcfvabbcablmùdxeggse        i=1
 abbcab                      j=3
 
text[i+j]!=motif[j] so we calculate shift we have d[3]["v"] dont exist so i=5
abcfvabbcablmùdxeggse        i=5
     abbcab                  j=5
text[i+j]==motif[j] so j=j-1

 abcfvabbcablmùdxeggse       i=5
      abbcab                 j=4
      
text[i+j]==motif[j] so j=j-1

 abcfvabbcablmùdxeggse       i=5
      abbcab                 j=3
      
text[i+j]==motif[j] so j=j-1

 abcfvabbcablmùdxeggse       i=5
      abbcab                 j=2

text[i+j]==motif[j] so j=j-1

 abcfvabbcablmùdxeggse       i=5
      abbcab                 j=1
text[i+j]==motif[j] so j=j-1

 abcfvabbcablmùdxeggse       i=5
      abbcab                 j=0

we found the motif !
    
## Multiple Pattern Matching

### Rabin-Karp
**Principle:** We start by applying one or more hash functions on the patterns and the current window of text. At each iteration, we compare the hash value of the current window with that of the patterns. In case of equality, we compare the characters of the window with the patterns to confirm the match.

### Aho-Corasick
**Principle:** The algorithm begins by constructing a tree from the patterns to search for. Each node in the tree represents a prefix of one or more patterns. We perform the output function if we are at the end of a pattern. Then, we move to the failure function. It is computed for each node in the tree. This function helps make efficient transitions between nodes during the search process (where to go if a match fails at a certain node). The function returns the longest prefix of the tree that is a suffix of the pattern for the search. Starting from the root of the tree, it moves through the tree based on the characters of the text. If the current character exists in the path, we continue to the next node; otherwise, we use the failure function.
