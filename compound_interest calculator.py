# A Simple and Compound Interest Calculator

def print_intro():
    print("Welcome to the wolving compound interest calculator.")
    print("This program calculates your potential returns when you invest with us.")

def get_input():
    principal = float(input("How much would you like to invest?: "))
    rate = float(input("What is the interest rate on your account?: "))
    years = int(input("How long are you planning to invest (in years)?: "))
    return principal, rate, years

def simple_interest(principal, rate, years):
    return principal * (1 + (rate / 100) * years)

def compound_interest(principal, rate, years):
    compound_interest = principal * (pow((1 + rate / 100), years))
    return compound_interest

def print_simple_output(principal, rate, years, result):
    print("£{0} invested at {1:.1f}% for {2} years is: £{3:.2f}".format(principal, rate, years, result))

def print_compounding_output(principal, rate, years, result):
    print("£{0} invested at {1:.1f}% for {2} years with compound interest is: £{3:.2f}".format(principal, rate, years, result))

# ---------- Main driver function ----------
# 1. Print a welcome message explaining the purpose of the program.
# 2. Prompt the user for the necessary inputs (see formulae and brief) and convert the values the user enters into suitable data types.
# 3. Perform the simple and compound interest calculations.
# 4. Print the results to the terminal in the format specified.
def main():
    print_intro()
    principal, rate, years = get_input()
    simple_result = simple_interest(principal, rate, years)
    compound_result = compound_interest(principal, rate, years)
    print_simple_output(principal, rate, years, simple_result)
    print_compounding_output(principal, rate, years, compound_result)

# Program execution begins here
if __name__ == '__main__':
    main()
