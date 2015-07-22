# Aqui escribe tu codigo

import sys
import os

'''try:
    text = countries.decode("utf-8") #turn into a string
    variable = True
    for i in text:
        if i.isalpha() == True or i == " ": #if the string is alfhabet
            if variable == True: #if variable is true
                variable = True
        else:
            variable = False #else, make it false
    if variable == False: #if variable is false
        print "Invalid Country" #print message
        count = True'''

class country_and_capital(object):
    def __init__(self):
        self.CountryAndCapital = {}

    def menu(self):
        option_menu = "Invalid Input"
        while option_menu == "Invalid Input":
            self.clean_screen()
            self.menu_print()
            option_menu = self.menu_option()
            option_menu = self.validation_menu(option_menu)

            self.cycleMSG(option_menu, "Invalid option!!!")
        self.decision(option_menu)

    def menu_print(self):
        print "COUNTRY"
        print "COUNTRIES"
        print "CAPITALS"
        print "ALL"
        print "EXIT"

    def menu_option(self):
        option_menu = raw_input("What do you want to do: ")
        return option_menu

    #Function 1
    def validation_min(self, option_menu):
        option_menu = option_menu.lower()
        return option_menu

    #Function 2
    def validation_menu(self, option_menu):
        option_menu = self.validation_min(option_menu)
        if option_menu == 'country' or option_menu == "exit" or option_menu == "countries" or option_menu == "capitals" or option_menu == "all":
            return option_menu
        else:
            option_menu = "Invalid Input"
            return option_menu

    def decision(self, option_menu):
        if option_menu == "country":
            self.option_country()
        elif option_menu == "countries":
            self.option_show_countries()
        elif option_menu == "capitals":
            self.option_show_capitals()
        elif option_menu == "all":
            self.option_show_all()
        elif option_menu == "exit":
            self.option_exit()

    def option_country(self, country = ""):
        self.clean_screen()
        myCycle = True
        while myCycle == True:
            verify_add = "Added correctly"
            while verify_add == "Added correctly":
                verify_cc = "Country or Capital incorrect!!!"
                while verify_cc == "Country or Capital incorrect!!!":
                    country, capital = self.ask_country_capital()
                    verify_cc = self.verify_countrycapital(country, capital)
                    print "%s\n" % verify_cc
                verify_add = self.verify_add(country, capital)
            question_add = self.my_question_add()
            myCycle = self.decision_add(question_add)

    def ask_country_capital(self):
        country = raw_input("Enter the country: ")
        capital = raw_input("Enter the capital: ")
        return country, capital

    #Function 3
    def verify_countrycapital(self, country, capital):
        if country.isalpha() and capital.isalpha():
            return "Entered correctly"
        else:
            return "Country or Capital incorrect!!!"

    def add_country_and_capital(self, country, capital):
        country = country.lower()
        capital = capital.lower()
        self.CountryAndCapital [country] = capital
        return self.CountryAndCapital

    #Function 4
    def verify_add(self, country, capital):
        my_items = self.add_country_and_capital(country, capital)
        my_values = self.CountryAndCapital.values()
        if country in my_items and capital in my_values:
            verify_add = "Added correctly"
        else:
            verify_add = "Added incorrectly"
        return verify_add

    def my_question_add(self):
        question_add = raw_input("Do you want to add another country and capital? y/n: ")
        question_add = self.add_lower(question_add)
        return question_add

    #Function 5
    def add_lower(self, question_add):
        question_add = question_add.lower()
        return question_add

    #Function 6
    def decision_add(self, question_add):
        myCycle = False
        while myCycle == False:
            if question_add == "y":
                print ""
                myCycle = True
                return myCycle
            elif question_add == "n":
                self.menu()
                myCycle = False
                return myCycle
            else:
                print "Invalid option"
                question_add = self.my_question_add()

    def option_show_countries(self):
        self.clean_screen()
        my_countries = self.CountryAndCapital.keys()
        print "COUNTRIES:"
        for countries in my_countries:
            print countries
        self.cycleMSG("Invalid Input", "PRESS ENTER")
        self.menu()

    def option_show_capitals(self):
        self.clean_screen()
        my_capitals = self.CountryAndCapital.values()
        print "CAPITALS:"
        for capitals in my_capitals:
            print capitals
        self.cycleMSG("Invalid Input", "PRESS ENTER")
        self.menu()

    def option_show_all(self):
        self.clean_screen()
        countries_captials = self.CountryAndCapital.items()
        print "COUNTRIES AND CAPITALS"
        for countries,capitals in countries_captials:
            print "%s," %countries, capitals
        self.cycleMSG("Invalid Input", "PRESS ENTER")
        self.menu()

    def cycleMSG(self, option, message):
        cycleInvalide = option
        while cycleInvalide == "Invalid Input":
            enter = raw_input(message)
            if enter == "":
                cycleInvalide = "Valid Input"
            else:
                cycleInvalide = "Invalid Input"

    def clean_screen(self):
        os.system('reset')

    def option_exit(self):
        self.clean_screen()
        sys.exit()

def my_application():
    main = country_and_capital()
    main.menu()

if __name__ == "__main__":
    my_application()
