class Node:
    def __init__(self, data: int | str | None):
        self.data = data
        self.next: Node = None
