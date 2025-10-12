import Recipe.Recipe as Recipe
from Ingredient.Ingredient import Ingredient

def LoadRecipes():
    return [
        Recipe.Recipe(1, "Spaghetti Bolognese", [10, 5, 6, 1, 2]),
        Recipe.Recipe(2, "Chicken Curry", [1, 2, 5, 12]),
        Recipe.Recipe(3, "Beef Stroganoff", [1, 2, 5, 12]),
        Recipe.Recipe(4, "Vegetable Stir Fry"),
        Recipe.Recipe(5, "Fish Tacos"),
        Recipe.Recipe(6, "Lentil Soup"),
        Recipe.Recipe(7, "Caesar Salad"),
        Recipe.Recipe(8, "Pancakes"),
        Recipe.Recipe(9, "Grilled Cheese Sandwich"),
        Recipe.Recipe(10, "Chocolate Brownies"),
        Recipe.Recipe(11, "Cookies"),
        Recipe.Recipe(12, "Roast Chicken"),
        Recipe.Recipe(13, "Mashed Potatoes"),
        Recipe.Recipe(14, "Steak and Eggs"),
        Recipe.Recipe(15, "Shrimp Scampi"),
        Recipe.Recipe(16, "Quiche Lorraine"),
        Recipe.Recipe(17, "Tuna Salad"),
        Recipe.Recipe(18, "BLT Sandwich"),
        Recipe.Recipe(19, "French Toast"),
        Recipe.Recipe(20, "Apple Pie"),
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