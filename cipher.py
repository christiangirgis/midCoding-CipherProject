def encode_message(message, shift):
    encoded = ""
    for char in message:
        chartoEncode = ord(char)
        shiftedChar = chartoEncode + shift
        encodedChar = chr(shiftedChar)
        encoded += encodedChar
    return encoded

def encode_file(input_file, output_file, shift):

    try:   
        # Read everytrhing from the first file. 
        with open (input_file, 'r') as input_handle:
            original_text = input_handle. read()

        # Endcode the text and save it to the new file. 
        encoded_text = encode_message(original_text, shift)
        with open(output_file, 'w') as output_handle:
            output_handle.write(encoded_text)

        print(f"file '{input_file} was encoded and saved as '{output_file}'.")
    except FileNotFoundError:
        print(f"file '{input_file}' was not found'")
    except IOError as error :
        print(f"There was a problem working with the file : {error}")

choice = input("please chose 1 as incode or 2 for decode or 3 from a file")

if choice == "1":
    message = input("Enter your message: ")
    shift = int(input("Enter the shift number: "))
    encoded = encode_message(message,shift)
    print(encoded)
elif choice == "2":
    message = input("Enter your message: ")
    shift = int(input("Enter the shift number: "))
    encoded = ""
    for char in message:
        chartoEncode = ord(char)
        shiftedChar = chartoEncode - shift
        encodedChar = chr(shiftedChar)
        encoded += encodedChar
    print(encoded)
elif choice == "3":
    filename = input("input file")
    output = input("new file name")
    shift = int(input("enter shift number"))
    encode_file(filename, output, shift)
elif choice == "4":
    filename = input("input file")
    output = input("new file name")
    shift = int(input("enter shift number"))
    encode_file(filename, output, -shift)