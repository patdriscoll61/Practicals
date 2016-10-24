"""
Proctical 12 - Recursion

2D pyramid using for loop

Pat Driscoll

"""

def main():
    blocks = 0
    n = int(input("Enter a number of rows: "))
    for i in range (1,n+1,1):
        blocks += i
    print(blocks)

if __name__ == "__main__":
    main()