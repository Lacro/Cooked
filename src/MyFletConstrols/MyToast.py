import flet
import Views.Rout as Rout
import Settings.Parameters as Parameters
import MyFletConstrols.MyLabel as MyLabel

def Toast(message: str):
    Rout.Rout.page.open(flet.SnackBar(MyLabel.Text(message)))

def ToastSuccess(message: str):
    Rout.Rout.page.open(
        flet.SnackBar(
            content=MyLabel.Text(message),
            bgcolor=Parameters.AppColors.SuccessBackGround,
            behavior=flet.SnackBarBehavior.FLOATING,
        )
    )

def ToastError(message: str):
    Rout.Rout.page.open(
        flet.SnackBar(
            content=MyLabel.Text(message),
            bgcolor=Parameters.AppColors.ErrorBackGround,
            behavior=flet.SnackBarBehavior.FLOATING,
        )
    )

def CancelToast(message: str, cancel_action):
    Rout.Rout.page.open(
        flet.SnackBar(
            flet.Row(
                controls=[
                    MyLabel.Text(message, color=Parameters.AppColors.PrimaryFontColor),
                    flet.Container(
                        content = MyLabel.Text(
                            "Cancel",
                            color=Parameters.AppColors.PrimaryFontColor,
                        ),
                        on_click=cancel_action,
                        alignment=flet.alignment.center_right,
                        expand=True,
                    )
                ]
            ),
            bgcolor=Parameters.AppColors.PrimaryBackGround,
        )
    )
