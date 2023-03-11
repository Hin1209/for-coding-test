import sys

input = sys.stdin.readline

s = input().rstrip()
stack = []
out = ""

for i in range(len(s)):
    if s[i] == "*" or s[i] == "/":
        if stack:
            if stack[-1] == "*" or stack[-1] == "/":
                while len(stack) != 0 and stack[-1] != "+" and stack[-1] != "-" and stack[-1] != "(":
                    out += stack[-1]
                    stack.pop()
        stack.append(s[i])
    elif s[i] == "(":
        stack.append(s[i])
    elif s[i] == ")":
        while stack[-1] != "(":
            out += stack[-1]
            stack.pop()
        stack.pop()
    elif s[i] == "+" or s[i] == "-":
        if stack:
            while len(stack) != 0 and stack[-1] != "(":
                out += stack[-1]
                stack.pop()
            stack.append(s[i])
        else:
            stack.append(s[i])
    else:
        out += s[i]
        
while stack:
    out += stack[-1]
    stack.pop()
print(out)