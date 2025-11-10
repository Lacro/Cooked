import flet
import Rout as Rout

def UserActionSafe(action, parameters, on_success) -> None:
    try:
        action(*parameters)
        on_success()
    except Exception as ex:
        print(f"Error during user action {action} with parameters {parameters}: {ex}")
        Rout.Rout.page.open(flet.SnackBar(flet.Text(f"Error: {ex} !")))
