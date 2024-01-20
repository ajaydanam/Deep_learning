def full_name():
    try:
        fir_name = str(input("Enter your first_name :"))
        las_name = str(input("Enter your last_name:"))
        if validateString(fir_name) and validateString(las_name):
            full_name = fir_name + " " + las_name
            print(full_name)
            return full_name
        else:
            print("please enter a valid string")
    except Exception as error:
        print("Error occured {}".format(error))
def validateString(name):

    if name != '' and name is not None and name.isspace() != True and name.isnumeric() != True:
        return True
    else:
        return False        

def string_alternative(full_name):
    try:
        alt_name = full_name
        print(alt_name[::2])
    except Exception as error:
        print("Error occured {}".format(error))

if __name__ == "__main__":
    inp_name= full_name()
    string_alternative(inp_name)