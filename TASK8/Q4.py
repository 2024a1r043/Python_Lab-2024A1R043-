#WAP to take a word and print it in reverse order using slicing. Also check whether it is the same forward and backward
word = input("Enter a word: ")
print("Reverse:", word[::-1])
print("Palindrome:", word == word[::-1])