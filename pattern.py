#RIGHT SIDE TRIANGLE UPWARD
def pattern():
 n=5
 for i in range(1,n+1):
 print(' *'*i)
#RIGHT SIDE TRIANGLE DOWNWARD
def pattern1():
 n=5
 for i in range(n , 0, -1):
 print(' *'*i)
pattern1()


#two pyramids from left side
n = 11
for i in range(n):
    if i < 5:
        print("* " * (i+1))
    else:
        print("* " * (n-i))


#diamond pyramid
def diamond_pattern(n):
    for i in range(1, n + 1):
        for j in range(1, n - i + 1):
            print(" ", end="")
        for k in range(1, 2 * i):
            if k % 2 == 1:
                print("*", end="")
            else:
                print(" ", end="")
        print("")

    for i in range(n - 1, 0, -1):
        for j in range(1, n - i + 1):
            print(" ", end="")
        for k in range(1, 2 * i):
            if k % 2 == 1:
                print("*", end="")
            else:
                print(" ", end="")
        print("")

# Example: Print a diamond pattern with 5 rows
n = 5
diamond_pattern(n)


#10. Hello pyramid
n = 5

for i in range(n):
    for j in range(n):
        if i == 0 or i == n - 1 or j == 0 or j == n - 1:
            print("*", end="")
        else:
            print(" ", end="")
    print()

def converted_hello_pyramid():
    word = "HELLO"
    for i in range(len(word)*2 - 1):
        if i < len(word):
            print(" " * (len(word) - i - 1), end="")
            print(*[word[j] for j in range(i+1)])
        else:
            print(" " * (i - len(word)), end="")
            print(*[word[j] for j in range(2*len(word)-1 - i)])

converted_hello_pyramid()


#SQUARE PATTERN
n=int(input('Enter a value:'))
for i in range(1,n+1):
 if i==1 or i==n:
 print('* '*n)
 else:print('* ',' '*(n-3),'*')


#.UPWARD TRIANGLE
def pattern6():
 n = int(input('Enter a num:'))
 for i in range(1,n+1):
 print(' '*(n-i),'*'*(i+(i-1)))
pattern6()


#.DOWNWORD TRIANGLE
def pattern7():
 n = int(input('Enter a num:'))
 for i in range(n,0,-1):
 print(' '*(n-i),'*' *(i+(i-1)))
pattern7()

