class Bangladesh:
    def capital(self):
        print("Dhaka is the capital of bangladesh")

    def language(self):
        print("Bangla is the official language of bangladesh")

    def type(self):
        print("Bangladesh is a developing country")

class USA:
    def capital(self):
        print("Wasington, D.C is the capital of USA")

    def language(self):
        print("English is the official language of USA")

    def type(self):
        print("USA is a developed country")

bd = Bangladesh()
usa = USA()

for country in (bd,usa):
    country.capital()
    country.language()
    country.type()