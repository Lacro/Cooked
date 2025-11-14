import flet as flet
import Views.Rout as Rout
import MyFletConstrols.MyLabel as MyLabel

def ParmatersView() -> flet.View:
    return flet.Column(
        controls=[
            MyLabel.Text("Params View"),
            flet.Button(
                "Edit ingredients",
                on_click=lambda e: Rout.Rout.Go(Rout.Rout.RouteAllIngredient)
            )
        ],
        expand=True,
        scroll=flet.ScrollMode.AUTO,
    )