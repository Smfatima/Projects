def has_vowel(word):
    vowels = "aeiouAEIOU"
    for char in word:
        if char in vowels:
            return True
    return False

def check_sentence(sentence):
    words = sentence.split()
    has_vowel_flag = False
    
    for word in words:
        if has_vowel(word):
            has_vowel_flag = True
            break
    
    return "Stop" if has_vowel_flag else "Write again"

# Example usage:
input_sentence = input("Enter a sentence: ")
check_sentence(input_sentence)
