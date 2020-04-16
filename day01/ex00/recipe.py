class Recipe:
    def __init__(self, name, cooking_lvl, cooking_time, ingredients, recipe_type, description=''):
        self.name = name
        self.cooking_lvl = cooking_lvl
        self.cooking_time = cooking_time
        self.ingredients = ingredients
        self.description = description
        self.recipe_type = recipe_type

    def __str__(self):
        """Return the string to print with the recipe info"""
        txt = f"Name: {self.name}\nCooking Level: {self.cooking_lvl}\nCooking Time: {self.cooking_time}\nIngredients: {self.ingredients}\nRecipe Type: {self.recipe_type}\nDescription: {self.description}"
        return txt
