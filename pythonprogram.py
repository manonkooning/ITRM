import tkinter as tk
import re

# nog even doen dat hij het einde ook niet pakt 
# 


def clear_text(text):
    '''removes text before and including the sentence *** START OF THE PROJECT GUTENBERG EBOOK ***, puts
    each word of the text into a list''' 
    pattern = r"\*\*\*(.*?)\*\*\*" 
    match = re.search(pattern, text)
    if match:
        new_text = text[match.end():]   
    text_list = new_text.split()
    return text_list

def word_counter(text_list):
    '''counts the amount of selected American-English and British-English words'''
    american_counter = 0
    british_counter = 0
    for word in text_list:
        if word == "mad" or word == "fall" or word == "cookie" or word == "hood" or word == "stove" or word == "apartment" or word == "elevator" or word == "baggage" or word == "math" or word == "mailbox": # if a word is American-English
            american_counter += 1
        if word == "angry" or word == "autumn" or word == "biscuit" or word == "bonnet" or word == "cooker" or word == "flat" or word == "lift" or word == "luggage" or word == "maths" or word == "postbox": # if a word is British-English
            british_counter += 1
        
    return american_counter, british_counter

def print_summary(american, british, text_list):
    print("Amount of selected American-English words found: ", american)
    print("Amount of selected British-English words found: ", british)
    # print("frequency of American-English words: ", round(american/len(text_list)))
    # print("frequency of British-English words: ", round(british/len(text_list)))
    


def main():
    filename = input("What is your filename called?: ")
    infile = open(filename, "r")
    text = infile.read()
    text_list = clear_text(text)
    american, british = word_counter(text_list)
    print_summary(american, british, text_list)
    


if __name__ == "__main__":
    main()    