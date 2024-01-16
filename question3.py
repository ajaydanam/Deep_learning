
def string_op():
    try:
        string1 = input("Enter your sentence here:")
        if string1 != '' and string1 is not None and string1.isspace() != True and string1.isnumeric() != True:
            string1 = string1.replace('python','pythons')
            print(string1)
        else:
            print("please enter a valid sentence")
    except Exception as error:
        print("Error occured {}".format(error))
#end of block3
if __name__ == "__main__":
    string_op()