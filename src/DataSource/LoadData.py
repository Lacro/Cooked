import Objects.Recipe as Recipe
import Objects.Ingredient as Ingredient
import Objects.Item as Item

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
        Ingredient.Ingredient(1, "Sel"),
        Ingredient.Ingredient(2, "Poivre"),
        Ingredient.Ingredient(3, "Huile d'olive"),
        Ingredient.Ingredient(4, "Beurre"),
        Ingredient.Ingredient(5, "Ail"),
        Ingredient.Ingredient(6, "Oignon"),
        Ingredient.Ingredient(7, "Tomate"),
        Ingredient.Ingredient(8, "Basilic"),
        Ingredient.Ingredient(9, "Parmesan"),
        Ingredient.Ingredient(10, "Spaghetti"),
        Ingredient.Ingredient(11, "Riz"),
        Ingredient.Ingredient(12, "Poulet"),
        Ingredient.Ingredient(13, "Boeuf"),
    ]

def LoadShoppingList():
    return [
        Item.Item(1, 2, "Gram"),
        Item.Item(2, 3, "Gram"),
        Item.Item(3, 1, "Liter"),
    ]