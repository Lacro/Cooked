import flet
import Rout
from Settings.Colors import AppColors
from Ingredient.IngredientView import IngredientListView

class Recipe:
    def __init__(self, id: int, name: str, items:list[int]=[]):
        self.id = id
        self.name = name
        self.items = items

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

    def GetView(self) -> flet.Column:
        return flet.Column([
            flet.Container(
                content=flet.Text(
                    self.name,
                    text_align=flet.TextAlign.CENTER,
                    color=AppColors.RecipeItemViewFontColor,
                ),
                bgcolor=AppColors.IngredientItemViewBackground,
                alignment=flet.alignment.center,
            ),
            IngredientListView().GetView(self.items),
        ])
