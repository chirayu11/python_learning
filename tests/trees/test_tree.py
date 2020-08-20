from code.linked_list.unsorted import LinkedListIterator
from code.trees.trees import create_binary_search_tree_with_minimal_height, max_height, \
    create_linked_lists_for_binary_tree


def test_create_binary_search_tree_with_minimal_height():
    # Given
    array = [1, 3, 7, 8, 10, 12, 13]

    # When
    actual = create_binary_search_tree_with_minimal_height(array)

    # Then
    assert max_height(actual) == 3
    assert [actual.left.left.value, actual.left.value, actual.left.right.value, actual.value,
            actual.right.left.value, actual.right.value, actual.right.right.value] \
           == [1, 3, 7, 8, 10, 12, 13]


def test_create_linked_lists_for_binary_tree():
    # Given
    array = [1, 3, 7, 8, 10, 12, 13]
    tree = create_binary_search_tree_with_minimal_height(array)

    # When
    actual_linked_lists = create_linked_lists_for_binary_tree(tree)

    # Then
    assert len(actual_linked_lists) == 3
    _assert_linked_list_has_items([8], actual_linked_lists[0])
    _assert_linked_list_has_items([3, 12], actual_linked_lists[1])
    _assert_linked_list_has_items([1, 7, 10, 13], actual_linked_lists[2])


def _assert_linked_list_has_items(items, linked_list):
    iterator = LinkedListIterator(linked_list)
    for n in iterator.all():
        items.remove(n.value)

    assert len(items) == 0
