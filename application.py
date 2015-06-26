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
        myCycle = True
        while myCycle == True:
            self.clean_screen()
            self.menu_print()
            option_menu = self.menu_option()
            myCycle = self.validation_menu(option_menu)

            self.cycleMSG(myCycle, "Invalid option!!!")
        self.decision(option_menu)

    def menu_print(self):
        print "COUNTRY"
        print "COUNTRIES"
        print "CAPITALS"
        print "ALL"
        print "EXIT"

    #Function test_menu_option
    def menu_option(self, option_menu = ""):
        if __name__ == "__main__":
            option_menu = raw_input("What do you want to do: ")
        option_menu = option_menu.lower()
        return option_menu

    def validation_menu(self, option_menu):
        if option_menu == 'country' or option_menu == "exit" or option_menu == "countries" or option_menu == "capitals" or option_menu == "all":
            myCycle = False
        else:
            myCycle = True
        return myCycle

    def decision(self, option_menu):
        if option_menu == "country":
            self.option_country()
        elif option_menu == "countries":
            self.option_show_countries()
        elif option_menu == "capitals":
            self.option_show_capitals()
        elif option_menu == "all":
            self.show_country_capital()
        elif option_menu == "exit":
            self.option_exit()

    def option_country(self, country = ""):
        self.clean_screen()
        myCycle = True
        while myCycle == True:

            myCycle = True
            while myCycle == True:
                country, capital = self.ask_country_capital()
                verify = self.verify_countrycapital(country, capital)

                if verify == "Entered correctly":
                    myCycle = False
                else:
                    print "Country or Capital incorrect\n"
                    myCycle = True

            self.add_country_and_capital(country, capital)
            question_add = self.my_question_add()
            myCycle = self.decision_add(question_add)

    def ask_country_capital(self):
        country = raw_input("Enter the country: ")
        capital = raw_input("Enter the capital: ")
        return country, capital

    def verify_countrycapital(self, country, capital):
        if (country and capital).isalpha():
            if __name__ == "__main__":
                print "Entered correctly"
            return "Entered correctly"

    def add_country_and_capital(self, country, capital):
        self.country = country
        self.capital = capital
        country = country.lower()
        capital = capital.lower()
        self.CountryAndCapital [country] = capital
        print self.CountryAndCapital
        return self.CountryAndCapital

    def my_question_add(self):
        question_add = raw_input("\nDo you want to add another country and capital? y/n: ")
        question_add = question_add.lower()
        return question_add

    def decision_add(self, question_add):
        while True:
            if question_add == "y":
                print ""
                return True
            elif question_add == "n":
                self.menu()
                return False
            else:
                print "Invalid"
                question_add = self.my_question_add()

    def option_show_countries(self):
        self.clean_screen()
        my_countries = self.CountryAndCapital.keys()
        print "COUNTRIES:"
        for countries in my_countries:
            print countries
        self.cycleMSG(True, "PRESS ENTER")
        self.menu()

    def option_show_capitals(self):
        self.clean_screen()
        my_capitals = self.CountryAndCapital.values()
        print "CAPITALS:"
        for capitals in my_capitals:
            print capitals
        self.cycleMSG(True, "PRESS ENTER")
        self.menu()

    def show_country_capital(self):
        self.clean_screen()
        countries_captials = self.CountryAndCapital.items()
        print "COUNTRIES AND CAPITALS"
        for countries,capitals in countries_captials:
            print "%s," %countries, capitals
        self.cycleMSG(True, "PRESS ENTER")
        self.menu()

    def cycleMSG(self, myCycle, message):
        cycleInvalide = myCycle
        while cycleInvalide == True:
            enter = raw_input(message)
            if enter == "":
                cycleInvalide = False
            else:
                cycleInvalide = True

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
