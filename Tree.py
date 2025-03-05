# Dylan Stitt
# Unit 6 Lab 3
# Traversals

class Tree:
    class TreeNode:

        def __init__(self, value):
            self.__value = value
            self.__children = []
            self.__parent = None

        def __str__(self, level=0):
            """Tree toString"""
            ret = " " * level + str(self.__value) + "\n"
            for child in self.__children:
                ret += child.__str__(level + 1)
            return ret

        def __set_parent(self, node):
            """Set parent of node"""
            if type(node) != type(self) and node is not None:
                raise TypeError("Given value is not type TreeNode")

            if node not in self.__children or node is None:
                self.__parent = node

    class Position:

        def __init__(self, memberOf, node):
            self.__member_of = memberOf
            self.__node = node

        def __str__(self):
            """Display position as value in node"""
            return str(self.get_value())

        def __repr__(self):
            """Display position when in collection"""
            return str(self)

        def __eq__(self, other):
            """Checks if two positions are equal"""
            return (type(self) == type(other)) and (self.__node is other._Position__node)

        def __ne__(self, other):
            """Checks if two positions are not equal"""
            return not (self == other)

        def get_value(self):
            """Returns the value of the position's node"""
            return self.__node._TreeNode__value

    def __init__(self):
        self.__root = None
        self.__size = 0

    def __str__(self):
        """Convert root to string"""
        return str(self.__root)

    def __validate(self, position):
        """Return node in specified position or raise exception if position does not belong to list or not a position"""
        if type(position) != self.Position:
            raise TypeError("Position must be of same type")

        if self is not position._Position__member_of:
            raise ValueError("Position does not belong to tree")

        return position._Position__node

    def __make_position(self, node):
        """Return new position object for a given node"""
        if type(node) != self.TreeNode:
            return None
        return self.Position(self, node)

    def __len__(self):
        """Returns the size of the tree"""
        return self.__size

    def add_root(self, element):
        """Inserts a new root into an empty tree"""
        if self.__root is not None:
            raise IndexError("Tree is not empty")

        node = self.TreeNode(element)
        self.__root = node
        self.__size += 1
        return self.__make_position(node)

    def add_left(self, position, element):
        """Adds a left child to the given position"""
        parent = self.__validate(position)
        node = self.TreeNode(element)

        if parent._TreeNode__left is not None:
            raise IndexError("Left child is not empty")

        parent._TreeNode__set_left(node)
        node._TreeNode__set_parent(parent)

        self.__size += 1
        return self.__make_position(node)

    def add_right(self, position, element):
        """Adds a right child to the given position"""
        parent = self.__validate(position)
        node = self.TreeNode(element)

        if parent._TreeNode__right is not None:
            raise IndexError("Right child is not empty")

        parent._TreeNode__set_right(node)
        node._TreeNode__set_parent(parent)

        self.__size += 1
        return self.__make_position(node)

    def add_child(self, position, element):
        """Adds a child to the given position"""
        parent = self.__validate(position)
        node = self.TreeNode(element)

        node._TreeNode__set_parent(parent)
        parent._TreeNode__children.append(node)

        self.__size += 1
        return self.__make_position(node)

    def is_root(self, position):
        """Determines if the given position is the root of the tree"""
        return self.__validate(position) is self.__root

    def is_leaf(self, position):
        """Determines if the given position is a leaf"""
        node = self.__validate(position)
        return len(node._TreeNode__children) == 0

    def is_ancestor(self, ancestor, descendant):
        """Determines if one node is an ancestor of another node"""
        descendant = self.__validate(descendant)
        ancestor = self.__validate(ancestor)

        while descendant is not self.__root:
            if descendant._TreeNode__parent is ancestor:
                return True
            descendant = descendant._TreeNode__parent
        return False

    def are_siblings(self, sibling1, sibling2):
        """Determines if two nodes are siblings"""
        if self.__validate(sibling1) is self.__validate(sibling2) or self.is_root(sibling1) or self.is_root(sibling2):
            return False
        if self.__validate(sibling2)._TreeNode__parent is self.__validate(sibling1)._TreeNode__parent:
            return True
        return False

    def get_root(self):
        """Returns the root of the tree in position"""
        return self.__make_position(self.__root)

    def get_parent(self, position):
        """Returns the parent of the given position"""
        return self.__make_position(self.__validate(position)._TreeNode__parent)

    def num_children(self, position):
        """Returns the number of children of the given position"""
        children = self.get_children(position)
        return 0 if children is None else len(children)

    def get_depth(self, position):
        """Returns the depth of the given position"""
        ancestors = self.get_ancestors(position)
        return 0 if ancestors is None else len(ancestors)

    def get_ancestors(self, position):
        """Returns a list of ancestors of the given position"""
        ancestors = []
        node = self.__validate(position)

        if self.is_root(position):
            return None

        while node._TreeNode__value is not None:
            node = node._TreeNode__parent
            if node is None:
                break

            ancestors.append(self.__make_position(node))
        return ancestors

    def get_children(self, position):
        """Returns a list of children of the given position"""
        c = []
        node = self.__validate(position)

        if self.is_leaf(position):
            return None

        for child in node._TreeNode__children:
            c.append(self.__make_position(child))
        return c

    def get_siblings(self, position):
        """Returns the sibling of the given position"""
        node = self.__validate(position)
        siblings = []

        if self.is_root(position):
            return None

        for child in node._TreeNode__children:
            if child is not node:
                siblings.append(self.__make_position(child))
        return siblings

    def replace(self, position, element):
        """Replaces the contents of the node at the given position"""
        node = self.__validate(position)
        oldVal = node._TreeNode__value
        node._TreeNode__value = element
        return oldVal

    ####################################################################################################################
    def delete(self, position):
        """Removes a node from the tree"""
        node = self.__validate(position)
        children = self.num_children(position)

        if children == 2:
            raise Exception("Cannot delete node with two children")

        elif children == 1:
            child = node._TreeNode__left if node._TreeNode__left is not None else node._TreeNode__right

            if node is self.__root:
                self.__root = child
            elif node._TreeNode__left is not None:
                node._TreeNode__parent._TreeNode__set_left(child)
                child._TreeNode__set_parent(node._TreeNode__parent)
            else:
                node._TreeNode__parent._TreeNode__set_right(child)
                child._TreeNode__set_parent(node._TreeNode__parent)

        else:
            if node is self.__root:
                self.__root = None
            elif node._TreeNode__parent._TreeNode__left is node:
                node._TreeNode__parent._TreeNode__set_left(None)
            else:
                node._TreeNode__parent._TreeNode__set_right(None)

        self.__size -= 1
        if self.__size == 0:
            self.__root = None

        node._TreeNode__set_parent(node)
        return node._TreeNode__value

    def preorder_traversal(self, node=None, result=[]):
        """Preorder tree traversal"""
        if node is None:
            node = self.__root

        result.append(node._TreeNode__value)

        if node._TreeNode__left is not None:
            self.preorder_traversal(node._TreeNode__left, result)
        if node._TreeNode__right is not None:
            self.preorder_traversal(node._TreeNode__right, result)

        return result

    def postorder_traversal(self, node=None, result=[]):
        """Postorder tree traversal"""
        if node is None:
            node = self.__root

        if node._TreeNode__left is not None:
            self.postorder_traversal(node._TreeNode__left, result)
        if node._TreeNode__right is not None:
            self.postorder_traversal(node._TreeNode__right, result)

        result.append(node._TreeNode__value)

        return result

    def inorder_traversal(self, node=None, result=[]):
        """Inorder tree traversal"""
        if node is None:
            node = self.__root

        if node._TreeNode__left is not None:
            self.inorder_traversal(node._TreeNode__left, result)

        result.append(node._TreeNode__value)

        if node._TreeNode__right is not None:
            self.inorder_traversal(node._TreeNode__right, result)

        return result
