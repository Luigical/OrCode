#Create a dictionary of words
word_values = {
    "orem": 3,
    "oracle": 5,
    "orgin": 4,
    "apple": 2,
    "bore":2,
}

#Check if string starts with the substring
def count(substring):
    total = 0
    for word, value in word_values.items():
        if word.startswith(substring):
            total += value
    return total

#Add a word to the dictionary
def add_word(word, value):
    word_values[word] = value
    print(f"Added the word " + word)


#Test Print Statements
print(count("or"))
print(count("org"))
add_word("organ", 5)
print(count("or"))
print(count("org"))
print(count("ginor"))
print(count("duck"))
print(count("rock"))
