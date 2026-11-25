import pytest
from LinkedList import LinkedList


@pytest.fixture
def sample_linked_list() -> LinkedList:
    ll = LinkedList(10)
    for node in range(2, 6):
        ll.append(node * 10)
    return ll


class TestLinkedListTraversalMethod:
    def test_get_node_from_linked_list(self, sample_linked_list: LinkedList):
        pass

    def test_find_mid_node_in_linked_list(self, sample_linked_list: LinkedList):
        pass

    def test_loop_in_linked_list(self, sample_linked_list: LinkedList):
        pass
