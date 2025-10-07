import flet
from Recipe.RecipesView import RecipeListView
from flet import TemplateRoute

class Rout:
    def __init__(self):
        self.page: flet.Page = None

    def SetPage(self, page: flet.Page):
        self.page = page

        self.page.title = "Cooked"
        
        self.HomeRecipesRoute = "/Recipes"
        self.HomeShoppingRoute = "/Shopping"
        self.HomeParamsRoute = "/Params"

        self.page.on_route_change = self.get_router()
        self.page.on_view_pop = self.get_poper()
        self.template_route = TemplateRoute(page.route)
        self.page.go(page.route)
    
    def Go(self, route: str): self.page.go(route)
    def RouteIs(self, route: str) -> bool: 
        print(f"Matching route {self.page.route} with {route} -> {self.template_route.match(route)}")
        return self.page.route == route
    def RouteIsLike(self, route: str) -> bool:
        print(f"Matching route {self.template_route.route} with template {route} -> {self.template_route.match(route)}")
        return self.template_route.match(self.page.route)

    def get_router(self):
        navigationBar = self.get_navigation_bar()

        def on_rout_change(e: flet.RouteChangeEvent):
            print(f"Route changed to: {e}")
            self.template_route.route = e.route

            if self.RouteIs("/") or self.RouteIs(self.HomeRecipesRoute):
                self.page.views.clear()
                self.page.views.append(
                    flet.View(
                        controls = [
                            flet.Text("Recipes"),
                            flet.Text(f"Initial route: {e.route}"),
                            RecipeListView().GetView(),
                            navigationBar,
                        ],
                    )
                )

            elif self.RouteIsLike("/Recipes/:id") and hasattr(self.template_route, 'id'):
                print(f"Matched recipe route with id: {self.template_route.id}")
                self.page.views.clear()
                self.page.views.append(
                    flet.View(
                        controls = [
                            flet.Text(f"Recipe {self.template_route.id}"),
                            flet.Text(f"Initial route: {e.route}"),
                            navigationBar,
                        ],
                    )
                )

            elif self.RouteIs(self.HomeShoppingRoute):
                self.page.views.clear()
                self.page.views.append(
                    flet.View(
                        controls = [
                            flet.Text("Shopping"),
                            flet.Text(f"Initial route: {e.route}"),
                            navigationBar,
                        ],
                    )
                )

            elif self.RouteIs(self.HomeParamsRoute):
                self.page.views.clear()
                self.page.views.append(
                    flet.View(
                        controls = [
                            flet.Text("Params"),
                            flet.Text(f"Initial route: {e.route}"),
                            navigationBar,
                        ],
                    )
                )

            self.page.update()

        return on_rout_change

    def get_poper(self):
        def on_pop(view):
            print(f"Pop view")
            self.page.views.pop()
            top_view = self.page.views[-1]
            self.page.go(top_view.route)

        return on_pop
    
    def get_navigation_bar(self):
        NavigationMenu = [
            flet.NavigationBarDestination(
                icon=flet.Icons.FOOD_BANK,
                label="Recipes",
                data=self.HomeRecipesRoute,
            ),
            flet.NavigationBarDestination(
                icon=flet.Icons.SHOPPING_CART,
                label="Shopping",
                data=self.HomeShoppingRoute,
            ),
            flet.NavigationBarDestination(
                icon=flet.Icons.SETTINGS,
                label="Params",
                data=self.HomeParamsRoute,
            ),
        ]

        def handle_nav_change(e):
            if not 0 <= e.control.selected_index < len(NavigationMenu):
                return
            self.page.go(NavigationMenu[e.control.selected_index].data)
            self.page.update()

        return flet.NavigationBar(on_change=handle_nav_change, destinations=NavigationMenu)

HomePageRouter = Rout()
