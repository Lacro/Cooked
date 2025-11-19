import flet as flet
import MyFletConstrols.MySearchBar as MySearchBar
import Objects.Item as Item
import UserActions.ShoppingListActions as ShoppingListActions
import DataSource.DataSource as DataSource
import Settings.Parameters as Parameters
import MyFletConstrols.MyLabel as MyLabel
import Views.Rout as Rout
from MyFletConstrols.MyToast import Toast

def ShoppingListView() -> flet.View:
    def EditItemModal(item:Item.Item) -> flet.AlertDialog:
        quantity_input = flet.TextField(
            label="Quantity",
            value=str(item.quantity),
            keyboard_type=flet.KeyboardType.NUMBER,
        )

        unit_input = flet.TextField(
            label="Unit",
            value=str(item.unit),
            keyboard_type=flet.KeyboardType.TEXT,
        )

        def on_save(e):
            if (ShoppingListActions.UpdateItemInShoppingList(
                item,
                quantity_input.value,
                unit_input.value
            )):
                Rout.Rout.page.close(edit_dialog)
        
        def on_cancel(e):
            Toast("Edit cancelled.")
            Rout.Rout.page.close(edit_dialog)

        edit_dialog = flet.AlertDialog(
            title=MyLabel.Title(f"{item.GetIngredientName()}:"),
            content=flet.Column(
                controls=[
                    quantity_input,
                    unit_input,
                ]
            ),
            actions=[
                flet.TextButton("Save", on_click=on_save),
                flet.TextButton("Cancel", on_click=on_cancel),
            ],
        )
        
        Rout.Rout.page.open(edit_dialog)

    def ShoppingListItemView(item:Item.Item) -> flet.Container:
        return flet.Container(
            content = flet.Row(
                controls=[
                    flet.Container(width = 10),
                    MyLabel.Text(item.GetIngredientName(), expand=True, text_align=flet.TextAlign.LEFT),
                    flet.Container(expand=True),
                    flet.Container(
                        content=MyLabel.Text(f"{item.quantity} {item.unit}"),
                        on_click=lambda e: EditItemModal(item)
                    ),
                    flet.Container(expand=True),
                    flet.Container(
                        content=flet.Icon(flet.Icons.DELETE, color=Parameters.AppColors.SecondaryFontColor),
                        on_click=lambda e: ShoppingListActions.RemoveItemFromShoppingList(item.ingredient_id)
                    ),
                ],
            ),
            bgcolor=Parameters.AppColors.ShoppingItemViewBackground,
            alignment=flet.alignment.center,
            border_radius=10,
        )
    
    return flet.Column(
        controls=[
            MySearchBar.IngredientSearchBar(on_selection=lambda e: ShoppingListActions.AddItemToShoppingList(e.control.data)),
            flet.ListView(
                controls= [ShoppingListItemView(item) for item in DataSource.DataSource.GetShoppingList()],
                expand=True,
                spacing=10,
                padding=20,
            ),
        ],
    )
