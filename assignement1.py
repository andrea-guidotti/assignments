from matplotlib import pyplot as plt
import os
import argparse
import time

# Set command line inputs to avoid hardcoding 
parser = argparse.ArgumentParser(
    prog="lettersCounter",
    description="Counts the relative frequency of letters in a text",
    epilog= "enjoy!")

parser.add_argument("file", help = "input file to be analyze")
parser.add_argument(
     "-p", 
     "--plot",
     action="store_true", 
     help="Show histogram of letter frequencies")

args = parser.parse_args()
path = args.file

# List of letters of the alphabet to count
letters = "abcdefghijklmnopqrstuvwxyz"

# Initialize a dictionary to store letter counts
# Key = letter, Value = number of occurrences
letter_counts = {}
for letter in letters:
    letter_counts[letter] = 0

# Open the text file in read mode with UTF-8 encoding
with open(f"{path}", "r", encoding="UTF-8") as file:
    # Read the file line by line
    for line in file:
        # Remove spaces and convert the line to lowercase
        clean_line = line.replace(" ", "").lower()
        # Iterate over each character in the cleaned line
        for char in clean_line:
            # Update the count only if the character is a letter in the alphabet
            if char in letter_counts:
                letter_counts[char] += 1

# Compute total letters in text to extract frequencies
totalCounter = sum(letter_counts.values())

# Initialize a dictionary to store relative frequencies
freq = {key: count/totalCounter for key, count in letter_counts.items()}

print( "Here the letters' frequencies: \n")
for letter, frequency in freq.items():
    print(f"{letter}: {frequency}\n")

# Plot Histograf if requested from command line 
if args.plot:
    plt.bar(letter_counts.keys(),letter_counts.values(),)
    plt.xlabel("Letters")
    plt.ylabel("Occurrences")
    plt.title("Letter Histogram")
    plt.show()

      



