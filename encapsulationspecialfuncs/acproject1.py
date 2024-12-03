class StringReverser:
    def reverse_words(self, input_string):
        words = input_string.split()
        reversed_words = words[::-1]
        return " ".join(reversed_words)


if __name__ == "__main__":
    reverser = StringReverser()
    sample_string = "Hello world this is Python"
    reversed_string = reverser.reverse_words(sample_string)
    print("Original String:", sample_string)
    print("Reversed String:", reversed_string)