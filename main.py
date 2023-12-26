# # create a code in which if the word contains specific letters it will print "not including"


# def find_letters(arr, letter):
#     letter_indicies =  []
    
#     for index, word in enumerate(arr):
#         if letter in word:
#             letter_indicies.append(index)
            
#         return letter_indicies
    
# # user input

# words_input = input("Enter words separated by spaces: ")
# words_array = words_input.split()

# # Get user input for the letter to find
# letter_to_find = input("Enter a letter to find: ")

# indices = find_letters(words_array, letter_to_find)
# if indices:
#     print(f"The letter '{letter_to_find}' was found at indices: {indices}")
# else:
#     print(f"The letter '{letter_to_find}' was not found in the array.")



# def find_letters_in_words(arr, words):
#     letter_indices = []
#     words = "maryamyoongi"
    
#     for index, word in enumerate(arr):
#         found_words = [char for char in word if char in words]
        
#         if letter in word and found_words:
#             if letter_indices.get[letter]:
#                 letter_indices[letter].append((index, len(found_words) ))
                
#         else:
#             letter_indices[letter] = [(index, len(found_words))]
    
#     return letter_indices.get(letter, [])


# word_input = input("enter the words separated by space: ")
# word_array = word_input.split()

# indices_with_word = find_letters_in_words(word_array)

# if indices_with_word:
#     print("Letter found in words: ")
    
#     for letter, indices in indices_with_word.item():
#         print(f"letter '{letter}' found in words at indices: {indices}")
        
#     else: print("No words match with given set of words.")

def find_letters_in_words(arr, letters):
    letter_indices = {}
    
    for letter in letters:
        letter_indices[letter] = []  # Initialize each letter's index list

        for index, word in enumerate(arr):
            if letter in word:
                found_letters = [char for char in word if char == letter]
                letter_indices[letter].append((index, len(found_letters)))
    
    return letter_indices


word_input = input("Enter the words separated by space: ")
word_array = word_input.split()

letters_input = input("Enter letters to find separated by space: ")
letters_to_find = letters_input.split()

indices_with_words = find_letters_in_words(word_array, letters_to_find)

if indices_with_words:
    print("Letters found in words:")
    
    for letter, indices in indices_with_words.items():
        print(f"Letter '{letter}' found in words at indices: {indices}")
else:
    print("No words match with the given set of words.")
