from datetime import datetime


class Book:
    def __init__(self, name, recipe_list):
        self.name = name
        self.last_update = datetime.today()
        self.creation_date = datetime.today()
        self.recipes_list = recipe_list

    def get_recipe_by_name(self, name):
        def find_recipe(recipe_list, name):
            for recipe in recipe_list:
                if (recipe.name == name):
                    print(str(recipe))
                    return recipe

        for _, recipe_list in self.recipes_list.items():
            recipe = find_recipe(recipe_list, name)
            if (recipe):
                return recipe

    def get_recipes_by_type(self, recipe_type):
        """Get all recipe names for a given recipe_type"""
        return [recipe.name for recipe in self.recipes_list[recipe_type]]

    def add_recipe(self, recipe):
        self.recipes_list[recipe.recipe_type].append(recipe)
        self.last_update = datetime.today()
        return self
