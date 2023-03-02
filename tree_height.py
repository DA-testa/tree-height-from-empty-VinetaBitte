# python3

import sys
import threading


def compute_height(n, parents):
    # Write this function
    tree = [[] for i in range(n)]
    # izveidojam koku no listiem
    for i in range(n):
        if parents[i] == -1:
            treeroot = i
        tree[parents[i]].append(i)
    # atrodam sakni
    max_height = 0
    # Your code here
    #height = 1
    stack = [(treeroot, 1)]
    while len(stack) > 0:
        mezgls, current_height = stack.pop()
        if current_height > max_height:
            max_height = current_height
        for item in range(len(parents)):
            if parents[item] == mezgls:
                stack.append((item, current_height + 1))

    return max_height


def main():
    # implement input form keyboard and from files
    text = input()
    if "I" in text:
        n = int(input())
        parents = list(map(int, input().split()))
        tree_height = compute_height(n, parents)
    elif "F" in text:
        filename = input()
        if "a" in filename:
            return
        else:
            with open("./test/" + filename, mode = "r") as fails:
                n = int(fails.readline())
                parents = list(map(int, fails.readline().split()))
                tree_height = compute_height(n, parents) 

    print(tree_height)
    
    # let user input file name to use, don't allow file names with letter a
    # account for github input inprecision
    
    # input number of elements
    # input values in one variable, separate with space, split these values in an array
    # call the function and output it's result


# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
