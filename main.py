import random
from secrets import randbelow


destinations=['Sacramento', 'Stockton', 'San Francisco', 'Santa Clara']

sacramento_restaurants= ['Tower Cafe', 'Mikuni', 'Burgers & Brew', 'Rio City Cafe' ]
stockton_restaurants= ['Garlic Brothers', 'Lumberjacks', 'Prime Table Steak House', 'Blazin Cajun']
san_francisco_restaurants= ['Lucca Delicatessen', 'Sweet Maple','Lazy Bear','Scomas Restaurant']
santa_clara_restaurants= ['HiroNori', 'Rawasf', 'Fogo de Chao', 'Smoking Pig BBQ']

cali_restaurants= [sacramento_restaurants, stockton_restaurants, san_francisco_restaurants, santa_clara_restaurants]

transportaions= ['car','train','airplane', 'bus']

sacramento_entertainments= ['California State Railroad Museum', 'State Capitol','McKinley Park', 'Cathedral of the Blessed Sacrament']
stockton_entertainments= ['Pixie Woods-Louis Park','Banner Island Ballpark', 'Stockton 99 Speedway', 'Stockton Certified Farmers Market']
san_francisco_entertainments= ['Alcatraz Island', 'Golden Gate Bridge', 'Palace of Fine Arts Theater', 'Exploratorium']
santa_clara_entertainments= ['Levis Stadium', 'Californias Great America', 'Westfield Valley Fair Shopping Center', 'Central Park']

cali_entertainments= [sacramento_entertainments, stockton_entertainments, san_francisco_entertainments, santa_clara_entertainments]

intial_greeting= 'Hello! Sit back and relax, while we plane your next trip in Northern California!'

# def choosing_random_destination(norcal_cities):
#     user_input= input('Which city in Norcal would you like to visit: ')
#     while user_input != norcal_cities[0] or user_input != norcal_cities[1] or user_input != norcal_cities[2] or user_input != norcal_cities[3]:
#       user_input= input('Which city in Norcal would you like to visit: ')  
#     if user_input == norcal_cities[0]:
#        return result 
#     else:
#         print(user_input)

# choosing_random_destination(destinations)
# print(f'You have chosen ')

def randomizer(my_list):
    random_item= random.choice(my_list)
    return random_item

random_destination= randomizer(destinations)
random_entertainment= randomizer(cali_entertainments)
final_entertainment= randomizer(random_entertainment)
random_travel= randomizer(transportaions)
random_restaurant= randomizer(cali_restaurants)
final_restaurant= randomizer(random_restaurant)

print(f'You will be spending the day in {random_destination}, you will get there by {random_travel}, then you will explore {final_entertainment} and end the day with a delicious meal at {final_restaurant}.')
    















