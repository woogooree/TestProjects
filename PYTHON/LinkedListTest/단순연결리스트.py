class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


head = ListNode('일')

#add new_node
curr_node = head

new_node = ListNode('월')
curr_node.next = new_node
curr_node=curr_node.next

curr_node.next = ListNode('화')
curr_node=curr_node.next

curr_node.next = ListNode('수')
curr_node=curr_node.next

curr_node.next = ListNode('목')
curr_node=curr_node.next

curr_node.next = ListNode('금')
curr_node=curr_node.next

curr_node.next = ListNode('토')
curr_node=curr_node.next

#print all node
node=head
while node:
    print("value:", node.val)
    node=node.next

if node is None :
    print("final node")
