# class LincList:
#     head = None
#     length = 0
#
#     class Node:
#         element = None
#         next_node = None
#
#         def __init__(self, element, next_node=None):
#             self.element = element
#             self.next_node = next_node
#
#     def __str__(self):
#         node = self.head
#         line = '['
#         while node.next_node:
#             line += str(node.element) + ', '
#             node = node.next_node
#         line += str(node.element) + ']'
#         return line
#
#     def empty(self):
#         return self.head is None
#
#     def append(self, element):
#         if not self.head:
#             self.head = self.Node(element)
#             self.length += 1
#             return element
#         node = self.head
#         while node.next_node:
#             node = node.next_node
#         node.next_node = self.Node(element)
#         self.length += 1
#         return element
#
#     def __getitem__(self, key):
#         ind = 0
#         node = self.head
#         while ind < key:
#             node = node.next_node
#             ind += 1
#         return node.element
#
#     def insert(self, key, value):
#         ind = 0
#         node = self.head
#         prev_node = self.head
#
#         if key == 0:
#             old_head = self.head
#             self.head = self.Node(value, next_node=old_head)
#             self.length += 1
#             return value
#         while ind < key:
#             prev_node = node
#             node = node.next_node
#             ind += 1
#         prev_node.next_node = self.Node(value, next_node=node)
#         self.length += 1
#         return value
#
#     def __delitem__(self, key):
#         ind = 0
#         node = self.head
#         prev_node = node
#
#         if key == 0:
#             old_head = self.head
#             element = self.head.element
#             self.head = self.head.next_node
#             self.length -= 1
#             del old_head
#             return element
#         while ind < key:
#             prev_node = node
#             node = node.next_node
#             ind += 1
#         prev_node.next_node = node.next_node
#         element = node.element
#         self.length -= 1
#         del node
#         return element
#
#     def __len__(self):
#         return self.length
#
#
# a = LincList()
#
# a.append(855)
# a.append(78787.00)
# a.append('123')
# a.append(85473)
#
# a.insert(0, 222)
# print(a)
# del(a[0])
# print(a)
#
# # print(a[2])
# # print(a.empty())
# # print(a.length)

### TREE

class Node:
    def __init__(self, key):
        self.t_key = key

    def set_key(self, key):
        self.t_key = key

    def key(self):
        return self.t_key

    def __str__(self):
        return str(self.t_key)


class Tree(Node):
    def __init__(self, key):
        super().__init__(key)
        self.t_children = []

    def add_child(self, child):
        self.t_children.append(child)

    def remove_child(self, key):
        for child in self.t_children:
            if child.key() == key:
                self.t_children.remove(child)
                return True
        return False

    def get_child(self, key):
        for child in self.t_children:
            if child.key() == key:
                return child
        return None

    def get_children(self):
        return self.t_children


def constr_tree():
    node7 = Tree(7)
    node9 = Tree(9)
    node10 = Tree(10)
    node11 = Tree(11)
    node12 = Tree(12)
    node13 = Tree(13)
    node14 = Tree(14)
    node15 = Tree(15)

    node8 = Tree(8)
    node8.add_child(node14)
    node8.add_child(node15)

    node4 = Tree(4)
    node4.add_child(node8)
    node4.add_child(node9)

    node5 = Tree(5)
    node5.add_child(node10)
    node5.add_child(node11)

    node6 = Tree(6)
    node6.add_child(node12)
    node6.add_child(node13)

    node2 = Tree(2)
    node2.add_child(node4)
    node2.add_child(node5)

    node3 = Tree(3)
    node3.add_child(node6)
    node3.add_child(node7)

    root = Tree(1)
    root.add_child(node2)
    root.add_child(node3)

    return root

tree = constr_tree()

nd11 = tree.get_child(2).get_child(5).get_child(11)
print(nd11)
