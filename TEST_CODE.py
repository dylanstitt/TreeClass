##### Global color variables #####
from colorama import Fore

R = Fore.RED
G = Fore.GREEN
B = Fore.BLUE
W = Fore.RESET
P = Fore.CYAN

'''IF COLORAMA NOT FOUND - ENTER INTO TERMINAL:
pip install colorama'''


##################################

def result(flag):
    if flag:
        return f"{G}PASSED{W}"

    return f"{R}FAILED{W}"


def TEST_binary_node(class_ref):
    print("~" * 50)
    print(f"{P}TEST CATEGORY: BinaryNode class{W}\n")

    test_node = class_ref.BinaryNode("X")

    test = type(test_node) == class_ref.BinaryNode
    print(f"New BinaryNode object was created: {result(test)}")

    test = test_node._BinaryNode__parent == test_node._BinaryNode__left == test_node._BinaryNode__right == None
    print(f"BinaryNode parent, left, & right pointers initialize to None: {result(test)}")

    print(f"\n{P}__set_parent(){W}")
    test_parent = class_ref.BinaryNode("P")

    try:
        test_node._BinaryNode__set_parent("P")
        print(f"Cannot set parent to non-node type: {result(False)}")
    except:
        print(f"Cannot set parent to non-node type: {result(True)}")

    test_node._BinaryNode__set_parent(test_parent)
    test = test_node._BinaryNode__parent is test_parent
    print(f"Node parent pointer can be set to a node object: {result(test)}")

    test_node._BinaryNode__set_parent(None)
    test = test_node._BinaryNode__parent is None
    print(f"Node parent pointer can be set to None: {result(test)}")

    print(f"\n{P}__set_left(){W}")
    test_left = class_ref.BinaryNode("L")

    try:
        test_node._BinaryNode__set_left("L")
        print(f"Cannot set left child to non-node type: {result(False)}")
    except:
        print(f"Cannot set left child to non-node type: {result(True)}")

    test_node._BinaryNode__set_left(test_left)
    test = test_node._BinaryNode__left is test_left
    print(f"Node left child pointer can be set to a node object: {result(test)}")

    test_node._BinaryNode__set_left(None)
    test = test_node._BinaryNode__left is None
    print(f"Node left child pointer can be set to None: {result(test)}")

    print(f"\n{P}__set_right(){W}")
    test_right = class_ref.BinaryNode("R")

    try:
        test_node._BinaryNode__set_right("R")
        print(f"Cannot set right child to non-node type: {result(False)}")
    except:
        print(f"Cannot set right child to non-node type: {result(True)}")

    test_node._BinaryNode__set_right(test_right)
    test = test_node._BinaryNode__right is test_right
    print(f"Node right child pointer can be set to a node object: {result(test)}")

    test_node._BinaryNode__set_right(None)
    test = test_node._BinaryNode__right == None
    print(f"Node right child pointer can be set to None: {result(test)}")

    print(f"\n{P}Node Pointer Relationships{W}")

    test_node = class_ref.BinaryNode("X")
    test_parent = class_ref.BinaryNode("P")

    try:
        test_node._BinaryNode__set_parent(test_node)
        print(f"A node can be its own parent: {result(True)}")
    except:
        print(f"A node can be its own parent: {result(False)}")

    try:
        test_node._BinaryNode__set_left(test_node)
        test_node._BinaryNode__set_right(test_node)
        print(f"A node's left or right cannot point to itself: {result(False)}")
    except:
        print(f"A node's left or right cannot point to itself:  {result(True)}")

    test_node._BinaryNode__set_parent(test_parent)
    try:
        test_node._BinaryNode__set_left(test_parent)
        test_node._BinaryNode__set_right(test_parent)
        print(f"A node's parent cannot also be its child: {result(False)}")
    except:
        print(f"A node's parent cannot also be its child: {result(True)}")

    test_node._BinaryNode__set_parent(None)
    test_node._BinaryNode__set_left(test_left)
    try:
        test_node._BinaryNode__set_parent(test_left)
        test_node._BinaryNode__set_right(test_left)
        print(f"A node's left cannot also be its right or its parent: {result(False)}")
    except:
        print(f"A node's left cannot also be its right or its parent: {result(True)}")

    test_node._BinaryNode__set_left(None)
    test_node._BinaryNode__set_right(test_right)
    try:
        test_node._BinaryNode__set_parent(test_right)
        test_node._BinaryNode__set_left(test_right)
        print(f"A node's right cannot also be its left or its parent: {result(False)}")
    except:
        print(f"A node's right cannot also be its left or its parent: {result(True)}")

    print("~" * 50, "\n\n")


