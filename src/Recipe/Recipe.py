import flet
import Rout
import DataSource.DataSource as DataSource
from Settings.Colors import AppColors
import Ingredient.Ingredient as Ingredient

class Recipe:
    def __init__(self, id: int, name: str, items:list[int]=[]):
        self.id = id
        self.name = name
        self.items = items

    def GetView(self) -> flet.Column:
        return flet.Column([
            flet.Container(
                content=flet.Text(
                    self.name,
                    color=AppColors.RecipeItemViewFontColor,
                ),
                bgcolor=AppColors.IngredientItemViewBackground,
                alignment=flet.alignment.center,
            ),
            flet.Text(
                "Ingredients :",
                color=AppColors.RecipeItemViewFontColor,
                bgcolor=AppColors.IngredientItemViewBackground,
            ),
            Ingredient.Ingredient.GetListView(self.items),
            flet.Text(
                "Steps :",
                color=AppColors.RecipeItemViewFontColor,
                bgcolor=AppColors.IngredientItemViewBackground,
            ),
        ])

    @staticmethod
    def GetListView() -> flet.View:
        recipes = DataSource.DataSource.GetRecipes()

        grid = flet.GridView()
        grid.runs_count = 3
        for recipe in recipes:
            grid.controls.append(recipe.GetItemView())
        
        return grid
    
    def GetItemView(self) -> flet.Container:
        return flet.Container(
            content=flet.CupertinoButton(
                content=flet.Text(
                    self.name,
                    text_align=flet.TextAlign.CENTER,
                    color=AppColors.RecipeItemViewFontColor,
                ),
                on_click=lambda e: Rout.Rout.Go(f"/Recipes/{self.id}/"),
                border_radius=10,
            ),
            bgcolor=AppColors.RecipeItemViewBackground,
            alignment=flet.alignment.center,
        )
