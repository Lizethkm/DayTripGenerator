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

















