import requests

def get_recipes_by_ingredients(ingredients, number, api_key, rank):
    url = f"https://api.spoonacular.com/recipes/findByIngredients?ingredients={ingredients}&number={numberofrecipes}&apiKey={api_key}&ranking={rank}"
    response = requests.get(url)
    data = response.json()
    return data

def get_nutrion_by_id(id, api_key):
    url = f"https://api.spoonacular.com/recipes/{id}/nutritionWidget.json?apiKey={api_key}"
    response = requests.get(url)
    data = response.json()
    return data

numberofrecipes = 1
api_key = "804caf8927fb46e88c6334ef4c298e98"
rank = 1

def print_recipes(ingredients):
    recipes = get_recipes_by_ingredients(ingredients, numberofrecipes, api_key,rank)
    for recipe in recipes:
        print("Title:", recipe["title"])
        print("Image URL:", recipe["image"])
        print("----------")
    print(recipes)
    print(get_nutrion_by_id(recipes[0]["id"], api_key))