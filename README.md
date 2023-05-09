FractionCalculator

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
