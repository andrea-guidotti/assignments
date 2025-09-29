import os

# List of letters of the alphabet to count
letters = "abcdefghijklmnopqrstuvwxyz"

# Initialize a dictionary to store letter counts
# Key = letter, Value = number of occurrences
letter_counts = {}
for letter in letters:
    letter_counts[letter] = 0

# Open the text file in read mode with UTF-8 encoding
with open("test.txt", "r", encoding="UTF-8") as file:
    # Read the file line by line
    for line in file:
        # Remove spaces and convert the line to lowercase
        clean_line = line.replace(" ", "").lower()
        # Iterate over each character in the cleaned line
        for char in clean_line:
            # Update the count only if the character is a letter in the alphabet
            if char in letter_counts:
                letter_counts[char] += 1

