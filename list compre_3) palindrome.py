palindrome = [no for no in range(100, 1000) if str(no) == str(no)[::-1]]
print(palindrome)

middle = len(palindrome) // 2
middle_five = palindrome[middle-2 : middle+3]
print(middle_five)