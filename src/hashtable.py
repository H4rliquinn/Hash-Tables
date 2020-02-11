# '''
# Linked List hash table key/value pair
# '''
class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
    def __str__(self):
        curr=self
        retstr=f'LP:{curr.key}/{curr.value}'
        while curr.next!=None:
            curr=curr.next
            retstr+=f'->LP:{curr.key}/{curr.value}'
        return retstr

class HashTable:
    '''
    A hash table that with `capacity` buckets
    that accepts string keys
    '''
    def __init__(self, capacity):
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage = [None] * capacity

    def __str__(self):
        retstr=""
        for i in self.storage:
            if i!=None:
                print(i)
        return retstr

    def _hash(self, key):
        '''
        Hash an arbitrary key and return an integer.
        You may replace the Python hash with DJB2 as a stretch goal.
        '''
        return hash(key)


    def _hash_djb2(self, key):
        '''
        Hash an arbitrary key using DJB2 hash

        OPTIONAL STRETCH: Research and implement DJB2
        '''                                                                                                                              
        hash = 5381
        for x in key:
            hash = (( hash << 5) + hash) + ord(x)
        return hash & 0xFFFFFFFF


    def _hash_mod(self, key):
        '''
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        '''
        return self._hash_djb2(key) % self.capacity


    def insert(self, key, value):
        '''
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Fill this in.
        '''
        hash=self._hash_mod(key)
        new_pair=LinkedPair(key,value)
        if self.storage[hash] != None:
            new_pair.next=self.storage[hash]
        self.storage[hash]=new_pair
        return new_pair

    def remove(self, key):
        '''
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Fill this in.
        '''
        hash=self._hash_mod(key)
        if self.storage[hash] == None:
            print("WARNING: Key does not exist. Unable to remove")
            return 0
        elif self.storage[hash].next==None:
            self.storage[hash]=None
            return key
        else:
            curr=self.storage[hash]
            prev=None
            while True:
                if curr.key==key:
                    # print(key,curr.key,curr.value)
                    if prev==None:
                        self.storage[hash]=curr.next
                    elif curr.next==None:
                        prev.next=None
                    else:
                        prev.next=curr.next
                    return key
                elif curr.next==None:
                    print("WARNING: Key does not exist. Unable to remove")
                    return 0
                prev=curr
                curr=curr.next        


    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Fill this in.
        '''
        hash=self._hash_mod(key)
        if self.storage[hash] == None:
            return None
        elif self.storage[hash].next==None:
            return self.storage[hash].value
        else:
            curr=self.storage[hash]
            while True:
                if curr.key==key:
                    # print(key,curr.key,curr.value)
                    return curr.value
                elif curr.next==None:
                    return None
                curr=curr.next
        
    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Fill this in.
        '''
        self.capacity = self.capacity*2
        old_storage=self.storage[:]
        self.storage = [None] * self.capacity
        for i in old_storage:
            if i !=None:
                # print("RESIZE",i.key,i.value)
                curr=i
                self.insert(curr.key,curr.value)
                while curr.next !=None:
                    curr=curr.next
                    # print("RESIZE-LINK",curr.key,curr.value,curr.next)
                    self.insert(curr.key,curr.value)                


if __name__ == "__main__":
    ht = HashTable(2)

    ht.insert("line_1", "Tiny hash table")
    ht.insert("line_2", "Filled beyond capacity")
    ht.insert("line_3", "Linked list saves the day!")


    # Test storing beyond capacity
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    print("")
    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    print("")
