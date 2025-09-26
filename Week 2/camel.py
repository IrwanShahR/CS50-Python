word = input("camelCase: ")

snakecase = ""
for char in word:
    if char.isupper():
        snakecase += "_"
        snakecase += char.lower()
    else:
        snakecase += char

print(f"snake_case: {snakecase}")
