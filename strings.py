
name = input("enter youer name")
print(name.upper())
print(name.lower())
print(name.title())

fav_food = input("favorite food")
x = fav_food.strip()

print("favorite", x, "food")

word = input("give me word") 
print(len(word))
print(word[1:])
print(word[-1:])

sentence = "i like cats"
x = sentence.replace("cats","dogs")

def find_letter():
    print("Find Letter")
    word = input("Enter a word: ")
    letter = input("Enter a letter to search for: ")
    idx = word.find(letter)
    idx = word.lower().find(letter.lower())
    print(f"Word: {word}, Letter: {letter}, Index: {idx}")



wordSix = input("enter another word! ")
print(wordSix.count('a'))

"""def first_three_letters(): 
   print("First three letters")  
 word = input("Enter a word: ")
 print(f"First 3 letters of {word}: {word[0:3]}") 
  print()"""

secret_word = input ("\n9) Enter a word with at least 5 letters
print ("First 2 letters:", [secret_word [:21) print ("Middle part:", secret_word [2:-21)
print("Last 2 letters:", secret_word[-2:])

inspect_sentence = input("\n10) Enter a sentence: "]
print("Lowercase:", inspect_sentence. Lower())
print("Uppercase:", inspect_sentence.upper())
print "Total characters:", len( inspect_sentence)) print ("Contains 'python':", "python" in inspect_sentence. lower
