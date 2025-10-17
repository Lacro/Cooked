import flet
import DataSource.DataSource as DB
import Settings.Parameters as Parameters
import Recipe.Recipe as Recipe
import Ingredient.Ingredient as Ingredient
from flet import TemplateRoute

class Rout:
    page: flet.Page = None
    template_route: TemplateRoute = None

    HomeRecipesRoute: str = "/Recipes"
    HomeShoppingRoute: str = "/Shopping"
    HomeParamsRoute: str = "/Params"

    PageIngredientRoute: str = "/Ingredients"


    @staticmethod
    def SetPage(page: flet.Page):
        Rout.page = page
        Rout.page.title = "Cooked"
        
        Rout.template_route = TemplateRoute(page.route)

        Rout.page.on_route_change = Rout.get_router()
        Rout.page.on_view_pop = Rout.get_poper()
        Rout.page.go(page.route)
        Rout.Go = Rout.page.go # easier access to the page.go method
        Rout.GoBack = Rout.page.on_view_pop # easier access to the page.on_view_pop method
    
    @staticmethod
    def RouteIsLike(route: str) -> bool:
        ret:bool = Rout.template_route.match(route)
        print(f"Matching route \"{Rout.page.route}\" with template \"{route}\" -> {ret}")
        return ret

    @staticmethod
    def get_router():
        navigationBar = Rout.get_navigation_bar()

        def on_rout_change(e: flet.RouteChangeEvent):
            print(f"Route changed to: {e}")
            Rout.template_route.route = e.route # update the route in the template route module

            curent_view = flet.Text(f"404: Page not Found : {e.route}")

            if Rout.RouteIsLike("/") or Rout.RouteIsLike(Rout.HomeRecipesRoute):
                Rout.page.views.clear()
                curent_view = Recipe.Recipe.GetListView()
            elif Rout.RouteIsLike("/Recipes/:id") and hasattr(Rout.template_route, 'id'):
                print(f"Matched recipe route with id: {Rout.template_route.id}")
                recipe = DB.DataSource.GetRecipeByID(int(Rout.template_route.id))
                if recipe:
                    curent_view = recipe.GetView()
                else:
                    curent_view = flet.Text(f"Recipe {Rout.template_route.id} not found")

            elif Rout.RouteIsLike(Rout.PageIngredientRoute):
                curent_view = Ingredient.Ingredient.GetListView(withAddButton=True)
            elif Rout.RouteIsLike("/Ingredients/:id") and hasattr(Rout.template_route, 'id'):
                print(f"Matched ingredient route with id: {Rout.template_route.id}")
                ingredient = DB.DataSource.GetIngredientByID(int(Rout.template_route.id))
                if ingredient:
                    curent_view = ingredient.GetView()
                else:
                    curent_view = flet.Text(f"Ingredient {Rout.template_route.id} not found")

            elif Rout.RouteIsLike(Rout.HomeShoppingRoute):
                Rout.page.views.clear()
                curent_view = flet.Text("Shopping")

            elif Rout.RouteIsLike(Rout.HomeParamsRoute):
                Rout.page.views.clear()
                curent_view = Parameters.Parameters.GetView()
                
            Rout.page.views.append(
                flet.View(
                    route=e.route,
                    controls = [
                        flet.Container(height = 20), # spacer to avoid front camera inside display
                        flet.Row(
                            controls=[
                                flet.Button(
                                    "Back",
                                    on_click=Rout.GoBack
                                ),
                                flet.Container(
                                    flet.Text(
                                        f"COOKED",
                                        style=flet.TextThemeStyle.HEADLINE_MEDIUM,
                                        text_align=flet.TextAlign.CENTER,
                                    ),
                                    expand=1,
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
        
            print(f"Added page, new stack:")
            for i, v in enumerate(Rout.page.views):
                print(f" {i}: \"{v.route}\"")


        return on_rout_change

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
                data=Rout.HomeRecipesRoute,
            ),
            flet.NavigationBarDestination(
                icon=flet.Icons.SHOPPING_CART,
                label="Shopping",
                data=Rout.HomeShoppingRoute,
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
