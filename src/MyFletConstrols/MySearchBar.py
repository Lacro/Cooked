import flet as flet
import DataSource.DataSource as DataSource
import MyFletConstrols.MyLabel as MyLabel

class SearchBar(flet.SearchBar):
    def __init__(self, **kwargs):
        kwargs['on_tap']    = self.handle_tap
        kwargs['on_change'] = self.handle_change
        kwargs['on_submit'] = self.handle_submit

        super().__init__(**kwargs)
    
    def handle_tap(self, e):
        print(f"handle_tap: {self} {e}")
        self.open_view()

    def handle_change(self, e):
        print(f"handle_change: {self} {e}")

    def handle_submit(self, e):
        print(f"handle_submit: {self} {e}")


class IngredientSearchBar(SearchBar):
    def __init__(self, on_selection, **kwargs):
        kwargs['bar_hint_text'] = "Search ingredient..."
        kwargs['controls'] = self.GetControls(on_selection=on_selection)
        super().__init__(**kwargs)
    
    def GetControls(self, on_selection):
        return  [
            flet.ListTile(
                title=MyLabel.Text(ingredient.name),
                on_click=self.on_element_clicked(on_selection=on_selection),
                data=ingredient.id,
            )
            for ingredient in DataSource.DataSource.GetIngredients()
        ]
    
    def on_element_clicked(self, on_selection):
        def handle_click(e):
            self.close_view("")
            on_selection(e)

        return handle_click

