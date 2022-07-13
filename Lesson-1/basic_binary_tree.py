"""
    Question: Implement a binary tree using python
"""
# Here's a simple class representing a node within a binary tree.
class TreeNode:
    def __init__(self, key):
        self.key = key;
        self.left = None;
        self.right = None;

    def __repr__(self):
        return f"key = {self.key}, left = {self.left.key}, right = {self.right.key}";


# Let's create objects representing each node of the above class
node0 = TreeNode(3);
node1 = TreeNode(4);
node2 = TreeNode(5);

node0.left = node1;
node0.right = node2;

# And we're done! We can create a new variable tree which simply points to the root node, and use it to access all the nodes within the tree.

tree = node0;
print(tree);