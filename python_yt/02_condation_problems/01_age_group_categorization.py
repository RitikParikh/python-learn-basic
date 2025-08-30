age = input("Provide me age: ")

def calculateAge(number):
    try:
        age = int(number)
        result = "Your provided person's age group is: "
        match True:
            case _ if (age > 0 and age < 13):
                print(result + "Child")
            case _ if (age >= 13 and age < 20):
                print(result + "Teenager")
            case _ if (age >= 20 and age < 60):
                print(result + "Adult")
            case _ if (age >= 60):
                print(result + "Senior")
            case _:
                print("Your provided person's age should be greater then 1")
            
        
        return True
    except ValueError:
        print("Input not accepted — it must be a number")
        return False

    
calculateAge(age)