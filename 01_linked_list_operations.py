class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def print_list(self):
        curr = self.head
        while curr:
            print(curr.data, end=" -> ")
            curr = curr.next
        print("None")

def reverse_linked_list(llist):
    prev = None
    current = llist.head
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    llist.head = prev

def sorted_insert(sorted_head, new_node):
    if sorted_head is None or sorted_head.data >= new_node.data:
        new_node.next = sorted_head
        sorted_head = new_node
    else:
        current = sorted_head
        while current.next is not None and current.next.data < new_node.data:
            current = current.next
        new_node.next = current.next
        current.next = new_node
    return sorted_head

def insertion_sort_linked_list(llist):
    sorted_head = None
    current = llist.head
    while current:
        next_node = current.next
        sorted_head = sorted_insert(sorted_head, current)
        current = next_node
    llist.head = sorted_head

def merge_sorted_lists(list1, list2):
    dummy = Node(0)
    tail = dummy
    l1 = list1.head
    l2 = list2.head

    while l1 and l2:
        if l1.data < l2.data:
            tail.next = l1
            l1 = l1.next
        else:
            tail.next = l2
            l2 = l2.next
        tail = tail.next

    if l1:
        tail.next = l1
    if l2:
        tail.next = l2

    merged_list = LinkedList()
    merged_list.head = dummy.next
    return merged_list

# Створення однозв'язних списків
llist1 = LinkedList()
llist1.append(10)
llist1.append(20)
llist1.append(30)

llist2 = LinkedList()
llist2.append(15)
llist2.append(25)
llist2.append(35)

print("Список 1:")
llist1.print_list()

print("Список 2:")
llist2.print_list()

# Реверсування списку 1
reverse_linked_list(llist1)
print("Реверсований список 1:")
llist1.print_list()

# Сортування списку 1
insertion_sort_linked_list(llist1)
print("Відсортований список 1:")
llist1.print_list()

# Об'єднання двох відсортованих списків
merged_list = merge_sorted_lists(llist1, llist2)
print("Об'єднаний відсортований список:")
merged_list.print_list()
