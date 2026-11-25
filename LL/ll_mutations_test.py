import pytest
from LinkedList import LinkedList


@pytest.fixture(scope="function")
def sample_linked_list() -> LinkedList:
    ll = LinkedList(10)
    for node in range(2, 6):
        ll.append(node * 10)
    return ll


class TestLinkedListMutationMethods:
    def test_pop_head_from_linked_list(self, sample_linked_list: LinkedList):
        assert sample_linked_list.pop_head().data == 10
        for node in range(6, 11):
            sample_linked_list.append(node * 10)
            sample_linked_list.prepend(node * 10)
        assert sample_linked_list.pop_head().data == 100

    def test_pop_tail_from_linked_list(self, sample_linked_list: LinkedList):
        assert sample_linked_list.pop_tail().data == 50
        for node in range(2, 11):
            sample_linked_list.prepend(node * 10)
            sample_linked_list.append(node * 10)
        assert sample_linked_list.pop_tail().data == 100

    def test_set_node_data_in_linked_list_node(self, sample_linked_list: LinkedList):
        assert sample_linked_list.set_(3, 500) == True
        assert sample_linked_list.set_(5, 1000) == False

    def test_insert_into_linked_list(self, sample_linked_list: LinkedList):
        assert sample_linked_list.insert(3, 250)
        assert sample_linked_list.get_length() == 6
        assert sample_linked_list.get(3).data == 250

    def test_remove_into_linked_list(self, sample_linked_list: LinkedList):
        assert sample_linked_list.remove(3).data == 40

    def test_reverse_linked_list(self, sample_linked_list: LinkedList, capsys):
        sample_linked_list.reverse()
        out: str = capsys.readouterr().out
        assert "The Linkedlist with indices is:" in out
        assert "[0] => 50" in out
        assert "[4] => 10" in out
        assert "Length: 5 | Head: 50 | Tail: 10\n" in out
