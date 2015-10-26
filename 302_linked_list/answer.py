from node import Node


def delete_middle_node(node):
    if node.next:
        node.data = node.next.data
        node.next = node.next.next


def add(node1, node2, residual=0):
    s = 0
    if node1: s += node1.data
    if node2: s += node2.data
    s += residual

    result = Node(s % 10)

    if (node1 and node1.next) or (node2 and node2.next) or s >= 10:
        next = add(node1.next if node1 else None, node2.next if node2 else None, 1 if s >= 10 else 0)
        result.next = next
    return result
