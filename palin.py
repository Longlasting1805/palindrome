def findPalindrome():
    reverse = 0
    remainder = 0
    n = input("enter number")
    number = n
    while n != 0:
        remainder = n % 10
        reverse = reverse * 10 + remainder
        n /= 10

    if number == reverse:
        print('Given number is a palindrome number')
    else:
        print('Given number is not a palindrome number')
