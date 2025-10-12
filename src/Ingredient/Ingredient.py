import flet
import Rout
import DataSource.DataSource as DataSource
from Settings.Colors import AppColors

class Ingredient:
    def __init__(self, id: int, name: str):
        self.id = id
        self.name = name

    def GetView(self) -> flet.Container:
        return flet.Container(
            content=flet.Text(
                    self.name,
                    text_align=flet.TextAlign.CENTER,
                    color=AppColors.IngredientItemViewFontColor,
                ),
            bgcolor=AppColors.IngredientItemViewBackground,
            alignment=flet.alignment.center,
        )
    
    @staticmethod
    def GetListView(selection:list[int] = []) -> flet.View:
        ingredients = DataSource.DataSource.GetIngredients()

        grid = flet.GridView()
        grid.runs_count = 3

        if selection:
            displayIngredients = [ing for ing in ingredients if ing.id in selection]
        else:
            displayIngredients = ingredients

        for ingredient in displayIngredients:
            grid.controls.append(ingredient.GetItemView())
        
        return grid

    def GetItemView(self) -> flet.Container:
        return flet.Container(
            content=flet.CupertinoButton(
                content=flet.Text(
                    self.name,
                    text_align=flet.TextAlign.CENTER,
                    color=AppColors.IngredientItemViewFontColor,
                ),
                on_click=lambda e: Rout.Rout.Go(f"/Ingredients/{self.id}/"),
                border_radius=10,
            ),
            bgcolor=AppColors.IngredientItemViewBackground,
            alignment=flet.alignment.center,
        )
