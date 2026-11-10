class Node:
    def __init__(self,key,value):
        self.key=key
        self.value=value
        self.next=None
        self.prev=None
        self.freq=1
class DoublyLinkedList:
    def __init__(self):
        self.left=Node(0,0)
        self.right=Node(0,0)
        self.left.next=self.right
        self.right.prev=self.left
        self.size=0
    def add(self,node):
        node.next=self.left.next
        node.prev=self.left
        self.left.next.prev=node
        self.left.next=node
        self.size+=1
    def remove(self,node):
        node.next.prev=node.prev
        node.prev.next=node.next
        self.size-=1
    def remove_lru(self,node):
        if self.size==0:
            return None
        node=self.right.prev
        self.remove(node)
        return node

class LFUCache:

    def __init__(self, capacity: int):
        self.capacity=capacity
        self.freqMap={}
        self.keyMap={}
        self.minFreq=0
    def update(self,node):
        freq=node.freq
        self.freqMap[node.freq].remove(node)
        if freq==self.minFreq and self.freqMap[freq].size==0:
            self.minFreq+=1
        node.freq+=1
        if node.freq not in self.freqMap:
            self.freqMap[node.freq]=DoublyLinkedList()
        self.freqMap[node.freq].add(node)  

    def get(self, key: int) -> int:
        if key not in self.keyMap:
            return -1
        node=self.keyMap[key]
        self.update(node)
        return node.value
    
    def put(self, key: int, value: int) -> None:
        if self.capacity==0:
            return
        if key in self.keyMap:
            node=self.keyMap[key]
            node.value=value
            self.update(node)
            return
        if len(self.keyMap)==self.capacity:
            dll=self.freqMap[self.minFreq]
            removed_node=dll.remove_lru(dll)
            del self.keyMap[removed_node.key]
        new_node=Node(key,value)
        self.keyMap[key]=new_node
        if 1 not in self.freqMap:
            self.freqMap[1]=DoublyLinkedList()
        self.freqMap[1].add(new_node)
        self.minFreq=1
        


        


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)