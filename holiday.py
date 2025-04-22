"""
Calculate a user’s total holiday cost, which includes the plane cost, hotel cost, and car rental cost.
""" 

#This function will take num_nights as an argument and return a total cost for the hotel stay.
def hotel_cost(num_nights):
    
    #Set a price per night.
    price_per_night = 500
    return num_nights * price_per_night
    
#This function will take city_flight as an argument and return a cost for the flight.
def plane_cost(city_flight):
    
    #Set a price for the city (Johannesburg).
    if city_flight == "Johannesburg":
        return 950
    
    #Set a price for the city (Cape Town).
    elif city_flight == "Cape Town":
        return 1200
        
    #Set a price for the city (Durban).
    elif city_flight == "Durban":
        return 1100
        
    #Set a price for the city (East London).
    elif city_flight == "East London":
        return 1000
        
    #Set an answer if city not included.
    else:
        return 0 
        
#This function will take rental_days as an argument and return the total cost of the car rental.
def car_rental(rental_days):
    
    #Set a price for the car rental per day. 
    price_per_day = 150
    return rental_days * price_per_day
    
#This function takes three arguments:
#num_nights, city_flight, and rental_days.
#Using these three arguments, call the hotel_cost(), plane_cost(), and car_rental() functions with their respective arguments, and finally return the total cost for the holiday.
def holiday_cost(num_nights, city_flight, rental_days):
    
    #Calculate the total cost of the holiday.
    total = (hotel_cost(num_nights) + plane_cost(city_flight) + car_rental(rental_days))
    return total 
    
#Display the intro. 
print("Welcome to the Holiday Cost Calculator!")
print(" ")#Display line break

#Prompt user to input their holiday detials.
city_flight = input("Enter the city you'll be flying to: ")
num_nights = int(input("Enter the number of nights you'll be staying at the hotel: "))
rental_days = int(input("Enter the number of days you'll be hiring a car: "))

#Calculate the total cost of the holiday.
total_cost = holiday_cost(num_nights, city_flight, rental_days)


print(" ")#Display line break.
print("Holiday detials.")
print(" ")#Display line break.

#Display the holiday detials.
print(f"Flight to {city_flight}: R{plane_cost(city_flight)}")
print(f"Hotel for {num_nights} nights: R{hotel_cost(num_nights)}")
print(f"Car rental for {rental_days} days: R{car_rental(rental_days)}")
print(f"Total holiday cost: R{total_cost}")

print(" ")#Display line break.
print("Thank you for using us : ) ")