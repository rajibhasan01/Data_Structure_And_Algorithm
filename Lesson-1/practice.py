class TreeNode:
    def __init__(self, key):
        self.key = key;
        self.left = None;
        self.right = None;
    
    def __repr__(self):
        return f"key = {self.key}, left = {self.left.key}, right = {self.right.key}";


node0 = TreeNode(3);
node1 = TreeNode(4);
node2 = TreeNode(5);

node0.left = node1;
node0.right = node2;
print(node0);