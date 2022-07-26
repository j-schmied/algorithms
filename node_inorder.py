import Node


def inorder_traversal(root_node):
    if root_node is None:
        return

    inorder_traversal(root_node.left_child)
    print(root_node.value)
    inorder_traversal(root_node.right_child)


def main():
    root = Node.Node(10)
    root.add_left_child = Node.Node(5)
    root.add_right_child = Node.Node(15)

    inorder_traversal(root)

    exit(0)


if __name__ == '__main__':
    main()

