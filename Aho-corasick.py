import time

class TrieNode(object):    
    def __init__(self, char: str):
        self.char = char
        self.finished = False
        self.children= {} # J'ai utilisé un dictionnaire ici pour faciliter l'acces.
        self.output = [] # J'ai ajouté 'output' qui va contenir le mot courant. 
        self.fail = None
        

       # La fonction pour ajouter un mot dans le tri. À chaque ajout, le mot courant est ajoute a l'attribut 'output'.
def addText(root, string):

    node = root
    for i in range(len(string)):
        char = string[i]
        if char not in node.children:
            node.children[char] = TrieNode(char)
            node.output = string[0:i]
        node = node.children[char]
    node.output=string
    node.finished = True

# Cette fonction sert a initialiser mon trie avec '/' (equivalent a root (epsilon)) apr ajouter les motifs
def initializeTri(strings):
    root = TrieNode('/')
    for string in strings:
        addText(root,string)
    return root

# Cette fonction retourne le plus long préfixe qui est également un suffixe du motif pour un nœud. Ses paramètres sont root: le trie, et text: le mot courant du nœud.
def findLongestPrefixInRootForNode(root, text):
    node = root  # Ceci est un nœud temporaire juste pour ne pas perdre le nœud racine.
    for char in text:
        if char not in node.children:  # Si le caractère n'est pas dans les fils du nœud, alors nous retournons le nœud. Sinon, nous continuons dans le fils correspondant au caractère.
            return node
        else: 
            node = node.children[char]
    return node


# Pour créer les fonctions d'échec, j'ai utilisé un tableau comme une file pour parcourir les nœuds en niveau (BFS).
def createFailureLinks(root):
    queue = []
    root.fail = root  # Le nœud d'échec de la racine est la racine elle-même.
    for child in root.children.values():  # Pour les premiers fils, la fonction d'échec doit retourner vers la racine.
        queue.append(child)
        child.fail = root
    while queue:  # On parcourt l'arbre niveau par niveau (BFS).
        node = queue.pop(0)
        for child in node.children.values():
            queue.append(child)
            child.fail = findLongestPrefixInRootForNode(root, child.output[1:len(child.output)])  # Pour les autres, il faut d'abord chercher le plus long préfixe qui est un suffixe du motif pour un nœud.
            # J'ai supprimé le premier indice de l'élément car il n'est pas nécessaire de vérifier le premier élément (car logiquement le premier élément dans l'arbre est la racine).
    return root

def ahoCorasick(text, root):
    nbrComparison = 0
    node = root
    checked = False  # Cette variable est juste pour ne pas compter le nombre de comparaisons quand on ai dans le root la premier fois avant trouver que le caractère n'existe pas (root->root)
    occurrences = {}  # Dictionnaire des occurrences pour retourner chaque motif et les index dans le texte.
    for i in range(len(text)):
        if i != 0 and node is root and not checked:  # Si le nœud est la racine et que nous ne sommes pas au premier indice, alors nous devons incrémenter ceci dans le cas où un caractère n'existe pas.
            nbrComparison += 1
        checked = False
        char = text[i]
        while char not in node.children and node is not root:
            # On entre dans les échecs si le caractère n'existe pas et n'est pas la racine.
            node = node.fail
            nbrComparison += 1
            checked = True  # Ceci est pour quand on arrive à la racine la première fois, nous ne comparons pas. Nous comparons dans la racine seulement si l'élément n'existe pas.
        if char in node.children:
            node = node.children[char]
            nbrComparison += 1
        if node.finished:
            # Cela sert à afficher les occurrences et leurs index dans le texte.
            if node.output not in occurrences:
                occurrences[node.output] = []
            occurrences[node.output].append(i - len(node.output) + 1)  # Cela sert à afficher les occurrences et leurs index dans le texte.

    return occurrences, nbrComparison

motifs=["ze","rby","y"]
root = initializeTri(motifs)
root = createFailureLinks(root)
text = "bybobybcdbdbdeddd"
debutTemps=time.time()
occurences,nbrComparison = ahoCorasick(text, root)
TempsFin=time.time()
Temps=TempsFin - debutTemps  # pour calculer temps d’exécution

print(f"---------------------------------------")
print(f"Motifs : {motifs} ")
print(f"Text : {text} ")
print(f"Table des occurrences : {occurences} ")
print(f"Nombre de combarison : {nbrComparison}")
print(f"Temps d'execuson: {Temps * 1000000 } microseconds ")
print(f"---------------------------------------")
