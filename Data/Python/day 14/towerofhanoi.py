def towers_of_hanoi(n, source, destination, auxiliary):
    if n == 1:
        print(f"Move disk 1 from {source} to {destination}")
        return
    towers_of_hanoi(n - 1, source, auxiliary, destination)
    print(f"Move disk {n} from {source} to {destination}")
    towers_of_hanoi(n - 1, auxiliary, destination, source)

# Driver Code
if __name__ == "__main__":
    n = int(input("Enter number of towers"))  # Number of disks
    towers_of_hanoi(n, 'A', 'C', 'B')