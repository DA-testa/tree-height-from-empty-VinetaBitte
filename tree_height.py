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
        else:
            tree[parents[i]].append(i)
    # atrodam sakni
    def recursion_compute_height(mezgls):
        if not tree[mezgls]:
            return 1
        # ja saknei vai mezglam nav pecteču atgriezam 1
        else:
            max_height = 0
            levels = (recursion_compute_height(mezglaberns) for mezglaberns in tree[mezgls])
            max_height = max(levels)
            return max_height + 1
            # atrodam pectecu augstumus
            # atgriezam tos + 1, jo sakne vel ir limenis

    return recursion_compute_height(treeroot)


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
