import sys
sys.setrecursionlimit(10**6)

input = sys.stdin.readline

n = int(input())
inorder = list(map(int, input().split()))
postorder = list(map(int, input().split()))
index = [0] * (n+1)

for i in range(len(inorder)):
    index[inorder[i]] = i

def find_subtree(in_start,in_end,post_start,post_end):
    if in_start > in_end or post_start > post_end:
        return
    
    root = postorder[post_end]
    index_root = index[root]
    size_left = index_root - in_start
    
    print(root, end=" ")
    find_subtree(in_start,index_root-1,post_start,post_start+size_left-1)
    find_subtree(index_root+1,in_end,post_start+size_left,post_end-1)
    
find_subtree(0,n-1,0,n-1)
    