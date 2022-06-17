# https://www.hackerrank.com/challenges/one-month-preparation-kit-reverse-a-linked-list/problem?h_l=interview&isFullScreen=false&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=one-month-preparation-kit&playlist_slugs%5B%5D=one-month-week-three

class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = SinglyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node


        self.tail = node

def print_singly_linked_list(node):
    while node:
        print(node.data, end=' ')
        node = node.next
    
    print()

def reverse(llist):
    pre_node = None
    curr_node = llist
    next_node = curr_node.next
    
    while curr_node:
        curr_node.next = pre_node
        
        pre_node = curr_node
        curr_node = next_node
        if next_node:
            next_node = next_node.next
    
    return pre_node
    
if __name__ == '__main__':
        llist = SinglyLinkedList()
        llist.insert_node(1)
        llist.insert_node(2)
        llist.insert_node(3)
        llist.insert_node(4)
        llist.insert_node(5)

        llist1 = reverse(llist.head)

        print_singly_linked_list(llist1)

# Output:
# 5 4 3 2 1