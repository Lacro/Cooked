import flet as flet
import Rout as Rout
import DataSource.DataSource as DB
import DataSource.DataSource as DataSource
import Settings.Colors as AppColors
import Recipe.Recipe as Recipe
import Views.IngredientViews as IngredientViews

def RecipeViewByID(recipeID:int) -> flet.Column:
    recipe = DB.DataSource.GetRecipeByID(recipeID)

    if not recipe:
        return flet.Text(f"Recipe {Rout.template_route.id} not found")
    else:
        return flet.Column(controls = [
                flet.Row(controls = [
                        flet.Button(
                            "Modify",
                            on_click=lambda e: print("Add Ingredient clicked!")
                        ),
                        flet.Container(
                            content=flet.Text(
                                recipe.name,
                                color=AppColors.AppColors.RecipeItemViewFontColor,
                            ),
                            bgcolor=AppColors.AppColors.IngredientItemViewBackground,
                            alignment=flet.alignment.center,
                        ),
                    ]),
                flet.Text(
                    "Ingredients :",
                    color=AppColors.AppColors.RecipeItemViewFontColor,
                    bgcolor=AppColors.AppColors.IngredientItemViewBackground,
                ),
                IngredientViews.IngredientListView(recipe.items),
                flet.Text(
                    "Steps :",
                    color=AppColors.AppColors.RecipeItemViewFontColor,
                    bgcolor=AppColors.AppColors.IngredientItemViewBackground,
                ),
            ])

def RecipeListView() -> flet.View:
    def RecipeListItemView(recipe:Recipe.Recipe) -> flet.Container:
        return flet.Container(
            content=flet.CupertinoButton(
                content=flet.Text(
                    recipe.name,
                    text_align=flet.TextAlign.CENTER,
                    color=AppColors.AppColors.RecipeItemViewFontColor,
                ),
                on_click=lambda e: Rout.Rout.Go(f"/Recipes/{recipe.id}/"),
                border_radius=10,
            ),
            bgcolor=AppColors.AppColors.RecipeItemViewBackground,
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
                expand=1,
            ),
        ],
    )

