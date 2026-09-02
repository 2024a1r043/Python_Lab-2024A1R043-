#WAP to take a string and seperate charcters present at even index positions and odd index positions
string = input("Enter a string: ")
even_index_chars = string[::2]
odd_index_chars = string[1::2]
print("Characters at even index positions:", even_index_chars)
print("Characters at odd index positions:", odd_index_chars)