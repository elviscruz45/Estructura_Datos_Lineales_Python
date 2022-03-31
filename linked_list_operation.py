from node import Node

head=None

for count in range(1,6):
    head=Node(count,head)

'''

while head !=None:

    print(head.data)
    head=head.next

'''
'''
probe=head

while probe !=None:
    print(probe.data)
    probe=probe.next
    
probe=head

target_item=2

while probe != None and target_item != probe.data:
    probe=probe.next


if probe !=None:
    print(f"Target item {target_item} has been found")
else:
    print(f"Target item {target_item} is not in the linked list")
'''


'''
probe=head
target_item=3
new_item="Z"

while probe!= None and target_item !=probe.data:
    probe=probe.next
    
    if probe !=None:
        probe.data=new_item
        print("{new_item} replaced th old value in the node {target_item}")
    else:
        print(f"The target_item is not in the link list")

'''



head=Node("F",head)
new_node=Node("K")

if head is None:
    head=new_node
else:
    probe=head
    while probe.next != None:
        probe=probe.next
    probe.next=new_node

'''
probe=head
while probe.next:
    print(probe.data)
    probe=probe.next
  
'''

'''    
    
removed_item=head.data
head=head.next
print(removed_item)
'''    



'''
head=Node("F",head)

removed_item=head.data

if head.next is None:
    head=None
else:
    probe=head
    while probe.next.next !=None:
        probe=probe.next
    removed_item=probe.next.data
    probe.next=None
'''

print(probe.data)
removed_item=head.data
print(removed_item)

if head.next is None:
    head=None
else:
    probe=head
    while probe.next.next !=None:
        probe=probe.next
    removed_item=probe.next.data
    probe.next=None
    
print(removed_item)