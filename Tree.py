# Dylan Stitt
# Unit 6 Lab 3
# Traversals

class BinaryTree:
    class BinaryNode:

        def __init__(self, value, left=None, right=None):
            self.__value = value
            self.__left = left
            self.__right = right
            self.__parent = None

        def __str__(self):
            """Display to enable view for whole tree"""
            return f"|{self.__value}| \n({self.__value})L: {self.__left} \n({self.__value})R: {self.__right}"

        def __set_parent(self, node):
            """Set parent of node"""
            if type(node) != type(self) and node is not None:
                raise TypeError("Given value is not type BinaryNode")

            if node is not self.__left and node is not self.__right or node is None:
                self.__parent = node

        def __set_left(self, node):
            """Set left child of node"""
            if type(node) != type(self) and node is not None:
                raise TypeError("Given value is not type BinaryNode")

            if node is not self.__parent and node is not self.__right and node is not self or node is None:
                self.__left = node
            else:
                raise TypeError("Given value is not type BinaryNode")

        def __set_right(self, node):
            """Set right child of node"""
            if type(node) != type(self) and node is not None:
                raise TypeError("Given value is not type BinaryNode")

            if node is not self.__parent and node is not self.__left and node is not self or node is None:
                self.__right = node
            else:
                raise TypeError("Given value is not type BinaryNode")

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
            return self.__node._BinaryNode__value

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
        if type(node) != self.BinaryNode:
            return None
        return self.Position(self, node)

    def __len__(self):
        """Returns the size of the tree"""
        return self.__size

    def add_root(self, element):
        """Inserts a new root into an empty tree"""
        if self.__root is not None:
            raise IndexError("Tree is not empty")

        node = self.BinaryNode(element)
        self.__root = node
        self.__size += 1
        return self.__make_position(node)

    def add_left(self, position, element):
        """Adds a left child to the given position"""
        parent = self.__validate(position)
        node = self.BinaryNode(element)

        if parent._BinaryNode__left is not None:
            raise IndexError("Left child is not empty")

        parent._BinaryNode__set_left(node)
        node._BinaryNode__set_parent(parent)

        self.__size += 1
        return self.__make_position(node)

    def add_right(self, position, element):
        """Adds a right child to the given position"""
        parent = self.__validate(position)
        node = self.BinaryNode(element)

        if parent._BinaryNode__right is not None:
            raise IndexError("Right child is not empty")

        parent._BinaryNode__set_right(node)
        node._BinaryNode__set_parent(parent)

        self.__size += 1
        return self.__make_position(node)

    def is_root(self, position):
        """Determines if the given position is the root of the tree"""
        return self.__validate(position) is self.__root

    def is_leaf(self, position):
        """Determines if the given position is a leaf"""
        node = self.__validate(position)
        return node._BinaryNode__left is None and node._BinaryNode__right is None

    def is_ancestor(self, ancestor, descendant):
        """Determines if one node is an ancestor of another node"""
        descendant = self.__validate(descendant)
        ancestor = self.__validate(ancestor)

        while descendant is not self.__root:
            if descendant._BinaryNode__parent is ancestor:
                return True
            descendant = descendant._BinaryNode__parent
        return False

    def are_siblings(self, sibling1, sibling2):
        """Determines if two nodes are siblings"""
        if self.__validate(sibling1) is self.__validate(sibling2) or self.is_root(sibling1) or self.is_root(sibling2):
            return False
        if self.__validate(sibling2)._BinaryNode__parent is self.__validate(sibling1)._BinaryNode__parent:
            return True
        return False

    def get_root(self):
        """Returns the root of the tree in position"""
        return self.__make_position(self.__root)

    def get_left(self, position):
        """Returns the left child of the given position"""
        return self.__make_position(self.__validate(position)._BinaryNode__left)

    def get_right(self, position):
        """Returns the right child of the given position"""
        return self.__make_position(self.__validate(position)._BinaryNode__right)

    def get_parent(self, position):
        """Returns the parent of the given position"""
        return self.__make_position(self.__validate(position)._BinaryNode__parent)

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

        while node._BinaryNode__value is not None:
            node = node._BinaryNode__parent
            if node is None:
                break

            ancestors.append(self.__make_position(node))
        return ancestors

    def get_children(self, position):
        """Returns a list of children of the given position"""
        children = []
        node = self.__validate(position)

        if self.is_leaf(position):
            return None

        if node._BinaryNode__left is not None:
            children.append(self.__make_position(node._BinaryNode__left))
        if node._BinaryNode__right is not None:
            children.append(self.__make_position(node._BinaryNode__right))

        return children

    def get_sibling(self, position):
        """Returns the sibling of the given position"""
        node = self.__validate(position)

        if self.is_root(position):
            return None

        if node is node._BinaryNode__parent._BinaryNode__left:
            return self.__make_position(node._BinaryNode__parent._BinaryNode__right)
        return self.__make_position(node._BinaryNode__parent._BinaryNode__left)

    def replace(self, position, element):
        """Replaces the contents of the node at the given position"""
        node = self.__validate(position)
        oldVal = node._BinaryNode__value
        node._BinaryNode__value = element
        return oldVal

    def delete(self, position):
        """Removes a node from the tree"""
        node = self.__validate(position)
        children = self.num_children(position)

        if children == 2:
            raise Exception("Cannot delete node with two children")

        elif children == 1:
            child = node._BinaryNode__left if node._BinaryNode__left is not None else node._BinaryNode__right

            if node is self.__root:
                self.__root = child
            elif node._BinaryNode__left is not None:
                node._BinaryNode__parent._BinaryNode__set_left(child)
                child._BinaryNode__set_parent(node._BinaryNode__parent)
            else:
                node._BinaryNode__parent._BinaryNode__set_right(child)
                child._BinaryNode__set_parent(node._BinaryNode__parent)

        else:
            if node is self.__root:
                self.__root = None
            elif node._BinaryNode__parent._BinaryNode__left is node:
                node._BinaryNode__parent._BinaryNode__set_left(None)
            else:
                node._BinaryNode__parent._BinaryNode__set_right(None)

        self.__size -= 1
        if self.__size == 0:
            self.__root = None

        node._BinaryNode__set_parent(node)
        return node._BinaryNode__value

    def preorder_traversal(self, node=None, result=[]):
        """Preorder tree traversal"""
        if node is None:
            node = self.__root

        result.append(node._BinaryNode__value)

        if node._BinaryNode__left is not None:
            self.preorder_traversal(node._BinaryNode__left, result)
        if node._BinaryNode__right is not None:
            self.preorder_traversal(node._BinaryNode__right, result)

        return result

    def postorder_traversal(self, node=None, result=[]):
        """Postorder tree traversal"""
        if node is None:
            node = self.__root

        if node._BinaryNode__left is not None:
            self.postorder_traversal(node._BinaryNode__left, result)
        if node._BinaryNode__right is not None:
            self.postorder_traversal(node._BinaryNode__right, result)

        result.append(node._BinaryNode__value)

        return result

    def inorder_traversal(self, node=None, result=[]):
        """Inorder tree traversal"""
        if node is None:
            node = self.__root

        if node._BinaryNode__left is not None:
            self.inorder_traversal(node._BinaryNode__left, result)

        result.append(node._BinaryNode__value)

        if node._BinaryNode__right is not None:
            self.inorder_traversal(node._BinaryNode__right, result)

        return result
