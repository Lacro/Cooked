import flet
from Settings.Colors import AppColors
import DataSource.DataSource as DataSource

class IngredientListView():
    def __init__(self):
        pass

    def GetView(self, selection:list[int] = []) -> flet.View:
        self.ingredients = DataSource.DataSource.GetIngredients()

        self.grid = flet.GridView()
        self.grid.runs_count = 3

        if selection:
            displayIngredients = [ing for ing in self.ingredients if ing.id in selection]
        else:
            displayIngredients = self.ingredients

        for ingredient in displayIngredients:
            self.grid.controls.append(ingredient.GetItemView())
        
        return self.grid
