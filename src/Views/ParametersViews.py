import flet as flet
import Rout as Rout

def ParmatersView() -> flet.View:
    return flet.Column(
        controls=[
            flet.Text("Params View"),
            flet.Button(
                "Edit ingredients",
                on_click=lambda e: Rout.Rout.Go(Rout.Rout.RouteAllIngredient)
            )
        ]
    )