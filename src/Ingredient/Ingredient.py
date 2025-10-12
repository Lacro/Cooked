import flet
from Settings.Colors import AppColors
import Rout

class Ingredient:
    def __init__(self, id: int, name: str):
        self.id = id
        self.name = name

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
