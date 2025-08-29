import re


def check():
    pattern = r"^A.*A$"
    strings = ["A", "AA", "ABA", "APPLE", "AP123", "AB"]

    for text in strings:
        if re.match(pattern, text):
            print("Pattern is valid")
        else:
            print("Invalid pattern")

if __name__ == "__main__":
    check()