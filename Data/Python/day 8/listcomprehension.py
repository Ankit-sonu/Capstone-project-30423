

def main():
    data = [x * x for x in range(1, 6)]
    print(data)

    n = int(input("Enter a numbers"))
    evenos = [x for x in range(1, n + 1) if x % 2 == 0]
    print(evenos)

    names = ["alice", "bob", "charlie", "david"]
    uppernames = [name.upper() for name in names]
    print(uppernames)

    list = [1, 2, 3, 4, 5]
    result = ['even' if x % 2 == 0 else 'odd' for x in list]
    print(result)

    matrix = [[1, 2], [3, 4], [5, 6]]
    flatmatrix = [num for row in matrix for num in row]
    print(flatmatrix)

if __name__ == '__main__':
    main()