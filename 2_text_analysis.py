sentence = input("Enter a sentence: ")

words = sentence.split()
vowels = "aeiou"
vowel_count = 0

for character in sentence:
    if character.lower() in vowels:
        vowel_count += 1

print("Characters: %d" % len(sentence))
print("Words: %d" % len(words))
print("Vowels: %d" % vowel_count)

if len(words) > 0:
    print("First word: %s" % words[0])
    print("Last word: %s" % words[-1])
else:
    print("First word: ")
    print("Last word: ")

print("Reversed: %s" % sentence[::-1])
print("Words in reverse order: %s" % " ".join(words[::-1]))


cleaned_sentence = ""

for character in sentence:
    if character.isalnum():
        cleaned_sentence += character.lower()

if cleaned_sentence == cleaned_sentence[::-1]:
    print("Palindrome: Yes")
else:
    print("Palindrome: No")
