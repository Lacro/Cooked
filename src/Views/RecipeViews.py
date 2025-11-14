import flet as flet
import Views.Rout as Rout
import DataSource.DataSource as DB
import DataSource.DataSource as DataSource
import Settings.Parameters as Parameters
import Objects.Recipe as Recipe
import Views.IngredientViews as IngredientViews
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
                IngredientViews.IngredientListView(recipe.items),
                MyLabel.Text("Steps :", bgcolor=Parameters.AppColors.IngredientItemViewBackground),
            ])

def RecipeListView() -> flet.View:
    def RecipeListItemView(recipe:Recipe.Recipe) -> flet.Container:
        return flet.Container(
            content=flet.CupertinoButton(
                content=MyLabel.Text(recipe.name),
                on_click=lambda e: Rout.Rout.Go(f"/Recipes/{recipe.id}/"),
                border_radius=10,
            ),
            bgcolor=Parameters.AppColors.RecipeItemViewBackground,
            alignment=flet.alignment.center,
        )

    return flet.Column(
        controls = [
            flet.Button(
                "Create Recipe",
                on_click=lambda e: print("Create Recipe clicked!")
            ),
            flet.GridView(
                controls= [RecipeListItemView(r) for r in DataSource.DataSource.GetRecipes()],
                runs_count = 3,
            ),
        ],
        expand=True,
        scroll=flet.ScrollMode.AUTO,
    )

