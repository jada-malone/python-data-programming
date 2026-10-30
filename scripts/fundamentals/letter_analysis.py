from collections import defaultdict

# PROGRAM: Letter Frequency Analyzer
# PURPOSE: Analyze the frequency of each letter in five-letter words 
#          from a file based on their position in the word.
# INPUT: File containing five-letter words
# PROCESS: Count occurrences of each letter at each position in the words.
# OUTPUT: Frequency counts of each letter for each position in the word.
# HONOR CODE: On my honor, as an Aggie, I have neither given nor 
#             received unauthorized aid on this academic work.

def analyze_letter_positions(filename):
    """
    Analyzes letter frequencies in five-letter words from a file.
    """
    # Initialize a dictionary to count occurrences
    letter_count = defaultdict(lambda: [0, 0, 0, 0, 0])
    
    with open(filename, 'r') as file:
        for line in file:
            word = line.strip()
            if len(word) == 5:  # Ensure the word has exactly 5 letters
                for i, char in enumerate(word):
                    letter_count[char][i] += 1
    
    # Print the results
    for letter, counts in sorted(letter_count.items()):
        print(f"Letter '{letter}': {counts}")

if __name__ == "__main__":
    # The original file was cut off after the line above; this call was added so the script runs.
    analyze_letter_positions("five-letter-words.txt")
