import flet
from flet.core.colors import Colors as FletColors
import Views.Rout as Rout

def Toast(message: str):
    Rout.Rout.page.open(flet.SnackBar(flet.Text(message)))

def ToastSuccess(message: str):
    Rout.Rout.page.open(
        flet.SnackBar(
            content=flet.Text(message),
            bgcolor=FletColors.GREEN,
            behavior=flet.SnackBarBehavior.FLOATING,
        )
    )

def ToastError(message: str):
    Rout.Rout.page.open(
        flet.SnackBar(
            content=flet.Text(message),
            bgcolor=FletColors.RED,
            behavior=flet.SnackBarBehavior.FLOATING,
        )
    )
