#import
import random
import string

#this will be input that contains word to be code or decode
text = input("Enter text that you want to encode or decode: ")

#this input will ask user whether he want to code or decode the word
input1 = input("Type 'a' if you want to code the word and type 'b' if you want to decode: ")

#If user type "a" to code the word this if statements will work
if input1.lower() == "a":
    words = text.split()
    encoded_sentence = ""
    for word in words:
        if len(word) >= 1:
            first_letter = word[0]
            rest_of_word = word[1:]
            random_string_start = ''.join(random.choices(string.ascii_lowercase, k=3))
            random_string_end = ''.join(random.choices(string.ascii_lowercase, k=3))
            encoded_word = random_string_start + rest_of_word + first_letter + random_string_end
        else:
            encoded_word = word
        encoded_sentence += encoded_word + " "
    print(encoded_sentence.strip())
        
#if user type "b" to decode the word this elif statement will work
elif input1.lower() == "b":
    words = text.split()
    decoded_sentence = ""
    for word in words:
        if len(word) >= 1:
            word_without_random = word[3:-3]
            last_letter = word_without_random[-1]
            rest_of_word = word_without_random[:-1]
            decoded_word = last_letter + rest_of_word
        else:
            decoded_word = word
        decoded_sentence += decoded_word + " "
    print(decoded_sentence.strip())
        
#if user type letter other than a or b this will be printed
else:
    print("Please type 'a' or 'b' for encoding or decoding, respectively.")
