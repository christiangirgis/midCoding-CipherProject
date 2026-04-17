
choice = input("please chose incode or decode")
if choice == "incode":
    message = input("Enter your message: ")
    shift = int(input("Enter the shift number: "))
    encoded = ""
    for char in message:
        chartoEncode = ord(char)
        shiftedChar = chartoEncode + shift
        encodedChar = chr(shiftedChar)
        encoded += encodedChar
    print(encoded)
else:
    message = input("Enter your message: ")
    shift = int(input("Enter the shift number: "))
    encoded = ""
    for char in message:
        chartoEncode = ord(char)
        shiftedChar = chartoEncode - shift
        encodedChar = chr(shiftedChar)
        encoded += encodedChar
    print(encoded)