def TEST_position(class_ref):
    print("~" * 50)
    print(f"{P}TEST CATEGORY: Position class{W}\n")

    temp_BT = class_ref()
    temp_node = class_ref.BinaryNode("X")
    temp_pos = temp_BT.Position(temp_BT, temp_node)

    test = temp_pos._Position__member_of is temp_BT
    print(f"member_of attribute stores a BinaryTree object: {result(test)}")

    test = temp_pos._Position__node is temp_node
    print(f"node attribute stores a BinaryNode object: {result(test)}")

    test = temp_pos.get_value() == "X"
    print(f"get_value method returns node contents: {result(test)}")

    print("~" * 50, "\n\n")


def TEST_new_binary_tree(BT):
    print("~" * 50)
    print(f"{P}TEST CATEGORY: BinaryTree initialization{W}\n")

    test = BT._BinaryTree__root is None
    print(f"New BinaryTree's root is None: {result(test)}")

    test = BT._BinaryTree__size == 0
    print(f"New BinaryTree's size is zero: {result(test)}")

    print("~" * 50, "\n\n")


def TEST_make_position_validate(BT, class_ref):
    print("~" * 50)
    print(f"{P}TEST CATEGORY: Make Position and Validate Utilities{W}\n")

    temp_BT = class_ref()
    test_node = class_ref.BinaryNode("X")

    pos = BT._BinaryTree__make_position(test_node)

    print(f"{P}__make_position(){W}")
    test = type(pos) == class_ref.Position
    print(f"make_position method returns Position object: {result(test)}")

    test = pos._Position__node is test_node
    print(f"New position contains a node object: {result(test)}")

    pos1 = BT._BinaryTree__make_position(None)
    pos2 = BT._BinaryTree__make_position("A")
    test = pos1 == pos2 == None
    print(f"make_position returns none when given a non-node object: {result(test)}")

    print(f"\n{P}__validate(){W}")
    node = BT._BinaryTree__validate(pos)
    test = node is test_node
    print(f"validate returns node object from valid position: {result(test)}")

    temp_pos = temp_BT._BinaryTree__make_position("Y")
    try:
        node = BT._BinaryTree__validate(temp_pos)
        print(f"validate raises exception if position is not in this list: {result(False)}")
    except:
        print(f"validate raises exception if position is not in this list: {result(True)}")

    try:
        node = BT._BinaryTree__validate("X")
        print(f"validate raises exception if argument is not type Position: {result(False)}")
    except:
        print(f"validate raises exception if argument is not type Position: {result(True)}")

    test_node._BinaryNode__set_parent(test_node)
    try:
        node = BT._BinaryTree__validate(test_node)
        print(f"validate raises exception if given node is depreciated: {result(False)}")
    except:
        print(f"validate raises exception if given node is depreciated: {result(True)}")

    print("~" * 50, "\n\n")


def TEST_add_nodes(BT):
    print("~" * 50)
    print(f"{P}TEST CATEGORY: Adding Nodes{W}\n")

    print(f"{P}add_root(){W}")
    pos1 = BT.add_root("A")
    test = type(pos1) == BT.Position
    print(f"add_root returns a position object: {result(test)}")

    test = len(BT) == 1
    print(f"add_root increases tree size to 1: {result(test)}")

    test = pos1.get_value() == "A"
    print(f"root contains a node object with the correct value: {result(test)}")

    test = pos1._Position__node._BinaryNode__parent is None
    print(f"root has no parent: {result(test)}")

    try:
        BT.add_root("X")
        print(f"Cannot add root if root already exists: {result(False)}")
    except:
        print(f"Cannot add root if root already exists: {result(True)}")

    print(f"{P}\nadd_left(){W}")
    pos2 = BT.add_left(pos1, "B")

    test = type(pos2) == BT.Position
    print(f"add_left returns a position object: {result(test)}")

    test = len(BT) == 2
    print(f"add_left increases tree size: {result(test)}")

    test = pos2.get_value() == "B"
    print(f"left child contains a node object with the correct value: {result(test)}")

    test = pos2._Position__node._BinaryNode__parent is pos1._Position__node
    print(f"left child is attached to its parent: {result(test)}")

    test = pos1._Position__node._BinaryNode__left is pos2._Position__node
    print(f"parent is attached to its left child: {result(test)}")

    try:
        BT.add_left(pos1, "X")
        print(f"Cannot add left child if left child already exists: {result(False)}")
    except:
        print(f"Cannot add left child if left child already exists: {result(True)}")

    print(f"{P}\nadd_right(){W}")
    pos3 = BT.add_right(pos1, "C")

    test = type(pos3) == BT.Position
    print(f"add_right returns a position object: {result(test)}")

    test = len(BT) == 3
    print(f"add_right increases tree size: {result(test)}")

    test = pos3.get_value() == "C"
    print(f"right child contains a node object with the correct value: {result(test)}")

    test = pos3._Position__node._BinaryNode__parent is pos1._Position__node
    print(f"right child is attached to its parent: {result(test)}")

    test = pos1._Position__node._BinaryNode__right is pos3._Position__node
    print(f"parent is attached to its right child: {result(test)}")

    try:
        BT.add_right(pos1, "X")
        print(f"Cannot add right child if right child already exists: {result(False)}")
    except:
        print(f"Cannot add right child if right child already exists: {result(True)}")

    d = BT.add_left(pos2, "D")
    e = BT.add_right(pos2, "E")
    f = BT.add_left(e, "F")

    print("~" * 50, "\n\n")
    return [pos1, pos2, pos3, d, e, f]


