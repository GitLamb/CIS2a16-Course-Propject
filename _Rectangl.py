#Jason Lambert
#CSI261
#Rectangle

class Rectangle:
    def __init__(self, height, width):
        self.height = height
        self.width = width

    def perimeter(self):
        return 2 * (self.height + self.width)

    def area(self):
        return self.height * self.width

    def print_rectangle(self):
        for i in range(self.height):
            if i == 0:
                print('*')
            elif i == self.height - 1:
                print('*' * self.width)
            else:
                print('*')

# Create a Rectangle object with height 5 and width 7
rect = Rectangle(5, 7)

# Display the results
print(f"Height: {rect.height}")
print(f"Width: {rect.width}")
print(f"Perimeter: {rect.perimeter()}")
print(f"Area: {rect.area()}")
rect.print_rectangle()

# Prompt to continue
choice = input("Continue? (y/n): ")
if choice.lower() == 'y':
    print("Continuing...")
else:
    print("Exiting...")