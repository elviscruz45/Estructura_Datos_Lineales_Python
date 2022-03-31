class Node:
    def __init__(self,data,next=None):
        self.data=data
        self.next=next



'''
node1=None
node2=Node("A",None)
node3=Node("B",node2)
node1=Node("C",node3)

head=None

for count in range(1,5):
    head=Node(count,head)


while head !=None:
    print(head.data)
    head=head.next

'''        