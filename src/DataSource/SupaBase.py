import Objects.Recipe as Recipe
import Objects.Ingredient as Ingredient
import Objects.Item as Item
import DataSource.DataBaseInfo as DBInfo
import DataSource.DataBaseSecrets as DataBaseSecrets
from supabase import create_client, Client, acreate_client, AsyncClient

supabase: Client = create_client(
    DataBaseSecrets.SUPABASE_URL,
    DataBaseSecrets.SUPABASE_KEY,
)

async def Initialize(callback):
    asyncsupabase: AsyncClient = await acreate_client(
        DataBaseSecrets.SUPABASE_URL,
        DataBaseSecrets.SUPABASE_KEY,
    )

    def handle_record_updated(payload):
        callback()

    response = (
        await asyncsupabase
            .channel("shopping_list:all")
            .on_postgres_changes(
                "*",
                schema="public",
                table=DBInfo.TABLE_SHOPPING_LIST,
                callback=handle_record_updated
            )
            .subscribe()
    )


def LoadRecipes():
    response = (
        supabase.table(DBInfo.TABLE_RECIPES)
        .select("*")
        .execute()
    )

    return [
        Recipe.Recipe(
            id      = elt[DBInfo.TABLE_RECIPES_ID],
            name    = elt[DBInfo.TABLE_RECIPES_NAME],
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
            id               = elt[DBInfo.TABLE_INGREDIENTS_ID],
            name             = elt[DBInfo.TABLE_INGREDIENTS_NAME],
            default_quantity = elt[DBInfo.TABLE_INGREDIENTS_DEFAULT_QUANTITY],
            default_unit     = elt[DBInfo.TABLE_INGREDIENTS_DEFAULT_UNIT],
        )
        for elt in response.data
    ]

def AddIngredient(ingredient:Ingredient.Ingredient):
    (
        supabase.table(DBInfo.TABLE_INGREDIENTS)
            .insert({
                DBInfo.TABLE_INGREDIENTS_NAME:              ingredient.name,
                DBInfo.TABLE_INGREDIENTS_DEFAULT_QUANTITY:  ingredient.default_quantity,
                DBInfo.TABLE_INGREDIENTS_DEFAULT_UNIT:      ingredient.default_unit,
            })
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
            ingredient_id   = elt[DBInfo.TABLE_SHOPPING_LIST_INGREDIENT_ID],
            quantity        = elt[DBInfo.TABLE_SHOPPING_LIST_QUANTITY],
            unit            = elt[DBInfo.TABLE_SHOPPING_LIST_UNIT]
        )
        for elt in response.data
    ]

def AddItemToShoppingList(item: Item.Item):
    (
        supabase.table(DBInfo.TABLE_SHOPPING_LIST)
            .insert({
                DBInfo.TABLE_SHOPPING_LIST_INGREDIENT_ID:   item.ingredient_id,
                DBInfo.TABLE_SHOPPING_LIST_QUANTITY:        item.quantity,
                DBInfo.TABLE_SHOPPING_LIST_UNIT:            item.unit,
            })
            .execute()
    )

def RemoveItemFromShoppingList(ingredient_id: int):
    (
        supabase.table(DBInfo.TABLE_SHOPPING_LIST)
            .delete()
            .eq(DBInfo.TABLE_SHOPPING_LIST_INGREDIENT_ID, ingredient_id)
            .execute()
    )

def UpdateItemInShoppingList(item: Item.Item):
    (
        supabase.table(DBInfo.TABLE_SHOPPING_LIST)
            .update({
                DBInfo.TABLE_SHOPPING_LIST_QUANTITY: item.quantity,
                DBInfo.TABLE_SHOPPING_LIST_UNIT:     item.unit,
            })
            .eq(DBInfo.TABLE_SHOPPING_LIST_INGREDIENT_ID, item.ingredient_id)
            .execute()
    )
