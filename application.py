# Aqui escribe tu codigo

import sys
import os
import smtplib, getpass
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

class country_and_capital(object):
    def __init__(self):
        self.CountryAndCapital = {}

    def menu(self):
        while True:
            option_menu = "Invalid Input"
            while option_menu == "Invalid Input":
                self.clean_screen()
                self.menu_print()
                option_menu = self.menu_option()
                option_menu = self.validation_menu(option_menu)

                self.cycleMSG(option_menu, "Invalid option!!!")
            self.decision(option_menu)

    def menu_print(self):
        print "1.COUNTRY"
        print "2.COUNTRIES"
        print "3.CAPITALS"
        print "4.ALL"
        print "5.ALLORDERED"
        print "6.ALLMAIL"
        print "7.EXIT"

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
        if option_menu == 'country' or option_menu == "exit" or option_menu == "countries" or option_menu == "capitals" or option_menu == "all" or option_menu == "allordered" or option_menu == "allmail":
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
        elif option_menu == "allordered":
            self.option_all_ordered()
        elif option_menu == "allmail":
            self.option_send_email()
        elif option_menu == "exit":
            self.option_exit()

    def option_country(self, country = ""):
        self.clean_screen()
        myCycle = "Add country"
        while myCycle == "Add country":
            call_add_and_verify = "Added incorrectly"
            while call_add_and_verify == "Added incorrectly":
                verify_cc = "Country or Capital incorrect!!!"
                while verify_cc == "Country or Capital incorrect!!!":
                    country, capital = self.ask_country_capital()
                    verify_cc = self.verify_countrycapital(country, capital)
                    print "%s\n" % verify_cc
                call_add_and_verify = self.call_add_and_verify(country, capital)
            question_add = self.my_question_add()
            myCycle = self.decision_add(question_add)

    def ask_country_capital(self):
        country = raw_input("Enter the country: ")
        capital = raw_input("Enter the capital: ")
        country, capital = self.min_country_capital(country, capital)
        return country, capital

    #Function 3
    def min_country_capital(self, country, capital):
        country = country.lower()
        capital = capital.lower()
        return country, capital

    #Function 4
    def verify_countrycapital(self, country, capital):
        country, capital = self.validate_spaces(country, capital)
        if country.isalpha() and capital.isalpha():
            return "Entered correctly"
        else:
            return "Country or Capital incorrect!!!"

    def validate_spaces(self,country, capital):
        if " " in country:
            part1, part2 = country.split(" ")
            country = part1 + part2
        if " " in capital:
            part1, part2 = capital.split(" ")
            capital = part1 + part2
        return country, capital

    #Function 5
    def call_add_and_verify(self, country, capital):
        my_items = self.add_country_and_capital(country, capital)
        my_values = self.CountryAndCapital.values()
        if country in my_items and capital in my_values:
            call_add_and_verify = "Added correctly"
        else:
            call_add_and_verify = "Added incorrectly"
        return call_add_and_verify

    def add_country_and_capital(self, country, capital):
        self.CountryAndCapital [country] = capital
        return self.CountryAndCapital

    def my_question_add(self):
        question_add = raw_input("Do you want to add another country and capital? y/n: ")
        question_add = self.add_lower(question_add)
        return question_add

    #Function 6
    def add_lower(self, question_add):
        question_add = question_add.lower()
        return question_add

    def decision_add(self, question_add):
        question_add = self.pass_if_question_is_valid(question_add)
        if question_add == "y":
            print ""
            myCycle = "Add country"
        elif question_add == "n":
            myCycle = "Not add country"
        return myCycle

    def pass_if_question_is_valid(self, question_add):
        myCycle = self.verify_question_add(question_add)
        while myCycle == "Invalid option":
            question_add = self.my_question_add()
            myCycle = self.verify_question_add(question_add)
        return question_add

    #Function 7
    def verify_question_add(self, question_add):
        if question_add != "y" and question_add != "n":
            return "Invalid option"
        else:
            return "Valid option"

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

    def option_all_ordered(self):
        self.clean_screen()
        print "COUNTRIES AND CAPITALS ORDERED"
        for key, value in sorted(self.CountryAndCapital.items()):
            print key, value
        self.cycleMSG("Invalid Input", "PRESS ENTER")
        self.menu()

    def option_send_email(self):
        self.clean_screen()

        user = 'danielsandoval182@gmail.com'
        receiver = 'danielsandoval182@gmail.com'
        self.print_info_mail(user, receiver)
        password = getpass.getpass('Enter the password: ')

        header = MIMEMultipart()
        header['From'] = user
        header['To'] = receiver
        header['Subject'] = "Prueba enviar correos python"
        for key, value in self.CountryAndCapital.items():
            message = key + ", " + value
            header.attach(MIMEText(message, 'plain'))

        try:
            mail = smtplib.SMTP('smtp.gmail.com', 587) #Host y puerto SMTP de Gmail
            mail.starttls() #Protocolo de cifrado de datos utilizado por gmail
            mail.login(user, password)
            mail.sendmail(user, receiver, header.as_string())

            mail.close() #Close conection SMTP

            print "Email sent"
            self.cycleMSG("Invalid Input", "PRESS ENTER")
        except ValueError:
            print "Error: unable to send mail"
        self.menu()

    def print_info_mail(self, user, receiver):
        print "From %s" % user
        print "To: %s" % receiver

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
