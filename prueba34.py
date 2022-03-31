from node import Node

head=None

for count in range(1,6):
    head=Node(count,head)



head=Node("F",head)
new_node=Node("K")

if head is None:
    head=new_node
else:
    probe=head
    while probe.next != None:
        probe=probe.next
    probe.next=new_node


print(probe.data)
print(head.data)
print(head.next.data)
print(head.next.next.data)
print(head.next.next.next.data)
print(head.next.next.next.next.next.data)
print(head.next.next.next.next.next.next.data)
