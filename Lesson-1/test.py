class TreeNode:
    def __init__(self, key):
        self.key = key;
        self.left = None;
        self.right = None;

    def __repr__(self):
        return f"{self.key} is the key";

node0 = TreeNode(2);
node1 = TreeNode(3);
node3 = TreeNode(4);
count = 0;

def parse_tree(data):
    global count;
    count += 1;
    print(f"{count}. data -> ", data);
    if isinstance(data, tuple) and len(data) == 3:
        node = TreeNode(data[1]);
        node.left = parse_tree(data[0]);
        node.right = parse_tree(data[2]);
    elif data is None:
        node = None;
    else:
        node = TreeNode(data);

    return node;


tree_tuple = ((1, 3, None), 2, ((None, 3, 4), 5, (6, 7, 8)));
tree = parse_tree(tree_tuple);

def tree_to_tuple(node):
    print(node);
    if isinstance(node, TreeNode):
        if node.left is None and node.right is None:
            return node.key;
    else: return node;
    return (tree_to_tuple(node.left), node.key, tree_to_tuple(node.right));
tuple_tree = tree_to_tuple(tree)
print(tuple_tree);

def display_keys(node, space="\t", level=0):
    if node in None:
        print(space*level + '#');
        return
    if node.left is None and node.right is None:
        print(space*level + str(node.key))
        return

    display_keys(node.right, space, level+1);
    print(space*level + str(node.key));
    display_keys(node.left, space, level+1);