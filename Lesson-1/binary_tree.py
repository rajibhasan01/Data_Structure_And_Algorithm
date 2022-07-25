class TreeNode:
    def __init__(self, key):
        self.key = key;
        self.left = None;
        self.right = None;

# Tuple items are ordered, unchangeable, and allow duplicate values.
# The differences between tuples and lists are, the tuples cannot be changed unlike lists
# Tuples are immutable which means you cannot update or change the values of tuple elements.
# You are able to take portions of existing tuples to create new tuples.
# Removing individual tuple elements is not possible.
# To explicitly remove an entire tuple, just use the del statement.
"""
    Basic Tuples Operations:
    ------------------------
    Python Expression	            Results	                        Description
    len((1, 2, 3))	                3	                            Length
    (1, 2, 3) + (4, 5, 6)	        (1, 2, 3, 4, 5, 6)	            Concatenation
    ('Hi!',) * 4	                ('Hi!', 'Hi!', 'Hi!', 'Hi!')	Repetition
    3 in (1, 2, 3)	                True	                        Membership
    for x in (1, 2, 3): print x,	1 2 3	                        Iteration

    Built-in Tuple Functions:
    -------------------------
    1. cmp(tuple1, tuple2)
    2. len(tuple)
    3. max(tuple)
    4. min(tuple)
    5. tuple(seq) //Converts a list into tuple.


"""


def parse_tuple(data):
    # print(data);
    if isinstance(data, tuple) and len(data) == 3:
        node = TreeNode(data[1]);
        node.left = parse_tuple(data[0]);
        node.right = parse_tuple(data[2]);

    elif data is None:
        node = None;
    else:
        node = TreeNode(data);

    return node;
"""
    The purse_tuple creates a new root node when a tuple of size 3 as an the input.
    Interestingly to create the left and right subtrees for the node, the parse_tuple function invokes itselft.
    The chain of recursive calls ends when parse_tuple encounters a number or None as input.
"""
# Tree to tuple converstion
def tree_to_tuple(node):
    print(node);
    if isinstance(node, TreeNode):
        if node.left is None and node.right is None:
            return node.key;
    else: return node;
    return (tree_to_tuple(node.left), node.key, tree_to_tuple(node.right));

# display tree
def display_keys(node, space='\t', level=0):
    # print(node.key if node else None, level);

    # If the node is empty
    if node is None:
        print(space*level + '0');
        return

    # If the node is a leaf
    if node.left is None and node.right is None:
        print(space*level + str(node.key));
        return;

    # If the node has children
    display_keys(node.right, space, level+1)
    print(space*level + str(node.key));
    display_keys(node.left, space, level+1);

tree_tuple = ((1,3,None), 2, ((None, 3, 4), 5, (6,7,8)));
tree2 = parse_tuple(tree_tuple);


# Manually print the tree data
print(tree2.key);
print(tree2.left.key, tree2.right.key);
print(tree2.left.left.key, tree2.left.right, tree2.right.left.key, tree2.right.right.key);
print(tree2.right.left.right.key, tree2.right.right.left.key, tree2.right.right.right.key);

# Automatically print the tree
print('The Tree are shown below: ')
display_keys(tree2, '   ');
