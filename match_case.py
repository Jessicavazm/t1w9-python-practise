# Match case compares the variable to a series of cases to match with the right case and execute it's block of code.
day = 'Friday' 

match day:
    case 'Monday':
        print("It's Monday, start of the work week!")
    case 'Tuesday':
        print("It's Tuesday.")
    case 'Wednesday':
        print("It's Wednesday, halfway through the week.")
    case 'Thursday':
        print("It's Thursday.")
    case 'Friday':
        print("It's Friday, almost weekend!")
    case 'Saturday' | 'Sunday':
        print("It's the weekend!")
    case _: # Default case, this is executed if value doesn't match any of the cases above.
        print("Not a valid day of the week.")