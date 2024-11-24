class Node:
    def __init__(self, value:int, next=None):
        self.value = value
        self.next = next

class SingleLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, new_node:Node):
        temp = self.head
        self.head = new_node
        new_node.next = temp

    def insert_at_end(self, new_node:Node):
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    def insert_at_position(self, new_node:Node, position:int):
        temp = self.head
        prev_node = None
        for index in range(1, position):
            prev_node = temp
            temp = temp.next
        prev_node.next = new_node
        new_node.next = temp

    def delete_beginning(self):
        self.head = self.head.next

    def delete_end(self):
        temp = self.head
        prev_node = temp
        while temp.next:
            prev_node = temp
            temp = temp.next
        prev_node.next = None

    def delete_at_position(self, position:int):
        temp = self.head
        prev_node = None
        for index in range(1, position):
            prev_node = temp
            temp = temp.next
        prev_node.next = temp.next

    def reverse(self):
        prev_node = None
        curr_node = self.head
        next_node = self.head
        while next_node:
            next_node = next_node.next
            curr_node.next = prev_node
            prev_node, curr_node = curr_node, next_node
        self.head = prev_node

    def count(self):
        count = 0
        temp = self.head
        while temp:
            count += 1
            temp = temp.next
        return count

    def print_nodes(self):
        temp = self.head
        while temp:
            print(temp.value)
            temp = temp.next

node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)

sll = SingleLinkedList()
sll.print_nodes()
sll.insert_at_beginning(node1)
sll.insert_at_beginning(node2)
sll.insert_at_end(node3)
sll.insert_at_end(node4)
sll.print_nodes()
print("After Insert at Position")
sll.insert_at_position(node5, 3)
sll.print_nodes()
print("Delete at beginning")
sll.delete_beginning()
sll.print_nodes()
print("Delete at End")
sll.delete_end()
sll.print_nodes()
print("Delete at position")
sll.delete_at_position(2)
sll.print_nodes()
print("Reverse the list")
sll.reverse()
sll.print_nodes()
print("Number of Nodes: ", sll.count())