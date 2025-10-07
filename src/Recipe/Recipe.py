import flet
from Settings.Colors import AppColors
import Rout

class Recipe:
    def __init__(self, id: int, name: str, items: dict={}):
        self.id = id
        self.name = name
        self.items = items

    def GetItemView(self) -> flet.Text:
        return flet.Container(
            content=flet.CupertinoButton(
                content=flet.Text(
                    self.name,
                    text_align=flet.TextAlign.CENTER,
                    color=AppColors.RecipeItemViewFontColor,
                ),
                on_click=lambda e: Rout.HomePageRouter.Go(f"/Recipes/{self.id}"),
                border_radius=10,
            ),
            bgcolor=AppColors.RecipeItemViewBackground,
            alignment=flet.alignment.center,
        )

    def GetView(self) -> flet.Page:
        page = flet.Page()
        page.title = self.name
        return page
