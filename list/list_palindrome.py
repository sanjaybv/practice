from linked_list import Node, make_list

head = make_list([1])
print head

def is_palindrome(head):
    stack = []
    slow = fast = head
    while fast:
        if not fast.next:
            # odd
            slow = slow.next
            break
        stack.append(slow.value)
        slow = slow.next
        fast = fast.next.next
    
    while len(stack):
        if stack.pop() != slow.value:
            return False
        slow = slow.next
    
    return True

'''
def is_palindrome(head):
    stack = []
    curr = head
    stack.append(curr.value)
    fast = head
    while fast.next:
        if fast.next.next:
            curr = curr.next
            stack.append(curr.value)
            fast = fast.next.next
        else:
            # ended, even number of items
            break
    else:
        # ended, odd number of items
        stack = stack[:-1]
    curr = curr.next

    while len(stack):
        if stack[-1] != curr.value:
            print 'not palindrome!'
            break
        stack = stack[:-1]
        curr = curr.next
    else:
        print 'palindrome!'
'''

print is_palindrome(head)
