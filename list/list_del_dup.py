from linked_list import Node, make_list

head = make_list([4, 4, 3, 'b', 5, 2, 5, 'b', 1, 2, 4])
print head

def del_dup(head):
    dup_set = set()
    dup_set.add(head.value)
    curr = head
    while curr.next:
        if curr.next.value in dup_set:
            curr.next = curr.next.next
        else:
            dup_set.add(curr.next.value)
            curr = curr.next

del_dup(head)
print head
