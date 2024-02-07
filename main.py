import requests


def search_recipes(ingredient):
    app_id = "cf1f79f6"
    app_key = "66dc350344358a459b870d384f3d2b63"
    result = f"https://api.edamam.com/search?q={ingredient}&app_id={app_id}&app_key={app_key}"
    response = requests.get(result)

    # if response.status_code == 200:
    data = response.json()
    return data.get('hits', [])
    # else:
    #     print(f"Error: Unable to retrieve recipes. Status Code: {response.status_code}")
    #     return []


def display_recipes(recipes):
    if not recipes:
        print("No recipes found.")
    else:
        stop_index = 10
        for index, recipe in enumerate(recipes, start=1):
            if index > stop_index:
                break

            recipe_data = recipe['recipe']
            print(f"\nRecipe {index}:")
            print(f"Label: {recipe_data['label']}")
            print(f"Ingredients: {', '.join(recipe_data['ingredientLines'])}")
            print(f"URL: {recipe_data['url']}")


def run():
    # app_id = input("Enter your Edamam Application ID: ")
    # app_key = input("Enter your Edamam Application Key: ")

    ingredient = input("Enter an ingredient (or ingredients) to search for recipes: \n")

    recipes = search_recipes(ingredient)

    display_recipes(recipes)


run()


