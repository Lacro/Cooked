import flet
import Views.Rout as Rout
import UserActions.IngredientActions as IngredientActions
import DataSource.DataSource as DB
import Settings.Parameters as Parameters
import Objects.Ingredient as Ingredient
import DataSource.DataSource as DataSource
import MyFletConstrols.MyLabel as MyLabel

def IngredientViewByID(ingredient_id:int) -> flet.Container:
    ingredient = DB.DataSource.GetIngredientByID(ingredient_id)

    if not ingredient:
        return MyLabel.Text(f"Ingredient {Rout.template_route.id} not found")
    else:
        return flet.Container(
            content=MyLabel.Text(ingredient.name),
            bgcolor=Parameters.AppColors.IngredientItemViewBackground,
            alignment=flet.alignment.center,
        )

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

def CreateIngredientView() -> flet.Container:
    inputName = flet.TextField(label="Ingredient Name")

    return flet.Column(
        controls=[
            flet.Container(
                content=MyLabel.Text("Create Ingredient"),
                bgcolor=Parameters.AppColors.IngredientItemViewBackground,
                alignment=flet.alignment.center,
            ),
            inputName,
            flet.ElevatedButton("Create", on_click=lambda e: IngredientActions.CreateIngredient(inputName.value)),
    ])