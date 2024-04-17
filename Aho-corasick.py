class TrieNode(object):    
    def __init__(self, char: str):
        self.char = char
        self.finished = False
        self.children= {}
        self.output = []
        self.fail = None
    
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

def initializeTri(strings):
    root = TrieNode('/')
    for string in strings:
        addText(root,string)
    return root
def BuildingFailures(root):
    queue = []
    for child in root.children.values():
        queue.append(child)
        child.fail = root
    while queue:
        node = queue.pop(0)
        for key, child in node.children.items():
            queue.append(child)
            fail = node.fail
            while fail != root and key not in fail.children:
                fail = fail.fail
            if key in fail.children:
                child.fail = fail.children[key]
            else:
                child.fail = root
    return root
def findLongestPrefixInRootForNode(root, text):
    node = root
    for char in text:
        while char not in node.children:
            if node is root:
                break
            node = node.fail
        if char in node.children:
            node = node.children[char]
    return node
def createFailurLinks(root):
    queue = []
    root.fail = root
    for child in root.children.values():
        queue.append(child)
        child.fail = root
    while queue:
        node = queue.pop(0)
        for child in node.children.values():
            queue.append(child)
            child.fail =findLongestPrefixInRootForNode(root,child.output[1:len(child.output)])
    return root
def ahoCorasick(text, root):
    node = root
    occurences = []
    for i in range(len(text)):
        char = text[i]
        while char not in node.children and node is not root:
            node = node.fail
        if char in node.children:
            node = node.children[char]
        if node.finished:
            occurences.append(i-len(node.output)+1)
            print(node.output)
    return occurences
root = initializeTri(["tatt","at","tt"])
root = createFailurLinks(root)
text = "atgtt"
# print(root.children["t"].children["t"].fail)
# root =root.children["t"].children["t"].fail
ahoCorasick(text, root)
# print(root.output)