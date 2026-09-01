# Without typecasting (treats input as string, repeats string 3 times)
val_str = input("Enter a number: ")
result_str = val_str * 3

# With typecasting to integer (performs numerical multiplication)
val_int = int(val_str)
result_int = val_int * 3

print("Without typecasting (String repetition):", result_str)
print("With typecasting (Integer multiplication):", result_int)