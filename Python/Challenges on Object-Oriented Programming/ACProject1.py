class RomanConverter:
    def __init__(self, number):
        self.number = number

    def convert_to_roman(self):
        num_to_roman = [
            (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
            (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
            (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
        ]

        number = self.number
        roman_numeral = ""

        for value, numeral in num_to_roman:
            count = number // value
            roman_numeral += numeral * count
            number %= value

        return roman_numeral

if __name__ == "__main__":        
    number = int(input("Enter a number to convert to Roman numerals: "))
    converter = RomanConverter(number)
    print(f"The Roman numeral for {number} is {converter.convert_to_roman()}.")