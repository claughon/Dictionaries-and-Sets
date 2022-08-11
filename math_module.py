#Calculate the square footage of a room
def squareFootage():
    width = float(input("What is the width of the room? "))
    length = float(input("What is the length of the room? "))
    area = width * length
    print("Your room is " + str(area) + " square feet.")




#Find the circumference of a circle
def circumferenceCircle():
    radius = float(input("Enter the radius of the circle "))
    circumference = 2 * 3.14 * radius
    print("Circumference = ", circumference)