def capitalize_words():
    user_input = input("Enter a string: ")
    capitalized = ' '.join(word.capitalize() for word in user_input.split())
    return capitalized
result = capitalize_words()
print("Capitalized String:", result)
