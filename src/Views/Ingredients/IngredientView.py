import flet
import Views.Rout as Rout
import DataSource.DataSource as DB
import Settings.Parameters as Parameters
import MyFletConstrols.MyLabel as MyLabel

def IngredientViewByID(ingredient_id:int) -> flet.Container:
    ingredient = DB.DataSource.GetIngredientByID(ingredient_id)

    if not ingredient:
        return MyLabel.Text(f"Ingredient {Rout.template_route.id} not found")
    else:
        return flet.Container(
            content=MyLabel.Text(ingredient.name),
            bgcolor=Parameters.AppColors.IngredientItemViewBackground,
            alignment=flet.alignment.center,
        )