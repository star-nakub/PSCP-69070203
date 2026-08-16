
text = "Hello World"
length = len(text)
if length > 5:
    print(f"The text is too long: {length} characters")
# With walrus operator
# text = "Hello World"
# if (length := len(text)) > 5:
#     print(f"The text is too long: {length} characters")
