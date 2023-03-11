import sys

input = sys.stdin.readline

num = int(input())

alp_to_num = {"A":1,"B":2,"C":3,"D":4,"E":5,"F":6,"G":7,"H":8,"I":9,"J":10,"K":11,
              "L":12,"M":13,"N":14,"O":15,"P":16,"Q":17,"R":18,"S":19,"T":20,
              "U":21,"V":22,"W":23,"X":24,"Y":25,"Z":26}

num_to_alp = {1:"A",2:"B",3:"C",4:"D",5:"E",6:"F",7:"G",8:"H",9:"I",10:"J",11:"K",
              12:"L",13:"M",14:"N",15:"O",16:"P",17:"Q",18:"R",19:"S",20:"T",
              21:"U",22:"V",23:"W",24:"X",25:"Y",26:"Z"}

tree = [{"left":0,"right":0} for i in range(num+1)]
pre_visit = [0 for i in range(num+1)]
in_visit = [0 for i in range(num+1)]
post_visit = [0 for i in range(num+1)]

for i in range(num):
    par, left, right = input().split()
    if left != '.':
        tree[alp_to_num[par]]["left"] = alp_to_num[left]
    if right != '.':
        tree[alp_to_num[par]]["right"] = alp_to_num[right]
    
def preorder(elem):
    res = ""
    if pre_visit[elem] == 0:
        res += num_to_alp[elem]
        pre_visit[elem] = 1
    left = tree[elem]["left"]
    right = tree[elem]["right"]
    if left != 0:
        res += preorder(left)
    if right != 0:
        res += preorder(right)
    return res
    
def inorder(elem):
    res = ""
    left = tree[elem]["left"]
    right = tree[elem]["right"]
    if left != 0:
        res += inorder(left)
    if in_visit[elem] == 0:
        res += num_to_alp[elem]
        in_visit[elem] = 1
    if right != 0:
        res += inorder(right)
    return res

def postorder(elem):
    res = ""
    left = tree[elem]["left"]
    right = tree[elem]["right"]
    if left != 0:
        res += postorder(left)
    if right != 0:
        res += postorder(right)
    if post_visit[elem] == 0:
        res += num_to_alp[elem]
        post_visit[elem] = 1
    return res

print(preorder(1))
print(inorder(1))
print(postorder(1))
