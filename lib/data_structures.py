spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]
####### one###########
def get_names(spicy_foods):
    all_names = [s["name"] for s in spicy_foods if "name" in s]
    print(all_names)
    return all_names
get_names(spicy_foods)

####two############
def get_spiciest_foods(spicy_foods):
    final = [food for food in spicy_foods if food.get("heat_level", 0) > 5]
    print(final)
    return final
    pass
get_spiciest_foods(spicy_foods)


#############three###########
def print_spicy_foods(spicy_foods):
    pepe = "🌶"
    for food in spicy_foods:
        if "name" and "cuisine"and "heat_level" in food:
            spicy_fin_food = f"{food["name"]} ({food["cuisine"]}) | Heat Level: {food["heat_level"]*pepe}"
            print(spicy_fin_food)
    
    pass
print_spicy_foods(spicy_foods)


#############four############
def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for food in spicy_foods:
        if food["cuisine"] == cuisine:
            print(food)
            return food   
    pass
get_spicy_food_by_cuisine(spicy_foods, "American")

###################five#############

def print_spiciest_foods(spicy_foods):
    pepe = "🌶"
    for food in spicy_foods:
        if food.get("heat_level", 0) > 5:
            spicy_fin_food = f"{food["name"]} ({food["cuisine"]}) | Heat Level: {food["heat_level"]*pepe}"
            print(spicy_fin_food)
        pass

print_spiciest_foods(spicy_foods)



############Six############

def get_average_heat_level(spicy_foods):
    heat_levels = [s["heat_level"] for s in spicy_foods if "heat_level" in s]
    average = sum(heat_levels) / len(heat_levels)
    return average

def create_spicy_food(spicy_foods, spicy_food):
        spicy_foods.append(spicy_food)
        return spicy_foods
        pass

new_food = {
    'name': 'Griot',
    'cuisine': 'Haitian',
    'heat_level': 10,
}
create_spicy_food(spicy_foods, new_food)