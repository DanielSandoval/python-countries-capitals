# Aqui escribe tu codigo

def country(country = ""):
    if __name__ == "__main__":
        country = raw_input("Enter a country: ")
    country = country.lower()
    return country

def capital(capital = ""):
    if __name__ == "__main__":
        capital = raw_input("Enter the capital: ")
    capital = capital.lower()
    return capital

def capitals_countries(first_word):
    if first_word == "country":
        country()
        capital()

def write_country(first_word = ""):
    if __name__ == "__main__":
        first_word = raw_input("Enter the word country: ")
    first_word = first_word.lower()
    capitals_countries(first_word)
    return first_word

def main():
    write_country()

if __name__ == "__main__":
    main()
