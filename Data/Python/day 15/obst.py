import sys

def optimal_bst(p, q, n):
    e = [[0] * (n + 2) for _ in range(n + 2)]  # expected cost
    w = [[0] * (n + 2) for _ in range(n + 2)]  # weight (sum of p and q)
    root = [[0] * (n + 1) for _ in range(n + 1)]  # root table

    # Initialization
    for i in range(1, n + 2):
        e[i][i - 1] = q[i - 1]
        w[i][i - 1] = q[i - 1]

    # Fill tables in increasing order of length
    for l in range(1, n + 1):  # l = length of subtrees
        for i in range(1, n - l + 2):
            j = i + l - 1
            e[i][j] = sys.maxsize
            w[i][j] = w[i][j - 1] + p[j - 1] + q[j]
            for r in range(i, j + 1):
                t = e[i][r - 1] + e[r + 1][j] + w[i][j]
                if t < e[i][j]:
                    e[i][j] = t
                    root[i][j] = r

    return e, root

def print_obst_structure(root, i, j, parent="None", direction="root"):
    if i > j:
        return
    r = root[i][j]
    print(f"Key[{r}] is the {direction} of {parent}")
    print_obst_structure(root, i, r - 1, f"Key[{r}]", "left child")
    print_obst_structure(root, r + 1, j, f"Key[{r}]", "right child")

# Example usage
keys = [10, 20, 30]
p = [0.3, 0.2, 0.5]
q = [0.1, 0.1, 0.1, 0.1]
n = len(keys)

e, root = optimal_bst(p, q, n)

print("Minimum expected cost:", e[1][n])
print("Optimal BST structure:")
print_obst_structure(root, 1, n)