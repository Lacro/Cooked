import flet
import Views.Rout as Rout
import DataSource.DataSource as DB
import Settings.Parameters as Parameters
import MyFletConstrols.MyLabel as MyLabel
from UserActions.IngredientActions import EditIngredient

def EditIngredientView(ingredient_id:int) -> flet.Container:
    ingredient = DB.DataSource.GetIngredientByID(ingredient_id)

    if not ingredient:
        return MyLabel.Text(f"Ingredient {Rout.template_route.id} not found")
    else:
        def on_save(e):
            EditIngredient(
                ingredient,
                default_quantity_input.value,
                default_unit_input.value,
            )

        default_quantity_input = flet.TextField(
            label="Default quantity",
            value=str(ingredient.default_quantity),
            keyboard_type=flet.KeyboardType.NUMBER,
        )

        default_unit_input = flet.TextField(
            label="Default unit",
            value=str(ingredient.default_unit),
            keyboard_type=flet.KeyboardType.TEXT,
        )

        return flet.Column(
            controls = [
                flet.Container(
                    MyLabel.Text(ingredient.name),
                    bgcolor=Parameters.AppColors.IngredientItemViewBackground,
                    alignment=flet.alignment.center,
                ),
                default_quantity_input,
                default_unit_input,
                flet.Button(
                    text="Save",
                    on_click=on_save,
                ),
            ],
        )