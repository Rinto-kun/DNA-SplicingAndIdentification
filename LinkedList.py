from copy import deepcopy

hash_table = {"C":0,"T":1,"A":2,"G":3}
base = 4
modulus = 101

class Node:
    def __init__(self, val=None):
        self.val = val
        self.next = None
        self.prev = None
    
    def __repr__(self):
        ret = []
        cur = self
        while cur is not None:
            ret.append(cur.val)
            cur = cur.next
        return " > ".join(ret)
    
    def __str__(self):
        return self.val
    
    def __eq__(self,other):
        return self.val==other.val
    
    def insert_nodes(self,nodes,index:int):
        for _ in range(index-1):
            self = self.next
        
        temp = self.next
        self.next = deepcopy(nodes.head)

        while self.next is not None:
            self = self.next
            
        self.next = temp
        
        return self
    
    def __hash__(self):
        return hash_table[self.val]

class LinkedList:
    def __init__(self, data=None):
        self.head = None

        self.size = 0
        
        if data is not None:
            node = Node(val=data[0])
            self.size += 1
        self.head = node
        for i in range(1,len(data)):
            node.next = Node(val=data[i])
            node = node.next
            self.size += 1
    
    def insert_first(self, node):
        node.next = self.head
        self.head = node
        
        self.size += 1

    def insert_last(self, node):
        if self.head is None:
            self.head = node
            return
        for current_node in self:
            pass
        current_node.next = node
        
        self.size += 1

    def insert_at(self, target_node_data, new_node):
        for node in self:
            if node.val == target_node_data:
                new_node.next = node.next
                node.next = new_node
                return
        self.size += 1
    
    def __str__(self):
        ret = []
        for node in self:
            ret.append(node.val)
        return "".join(ret)
    
    def __repr__(self):
        ret = []
        for node in self:
            ret.append(str(node))
        return " -> ".join(ret)
    
    def __len__(self):
        if self.size == 0:
            return sum(1 for _ in self)
        else:
            return self.size
    
    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next
    
    def insert_ll(self,linked_list,index:int):
        self.head.insert_ll(linked_list, index)

    def __hash__(self):
        hash_sum = 0
        size = len(self)
        for i, node in enumerate(self):
            hash_sum = (hash_sum + base**(size-i-1)*hash(node)) % modulus
            # hash_sum += hash(node)
        return hash_sum
    
    def __eq__(self,other):
        return all(node_1.val==node_2.val for node_1,node_2 in zip(self,other))
    
    def cut(self,index):
        ret = []
        node = self.head
        while node is not None and index != 0:
            ret.append(node.val)
            node = node.next
            index -= 1
        return LinkedList(ret)
    
    def get_element(self,index):
        for i, node in enumerate(self):
            if i == index:
                return node