def VIEW_tree():
    print("~" * 50)
    print(f"{P}This is what your tree will look\nlike for the next round of tests. {W}\n")

    print("""
            (A)
            / \\
          (B) (C)
          / \\ 
        (D) (E)
            /
          (F)

    """)
    print("~" * 50, "\n\n")


def TEST_bool_getters(BT, nodes):
    # nodes = [A, B, C, D, E, F]

    print("~" * 50)
    print(f"{P}TEST CATEGORY: Boolean getters & num_children{W}\n")

    print(f"{P}is_root(){W}")

    expected = [1, 0, 0, 0, 0, 0]
    for i, n in enumerate(nodes):
        test = int(BT.is_root(n)) == expected[i]
        print(f"{n.get_value()} is root: {B}{BT.is_root(n)}{W} \t{result(test)}")

    try:
        BT.is_root("A")
        print(f"Position object argument is validated: {result(False)}")
    except:
        print(f"Position object argument is validated: {result(True)}")

    print(f"{P}\nis_leaf(){W}")
    expected = [0, 0, 1, 1, 0, 1]
    for i, n in enumerate(nodes):
        test = int(BT.is_leaf(n)) == expected[i]
        print(f"{n.get_value()} is leaf: {B}{BT.is_leaf(n)}{W} \t{result(test)}")

    try:
        BT.is_leaf("A")
        print(f"Position object argument is validated: {result(False)}")
    except:
        print(f"Position object argument is validated: {result(True)}")

    print(f"{P}\nis_ancestor(){W}")
    b_node = nodes[1]
    expected = [0, 0, 0, 1, 1, 1]
    for i, n in enumerate(nodes):
        res = BT.is_ancestor(b_node, n)
        test = int(res) == expected[i]
        print(f"B is an ancestor of {n.get_value()}: {B}{res}{W} \t{result(test)}")

    try:
        BT.is_ancestor("A", "B")
        print(f"Position object arguments are validated: {result(False)}")
    except:
        print(f"Position object arguments are validated: {result(True)}")

    print(f"{P}\nare_siblings(){W}")
    d_node = nodes[3]
    expected = [0, 0, 0, 0, 1, 0]
    for i, n in enumerate(nodes):
        res = BT.are_siblings(d_node, n)
        test = int(res) == expected[i]
        print(f"D and {n.get_value()} are siblings: {B}{res}{W} \t{result(test)}")

    try:
        BT.are_siblings("A", "B")
        print(f"Position object arguments are validated: {result(False)}")
    except:
        print(f"Position object arguments are validated: {result(True)}")

    print(f"{P}\nnum_children(){W}")
    f_node = nodes[5]
    expected = [2, 2, 0, 0, 1, 0]
    for i, n in enumerate(nodes):
        res = BT.num_children(n)
        test = int(res) == expected[i]
        print(f"{n.get_value()} has {B}{res}{W} children:  \t{result(test)}")

    try:
        BT.num_children("A", "B")
        print(f"Position object arguments are validated: {result(False)}")
    except:
        print(f"Position object arguments are validated: {result(True)}")

    print("~" * 50, "\n\n")


