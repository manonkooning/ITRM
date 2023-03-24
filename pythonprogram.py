import tkinter as tk
import re


def clear_text(text):
    '''removes text before and including the sentence *** START OF THE PROJECT GUTENBERG EBOOK ***, removes text after *** END OF THE PROJECT GUTENBERG EBOOK ***, puts each word of the text into a list''' 
    pattern = r"\*\*\*(.*?)\*\*\*"  
    matches = re.findall(pattern, text)
    if len(matches) >= 2:
        text_between = text[text.find(matches[0])+6 : text.find(matches[1])]
    text_list = text_between.split()
    return text_list


def word_counter(text_list):
    '''counts the amount of selected American-English and British-English words'''
    american_words = ["elevator", "apartment", "sidewalk", "gasoline", "fries", "trash", "candy", "diaper",
                      "mad", "cookie", "hood", "stove", "baggage", "math", "mailbox",
                      "truck", "vacation", "pants", "overpass", "drapes", "jelly"] 
    british_words = ["lift", "flat", "pavement", "petrol", "chips", "rubbish", "sweets", 
                     "nappy", "angry", "biscuit", "bonnet", "cooker", "luggage", "maths",
                     "postbox", "lorry", "holiday", "trousers", "flyover", "curtains", "jam"]
    american_counter = 0
    british_counter = 0
    american_freq = {}
    british_freq = {}
    for word in text_list:
        if word.lower() in [w.lower() for w in american_words]:
            american_counter += 1
            if word in american_freq:
                american_freq[word] += 1
            else:
                american_freq[word] = 1
        if word.lower() in [w.lower() for w in british_words]:
            british_counter += 1
            if word in british_freq:
                british_freq[word] += 1
            else:
                british_freq[word] = 1
        
    return american_counter, british_counter, american_freq, british_freq


def print_summary(american, british, american_freq, british_freq):
    '''prints a summary of the results'''
    print("Amount of selected American-English words found:", american)
    for key, value in american_freq.items():
        print(key, value, sep=': ')
    print("\n")
    
    print("Amount of selected British-English words found:", british)
    for key, value in british_freq.items():
        print(key, value, sep=': ')
    
    print("\n")
    if american > british:
        print("The American/British ratio is:", round(american/british, 2), "\nThere are more American-English words in this file than British-English words.")
    elif american == british:
        print("The amount of American-English and British-English words used is equal in this file. The American/British ratio is: 1")
    else:
        print("The American/British ratio is:", round(american/british, 2), "There are more British-English words in this file than American-English words.")
    

def main():
    filename = input("What is your filename called?: ")
    infile = open(filename, "r")
    text = infile.read()
    text_list = clear_text(text)
    american_count, british_count, american_freq, british_freq = word_counter(text_list)
    print_summary(american_count, british_count, american_freq, british_freq)
    

if __name__ == "__main__":
    main()    