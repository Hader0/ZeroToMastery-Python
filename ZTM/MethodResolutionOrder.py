class A:
    num = 10

class B(A):
    pass

class C(A):
    num = 1

class D(B, C): # D inhertis from B and C. Those inherit from A. 
    pass

print(D.num)
print(D.mro()) # Displays the order in which D runs