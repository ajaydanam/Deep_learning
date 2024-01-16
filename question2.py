
def arthmetic_operations():
    try:
        try:
            input2 = int(input("Enter your first number:"))#enter the 1st integer value
            input3 = int(input("Enter your second number :"))#enter the 2nd integer value
        except ValueError:
            print ("Please enter only number not strings")
            return None
        if type(input2) == int and type(input3) == int:
            addition = input2 + input3  #addition operator
            subtraction = input2 - input3 #subtraction operator
            multiplication = input2 * input3 #multiplication operator
            if input3 != 0:
                division = input2/input3 #division operator
            else:
                division = None
                print("division by zero is not possible")
            print("Addition of 2 numbers : ",addition)
            print("Substraction  of 2 numbers : ", subtraction)
            print("Multiplication  of 2 numbers : ", multiplication)
            print("Division  of 2 numners : " ,division)
        else:
            print("please enter a valid number")
    except Exception as error:
        print("Error occured {}".format(error))
#end

if __name__ == "__main__":
    arthmetic_operations()
