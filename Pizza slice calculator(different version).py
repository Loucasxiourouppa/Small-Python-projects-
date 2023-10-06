# user inputs
answer_1 = ["1"]
answer_2 = ["2"]
answer_3 = ["3"]
answer_4 = ["4"]
answer_5 = ["5"]
answer_6 = ["6"]
answer_7 = ["7"]
answer_8 = ["8"]
answer_9 = ["9"]
answer_10 = ["10"]


def promtp():
    x = int (input(" Enter the number of people "))
    y = int (input(" Enter the number of pizzas "))
    z = int (input(" Enter the number of slices per pizza "))
    
    print("Each person gets", y * z // x ,"slices ")
    print("There are",y * z % x  ,"leftover slices" )

    
required = ("\nUse only A, B, or C\n") 
    
        # if input invalid then this loops the code.

def invalid_input():

      
    print(" invalid input.")
    print(" Please enter a numeric Value")
    promtp()

promtp()
invalid_input()

#pizzas * slices
#awnser // people
#result 





