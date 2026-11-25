import pytest
from LinkedList import LinkedList


@pytest.fixture(scope="function")
def sample_linked_list() -> LinkedList:
    ll = LinkedList(10)
    for node in range(2, 6):
        ll.append(node * 10)
    return ll


class TestLinkedListCoreMethods:
    def test_is_empty_on_non_empty_list(self, sample_linked_list: LinkedList):
        assert sample_linked_list.is_empty() is False
        assert sample_linked_list.get_length() == 5

    def test_append_adds_to_tail(self, sample_linked_list: LinkedList):
        assert sample_linked_list.append(60) is True
        assert sample_linked_list.get_length() == 6
        assert sample_linked_list.get_tail().data == 60

    def test_prepend_add_to_head(self, sample_linked_list: LinkedList):
        assert sample_linked_list.prepend(0) is True
        assert sample_linked_list.get_length() == 6
        assert sample_linked_list.get_head().data == 0

    def test_print_list(self, sample_linked_list: LinkedList, capsys):
        sample_linked_list.append(60)
        sample_linked_list.prepend(0)
        sample_linked_list.print_list()
        out: str = capsys.readouterr().out
        assert "The Linkedlist is:" in out
        assert "0\n10\n20\n30\n40\n50\n60\n" in out
        assert "Length: 7 | Head: 0 | Tail: 60" in out

    def test_print_list_by_idx(self, sample_linked_list: LinkedList, capsys):
        sample_linked_list.append(60)
        sample_linked_list.prepend(0)
        sample_linked_list.print_list_by_idx()
        out: str = capsys.readouterr().out
        assert "The Linkedlist with indices is:" in out
        assert "Index [0] => 0" in out
        assert "Index [6] => 60" in out
        assert "Length: 7 | Head: 0 | Tail: 60" in out
