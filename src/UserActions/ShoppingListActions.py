from MyFletConstrols.MyToast import ToastSuccess, ToastError, CancelToast
from Objects import Item, Ingredient
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
    except Exception as error:
        LogError(f"Error while creating item: {error}")
        ToastError(f"Failed to add {ingredient.name} to shopping list: {str(error)}")

def RemoveItemFromShoppingList(item:Item.Item):
    def AddBack(item:Item.Item):
        try:
            DataSource.DataSource.AddItemToShoppingList(item)
        except Exception as error:
            LogError(f"Error while creating item: {error}")
            ToastError(f"Failed to add {item.GetIngredientName()} to shopping list: {str(error)}")

    try:
        DataSource.DataSource.RemoveItemFromShoppingList(item.ingredient_id)
        CancelToast(
            f"Removed {item.GetIngredientName()} from shopping list.",
            cancel_action=lambda e: AddBack(item)
        )
    except Exception as error:
        LogError(f"Error while canceling remove of item {item} : {error}")
        ToastError(f"Failed to azdd back item: {str(error)}")

def UpdateItemInShoppingList(item:Item.Item, quantity:int, unit:str) -> bool:
    try:
        updatedItem = item
        updatedItem.quantity = int(quantity)
        updatedItem.unit = unit

        updatedItem.Validate()

        DataSource.DataSource.UpdateItemInShoppingList(updatedItem)
        ToastSuccess(f"Updated item.")
        return True
    except Exception as error:
        ToastError(f"Failed to update item: {str(error)}")
        return False
