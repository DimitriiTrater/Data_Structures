class DbList:
    class Node:
        element = None
        next_node = None
        prev_node = None

        def __init__(self, element, next_node=None, prev_node=None) -> None:
            self.element = element
            self.next_node = next_node
            self.prev_node = prev_node

    head = None
    tail = None
    length = 0

    def append(self, element):
        self.length += 1
        if not self.head:
            self.head = self.Node(element)
            return element
        elif not self.tail:
            self.tail = self.Node(element, None, self.head)
            self.head.next_node = self.tail
            return element
        else:
            self.tail = self.Node(element, None, self.tail)
            self.tail.prev_node.next_node = self.tail
            return element

    def _del(self, index, reverse=False):
        if index == 0:
            el = self.head.element

            if self.head.next_node:
                self.head = self.head.next_node
                self.head.prev_node = None
            else:
                self.head = None
            return el
        elif index == self.length - 1:
            el = self.tail.element
            self.tail = self.tail.prev_node
            self.tail.next_node = None
            return el
        elif reverse:
            i = self.length - 1
            node = self.tail

            while i != index:
                node = node.prev_node
                i -= 1

            el = node.element
            node.prev_node.next_node, node.next_node.prev_node = node.next_node, node.prev_node
            del node

            return el
        else:
            i = 0
            node = self.head

            while i != index:
                node = node.next_node
                i += 1

            el = node.element
            node.prev_node.next_node, node.next_node.prev_node = node.next_node, node.prev_node
            del node

            return el

    def delete(self, index):
        if self.head:
            if index > self.length // 2:
                el = self._del(index, reverse=True)
            elif index <= self.length // 2:
                el = self._del(index, reverse=False)
            self.length -= 1
            return el

    def _assign(self, index, element, reverse=False):
        if index == 0:
            self.head.element = element
        elif index == self.length - 1:
            self.tail.element = element
        elif reverse:
            i = self.length - 1
            node = self.tail

            while i != index:
                node = node.prev_node
                i -= 1

            node.element = element
        else:
            i = 0
            node = self.head

            while i != index:
                node = node.next_node
                i += 1

            node.element = element

    def assign(self, index, element):
        if self.head:
            if index > self.length // 2:
                self._assign(index, element, reverse=True)
            elif index <= self.length // 2:
                self._assign(index, element, reverse=False)

    def is_empty(self):
        return self.length == 0

    def __str__(self):
        node = self.head
        line = '['
        try:
            while node.next_node:
                line += str(node.element) + ','
                node = node.next_node
            line += str(node.element) + ']'
            return line
        except AttributeError:
            return line + ']'


if __name__ == '__main__':
    a = DbList()
    a.append(7)
    a.delete(0)

    print(a)  # []
