from Recipe.Recipe import Recipe
from Ingredient.Ingredient import Ingredient

def LoadRecipes():
    return [
        Recipe(1, "Spaghetti Bolognese", [10, 5, 6, 1, 2]),
        Recipe(2, "Chicken Curry", [1, 2, 5, 12]),
        Recipe(3, "Beef Stroganoff"),
        Recipe(4, "Vegetable Stir Fry"),
        Recipe(5, "Fish Tacos"),
        Recipe(6, "Lentil Soup"),
        Recipe(7, "Caesar Salad"),
        Recipe(8, "Pancakes"),
        Recipe(9, "Grilled Cheese Sandwich"),
        Recipe(10, "Chocolate Brownies"),
        Recipe(11, "Cookies"),
        Recipe(12, "Roast Chicken"),
        Recipe(13, "Mashed Potatoes"),
    ]

def LoadIngredients():
    return [
        Ingredient(1, "Sel"),
        Ingredient(2, "Poivre"),
        Ingredient(3, "Huile d'olive"),
        Ingredient(4, "Beurre"),
        Ingredient(5, "Ail"),
        Ingredient(6, "Oignon"),
        Ingredient(7, "Tomate"),
        Ingredient(8, "Basilic"),
        Ingredient(9, "Parmesan"),
        Ingredient(10, "Spaghetti"),
        Ingredient(11, "Riz"),
        Ingredient(12, "Poulet"),
        Ingredient(13, "Boeuf"),
    ]