word_or_phrase = input().strip()
input_without_spaces = word_or_phrase.replace(" ", '')

if input_without_spaces == input_without_spaces[::-1]:
    print(f'palindrome: {word_or_phrase}')
else:
    print(f'not a palindrome: {word_or_phrase}')
