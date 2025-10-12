import flet
from Recipe.RecipeView import RecipeListView
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

            if Rout.RouteIsLike("/") or Rout.RouteIsLike(Rout.HomeRecipesRoute):
                Rout.page.views.clear()
                Rout.page.views.append(
                    flet.View(
                        controls = [
                            flet.Text("Recipes"),
                            flet.Text(f"Initial route: {e.route}"),
                            RecipeListView().GetView(),
                            navigationBar,
                        ],
                    )
                )

            elif Rout.RouteIsLike("/Recipes/:id") and hasattr(Rout.template_route, 'id'):
                Rout.page.views.clear()
                print(f"Matched recipe route with id: {Rout.template_route.id}")
                recipe = DataSource.GetRecipeByID(int(Rout.template_route.id))
                if recipe is None:
                    Rout.page.views.append(
                        flet.View(
                            controls = [
                                flet.Text(f"Recipe {Rout.template_route.id} not found"),
                                flet.Text(f"Initial route: {e.route}"),
                                navigationBar,
                            ],
                        )
                    )
                else:
                    Rout.page.views.append(
                        flet.View(
                            controls = [
                                flet.Text(f"Recipe {Rout.template_route.id}"),
                                flet.Text(f"Initial route: {e.route}"),
                                recipe.GetView(),
                                navigationBar,
                            ],
                        )
                    )

            elif Rout.RouteIsLike("/Ingredients/:id") and hasattr(Rout.template_route, 'id'):
                Rout.page.views.clear()
                print(f"Matched ingredient route with id: {Rout.template_route.id}")
                ingredient = DataSource.GetIngredientByID(int(Rout.template_route.id))
                if ingredient is None:
                    Rout.page.views.append(
                        flet.View(
                            controls = [
                                flet.Text(f"Ingredient {Rout.template_route.id} not found"),
                                flet.Text(f"Initial route: {e.route}"),
                                navigationBar,
                            ],
                        )
                    )
                else:
                    Rout.page.views.append(
                        flet.View(
                            controls = [
                                flet.Text(f"Ingredient {Rout.template_route.id}"),
                                flet.Text(f"Initial route: {e.route}"),
                                ingredient.GetView(),
                                navigationBar,
                            ],
                        )
                    )

            elif Rout.RouteIsLike(Rout.HomeShoppingRoute):
                Rout.page.views.clear()
                Rout.page.views.append(
                    flet.View(
                        controls = [
                            flet.Text("Shopping"),
                            flet.Text(f"Initial route: {e.route}"),
                            navigationBar,
                        ],
                    )
                )

            elif Rout.RouteIsLike(Rout.HomeParamsRoute):
                Rout.page.views.clear()
                Rout.page.views.append(
                    flet.View(
                        controls = [
                            flet.Text("Params"),
                            flet.Text(f"Initial route: {e.route}"),
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
