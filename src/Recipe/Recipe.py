import flet
import Rout
import DataSource.DataSource as DataSource
import Settings.Colors as AppColors
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
                    color=AppColors.AppColors.RecipeItemViewFontColor,
                ),
                bgcolor=AppColors.AppColors.IngredientItemViewBackground,
                alignment=flet.alignment.center,
            ),
            flet.Text(
                "Ingredients :",
                color=AppColors.AppColors.RecipeItemViewFontColor,
                bgcolor=AppColors.AppColors.IngredientItemViewBackground,
            ),
            Ingredient.Ingredient.GetListView(self.items),
            flet.Text(
                "Steps :",
                color=AppColors.AppColors.RecipeItemViewFontColor,
                bgcolor=AppColors.AppColors.IngredientItemViewBackground,
            ),
        ])

    @staticmethod
    def GetListView() -> flet.View:

        return flet.Column(
            controls = [
                flet.Button(
                    "Create Recipe",
                    on_click=lambda e: print("Create Recipe clicked!")
                ),
                flet.GridView(
                    controls= [r.GetItemView() for r in DataSource.DataSource.GetRecipes()],
                    runs_count = 3,
                    expand=1,
                ),
            ],
        )
    
    def GetItemView(self) -> flet.Container:
        return flet.Container(
            content=flet.CupertinoButton(
                content=flet.Text(
                    self.name,
                    text_align=flet.TextAlign.CENTER,
                    color=AppColors.AppColors.RecipeItemViewFontColor,
                ),
                on_click=lambda e: Rout.Rout.Go(f"/Recipes/{self.id}/"),
                border_radius=10,
            ),
            bgcolor=AppColors.AppColors.RecipeItemViewBackground,
            alignment=flet.alignment.center,
        )
