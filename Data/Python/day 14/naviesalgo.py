
def naives_algorithm(pattern, text):
    m = len(pattern)
    n = len(text)

    for i in range(n-m + 1):
        j = 0
        while j<m and text[i+j] == pattern[j]:
            j+=1
        if j == m:
            print(f"Pattern Found at index {i}")


if __name__ == "__main__":
    text1 = 'AABAACAADAABAABA'
    pattern1 = 'AABA'
    print("Pattern 1:")
    naives_algorithm(pattern1,text1)

