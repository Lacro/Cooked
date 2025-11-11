from MyFletConstrols.MyToast import ToastSuccess, ToastError
import Views.Rout as Rout
import Objects.Ingredient as Ingredient
import DataSource.DataSource as DataSource

def CreateIngredient(name:str):
    try:
        ingredient = Ingredient.Ingredient(name=name)
        ingredient.Validate()
        DataSource.DataSource.AddIngredient(ingredient)
        Rout.Rout.GoBack()
        ToastSuccess(f"Successfully created '{name}' !")
    except Exception as e:
        print(f"Error while creating ingredient : {e}")
        ToastError(f"Error: {e} !")
