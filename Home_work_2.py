# Сформуйте стрінг, в якому міститься інформація про певне слово.
# "Word [тут слово] has [тут довжина слова, отримайте з самого сдлва] letters",
# наприклад "Word 'Python' has 6 letters".
# Для отримання слова для аналізу скористайтеся константою або функцією input().


your_word = input("Enter your word: ")
word_length = len(your_word)
print("Word " + your_word + " has " + str(word_length) + " letters")