def TEST_BinNode_getters(BT, nodes):
    # nodes = [A, B, C, D, E, F]

    print("~" * 50)
    print(f"{P}TEST CATEGORY: Get BinaryNode Pointers{W}\n")

    print(f"{P}get_root(){W}")
    pos1 = BT.get_root()
    test = type(pos1) == type(nodes[0])
    print(f"get_root returns Position object: {result(test)}")

    test = pos1._Position__node is nodes[0]._Position__node
    print(f"Correct node returned in position: {result(test)}")

    test = pos1 == nodes[0]
    print(f"== correctly identifies equal Position objects: {result(test)}")

    print(f"\n{P}get_left(){W}")
    pos1 = BT.get_left(nodes[0])
    test = type(pos1) == type(nodes[0])
    print(f"get_left returns Position object: {result(test)}")

    test = pos1._Position__node is nodes[1]._Position__node
    print(f"Correct node returned in position: {result(test)}")

    test = pos1 == nodes[1]
    print(f"== correctly identifies equal Position objects: {result(test)}")

    pos2 = BT.get_left(nodes[-1])
    test = pos2 is None
    print(f"get_left returns None if left child doesn't exist: {result(test)}")

    print(f"\n{P}get_right(){W}")
    pos1 = BT.get_right(nodes[0])
    test = type(pos1) == type(nodes[0])
    print(f"get_right returns Position object: {result(test)}")

    test = pos1._Position__node is nodes[2]._Position__node
    print(f"Correct node returned in position: {result(test)}")

    test = pos1 == nodes[2]
    print(f"== correctly identifies equal Position objects: {result(test)}")

    pos2 = BT.get_right(nodes[-1])
    test = pos2 is None
    print(f"get_right returns None if right child doesn't exist: {result(test)}")

    print("~" * 50, "\n\n")


def TEST_family_relationships(BT, nodes):
    # nodes = [A, B, C, D, E, F]

    print("~" * 50)
    print(f"{P}TEST CATEGORY: Node Family Relationships{W}\n")

    print(f"{P}get_parent(){W}")
    par1 = BT.get_parent(nodes[0])
    test = par1 is None
    print(f"returns None if node is root: {result(test)}")

    expected = [nodes[0], nodes[0], nodes[1], nodes[1], nodes[4]]
    for i, n in enumerate(nodes[1:]):
        par2 = BT.get_parent(n)
        test = par2 == expected[i]
        print(f"Parent of {n.get_value()}: {B}{par2.get_value()}{W} \t{result(test)}")

    print(f"\n{P}get_children(){W}")
    ch1 = BT.get_children(nodes[-1])
    test = ch1 is None
    print(f"returns None if node is leaf: {result(test)}")

    ch2 = BT.get_children(nodes[1])
    test = type(ch2[0]) == type(ch2[1]) == type(nodes[0])
    print(f"list result contains position objects: {result(test)}")

    test = ch2[0] == nodes[3] and ch2[1] == nodes[4]
    print(f"returns list of correct child positions: {result(test)}")

    print(f"\n{P}get_sibling(){W}")
    sib1 = BT.get_sibling(nodes[-1])
    test = sib1 is None
    print(f"returns None if node has no sibling: {result(test)}")

    sib2 = BT.get_sibling(nodes[0])
    test = sib2 is None
    print(f"returns None if node is root: {result(test)}")

    expected = [nodes[2], nodes[1], nodes[4], nodes[3]]
    for i, n in enumerate(nodes[1:-1]):
        sib3 = BT.get_sibling(n)
        test = sib3 == expected[i]
        print(f"Sibling of {n.get_value()}: {B}{sib3.get_value()}{W} \t{result(test)}")

    print(f"\n{P}get_ancestors(){W}")
    anc1 = BT.get_ancestors(nodes[0])
    test = anc1 is None
    print(f"returns None if node is root: {result(test)}")

    anc2 = BT.get_ancestors(nodes[-1])
    test = type(anc2) == list
    print(f"returns list if node is not root: {result(test)}")

    expected = [nodes[4], nodes[1], nodes[0]]
    test = len(anc2) == len(expected)
    print(f"returns the correct number of ancestors: {result(test)}")

    test = True
    for i, pos in enumerate(anc2):
        if pos != expected[i]:
            test = False
    print(f"returned position objects contain the correct nodes: {result(test)}")

    print(f"\n{P}get_depth(){W}")
    expected = [0, 1, 1, 2, 2, 3]
    for i, n in enumerate(nodes):
        depth = BT.get_depth(n)
        test = depth == expected[i]
        print(f"Depth of node {n.get_value()}: {B}{depth}{W} \t{result(test)}")

    print("~" * 50, "\n\n")


