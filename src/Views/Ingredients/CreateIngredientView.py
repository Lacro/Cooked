import flet
import Views.Rout as Rout
import UserActions.IngredientActions as IngredientActions
import Settings.Parameters as Parameters
import MyFletConstrols.MyLabel as MyLabel

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