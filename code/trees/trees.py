from code.linked_list.unsorted import UnsortedLinkedList, LinkedListIterator


class Node(object):
    def __init__(self, value, left, right):
        self.value = value
        self.left = left
        self.right = right


def max_height(tree):
    if tree is None:
        return 0

    left_height = max_height(tree.left)
    right_height = max_height(tree.right)

    return left_height+1 if left_height > right_height else right_height+1


def create_binary_search_tree_with_minimal_height(sorted_numbers):
    if len(sorted_numbers) == 0:
        return None
    if len(sorted_numbers) == 1:
        return Node(sorted_numbers[0], None, None)

    mid = len(sorted_numbers)//2

    left_tree = create_binary_search_tree_with_minimal_height(sorted_numbers[:mid])
    right_tree = create_binary_search_tree_with_minimal_height(sorted_numbers[mid+1:])
    return Node(sorted_numbers[mid], left_tree, right_tree)


def create_linked_lists_for_binary_tree(tree):
    """Problem  4.3 Given a binary tree, creates n different linked lists for n different
    depths of the tree. Each linked list contains nodes from the same level of the tree."""

    current = UnsortedLinkedList()
    current.add(tree)

    result = [current]

    while current.length:

        iterator = LinkedListIterator(current)
        next = UnsortedLinkedList()
        for n in iterator.all():
            if n.left is not None:
                next.add(n.left)
            if n.right is not None:
                next.add(n.right)

        if next.length:
            result.append(next)

        current = next

    return result

