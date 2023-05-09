"""
Fractions

The program prints a command line interpreter that will print the prompt "> ",
after which the user shall enter a command. The entire line the user enters will
be interpreted to be a command. The operation of the program can finish with the
command "quit", which prints "Bye bye!" before quiting. If something else than a
known command is entered to the command interpreter, it will print
"Unknown command!". The command line interpreter shall give the user a new
prompt until the execution of the program ends.

The command "add" first asks the user to enter a fraction and then give it a
name. The fractions are saved to the calculator's memory, allowing the program
to use them in the commands in the later sections.

The command "print" allows you to print fractions saved to a calculator's
memory. The command asks the user to enter a fraction's name. The program prints
an error message if the name is not saved to the calculator's memory.

The command "list" prints an alphabetical list of the contents of each of the
calculator's memory locations. The command prints nothing if no fractions have
been saved.

The command "*" to the program you implemented in the previous section. The
command in question executes multiplication to the two fractions saved to the
calculator's memory. The command asks for two fraction names and prints an error
message if the user enters a name that does not exist.

The command "file" reads the input file and saves the fractions from the file to
the calculator's memory. The name of the input file is asked from the user. An
error message will be printed if there is any errors in the file or file cannot
be opened. The format of each row is: name=integer/integer

Writer of the program: EILeh

"""

class Fraction:
    """
    This class represents one single fraction that consists of
    numerator (osoittaja) and denominator (nimittäjä).
    """

    def __init__(self, numerator, denominator):
        """
        Constructor. Checks that the numerator and denominator are of
        correct type and initializes them.

        :param numerator: int, fraction's numerator
        :param denominator: int, fraction's denominator
        """

        # isinstance is a standard function which can be used to check if
        # a value is an object of a certain class.  Remember, in Python
        # all the data types are implemented as classes.
        # ``isinstance(a, b´´) means more or less the same as ``type(a) is b´´
        # So, the following test checks that both parameters are ints as
        # they should be in a valid fraction.
        if not isinstance(numerator, int) or not isinstance(denominator, int):
            raise TypeError

        # Denominator can't be zero, not in mathematics, and not here either.
        elif denominator == 0:
            raise ValueError

        self.__numerator = numerator
        self.__denominator = denominator

    # FI: Käänteisluku
    def reciprocal(self):
        return Fraction(self.__denominator, self.__numerator)

    # FI: Vastaluku
    def complement(self):
        return Fraction(-self.__numerator, self.__denominator)

    def multiply(self, other):

        # Initializes a new variable that stores the information of
        # multiplied numerator.
        new_numerator = self.__numerator * other.__numerator

        # Initializes a new variable that stores the information of
        # multiplied denominator.
        new_denominator = self.__denominator * other.__denominator

        # Returns the new fraction.
        return Fraction(new_numerator, new_denominator)

    def divide(self, other):
        # When dividing fractions, the division can be done by multiplying
        # the first fraction with the second fraction's reciprocal.

        # Initializes a new variable that stores the information of
        # divided numerator.
        new_numerator = self.__numerator * other.__denominator

        # Initializes a new variable that stores the information of
        # divided denominator.
        new_denominator = self.__denominator * other.__numerator

        # Returns the new fraction.
        return Fraction(new_numerator, new_denominator)

    def add(self, other):
        # When adding fractions together, the denominator must be the same
        # and to do that both fractions' denominators and numerators are
        # multiplied with each other denominators.

        # Initializes a new variable that stores the information of
        # multiplied numerator.
        new_numerator = self.__numerator * other.__denominator

        # Initializes a new variable that stores the information of
        # multiplied denominator.
        new_denominator = self.__denominator * other.__denominator

        # Initializes a new variable that stores the information of
        # multiplied numerator of the other fraction.
        new_other_numerator = other.__numerator * self.__denominator

        # Initializes a new variable that stores the information of
        # numerators added together.
        numerator_added = new_numerator + new_other_numerator

        # Returns the new fraction.
        return Fraction(numerator_added, new_denominator)

    def __It__(self, other):
        # When comparing fractions, the denominator must be the same
        # and to do that both fractions' denominators and numerators are
        # multiplied with each other denominators.

        # Initializes a new variable that stores the information of
        # multiplied numerator.
        new_numerator = self.__numerator * other.__denominator

        # Initializes a new variable that stores the information of
        # multiplied numerator of the other fraction.
        new_other_numerator = other.__numerator * self.__denominator

        return new_numerator < new_other_numerator

    def __gt__(self, other):
        # When comparing fractions, the denominator must be the same
        # and to do that both fractions' denominators and numerators are
        # multiplied with each other denominators.

        # Initializes a new variable that stores the information of
        # multiplied numerator.
        new_numerator = self.__numerator * other.__denominator

        # Initializes a new variable that stores the information of
        # multiplied numerator of the other fraction.
        new_other_numerator = other.__numerator * self.__denominator

        return new_numerator > new_other_numerator

    def __str__(self):
        return f"{self.__numerator}/{self.__denominator}"

    def deduct(self, other):
        # When deducting fractions, the denominator must be the same and to do
        # that both fractions' denominators and numerators are multiplied
        # with each other denominators.

        # Initializes a new variable that stores the information of
        # multiplied numerator.
        new_numerator = self.__numerator * other.__denominator

        # Initializes a new variable that stores the information of
        # multiplied denominator.
        new_denominator = self.__denominator * other.__denominator

        # Initializes a new variable that stores the information of
        # multiplied numerator of the other fraction.
        new_other_numerator = other.__numerator * self.__denominator

        # Initializes a new variable that stores the information of deducted
        # numerators.
        numerator_deducted = new_numerator - new_other_numerator

        # Returns the new fraction.
        return Fraction(numerator_deducted, new_denominator)

    def simplify(self):
        # Stores the value of the greatest common divisor in the variable
        # greatest_common.
        greatest_common = greatest_common_divisor(self.__numerator,
                                                  self.__denominator)

        # Stores a new value to the numerator by dividing the numerator by
        # the greatest common divisor.
        self.__numerator = self.__numerator // greatest_common

        # Stores a new value to the denominator by dividing the denominator by
        # the greatest common divisor.
        self.__denominator = self.__denominator // greatest_common

        # Calls the function return_string that prints the fraction in wanted
        # form after new values have been stored to the numerator and
        # denominator.
        return self.return_string()


    def return_string(self):
        """
        :returns: str, a string-presentation of the fraction in the format
                       numerator/denominator.
        """

        if self.__numerator * self.__denominator < 0:
            sign = "-"

        else:
            sign = ""

        return f"{sign}{abs(self.__numerator)}/{abs(self.__denominator)}"


