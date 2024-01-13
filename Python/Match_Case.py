"""Learning about the Match Case Statements in Python 3.10 and above."""

week_day = int(input("Enter Day Number : "))

match week_day:
    case 1:
        print('Monday')

    case 2:
        print("Tuesday")
        
    case 3:
        print("Wednesday")
        
    case 4:
        print("Thursday")
        
    case 5:
        print("Friday")
        
    case 6:
        print("Saturday")
        
    case 7:
        print("Sunday")
        
    # Case with if condition
    case _ if week_day > 7:
        print("Not a Day Number")
        
    case _ if week_day == 0:
        print("Using 1-indexing not 0-indexing")