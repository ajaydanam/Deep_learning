
def grade():
    try:
        try:
            score = int(input("Enter your score here:"))
        except ValueError:
            print ("Please enter number in numeric format not strings")
            return None
        if score != '' and score is not None:
            if score > 100 or score < 0:
                print("Score not in range please enter a valid score")
            else:
                if score >= 90 and score <= 100: #Range of Grade A score
                    print("A")
                elif score >= 80 and score <= 89: #Range of Grade B score
                    print("B")
                elif score >= 70 and score <= 79: #Range of Grade C score
                    print("c")
                elif score >= 60 and score <= 69: #Range of Grade D score
                    print("D")
                else:
                    print("F") #Grade F score
            
        else:
            print("please enter a valid number")
    except Exception as error:
        print("Error occured {}".format(error)) 
#end
if __name__ == "__main__":
    grade()
