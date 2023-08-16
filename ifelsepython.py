#print ("Please enter the time") shift-3 comments out the code
time = int(input("Please enter the time"))
mondayOff = (input("Do you have Monday off?"))
majorTask = (input("Do you have any Major Tasks?"))
gameOfThrones = (input("Do you want to watch The Game of Thrones?"))

if((time > 1000 or majorTask == "No") and gameOfThrones == "Yes" and mondayOff == "Yes"):
        print("You can watch The Game Of Thrones")
else:
        print("Sorry Bud, you cant watch anything because you work Monday & chores to do")
        
