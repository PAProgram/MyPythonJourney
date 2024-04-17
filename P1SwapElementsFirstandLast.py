#Python3 program to swap first and last element of list

#swap function
def swapList(newList):
    size=len(newList)
    temp = newList[0]
    newList[0]=newList[size-1]
    newList[size-1]=temp

def swapList2(newList):
    temp=newList[0]
    newList[0]=newList[-1]
    newList[-1]=temp

def swapList3(list): 
    # Storing the first and last element 
    # as a pair in a tuple variable get
    get = list[-1], list[0]
    print(get)
    print(list[0], list[1])
    # unpacking those elements
    list[0], list[-1] = get
    print(get)

def swapList4(list): 
    print("Inside Swaplist4")
    list[0], list[-1] = list[-1], list[0]

def swapList5(list):
    start, *middle, last = list
    list = [last, *middle, start]
    return list
    
def swapList6(list):
    first=list.pop(0)
    last=list.pop(-1)
    list.insert(0, last)
    list.insert(-1, first)
    return list

def swapList7(list):
    if len(list)>=2:
        print(list[-1:])
        print(list[1:-1])
        print(list[:1])
        list = list[-1:] + list[1:-1] + list[:1]
    return list

#Driver code
newList = [12,24, 35, 65, 43]
print(swapList4(newList))
print("newList - ", newList)

# -----------------------------


# list = [12, 34, 23,66, 38, 55]
# a, b, c, *d = list
# print(a)
# print(b)
# print(c)
# print(d)

