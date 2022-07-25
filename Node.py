class Node:
	
	def __init__(self, value: int, left_child: Node = None, right_child: Node = None):
		self._left_child: Node = left_child
		self._right_child: Node = right_child
		self._value = value

	def add_left_child(self, left: Node)
		if self.left_child == None:
			self._left_child = left

	def add_right_child(self, right: Node):
		if self._right_child == None:
			self._right_child = right
			
	def remove_left_child(self):
		if self._right_child == None:
			self._left_child = None
		
		if self._right_child not None:
			self._left_child = self.right_child
			self.remove_right_child()
			
	def remove_right_child(self):
		if self._right_child not None:
			self._right_child = None 	
