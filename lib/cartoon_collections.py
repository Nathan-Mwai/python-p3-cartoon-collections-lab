def roll_call_dwarves(names):
    [print(f"{index + 1}. {name}") for index,name in enumerate(names)]
    pass

def summon_captain_planet(planeteer):
    return [f"{power.title()}!" for power in planeteer]
    

def long_planeteer_calls(calls):
    return any(len(call) > 4 for call in calls )
# any returns true or false if condition is met


def find_the_cheese(snacks):
    cheese_types = {"cheddar", "gouda", "camembert"}
    
    for snack in snacks:
        if snack in cheese_types:
            return snack
    return None

