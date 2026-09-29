#!/usr/bin/env python3
# Created By: Bryson
# Date: 09 29, 2026
# This program asks the user for the radius of a circle
# and then calculates the area and circumference.


import constants


def main():

    # Get the radius from the user and convert to float
    radius = float(input("Enter radius of the circle (cm): "))

    # Calculate the circumference of the circle
    circumference = 2 * constants.PI * radius

    # Calculate the area of the circle
    Area = constants.PI * (radius * radius)

    # Display the circumference and area to the user with proper units
    print("The circumference is: {:.2f} cm".format(circumference))
    print("The area is: {:.2f} cm²".format(Area))


if __name__ == "__main__":
    main()
