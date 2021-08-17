from flask import request
from flask_restful import Resource
from http import HTTPStatus

from models.recipe import Recipe, recipe_list

class RecipeListResource(Resource):

    """Will find and return all recipe data by iterating through each item and returning a temporary list"""

    def get(self):

        data = []

        for recipe in recipe_list:
            if recipe.is_publish is True:
                data.append(recipe.data)

        return {"data": data}, HTTPStatus.OK

    """Creates a new recipe item using POST command"""

    def post(self):
        data = request.get_json()

        recipe = Recipe(name=data["name"],
                        description=data["description"],
                        num_of_servings=data["num_of_servings"],
                        cook_time=data["cook_time"],
                        directions=data["directions"]
        )

        recipe_list.append(recipe)

        return recipe.data, HTTPStatus.CREATED