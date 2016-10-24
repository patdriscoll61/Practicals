"""
Proctical 12 - Recursion

2D pyramid using recursion

Pat Driscoll

"""

def main():
    n = int(input("Enter a number of rows: "))
    print(blocks(n))

def blocks(n):
    if n <= 0:
        return 0
    return n + blocks(n-1)

if __name__ == "__main__":
    main()