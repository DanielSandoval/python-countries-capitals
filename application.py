# Aqui escribe tu codigo

import sys
import os

def option_exit():
    clean_screen()
    sys.exit()

def clean_screen():
    os.system('reset')

def min_countries_and_capitals(country, capital):
    if __name__ == "__main__":
        country = country.lower()
        capital = capital.lower()
    message = "Entered correctly"
    return message

def option_country(country = ""):
    clean_screen()
    if __name__ == "__main__":
        country = raw_input("Enter the country: ")
        capital = raw_input("Enter the capital: ")
        min_countries_and_capitals(country, capital)

def decision(first_word):
    if first_word == "country":
        option_country()
    elif first_word == "exit":
        option_exit()

def write_country(first_word = ""):
    if __name__ == "__main__":
        first_word = raw_input("Enter the word country: ")
    first_word = first_word.lower()
    decision(first_word)
    return first_word

def menu():
    clean_screen()
    print "COUNTRY"
    print "EXIT"
    write_country()

if __name__ == "__main__":
    menu()
