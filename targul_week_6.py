# -*- coding: utf-8 -*-
"""targul_week_6.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/18hCg_2IoaHmDtp_sZGRfDVc_qRyWLZzJ
"""

from firebase import firebase

FBconn = firebase.FirebaseApplication('https://tirgul5-4b251-default-rtdb.firebaseio.com', None)

def add_single_word(word):
    """Add a single word or update its count if it exists"""
    word = word.lower()
    words = FBconn.get('/wordCounter/', None) or {}
    if word in words:
        FBconn.put('/wordCounter/', word, words[word] + 1)
    else:
        FBconn.put('/wordCounter/', word, 1)

def add_text(text):
    """Add a full text: split into words and update counts"""
    for word in text.split():
        add_single_word(word)

def update_word_count(word, new_count):
    """Update the count of a specific word"""
    word = word.lower()
    words = FBconn.get('/wordCounter/', None) or {}
    if word in words:
        FBconn.put('/wordCounter/', word, new_count)
    else:
        print(f"The word '{word}' does not exist.")

def delete_word(word):
    """Delete a specific word"""
    word = word.lower()
    words = FBconn.get('/wordCounter/', None) or {}
    if word in words:
        FBconn.delete('/wordCounter/', word)
        print(f"The word '{word}' was deleted.")
    else:
        print(f"The word '{word}' does not exist.")

def display_all_words():
    """Display all words and their counts"""
    words = FBconn.get('/wordCounter/', None) or {}
    if words:
        print("\nSaved Words:")
        for word, count in words.items():
            print(f"{word}: {count}")
    else:
        print("\nNo words saved yet.")

while True:
    print("\nWord Counter Menu:")
    print("1. Add single word")
    print("2. Add text for analysis")
    print("3. Update word count")
    print("4. Delete a word")
    print("5. View all words")
    print("6. Exit")

    choice = input("\nEnter your choice (1-6): ")

    if choice == '1':
        word = input("Add single word: ")
        add_single_word(word)
    elif choice == '2':
        text = input("Add text for analysis: ")
        add_text(text)
    elif choice == '3':
        word = input("Update word count: ")
        try:
            new_count = int(input("Enter the new count: "))
            update_word_count(word, new_count)
        except ValueError:
            print("Please enter a valid number for count.")
    elif choice == '4':
        word = input("Enter the word to delete: ")
        delete_word(word)
    elif choice == '5':
        display_all_words()
    elif choice == '6':
        print("Exiting program...")
        break
    else:
        print("Invalid choice. Please try again.")