def greatest_common_divisor(a, b):
    """
    Euclidean algorithm. Returns the greatest common
    divisor (suurin yhteinen tekijä).  When both the numerator
    and the denominator is divided by their greatest common divisor,
    the result will be the most reduced version of the fraction in question.
    """

    while b != 0:
        a, b = b, a % b

    return a


def main():
    dictionary_of_fractions = {}
    is_input_correct = True

    first_operand_payload = ""
    second_operand_payload = ""
    second_fraction = ""
    first_fraction = ""

    while is_input_correct:
        command = input("> ")

        if command == "add":
            str_input_fraction = input("Enter a fraction in the form "
                                       "integer/integer: ")
            name = input("Enter a name: ")

            # Stores a new key-value pair to the dictionary
            # dictionary_of_fractions where the variable name is key and the
            # variable str_input_fraction is value.
            dictionary_of_fractions[name] = str_input_fraction

        elif command == "print":
            name = input("Enter a name: ")

            # If the input name was not found in the dictionary, prints an
            # error.
            if name not in dictionary_of_fractions:
                print(f"Name {name} was not found")
                continue

            # Prints the name of the fraction and the fraction itself.
            print(f"{name} = {dictionary_of_fractions[name]}")

        elif command == "list":
            # Goes through the keys of the dictionary and prints the
            # dictionary's keys and values.
            for fractions in sorted(dictionary_of_fractions):
                print(f"{fractions} = {dictionary_of_fractions[fractions]}")

        elif command == "*":
            name_first = input("1st operand: ")

            # If the name is found in the dictionary, finds also the values
            # of the current name and stores the information to variables for
            # later use.
            if name_first in dictionary_of_fractions:
                for key, first_operand_payload in \
                        dictionary_of_fractions.items():
                    if key == name_first:
                        first_fraction = first_operand_payload

            # If the name isn't in the dictionary, prints an error.
            else:
                print(f"Name {name_first} was not found")
                continue

            # Splits current name's value which is payload in the dictionary
            # and stores the numerator and denominator to a variables as an
            # integer.
            split_first_operand = first_fraction.split("/")
            first_numerator = int(split_first_operand[0])
            first_denominator = int(split_first_operand[1])

            name_second = input("2nd operand: ")

            # If the name is found in the dictionary, finds also the values
            # of the current name and stores the information to variables for
            # later use.
            if name_second in dictionary_of_fractions:
                for key, second_operand_payload in \
                        dictionary_of_fractions.items():
                    if key == name_second:
                        second_fraction = second_operand_payload

            # If the name isn't in the dictionary, prints an error.
            else:
                print(f"Name {name_second} was not found")
                continue

            # Splits current name's value which is payload in the dictionary
            # and stores the numerator and denominator to a variables as an
            # integer.
            split_second_operand = second_fraction.split("/")
            second_numerator = int(split_second_operand[0])
            second_denominator = int(split_second_operand[1])

            # Creates a new object for first_fraction_int.
            first_fraction_int = Fraction(first_numerator, first_denominator)

            # Creates a new object for second_fraction_int.
            second_fraction_int = Fraction(second_numerator, second_denominator)

            # Does the multiplication.
            fraction_multiplied = first_fraction_int.multiply\
                (second_fraction_int)

            # Checks if the '-' needs to added to the variable
            # fraction_multiplied.
            fraction_multiplied_str = fraction_multiplied.return_string()

            print(f"{first_numerator}/{first_denominator} * "
                  f"{second_numerator}/{second_denominator} = "
                  f"{fraction_multiplied_str}")

            # Simplifies the fraction.
            simplified_multiplied_fraction_str = fraction_multiplied.simplify()

            print(f"simplified {simplified_multiplied_fraction_str}")

        elif command == "file":
            file_name = input("Enter the name of the file: ")

            # Program tries to read the input file.
            try:
                file = open(file_name, mode="r")

            # If there was an error reading the file, program prints it.
            except FileNotFoundError:
                print("Error: the file cannot be read.")
                continue

            # Goes through every line in the file.
            for file_line in file:

                try:
                    # A single line in the file is split from '=' to separate
                    # the fraction itself and the name of the fraction.
                    split_row = file_line.split("=")

                    # Fraction's name is at the index zero.
                    fraction_name = split_row[0]

                    # The fraction itself is at the index one.
                    the_fraction = split_row[1]

                # If the line in the file doesn't have it formed correctly,
                # the program will print an error.
                except IndexError:
                    print("Error: the file cannot be read.")
                    continue

                try:
                    # The fraction is split from the '/' to separate
                    # numerator and denominator.
                    split_fraction = the_fraction.split("/")

                    # Initializes a new variable that stores the information
                    # of the numerator.
                    new_numerator = int(split_fraction[0])

                    # Initializes a new variable that stores the information
                    # of the denominator.
                    new_denominator = int(split_fraction[1])

                    # Initializes a new object.
                    fraction_object = Fraction(new_numerator, new_denominator)

                    # Returns a correct form to print the fraction.
                    fraction_clause = fraction_object.return_string()

                    # Adds the fraction from the file to the dictionary
                    # dictionary_of_fractions where its key is variable
                    # fraction_name and value is variable fraction_clause.
                    dictionary_of_fractions[fraction_name] = fraction_clause

                # If there is a problem reading the file, the program prints
                # an error.
                except IndexError:
                    print("Error: the file cannot be read.")
                    continue

        elif command == "quit":
            print("Bye bye!")
            return

        else:
            print("Unknown command!")


if __name__ == "__main__":
    main()