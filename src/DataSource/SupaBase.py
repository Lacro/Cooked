import Objects.Recipe as Recipe
import Objects.Ingredient as Ingredient
import Objects.Item as Item
import DataSource.DataBaseInfo as DBInfo
from supabase import create_client, Client

supabase: Client = create_client(DBInfo.SUPABASE_URL, DBInfo.SUPABASE_KEY)

def LoadRecipes():
    response = (
        supabase.table(DBInfo.TABLE_RECIPES)
        .select("*")
        .execute()
    )

    return [
        Recipe.Recipe(
            elt[DBInfo.TABLE_RECIPES_ID],
            elt[DBInfo.TABLE_RECIPES_NAME],
        )
        for elt in response.data
    ]

def LoadIngredients():
    
    response = (
        supabase.table(DBInfo.TABLE_INGREDIENTS)
        .select("*")
        .execute()
    )

    return [
        Ingredient.Ingredient(
            elt[DBInfo.TABLE_INGREDIENTS_ID],
            elt[DBInfo.TABLE_INGREDIENTS_NAME],
        )
        for elt in response.data
    ]

def AddIngredient(ingredient):
    (
        supabase.table(DBInfo.TABLE_INGREDIENTS)
            .insert({ DBInfo.TABLE_INGREDIENTS_NAME: ingredient.name })
            .execute()
    )


def LoadShoppingList():
    response = (
        supabase.table(DBInfo.TABLE_SHOPPING_LIST)
        .select("*")
        .execute()
    )

    return [
        Item.Item(
            elt[DBInfo.TABLE_SHOPPING_LIST_INGREDIENT_ID],
            elt[DBInfo.TABLE_SHOPPING_LIST_QUANTITY],
            elt[DBInfo.TABLE_SHOPPING_LIST_UNIT]
        )
        for elt in response.data
    ]
