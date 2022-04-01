from ast import keyword


class Node:
    def __init__(self,data,next=None):
        self.data=data
        self.next=next



listas=Node(5,Node(4,Node(3,Node(2,Node(1,None)))))
head=Node("zambrano",listas)

#------------------------------------------------------------------

print("1era prueba es una cagada")

print(head.data)
print(head.next.data)
print(head.next.next.data)
print(head.next.next.next.data)
print(head.next.next.next.next.data)
print(head.next.next.next.next.next.data)
print(head.next.next.next.next.next.next)

#------------------------------------------------------------------

print("2era prueba es una cagada probe=head new_node=NodeK")

new_node=Node("K")

probe=head

probe.next.next.next.next.next.next=new_node



print(head.data)
print(head.next.data)
print(head.next.next.data)
print(head.next.next.next.data)
print(head.next.next.next.next.data)
print(head.next.next.next.next.next.data)
print(head.next.next.next.next.next.next.data)
print(head.next.next.next.next.next.next.next)


#------------------------------------------------------------------

print("3era prueba es una cagada")

print(probe.data)
print(probe.next.data)
print(probe.next.next.data)
print(probe.next.next.next.data)
print(probe.next.next.next.next.data)
print(probe.next.next.next.next.next.data)
print(probe.next.next.next.next.next.next.data)
print(probe.next.next.next.next.next.next.next)
