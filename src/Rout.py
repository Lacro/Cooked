import flet
import Recipe.Recipe as Recipe
from DataSource.DataSource import DataSource
from flet import TemplateRoute

class Rout:
    page: flet.Page = None
    HomeRecipesRoute: str = "/Recipes"
    HomeShoppingRoute: str = "/Shopping"
    HomeParamsRoute: str = "/Params"
    template_route: TemplateRoute = None

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
                curent_view = Recipe.Recipe.GetListView()

            elif Rout.RouteIsLike("/Recipes/:id") and hasattr(Rout.template_route, 'id'):
                print(f"Matched recipe route with id: {Rout.template_route.id}")
                recipe = DataSource.GetRecipeByID(int(Rout.template_route.id))
                if recipe:
                    curent_view = recipe.GetView()
                else:
                    curent_view = flet.Text(f"Recipe {Rout.template_route.id} not found")

            elif Rout.RouteIsLike("/Ingredients/:id") and hasattr(Rout.template_route, 'id'):
                print(f"Matched ingredient route with id: {Rout.template_route.id}")
                ingredient = DataSource.GetIngredientByID(int(Rout.template_route.id))
                if ingredient:
                    curent_view = ingredient.GetView()
                else:
                    curent_view = flet.Text(f"Ingredient {Rout.template_route.id} not found")

            elif Rout.RouteIsLike(Rout.HomeShoppingRoute):
                curent_view = flet.Text("Shopping")

            elif Rout.RouteIsLike(Rout.HomeParamsRoute):
                curent_view = flet.Text("Params")
                
            Rout.page.views.clear()
            Rout.page.views.append(
                flet.View(
                    controls = [
                        flet.Text(f"Route: {e.route}"),
                        curent_view,
                        navigationBar,
                    ],
                )
            )
            Rout.page.update()

        return on_rout_change

    @staticmethod
    def get_poper():
        def on_pop(view):
            print(f"Pop view")
            Rout.page.views.pop()
            top_view = Rout.page.views[-1]
            Rout.page.go(top_view.route)

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
