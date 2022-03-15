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

intial_greeting= print('Hello! Sit back and relax, while we plan your next trip in Northern California!')
second_greeting= print('First, we will start with a destination.')


def randomizer(my_list):
    random_item= random.choice(my_list)
    return random_item

random_destination= randomizer(destinations)
print(f'We have selected {random_destination} for you!')
users_destination_confirmation= input(f'Would you like to continue y or n? ')
if users_destination_confirmation == 'y':
    print('Awesome!')
elif users_destination_confirmation =='n':
    while users_destination_confirmation != 'y':
        random_destination= randomizer(destinations)
        users_destination_confirmation= input(f'We have selected {random_destination}, would you like to continue, y/n? ')
print(f'{random_destination} is a great choice, now lets pick mode of transportation.')
    
    
random_travel= randomizer(transportaions)
print(f'We have selected {random_travel}.')
users_travel_confirmation= input(f'Would you like to continue y or n? ')
if users_travel_confirmation == 'y':
    print('Alright,')
elif users_travel_confirmation =='n':
    while users_travel_confirmation != 'y':
        random_travel= randomizer(transportaions)
        users_travel_confirmation= input(f'We have selected {random_travel}, would you like to continue, y/n? ')
print(f'You will get to {random_destination} by {random_travel}.')
print('Next, we will choose the entertainment.')

if random_destination == destinations[0]:
    random_entertainment= randomizer(cali_entertainments[0])
    print(f'We have selected {random_entertainment}.')
    users_entertainment_confirmation= input(f'Would you like to continue y or n? ')
    if users_entertainment_confirmation == 'y':
        print('Ooo,fun.')
    elif users_entertainment_confirmation =='n':
        while users_entertainment_confirmation != 'y':
            random_entertainment= randomizer(cali_entertainments[0])
            users_entertainment_confirmation= input(f'We have selected {random_entertainment}, would you like to continue, y/n? ')
if random_destination == destinations[1]:
    random_entertainment= randomizer(cali_entertainments[1])
    print(f'We have selected {random_entertainment}.')
    users_entertainment_confirmation= input(f'Would you like to continue y or n? ')
    if users_entertainment_confirmation == 'y':
        print('Ooo,fun.')
    elif users_entertainment_confirmation =='n':
        while users_entertainment_confirmation != 'y':
            random_entertainment= randomizer(cali_entertainments[1])
            users_entertainment_confirmation= input(f'We have selected {random_entertainment}, would you like to continue, y/n? ')
if random_destination == destinations[2]:
    random_entertainment= randomizer(cali_entertainments[2])
    print(f'We have selected {random_entertainment}.')
    users_entertainment_confirmation= input(f'Would you like to continue y or n? ')
    if users_entertainment_confirmation == 'y':
        print('Ooo,fun.')
    elif users_entertainment_confirmation =='n':
        while users_entertainment_confirmation != 'y':
            random_entertainment= randomizer(cali_entertainments[2])
            users_entertainment_confirmation= input(f'We have selected {random_entertainment}, would you like to continue, y/n? ')
if random_destination == destinations[3]:
    random_entertainment= randomizer(cali_entertainments[3])
    print(f'We have selected {random_entertainment}.')
    users_entertainment_confirmation= input(f'Would you like to continue y or n? ')
    if users_entertainment_confirmation == 'y':
        print('Ooo,fun.')
    elif users_entertainment_confirmation =='n':
        while users_entertainment_confirmation != 'y':
            random_entertainment= randomizer(cali_entertainments[3])
            users_entertainment_confirmation= input(f'We have selected {random_entertainment}, would you like to continue, y/n? ')
print('Finally, we will choose a restaurant.')

if random_destination == destinations[0]:
    random_restaurant= randomizer(cali_restaurants[0])
    print(f'We have selected {random_restaurant}.')
    users_restaurant_confirmation= input(f'Would you like to continue y or n? ')
    if users_restaurant_confirmation == 'y':
        print('Yummy!')
    elif users_restaurant_confirmation =='n':
        while users_restaurant_confirmation != 'y':
            random_restaurant= randomizer(cali_restaurants[0])
            users_restaurant_confirmation= input(f'We have selected {random_restaurant}, would you like to continue, y/n? ')
if random_destination == destinations[1]:
    random_restaurant= randomizer(cali_restaurants[1])
    print(f'We have selected {random_restaurant}.')
    users_restaurant_confirmation= input(f'Would you like to continue y or n? ')
    if users_restaurant_confirmation == 'y':
        print('Delicious!')
    elif users_restaurant_confirmation =='n':
        while users_restaurant_confirmation != 'y':
            random_restaurant= randomizer(cali_restaurants[1])
            users_restaurant_confirmation= input(f'We have selected {random_restaurant}, would you like to continue, y/n? ')
if random_destination == destinations[2]:
    random_restaurant= randomizer(cali_restaurants[2])
    print(f'We have selected {random_restaurant}.')
    users_restaurant_confirmation= input(f'Would you like to continue y or n? ')
    if users_restaurant_confirmation == 'y':
        print('Sounds tasty!')
    elif users_restaurant_confirmation =='n':
        while users_restaurant_confirmation != 'y':
            random_restaurant= randomizer(cali_restaurants[2])
            users_restaurant_confirmation= input(f'We have selected {random_restaurant}, would you like to continue, y/n? ')
if random_destination == destinations[3]:
    random_restaurant= randomizer(cali_restaurants[3])
    print(f'We have selected {random_restaurant}.')
    users_restaurant_confirmation= input(f'Would you like to continue y or n? ')
    if users_restaurant_confirmation == 'y':
        print('Bomb!')
    elif users_restaurant_confirmation =='n':
        while users_restaurant_confirmation != 'y':
            random_restaurant= randomizer(cali_restaurants[3])
            users_restaurant_confirmation= input(f'We have selected {random_restaurant}, would you like to continue, y/n? ')
print(f'You will be traveling to {random_destination} by {random_travel}, exploring {random_entertainment} and ending the day with a delicious meal at {random_restaurant}.')

users_trip_confirmation= input(f'Would you like to confirm your trip y or n? ')
if users_trip_confirmation == 'y':
        print('Sounds like a fun filled day!')
elif users_trip_confirmation =='n':
    while users_trip_confirmation != 'y':
        random_destination= randomizer(destinations)
        random_travel= randomizer(transportaions)
        random_entertainment= randomizer(cali_entertainments)
        random_restaurant= randomizer(cali_restaurants)
print('Sounds like a fun filled day!')    















