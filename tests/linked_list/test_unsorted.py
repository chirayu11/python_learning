from code.linked_list.unsorted import UnsortedLinkedList, LinkedListIterator


def test_unsorted_linked_list_can_be_created_and_iterated_over():
    # Given
    unsorted_list = UnsortedLinkedList()
    unsorted_list.add(9)
    unsorted_list.add(3)
    unsorted_list.add(7)
    list_iterator = LinkedListIterator(unsorted_list)

    # When
    actual_items = []
    for i in list_iterator.all():
        actual_items.append(i)

    # Then
    assert actual_items == [9, 3, 7]


def test_unsorted_list_get_kth_to_last():
    # Given
    unsorted_list = UnsortedLinkedList()
    unsorted_list.add(5)
    unsorted_list.add(4)
    unsorted_list.add(3)
    unsorted_list.add(2)
    unsorted_list.add(1)

    # When and Then
    assert 1 == unsorted_list.get_kth_to_last(1)
    assert 2 == unsorted_list.get_kth_to_last(2)
    assert 3 == unsorted_list.get_kth_to_last(3)
    assert 4 == unsorted_list.get_kth_to_last(4)
    assert 5 == unsorted_list.get_kth_to_last(5)
