import flet
import Settings.Parameters as Parameters
import DataSource.DataSource as DataSource
import Objects.Ingredient as Ingredient
import Views.Rout as Rout
import MyFletConstrols.MyLabel as MyLabel

def IngredientListView(selection:list[int] = [], withAddButton:bool=False) -> flet.View:
    def IngredientListItemView(ingredient:Ingredient.Ingredient) -> flet.Container:
        return flet.Container(
            content=flet.CupertinoButton(
                content=MyLabel.Text(ingredient.name),
                on_click=lambda e: Rout.Rout.go(f"/Ingredients/{ingredient.id}/"),
                border_radius=10,
            ),
            bgcolor=Parameters.AppColors.IngredientItemViewBackground,
            alignment=flet.alignment.center,
        )

    constrols = []
    if withAddButton:
        constrols.append(
            flet.Button(
                "Add New Ingredient",
                on_click=lambda e: Rout.Rout.go(Rout.Rout.RouteCreateIngredient),
        ))

    constrols.append(
        flet.Column(
            controls=[
                flet.GridView(
                    controls=[IngredientListItemView(ing) for ing in DataSource.DataSource.GetIngredients(selection)],
                    runs_count=3,
                    expand=True,
                ),
            ],
        ),
    )

    return flet.Column(
            controls = constrols,
            expand=True,
            scroll=flet.ScrollMode.AUTO,
        )