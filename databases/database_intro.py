### Challenge: How many drinks do you need to buy to throw a great party? 
# you will have a list of your friends, and their favorite drink. 
# you will also know how many drinks of a certain type are drunk per hour


#list of your friends and their favorite drink
favorite_drinks = {'Adam':'Gin and Tonic','Angela':'Mate Vodka','Sven':'Whiskey','Alexandra':'Whiskey',
                    'Michael':'White Wine','Ariana':'Gin and Tonic','Thomas':'beer','Eduardo':'White Wine',
                    'Leanne':'Red Wine', 'Karla':'Whiskey', 'Taylor': 'Mate Vodka','Jonathan':'Water'}


#types of drinks people drink, with lists of examples
cocktails = ['Gin and Tonic', 'Mate Vodka', 'Rum and Coke']

wines = ['Red Wine', 'White Wine']

liquors = ['whiskey', 'gin', 'vokda']

nonalcoholic = ['tea', 'water', 'orange juice']

# number of drinks per hour people drink, depeneding on the type. 
number_of_drinks_per_hour_per_type = {'cocktails':1, 'beers':3,'wines':2,'liquors':2,'nonalcoholic':3}

cocktails_counter = 0
wines_counter = 0
liquors_counter = 0
nonalcoholic_counter = 0

for favorite_drink in favorite_drinks:
    if favorite_drinks[favorite_drink] or favorite_drinks[favorite_drink].lower() in cocktails:
        cocktails_counter += +1
    elif favorite_drinks[favorite_drink] or favorite_drinks[favorite_drink].lower() in wines:
        wines_counter += +1
    elif favorite_drinks[favorite_drink] or favorite_drinks[favorite_drink].lower() in liquors:
        liquors_counter += +1
    elif favorite_drinks[favorite_drink] or favorite_drinks[favorite_drink].lower() in nonalcoholic:
        nonalcoholic_counter += +1
        
# print(cocktails_counter)
# print(wines_counter)
# print(liquors_counter)
# print(nonalcoholic_counter)

for category in number_of_drinks_per_hour_per_type:
    if category == "cocktails":  
        cocktails_total = cocktails_counter * number_of_drinks_per_hour_per_type[category]
        print(cocktails_total)
    elif category =="wines":
        wines_total = wines_counter * number_of_drinks_per_hour_per_type[category]
        print(wines_total)
    elif category =="liquors":
        liquors_total = liquors_counter * number_of_drinks_per_hour_per_type[category]
        print(liquors_total)
    elif category == "nonalcoholic":
        nonalcoholic_total = nonalcoholic_counter * number_of_drinks_per_hour_per_type[category]
        print(nonalcoholic_total)

total_drinks_per_person = cocktails_total + wines_total + liquors_total + nonalcoholic_total
total_drinks_for_party = total_drinks_per_person * 6 #six hour long party

print(total_drinks_for_party)

        





