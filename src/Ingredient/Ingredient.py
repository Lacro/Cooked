import flet
import Rout
import DataSource.DataSource as DataSource
import Settings.Colors as AppColors

class Ingredient:
    def __init__(self, id: int=None, name: str=""):
        self.id = id
        self.name = name
    
    @staticmethod
    def CreateIngredient(name: str) -> bool:
        if (not name) or (name.strip() == ""):
            print("Ingredient name cannot be empty")
            return False
        
        new_ingredient = Ingredient(name=name.strip())

        return DataSource.DataSource.AddIngredient(new_ingredient)

    # ==========================================================
    # ========================= Views ==========================

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
    def GetCreationView() -> flet.Container:
        inputName = flet.TextField(label="Ingredient Name")

        return flet.Column(
            controls=[
                flet.Container(
                    content=flet.Text(
                            "Create Ingredient",
                            text_align=flet.TextAlign.CENTER,
                            color=AppColors.AppColors.IngredientItemViewFontColor,
                        ),
                    bgcolor=AppColors.AppColors.IngredientItemViewBackground,
                    alignment=flet.alignment.center,
                ),
                inputName,
                flet.ElevatedButton("Create", on_click=lambda e: Ingredient.CreateIngredient(inputName.value)),
        ])

    @staticmethod
    def GetListView(selection:list[int] = [], withAddButton:bool=False) -> flet.View:
        constrols = []

        if withAddButton:
            constrols.append(
                flet.Button(
                    "Add New Ingredient",
                    on_click=lambda e: Rout.Rout.Go(Rout.Rout.RouteCreateIngredient),
            ))

        constrols.append(
            flet.GridView(
                controls=[ing.GetItemView() for ing in DataSource.DataSource.GetIngredients(selection)],
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
    
    # ========================= Views ==========================
    # ==========================================================
