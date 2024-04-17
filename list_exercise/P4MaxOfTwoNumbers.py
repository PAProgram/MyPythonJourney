#Naive Method- using if-else
def maximum(n1,n2):
    if n1>=n2:
        return n1
    else:
        return n2
    
#using Max() function
def maximum2(n1,n2):
    return max(n1,n2)

#conditional expression operator
def maximum3(n1,n2):
    return (n1 if n1>n2 else n2)

#using lambda function
maximum4 = lambda n1,n2:n1 if n1>n2 else b

#using list comprehension
def maximum5(n1,n2):
    return [n1 if n1>n2 else b]

#using sort method
def maximum6(n1, n2):
    x=[n2,n2]
    x.sort
    return x[-1]
#Driver Function
a=3
b=7
# print(maximum(a,b))
# print(maximum2(a,b))
# print(maximum3(a,b))
# print('lambda function - ',maximum4(a,b))
print('list comprehension - ',maximum5(a,b))
print('sort method - ',maximum6(a,b))



