
class UnsortedLinkedList(object):
    def __init__(self):
        self.head = None

    def add(self, item):
        node = Node(item, None)
        if self.head is None:
            self.head = node
        else:
            self._add_node_to_the_end(node)

    def _add_node_to_the_end(self, node):
        parent_node = self.head

        while parent_node.next_node is not None:
            parent_node = parent_node.next_node

        parent_node.next_node = node

    def get_kth_to_last(self, k):
        start_pointer = self.head
        end_pointer = self.head

        for i in range(0, k-1):
            end_pointer = end_pointer.next_node

        while end_pointer.next_node is not None:
            start_pointer = start_pointer.next_node
            end_pointer = end_pointer.next_node

        return start_pointer.item


class Node(object):
    def __init__(self, item, next_node):
        self.item = item
        self.next_node = next_node


class LinkedListIterator(object):
    def __init__(self, linked_list):
        self.linked_list = linked_list

    def all(self):
        current_node = self.linked_list.head

        while current_node is not None:
            item = current_node.item
            current_node = current_node.next_node
            yield item
