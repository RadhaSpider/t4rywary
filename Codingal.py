atten = int(input("enter the attendance of the student: "))
medical = input("did you have a medical cause Y or N: ")

#checking the user input predicting output accordingly

if medical == 'Y': #checking the condition 1
    print("Medical, Allowed")
else:
    if atten>=75:
        print("Allowed")
    else:
        print("You are not Allowed")
