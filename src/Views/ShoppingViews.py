import flet as flet
import MyFletConstrols.MySearchBar as MySearchBar
import Objects.Item as Item
import UserActions.ShoppingListActions as ShoppingListActions
import DataSource.DataSource as DataSource
import Settings.Parameters as Parameters
import MyFletConstrols.MyLabel as MyLabel

def ShoppingListView() -> flet.View:
    def ShoppingListItemView(item:Item.Item) -> flet.Container:
        return flet.Container(
            content = flet.Row(
                controls=[
                    MyLabel.Text(value=item.GetIngredientName()),
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
                divider_thickness=0,
                expand=True,
                spacing=10,
                padding=20,
            ),
        ],
    )
