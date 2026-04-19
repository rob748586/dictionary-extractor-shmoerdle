import json
# This script extracts five-letter words and their meanings from a JSON file and saves the results to a new JSON file.

def extract_data(file_path):
    """Extracts data from a JSON file and returns it as a dictionary."""
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

def extract_five_letter_words(data):
    """Extracts all five-letter words from the given data."""
    five_letter_words = []
    for word in data:
        if len(word) == 5:
            five_letter_words.append(word)
    return five_letter_words

def check_for_non_alpha(word):
    """Checks if a word contains any non-alphabetic characters."""
    allowed_letters = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
    for letter in word:
        if letter not in allowed_letters:
            return True
    return False

def extract_meanings(words, data):
    """Extracts meanings for the given words from the data."""
    meanings = {}
    total = 0
    filtered = 0
    for word in words:
        total += 1
        temp = [];
        check = check_for_non_alpha(word)
        if check:
             continue
        
        for meaning in data[word]["meanings"]:
            temp.append(meaning["def"])
        
        meanings[word.title()] = temp
        filtered += 1

    print (f"Total words: {total}, Filtered words: {filtered}")
    return meanings


if __name__ == "__main__":
    """Extracts five-letter words and their meanings from a JSON file and saves the results to a new JSON file."""
    file_path = "./aacompletewordset.json"
    data = extract_data(file_path)
    words = extract_five_letter_words(data)
    extracted_meanings = extract_meanings(words, data)

    json.dump(extracted_meanings, open("extracted_meanings.json", "w"), indent=4)