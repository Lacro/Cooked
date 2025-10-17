import flet as flet
import Rout as Rout

class Parameters:
    @staticmethod
    def GetView() -> flet.View:
        return flet.Column(
            controls=[
                flet.Text("Params View"),
                flet.Button(
                    "Edit ingredients",
                    on_click=lambda e: Rout.Rout.Go(Rout.Rout.PageIngredientRoute)
                )
            ]
        )