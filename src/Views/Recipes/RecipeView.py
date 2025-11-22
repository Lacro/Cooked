import flet as flet
import Views.Rout as Rout
import DataSource.DataSource as DB
import Settings.Parameters as Parameters
import Views.Ingredients.IngredientListView as IngredientListView
import MyFletConstrols.MyLabel as MyLabel

def RecipeViewByID(recipeID:int) -> flet.Column:
    recipe = DB.DataSource.GetRecipeByID(recipeID)

    if not recipe:
        return MyLabel.Text(f"Recipe {Rout.template_route.id} not found")
    else:
        return flet.Column(controls = [
                flet.Row(controls = [
                        flet.Button(
                            "Modify",
                            on_click=lambda e: print("Add Ingredient clicked!")
                        ),
                        flet.Container(
                            content=MyLabel.Text(recipe.name),
                            bgcolor=Parameters.AppColors.IngredientItemViewBackground,
                            alignment=flet.alignment.center,
                        ),
                    ]),
                MyLabel.Text("Ingredients :", bgcolor=Parameters.AppColors.IngredientItemViewBackground),
                IngredientListView.IngredientListView(recipe.items),
                MyLabel.Text("Steps :", bgcolor=Parameters.AppColors.IngredientItemViewBackground),
            ])
