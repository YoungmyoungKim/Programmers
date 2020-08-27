from collections import deque
class Node:
    def __init__(self,data=None):
        self.data = data
        self.childcount=0
        self.children={}
        
class Trie:
    def __init__(self):
        self.head = Node(None)
        
    def insert(self,string):
        l=len(string)
        node = self.head
        i=1
        while i<=l:
            if string[:i] not in node.children:
                node.children[string[:i]] = Node(string[:i])
            node.children[string[:i]].childcount+=1
            node = node.children[string[:i]]
            i+=1
            
    def find(self,string):
        node = self.head
        l = len(string)
        i=1
        while i<=l:
            if string[:i] in node.children:
                node = node.children[string[:i]]
                if i==l:
                    return node.childcount
            i+=1
        return 0
        
                
    
    def show(self):
        node = self.head
        dQ = deque([])
        dQ.append(node)
        while dQ:
            tmp = dQ.popleft()
            for value in tmp.children.values():
                dQ.append(value)
            print("data : "+str(tmp.data)+"  count : "+str(tmp.childcount))


trie = Trie()
trie.insert("STA")
trie.insert("STR")
trie.insert("STRW")
trie.insert("STR")
trie.show()
print(trie.find("STR"))

                
