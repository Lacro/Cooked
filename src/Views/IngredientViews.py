import flet
import Views.Rout as Rout
import Views.UserActions as UserActions
import DataSource.DataSource as DB
import Settings.Colors as AppColors
import Objects.Ingredient as Ingredient
import DataSource.DataSource as DataSource

def IngredientViewByID(ingredientID:int) -> flet.Container:
    ingredient = DB.DataSource.GetIngredientByID(ingredientID)

    if not ingredient:
        return flet.Text(f"Ingredient {Rout.template_route.id} not found")
    else:
        return flet.Container(
            content=flet.Text(
                    ingredient.name,
                    text_align=flet.TextAlign.CENTER,
                    color=AppColors.AppColors.IngredientItemViewFontColor,
                ),
            bgcolor=AppColors.AppColors.IngredientItemViewBackground,
            alignment=flet.alignment.center,
        )

def IngredientListView(selection:list[int] = [], withAddButton:bool=False) -> flet.View:
    def IngredientListItemView(ingredient:Ingredient.Ingredient) -> flet.Container:
        return flet.Container(
            content=flet.CupertinoButton(
                content=flet.Text(
                    ingredient.name,
                    text_align=flet.TextAlign.CENTER,
                    color=AppColors.AppColors.IngredientItemViewFontColor,
                ),
                on_click=lambda e: Rout.Rout.Go(f"/Ingredients/{ingredient.id}/"),
                border_radius=10,
            ),
            bgcolor=AppColors.AppColors.IngredientItemViewBackground,
            alignment=flet.alignment.center,
        )

    constrols = []
    if withAddButton:
        constrols.append(
            flet.Button(
                "Add New Ingredient",
                on_click=lambda e: Rout.Rout.Go(Rout.Rout.RouteCreateIngredient),
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
                content=flet.Text(
                        "Create Ingredient",
                        text_align=flet.TextAlign.CENTER,
                        color=AppColors.AppColors.IngredientItemViewFontColor,
                    ),
                bgcolor=AppColors.AppColors.IngredientItemViewBackground,
                alignment=flet.alignment.center,
            ),
            inputName,
            flet.ElevatedButton("Create", on_click=lambda e: UserActions.CreateIngredient(inputName.value)),
    ])