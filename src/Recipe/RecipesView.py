import flet
from Settings.Colors import AppColors
import DataSource.DataSource as DataSource

class RecipeListView():
    def __init__(self):
        pass

    def GetView(self) -> flet.View:
        self.recipes = DataSource.DataSource.GetRecipes()

        self.grid = flet.GridView()
        self.grid.runs_count = 3
        for recipe in self.recipes:
            self.grid.controls.append(recipe.GetItemView())
        
        return self.grid
