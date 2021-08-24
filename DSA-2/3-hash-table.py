# hash table DS store elements in key-value pairs where:
# -> Key - unique int that is used for indexing the values
# -> values- data that are assoicated with keys
# ex: key-Name, value-age of that person's name

# what is collision?
# -> basically is when hash function generates the same
# index for multiple keys that could make conflict.

# -> to solve this issue by following techniques:
# 1- Chaining: by using linked list to point to the next element

# 2- Open addressing: 
# 2.1- linear probing: find element to the right that 
# it has collide with, if it's empty just insert it there
# otherwise keep searching

# 2.2- double-hashing: the same as linear probling, but
# it can determine how many element it want to jump over
# instead of jump one by one like linear probing 
# ex: we decide to choose to jump by 3 element, it jump 3 
# times, if that index is empty we can insert if not we jump
# another 3 times until we find the empty one to insert to

#---------------------------------------------------------

# Python program to demonstrate working of HashTable 

hashTable = [[],] * 10

# check prime
def checkPrime(n):
    if n == 1 or n == 0:
        return 0

    for i in range(2, n//2):
        if n % i == 0:
            return 0
    
    return 1

# get prime number
def getPrime(n):
    if n % 2 == 0:
        n += 1
    
    while not checkPrime(n):
        n += 2
    
    return n

# hash function
def hashFunction(key):
    hashLength = getPrime(10)
    return key % hashLength

# insert data to hash table
def insertData(key, data):
    index = hashFunction(key)
    hashTable[index] = [key, data]

# remove data from hash table

def removeData(key):
    index = hashFunction(key)
    
    # swap key and data to 0
    hashTable[index] = 0


# insert data
insertData(123, "apple")
insertData(432, "mango")
insertData(213, "banana")
insertData(654, "guava")
print()
print("Before removing from hash table: ")
print(hashTable)
print()
removeData(654)
print("After removing from hash table: ")
print(hashTable)
print()