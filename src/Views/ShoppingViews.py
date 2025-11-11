import flet as flet
import MyFletConstrols.MySearchBar as MySearchBar
import Objects.Item as Item
import UserActions.ShoppingListActions as ShoppingListActions
import DataSource.DataSource as DataSource
import Settings.Colors as AppColors

def ShoppingListView() -> flet.View:
    def ShoppingListItemView(item:Item.Item) -> flet.Container:
        return flet.Container(
            content=flet.CupertinoButton(
                content=flet.Text(
                    item.GetIngredientName(),
                    text_align=flet.TextAlign.CENTER,
                    color=AppColors.AppColors.ShoppingItemViewFontColor,
                ),
                border_radius=10,
            ),
            bgcolor=AppColors.AppColors.ShoppingItemViewBackground,
            alignment=flet.alignment.center,
        )
    
    return flet.Column(
        controls=[
            MySearchBar.IngredientSearchBar(on_selection=lambda e: ShoppingListActions.AddItemToShoppingList(e.control.data)),
            flet.Text("Shopping list View"),
            flet.GridView(
                controls= [ShoppingListItemView(item) for item in DataSource.DataSource.GetShoppingList()],
                runs_count = 3,
            ),
        ],
        expand=True,
        scroll=flet.ScrollMode.AUTO,
    )
