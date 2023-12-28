def has_vowel(word):
    vowels = "aeiouAEIOU"
    for char in word:
        if char in vowels:
            return True
    return False

def check_sentence(sentence):
    words = sentence.split()
    for word in words:
        if has_vowel(word):
            print("Stop")
            return
    print("Write again")

# Example usage:
input_sentence = input("Enter a sentence: ")
check_sentence(input_sentence)
