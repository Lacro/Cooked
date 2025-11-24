from MyFletConstrols.MyToast import ToastSuccess, ToastError
import Views.Rout as Rout
import Objects.Ingredient as Ingredient
import DataSource.DataSource as DataSource
from Utils import LogError

def CreateIngredient(name:str):
    try:
        ingredient = Ingredient.Ingredient(name=name)
        ingredient.Validate()
        DataSource.DataSource.AddIngredient(ingredient)
        Rout.Rout.go_back()
        ToastSuccess(f"Successfully created '{name}' !")
    except Exception as e:
        LogError(f"Error while creating ingredient : {e}")
        ToastError(f"Error: {e} !")

def EditIngredient(ingredient:Ingredient.Ingredient, default_quantity:int, default_unit:str):
    try:
        ingredient.default_quantity = int(default_quantity)
        ingredient.default_unit = default_unit
        
        ingredient.Validate()

        DataSource.DataSource.UpdateIngredient(ingredient)
        Rout.Rout.go_back()
        ToastSuccess(f"Successfully updated '{ingredient.name}' !")
    except Exception as e:
        LogError(f"Error while editing ingredient : {e}")
        ToastError(f"Error: {e} !")
