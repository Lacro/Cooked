from MyFletConstrols.MyToast import ToastSuccess, ToastError
from Objects import Item
import DataSource.DataSource as DataSource
from Utils import LogError

def AddItemToShoppingList(ingredient_id:int):
    ingredient = DataSource.DataSource.GetIngredientByID(ingredient_id)

    if ingredient is None:
        ToastError(f"Ingredient with ID {ingredient_id} not found.")
        return
    
    try:
        new_item = Item.Item(
            ingredient_id = ingredient.id,
            quantity      = ingredient.default_quantity,
            unit          = ingredient.default_unit
        )
        new_item.Validate()
        DataSource.DataSource.AddItemToShoppingList(new_item)
        ToastSuccess(f"Added {ingredient.name} to shopping list.")
    except Exception as e:
        LogError(f"Error while creating item : {e}")
        ToastError(f"Failed to add {ingredient.name} to shopping list: {str(e)}")

def RemoveItemFromShoppingList(item_id:int):
    try:
        DataSource.DataSource.RemoveItemFromShoppingList(item_id)
        ToastSuccess(f"Removed item from shopping list.")
    except Exception as e:
        LogError(f"Error while removing item ID {item_id} : {e}")
        ToastError(f"Failed to remove item from shopping list: {str(e)}")