def TEST_replace_delete(BT, nodes):
    # nodes = [A, B, C, D, E, F]

    print("~" * 50)
    print(f"{P}TEST CATEGORY: replace & delete{W}\n")

    print(f"{P}replace(){W}")

    val = BT.replace(nodes[-1], "G")
    test = val == "F"
    print(f"returned the correct value: {result(test)}")

    test = nodes[-1].get_value() == "G"
    print(f"node information was updated: {result(test)}")

    print(f"\n{P}delete(){W}")
    # nodes = [A, B, C, D, E, G]

    res = BT.delete(nodes[-1])
    test = res == "G"
    print(f"Delete returns contents of node: {result(test)}")

    test = len(BT) == 5
    print(f"Delete decreases tree size: {result(test)}")

    test = nodes[-1]._Position__node._BinaryNode__parent is nodes[-1]._Position__node
    print(f"Depreciated node is it's own parent: {result(test)}")

    test = BT.num_children(nodes[-2]) == 0
    print(f"Parent node had child removed: {result(test)}")

    try:
        BT.delete(nodes[0])
        print(f"\nCannot delete node with two children: {result(False)}\n")
    except:
        print(f"\nCannot delete node with two children: {result(True)}\n")

    order = [nodes[4], nodes[1], nodes[3], nodes[0], nodes[2]]
    size = 5
    for node in order:
        print(f"{B}Ready to delete {node}{W}")
        print(f"\t{B}{node}'s child: {BT.get_children(node)}{W}")
        og_val = node.get_value()

        res = BT.delete(node)
        size -= 1

        test = res == og_val
        print(f"\tDelete returns contents of node: {result(test)}")

        test = len(BT) == size
        print(f"\tDelete decreases tree size: {result(test)}\n")

    test = len(BT) == 0
    print(f"Tree is empty: {result(test)}")

    test = BT._BinaryTree__root is None
    print(f"Empty tree has no root: {result(test)}")

    print("~" * 50, "\n\n")


