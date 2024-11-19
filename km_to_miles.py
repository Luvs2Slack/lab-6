def km_to_miles(kilometers):
    # complete function implementation here...
    if kilometers < 0:
        print("must be a positive number")

    miles = kilometers * 0.62

    miles = round(miles, 3)

    return miles
    
print(km_to_miles(5))