# Task a

fibonacci_1, fibonacci_2 = 1, 1
k = int(input("Write the number of a number from Fibonacci numbers: "))

while k > 1:
    fibonacci_1, fibonacci_2 = fibonacci_2, fibonacci_1 + fibonacci_2
    k -= 1
print(fibonacci_1)

fibonacci_1, fibonacci_2 = 1, 1
n = int(input("Write how many first Fibonacci numbers you want to find: "))

while n > 0:
    print(fibonacci_1, end=" ")
    fibonacci_1, fibonacci_2 = fibonacci_2, fibonacci_1 + fibonacci_2
    n -= 1

# Task b

sentence = input("Write the sentence of 2 to 20 words, in which all words are \
written from 2 to 10 Latin letters, written with 1 or more spaces and the \
period after the last word: ").replace("  ", " ").replace(".", "").split()
*first_words, last_word = sentence
words = list()

for i in sentence:
    if 2 > len(i) > 10:
        print("There are words in your sentence that have less than 2 or more than 10")
    if i == last_word:
        continue
    words.append(i)
print(sorted(words))

# Task c

word_1 = set(input("Write the first word: "))
word_2 = set(input("Write the second word: "))
letters_1 = word_1 - word_2
letters_2 = word_2 - word_1
print(letters_1 | letters_2)
