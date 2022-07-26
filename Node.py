class Node():
    def __init__(self, value: int, left_child=None, right_child=None):
        self._left_child = left_child
        self._right_child = right_child
        self._value = value

    def add_left_child(self, left):
        if self._left_child == None:
            self._left_child = left

    def add_right_child(self, right):
        if self._right_child == None:
            self._right_child = right

    def remove_left_child(self):
        if self._right_child == None:
            self._left_child = None

        if self._right_child != None:
            self._left_child = self.right_child
            self.remove_right_child()

    def remove_right_child(self):
        if self._right_child != None:
            self._right_child = None

    @property
    def value(self) -> int:
        return self._value

    @property
    def left_child(self):
        return self._left_child

    @property
    def right_child(self):
        return self._right_child
