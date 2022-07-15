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
        print(node.data, end=" ")
        node = node.next

    print()


def insertNodeAtPosition(llist, data, position):
    if position == 1:
        new_node = SinglyLinkedListNode(data)
        new_node.next = llist.next
        llist.next = new_node
    else:
        insertNodeAtPosition(llist.next, data, position - 1)
        
    return llist



llist = SinglyLinkedList()
llist.insert_node(1)
llist.insert_node(2)
llist.insert_node(3)
# llist.insert_node(4)
llist.insert_node(5)

print_singly_linked_list(llist.head)
llist_head = insertNodeAtPosition(llist.head, 0, 0)
print_singly_linked_list(llist.head)
