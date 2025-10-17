import flet
import Rout
import DataSource.DataSource as DataSource
import Settings.Colors as AppColors

class Ingredient:
    def __init__(self, id: int, name: str):
        self.id = id
        self.name = name

    def GetView(self) -> flet.Container:
        return flet.Container(
            content=flet.Text(
                    self.name,
                    text_align=flet.TextAlign.CENTER,
                    color=AppColors.AppColors.IngredientItemViewFontColor,
                ),
            bgcolor=AppColors.AppColors.IngredientItemViewBackground,
            alignment=flet.alignment.center,
        )
    
    @staticmethod
    def GetListView(selection:list[int] = [], withAddButton:bool=False) -> flet.View:
        # todo: optimisation
        ingredients = DataSource.DataSource.GetIngredients()
        if selection: displayIngredients = [ing for ing in ingredients if ing.id in selection]
        else        : displayIngredients = ingredients

        constrols = []

        if withAddButton:
            constrols.append(
                flet.Button(
                    "Add New Ingredient",
                    on_click=lambda e: print("Add Ingredient clicked!")
            ))

        constrols.append(
            flet.GridView(
                controls=[ing.GetItemView() for ing in displayIngredients],
                runs_count=3,
                expand=1,
            ),
        )

        return flet.Column(controls = constrols)

    def GetItemView(self) -> flet.Container:
        return flet.Container(
            content=flet.CupertinoButton(
                content=flet.Text(
                    self.name,
                    text_align=flet.TextAlign.CENTER,
                    color=AppColors.AppColors.IngredientItemViewFontColor,
                ),
                on_click=lambda e: Rout.Rout.Go(f"/Ingredients/{self.id}/"),
                border_radius=10,
            ),
            bgcolor=AppColors.AppColors.IngredientItemViewBackground,
            alignment=flet.alignment.center,
        )
