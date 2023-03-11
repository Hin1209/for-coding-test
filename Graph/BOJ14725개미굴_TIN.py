import sys

input = sys.stdin.readline

n = int(input())
root = []
tree = {}
for _ in range(n):
    tmp = list(input().split())
    depth = int(tmp[0])
    subtree = tree
    for i in tmp[1:]:
        if i not in subtree:
            subtree[i] = {}
        subtree = subtree[i]
                
def get_tree(tree, depth):
    keys = sorted(tree.keys())
    for key in keys:
        print("--" * depth, end="")
        print(key)
        get_tree(tree[key], depth+1)
        
get_tree(tree, 0)