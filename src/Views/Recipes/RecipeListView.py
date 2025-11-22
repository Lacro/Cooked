import flet
import DataSource.DataSource as DataSource
import Settings.Parameters as Parameters
import Objects.Recipe as Recipe
import Views.Rout as Rout
import MyFletConstrols.MyLabel as MyLabel

def RecipeListView() -> flet.View:
    def RecipeListItemView(recipe:Recipe.Recipe) -> flet.Container:
        return flet.Container(
            content=flet.CupertinoButton(
                content=MyLabel.Text(recipe.name),
                on_click=lambda e: Rout.Rout.go(f"/Recipes/{recipe.id}/"),
                border_radius=10,
            ),
            bgcolor=Parameters.AppColors.RecipeItemViewBackground,
            alignment=flet.alignment.center,
        )

    return flet.Column(
        controls = [
            flet.Button(
                "Create Recipe",
                on_click=lambda e: print("Create Recipe clicked!")
            ),
            flet.GridView(
                controls= [RecipeListItemView(r) for r in DataSource.DataSource.GetRecipes()],
                runs_count = 3,
            ),
        ],
        expand=True,
        scroll=flet.ScrollMode.AUTO,
    )
