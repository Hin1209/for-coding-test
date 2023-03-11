import sys
sys.setrecursionlimit(10**9)

input = sys.stdin.readline

preorder = []
while True:
    try:
        t = int(input())
        preorder.append(t)
    except:break
    
def find_tree(start,end):
    if start > end: 
        return
    
    div = end + 1
    
    for i in range(start+1, end+1):
        if preorder[start] < preorder[i]:
            div = i
            break
    
    find_tree(start+1,div-1)
    find_tree(div,end)
    print(preorder[start])

find_tree(0,len(preorder)-1)