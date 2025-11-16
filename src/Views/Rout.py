import flet
from flet import TemplateRoute
import Views.ParametersViews as ParametersViews
import Views.ShoppingViews as ShoppingViews
import Views.RecipeViews as RecipeViews
import Views.IngredientViews as IngredientViews
from Utils import LogError
import MyFletConstrols.MyLabel as MyLabel

class Rout:
    page: flet.Page = None
    template_route: TemplateRoute = None

    RouteAllRecipe: str = "/Recipes"
    RouteShoppingList: str = "/Shopping"
    HomeParamsRoute: str = "/Params"

    RouteAllIngredient: str = "/Ingredients"
    RouteCreateIngredient: str = "/Ingredients/New"

    @staticmethod
    def InitRouter(page: flet.Page):
        Rout.page = page
        Rout.page.on_route_change = Rout.on_rout_change_safe
        Rout.page.on_view_pop = Rout.on_pop
        Rout.go = Rout.page.go # easier access to the page.go method
        
        Rout.template_route = TemplateRoute(page.route)
        Rout.rout_is_like = Rout.template_route.match

        Rout.hist = []
        Rout.go(Rout.RouteAllRecipe)
        Rout.page.bottom_appbar = Rout.get_navigation_bar()
        Rout.body = flet.Container(content=flet.Text(""), expand=True)

        Rout.page.title = "Cooked"
        Rout.page.add(
            flet.Column(
                controls=[
                    flet.Container(height = 20), # spacer to avoid front camera inside display
                    flet.Row(
                        controls=[
                            flet.Button("Back", on_click=Rout.go_back),
                            flet.Container(
                                MyLabel.Title(f"COOKED", theme_style=flet.TextThemeStyle.HEADLINE_MEDIUM),
                                expand=True,
                                alignment=flet.alignment.center,
                            ),
                        ],
                    ),
                    Rout.body,
                ]
        ))

    @staticmethod
    def go_back(page=None): Rout.page.on_view_pop(Rout.page)

    @staticmethod
    def refresh():
        cur_path = Rout.hist.pop()
        Rout.on_rout_change_safe(flet.RouteChangeEvent(cur_path))

    @staticmethod
    def on_rout_change_safe(e: flet.RouteChangeEvent):
        def on_rout_change(e: flet.RouteChangeEvent):
            Rout.template_route.route = e.route # update the route in the template route module
            Rout.hist.append(e.route)

            print(f"Routing to {e.route}")
            print(f"Rout.hist: {Rout.hist}")

            curent_view = MyLabel.Text(f"404: Page not Found : {e.route}")

            # ============================================================
            # ========================= Recipes ==========================
            if Rout.rout_is_like("/") or Rout.rout_is_like(Rout.RouteAllRecipe):
                curent_view = RecipeViews.RecipeListView()
            elif Rout.rout_is_like("/Recipes/:id") and hasattr(Rout.template_route, 'id'):
                curent_view = RecipeViews.RecipeViewByID(int(Rout.template_route.id))
            # ========================= Recipes ==========================
            # ============================================================


            # ============================================================
            # ======================== Ingredient ========================
            elif Rout.rout_is_like(Rout.RouteAllIngredient):
                curent_view = IngredientViews.IngredientListView(withAddButton=True)
            elif Rout.rout_is_like(Rout.RouteCreateIngredient):
                curent_view = IngredientViews.CreateIngredientView()
            elif Rout.rout_is_like("/Ingredients/:id") and hasattr(Rout.template_route, 'id'):
                curent_view = IngredientViews.IngredientViewByID(int(Rout.template_route.id))
            # ======================== Ingredient ========================
            # ============================================================


            # ============================================================
            # ========================= Shopping =========================
            elif Rout.rout_is_like(Rout.RouteShoppingList):
                curent_view = ShoppingViews.ShoppingListView()
            # ========================= Shopping =========================
            # ============================================================


            # ============================================================
            # ======================== Parameters ========================
            elif Rout.rout_is_like(Rout.HomeParamsRoute):
                curent_view = ParametersViews.ParmatersView()
            # ======================== Parameters ========================
            # ============================================================
            
            Rout.body.content = curent_view
            Rout.page.update()
        
        try:
            on_rout_change(e)
        except Exception as ex:
            LogError(f"Error on routing {e.route}: {ex}")

    def on_pop(view):
        if len(Rout.hist) > 1:
            Rout.hist.pop()
            Rout.go(Rout.hist[-1])
            Rout.hist.pop()
    
    @staticmethod
    def get_navigation_bar():
        NavigationMenu = [
            flet.NavigationBarDestination(
                icon=flet.Icons.FOOD_BANK,
                label="Recipes",
                data=Rout.RouteAllRecipe,
            ),
            flet.NavigationBarDestination(
                icon=flet.Icons.SHOPPING_CART,
                label="Shopping",
                data=Rout.RouteShoppingList,
            ),
            flet.NavigationBarDestination(
                icon=flet.Icons.SETTINGS,
                label="Params",
                data=Rout.HomeParamsRoute,
            ),
        ]

        def handle_nav_change(e):
            if not 0 <= e.control.selected_index < len(NavigationMenu):
                return
            Rout.page.go(NavigationMenu[e.control.selected_index].data)
            Rout.page.update()

        return flet.NavigationBar(on_change=handle_nav_change, destinations=NavigationMenu)
