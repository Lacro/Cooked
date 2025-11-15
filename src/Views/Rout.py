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
    def SetPage(page: flet.Page):
        Rout.page = page
        Rout.page.title = "Cooked"
        
        Rout.template_route = TemplateRoute(page.route)

        Rout.page.on_route_change = Rout.get_router()
        Rout.page.on_view_pop = Rout.get_poper()
        Rout.page.go(page.route)
        Rout.Go = Rout.page.go # easier access to the page.go method

    @staticmethod
    def GoBack(page=None): Rout.page.on_view_pop(Rout.page)

    @staticmethod
    def RouteIsLike(route: str) -> bool:
        return Rout.template_route.match(route)

    @staticmethod
    def get_router():
        navigationBar = Rout.get_navigation_bar()

        def on_rout_change(e: flet.RouteChangeEvent):
            Rout.template_route.route = e.route # update the route in the template route module

            curent_view = MyLabel.Text(f"404: Page not Found : {e.route}")

            # ============================================================
            # ========================= Recipes ==========================
            if Rout.RouteIsLike("/") or Rout.RouteIsLike(Rout.RouteAllRecipe):
                Rout.page.views.clear()
                curent_view = RecipeViews.RecipeListView()
            elif Rout.RouteIsLike("/Recipes/:id") and hasattr(Rout.template_route, 'id'):
                curent_view = RecipeViews.RecipeViewByID(int(Rout.template_route.id))
            # ========================= Recipes ==========================
            # ============================================================


            # ============================================================
            # ======================== Ingredient ========================
            elif Rout.RouteIsLike(Rout.RouteAllIngredient):
                curent_view = IngredientViews.IngredientListView(withAddButton=True)
            elif Rout.RouteIsLike(Rout.RouteCreateIngredient):
                curent_view = IngredientViews.CreateIngredientView()
            elif Rout.RouteIsLike("/Ingredients/:id") and hasattr(Rout.template_route, 'id'):
                curent_view = IngredientViews.IngredientViewByID(int(Rout.template_route.id))
            # ======================== Ingredient ========================
            # ============================================================


            # ============================================================
            # ========================= Shopping =========================
            elif Rout.RouteIsLike(Rout.RouteShoppingList):
                Rout.page.views.clear()
                curent_view = ShoppingViews.ShoppingListView()
            # ========================= Shopping =========================
            # ============================================================


            # ============================================================
            # ======================== Parameters ========================
            elif Rout.RouteIsLike(Rout.HomeParamsRoute):
                Rout.page.views.clear()
                curent_view = ParametersViews.ParmatersView()
            # ======================== Parameters ========================
            # ============================================================
            
            Rout.page.views.append(
                flet.View(
                    route=e.route,
                    controls = [
                        flet.Container(height = 20), # spacer to avoid front camera inside display
                        flet.Row(
                            controls=[
                                flet.Button("Back", on_click=Rout.GoBack),
                                flet.Container(
                                    MyLabel.Title(f"COOKED", theme_style=flet.TextThemeStyle.HEADLINE_MEDIUM),
                                    expand=True,
                                    alignment=flet.alignment.center,
                                ),
                            ],
                        ),
                        curent_view,
                        navigationBar,
                    ],
                )
            )
            Rout.page.update()

        def on_rout_change_safe(e: flet.RouteChangeEvent):
            try:
                on_rout_change(e)
            except Exception as ex:
                LogError(f"Error on routing {e.route}: {ex}")

        return on_rout_change_safe

    @staticmethod
    def get_poper():
        def on_pop(view):
            if len(Rout.page.views) >= 2:
                Rout.page.views.pop()
            Rout.Go(Rout.page.views[-1].route)
            Rout.page.views.pop()

        return on_pop
    
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
