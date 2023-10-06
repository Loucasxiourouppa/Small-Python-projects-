# A Simple and Compound Interest Calulator

# function for my intro
def print_intro():
   print ("Welcome to wolving compound interest calculator.")
   print ("This program calculates your potential returns when you invest with us.")
print_intro()

# My function for the user input
def get_input():
   user_inputs = (principal, rate, years)
principal = float(input("How much would you like to invest?:"))
rate = float(input("What is the interest rate on your account?:"))
years = int(input("How long are you planning to invest (in years)?:"))

# My calculation for simple interest
    
def simple_interest(principal, rate, years):
   return(simple_outcome) 

rate = rate * 0.01
amount_principal = rate * principal
simple_earnings = amount_principal * years
simple_outcome = simple_earnings + principal

simple_result = simple_interest(principal, rate, years)

# My calculation for compound interest 
                       
def compound_interest(principal, rate, years):
   compound_outcome = principal * (1 + rate / 4) ** (4 * years)
   return(compound_outcome)
result = compound_interest(principal, rate, years)



# The function that prints my simple interest

                                 
def print_simple_output(principal, rate, years, result):
   print (" The simple interest is:", simple_interest(principal, rate, years))
 
# The function that prints my compound interest

def print_compounding_output(principal, rate, years, result):
   compound_interest(principal, rate, years)
   print (" The compound Interest is:", compound_interest(principal, rate, years))
   
 

# ---------- Challenge Functions (Optional) ----------

#def print_target_output(principal, rate, years):

    
#def get_target_input():
    


#def calculate_years_to_target(principal, rate, target):
    


    

# ---------- Main driver function ----------
# 1.	Print a welcome message explaining the purpose of the program.
# 2.	Prompt the user for the necessary inputs (see formulae and brief) and convert the values the user enters into suitable data types.
# 3.	Perform the simple and compound interest calculations.
# 4.	Print the results to the terminal in the format specified.
def main():
    
    
    simple_interest(principal, rate, years)
    compound_interest(principal, rate, years)
    print_simple_output(principal, rate, years, result)
    print_compounding_output(principal, rate, years, result)


# Program execution begins here
if __name__ == '__main__':
    main()
    
