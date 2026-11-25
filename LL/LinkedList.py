from Node import Node


class LinkedList:
    def __init__(self, data: int | str | None):
        node: Node = Node(data)
        self.head: Node = node

    def get_length(self, offset: int = 0) -> int:
        temp: Node | None = self.head
        len_: int = 0
        while temp is not None:
            temp = temp.next
            len_ += 1
            if temp == self.head:
                return max(0, len_ + offset)
        return max(0, len_ + offset)

    def modify_length(self, offset: int = 0) -> None:
        self.get_length(offset)

    def is_empty(self) -> bool:
        return self.get_head() == None

    def get_head(self) -> Node:
        return self.head

    def get_tail(self) -> Node:
        temp: Node | None = self.head
        while temp.next is not None:
            temp = temp.next
            if temp.next == self.head:
                return temp
        return temp

    # Simpler version
    def create_cycle(self) -> None:
        tail: Node | None = self.get_tail()
        tail.next = self.head

    def delete_test_cycle(self) -> None:
        tail: Node | None = self.get_tail()
        tail.next = None

    def print_list(self) -> None:
        print("The Linkedlist is:")
        if self.head is None:
            print("LinkedList is empty")
            return

        temp: Node | None = self.head
        while temp is not None:
            print(f"{temp.data}")
            if temp.next == self.head:
                print(f"{temp.next.data} (loop!)")
                break
            temp = temp.next

        print(
            f"Length: {self.get_length()} | Head: {self.get_head().data} | Tail: {self.get_tail().data}\n"
        )

    def print_list_by_idx(self) -> None:
        print("The Linkedlist with indices is:")
        if self.head is None:
            print("LinkedList is empty")
            return

        temp: Node | None = self.head
        length: int = self.get_length()

        for i in range(length):
            print(f"[{i}] => {temp.data}")
            if temp.next == self.head:
                print(f"[{i}] => {temp.next.data} (loop!)")
                break
            temp = temp.next

        print(
            f"Length: {length} | Head: {self.get_head().data} | Tail: {self.get_tail().data}\n"
        )

    # def create_test_cycle(self, index: int = 0) -> None:
    #     if self.head is None or index < 0 or index >= self.get_length():
    #         return False
    #     target: Node = self.get(index)
    #     temp: Node | None = self.head
    #     while temp.next is not None:
    #         temp = temp.next
    #     temp.next = target
    #     return True

    def append(self, data: int | str) -> bool:
        node: Node = Node(data)
        if self.head is None:
            self.head = node
        else:
            temp: Node | None = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = node
        self.modify_length(offset=1)
        return True

    def prepend(self, data: int | str) -> bool:
        node: Node = Node(data)
        if self.get_length() == 0 or self.head is None:
            self.head = node
        else:
            node.next = self.head
            self.head = node
        self.modify_length(offset=1)
        return True

    def pop_head(self) -> Node | None:
        if self.head is None:
            return None
        if self.get_length() == 1:
            temp: Node | None = self.head
            self.head = None
            self.modify_length(offset=-1)
            return temp
        temp: Node | None = self.head
        self.head = self.head.next
        temp.next = None
        self.modify_length(offset=-1)
        return temp

    def pop_tail(self) -> Node | None:
        if self.head is None:
            return None
        if self.get_length() == 1:
            temp: Node | None = self.head
            self.head = None
            self.modify_length(offset=-1)
            return temp
        temp: Node | None = self.head
        pre: Node = None
        while temp.next is not None:
            pre = temp
            temp = temp.next
        pre.next = None
        self.modify_length(offset=-1)
        return temp

    def get(self, index: int) -> Node | None:
        if index < 0 or index >= self.get_length():
            return None
        if index == self.get_length() - 1:
            return self.get_tail()
        if index == 0:
            return self.get_head()
        temp: Node | None = self.head
        for _ in range(index):
            temp = temp.next
        return temp

    def set_(self, index: int, data: int | str) -> bool:
        node: Node = self.get(index)
        if node is not None:
            node.data = data
            return True
        return False

    def insert(self, index: int, data: int | str) -> bool:
        if index < 0 or index > self.get_length():
            return False
        if index == 0:
            return self.prepend(data)
        if index == self.get_length() - 1:
            return self.append(data)
        pre: Node = self.get(index - 1)
        node: Node = Node(data)
        node.next = pre.next
        pre.next = node
        self.modify_length(offset=1)
        return True

    def remove(self, index: int) -> Node:
        if index < 0 or index >= self.get_length():
            return None
        if index == 0:
            return self.pop_head()
        if index == self.get_length() - 1:
            return self.pop_tail()
        pre: Node = self.get(index - 1)
        removed: Node = self.get(index)
        pre.next = removed.next
        removed.next = None
        self.modify_length(offset=-1)
        return removed

    def reverse(self) -> None:
        if self.get_length() <= 1:
            return
        temp: Node | None = self.head
        old_head: Node = temp
        after: Node = temp.next
        before: Node = None
        for _ in range(self.get_length()):
            after = temp.next
            temp.next = before
            before = temp
            temp = after
        self.head = before
        old_head.next = None
        self.print_list_by_idx()

    def find_mid(self) -> Node | None:
        if self.get_length() <= 0 or self.head is None:
            return None
        mid_index: int = self.get_length() // 2
        temp: Node | None = self.head
        for _ in range(mid_index):
            temp = temp.next
        return temp

    def has_loop(self) -> bool | None:
        if self.get_length() == 0 or self.head is None:
            return None
        slow: Node = self.head
        fast: Node = self.head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            if fast == slow:
                return True
        return False
