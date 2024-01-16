
def str_operation():
    try:
        input1 = str(input("Enter your string here:"))
        if input1 != '' and input1 is not None and input1.isspace() != True and input1.isnumeric() != True:
            # Deleting at least 2 characters
            output = input1[:-2]
            # reversal of the string after

            output = output[::-1]

            print(output)
        else:
            print("please enter a valid string")
    except Exception as error:
        print("Error occured {}".format(error))
if __name__ == "__main__":
    str_operation()