def TEST_docs(BT, class_ref):
    print("~" * 50)
    print(f"{P}TEST CATEGORY: Docstrings{W}\n")

    print("Position Class Docstrings:\n")
    doc = class_ref.Position.get_value.__doc__
    if doc != None:
        print(f"{B}get_value() Documentation:{W} {doc}\n")
    else:
        print(f"{R}get_value() Documentation Missing{W}\n")

    doc = class_ref.Position.__eq__.__doc__
    if doc != None:
        print(f"{B}__eq__() Documentation:{W} {doc}\n")
    else:
        print(f"{R}__eq__() Documentation Missing{W}\n")

    doc = class_ref.Position.__ne__.__doc__
    if doc != None:
        print(f"{B}__ne__() Documentation:{W} {doc}\n")
    else:
        print(f"{R}__ne__() Documentation Missing{W}\n")

    doc = class_ref.Position.__str__.__doc__
    if doc != None:
        print(f"{B}__str__() Documentation:{W} {doc}\n")
    else:
        print(f"{R}__str__() Documentation Missing{W}\n")

    doc = class_ref.Position.__repr__.__doc__
    if doc != None:
        print(f"{B}__repr__() Documentation:{W} {doc}\n")
    else:
        print(f"{R}__repr__() Documentation Missing{W}\n")

    print("\n\nBinaryNode Class Docstrings:\n")

    doc = class_ref.BinaryNode._BinaryNode__set_parent.__doc__
    if doc != None:
        print(f"{B}__set_parent() Documentation:{W} {doc}\n")
    else:
        print(f"{R}__set_parent() Documentation Missing{W}\n")

    doc = class_ref.BinaryNode._BinaryNode__set_left.__doc__
    if doc != None:
        print(f"{B}__set_left() Documentation:{W} {doc}\n")
    else:
        print(f"{R}__set_left() Documentation Missing{W}\n")

    doc = class_ref.BinaryNode._BinaryNode__set_right.__doc__
    if doc != None:
        print(f"{B}__set_right() Documentation:{W} {doc}\n")
    else:
        print(f"{R}__set_right() Documentation Missing{W}\n")

    doc = class_ref.BinaryNode.__str__.__doc__
    if doc != None:
        print(f"{B}__str__() Documentation:{W} {doc}\n")
    else:
        print(f"{R}__str__() Documentation Missing{W}\n")

    print("\n\nBinaryTree Class Docstrings:\n")
    doc = BT._BinaryTree__make_position.__doc__
    if doc != None:
        print(f"{B}make_position() Documentation:{W} {doc}\n")
    else:
        print(f"{R}make_position() Documentation Missing{W}\n")

    doc = BT._BinaryTree__validate.__doc__
    if doc != None:
        print(f"{B}validate() Documentation:{W} {doc}\n")
    else:
        print(f"{R}validate() Documentation Missing{W}\n")

    doc = BT.add_root.__doc__
    if doc != None:
        print(f"{B}add_root() Documentation:{W} {doc}\n")
    else:
        print(f"{R}add_root() Documentation Missing{W}\n")

    doc = BT.add_left.__doc__
    if doc != None:
        print(f"{B}add_left() Documentation:{W} {doc}\n")
    else:
        print(f"{R}add_left() Documentation Missing{W}\n")

    doc = BT.add_right.__doc__
    if doc != None:
        print(f"{B}add_right() Documentation:{W} {doc}\n")
    else:
        print(f"{R}add_right() Documentation Missing{W}\n")

    doc = BT.is_root.__doc__
    if doc != None:
        print(f"{B}is_root() Documentation:{W} {doc}\n")
    else:
        print(f"{R}is_root() Documentation Missing{W}\n")

    doc = BT.is_leaf.__doc__
    if doc != None:
        print(f"{B}is_leaf() Documentation:{W} {doc}\n")
    else:
        print(f"{R}is_leaf() Documentation Missing{W}\n")

    doc = BT.is_ancestor.__doc__
    if doc != None:
        print(f"{B}is_ancestor() Documentation:{W} {doc}\n")
    else:
        print(f"{R}is_ancestor() Documentation Missing{W}\n")

    doc = BT.are_siblings.__doc__
    if doc != None:
        print(f"{B}are_siblings() Documentation:{W} {doc}\n")
    else:
        print(f"{R}are_siblings() Documentation Missing{W}\n")

    doc = BT.num_children.__doc__
    if doc != None:
        print(f"{B}num_children() Documentation:{W} {doc}\n")
    else:
        print(f"{R}num_children() Documentation Missing{W}\n")

    doc = BT.get_root.__doc__
    if doc != None:
        print(f"{B}get_root() Documentation:{W} {doc}\n")
    else:
        print(f"{R}get_root() Documentation Missing{W}\n")

    doc = BT.get_left.__doc__
    if doc != None:
        print(f"{B}get_left() Documentation:{W} {doc}\n")
    else:
        print(f"{R}get_left() Documentation Missing{W}\n")

    doc = BT.get_right.__doc__
    if doc != None:
        print(f"{B}get_right() Documentation:{W} {doc}\n")
    else:
        print(f"{R}get_right() Documentation Missing{W}\n")

    doc = BT.get_ancestors.__doc__
    if doc != None:
        print(f"{B}get_ancestors() Documentation:{W} {doc}\n")
    else:
        print(f"{R}get_ancestors() Documentation Missing{W}\n")

    doc = BT.get_parent.__doc__
    if doc != None:
        print(f"{B}get_parent() Documentation:{W} {doc}\n")
    else:
        print(f"{R}get_parent() Documentation Missing{W}\n")

    doc = BT.get_children.__doc__
    if doc != None:
        print(f"{B}get_children() Documentation:{W} {doc}\n")
    else:
        print(f"{R}get_children() Documentation Missing{W}\n")

    doc = BT.get_sibling.__doc__
    if doc != None:
        print(f"{B}get_sibling() Documentation:{W} {doc}\n")
    else:
        print(f"{R}get_sibling() Documentation Missing{W}\n")

    doc = BT.get_depth.__doc__
    if doc != None:
        print(f"{B}get_depth() Documentation:{W} {doc}\n")
    else:
        print(f"{R}get_depth() Documentation Missing{W}\n")

    doc = BT.replace.__doc__
    if doc != None:
        print(f"{B}replace() Documentation:{W} {doc}\n")
    else:
        print(f"{R}replace() Documentation Missing{W}\n")

    doc = BT.delete.__doc__
    if doc != None:
        print(f"{B}delete() Documentation:{W} {doc}\n")
    else:
        print(f"{R}delete() Documentation Missing{W}\n")

    doc = class_ref.__len__.__doc__
    if doc != None:
        print(f"{B}__len__() Documentation:{W} {doc}\n")
    else:
        print(f"{R}__len__() Documentation Missing{W}\n")

    print("~" * 50, "\n\n")
