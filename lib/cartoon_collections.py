def roll_call_dwarves(dwarves):
    for index, name in enumerate(dwarves, start=1):
        print(f"{index}. {name}")

dwarf_names = ["Doc", "Dopey", "Bashful", "Grumpy"]
roll_call_dwarves(dwarf_names)

def summon_captain_planet(planeteer_calls):
    capitalized_calls = [call.capitalize() + "!" for call in planeteer_calls]
    return capitalized_calls

planeteer_calls = ["earth", "wind", "fire", "water", "heart"]
captain_planet_calls = summon_captain_planet(planeteer_calls)
print(captain_planet_calls)

def long_planeteer_calls(calls):
    for call in calls:
        if len(call) > 4:
            return True
    return False

# Example usage
short_words = ["puff", "go", "two"]
print(long_planeteer_calls(short_words))  # Output: False

assorted_words = ["two", "go", "industrious", "bop"]
print(long_planeteer_calls(assorted_words)) 

def find_the_cheese(ingredients):
    cheese_types = ["cheddar", "gouda", "camembert"]
    for ingredient in ingredients:
        if ingredient in cheese_types:
            return ingredient
    return None

snacks = ["crackers", "gouda", "thyme"]
print(find_the_cheese(snacks))  

soup = ["tomato soup", "cheddar", "oyster crackers", "gouda"]
print(find_the_cheese(soup))  

ingredients = ["garlic", "rosemary", "bread"]
print(find_the_cheese(ingredients))  

