import flet
import Views.Rout as Rout
import Settings.Parameters as Parameters
import MyFletConstrols.MyLabel as MyLabel

def Toast(message: str):
    Rout.Rout.page.open(
        flet.SnackBar(
            MyLabel.Text(message, color=Parameters.AppColors.PrimaryFontColor),
            bgcolor=Parameters.AppColors.PrimaryBackGround,
        )
    )

def ToastSuccess(message: str):
    Rout.Rout.page.open(
        flet.SnackBar(
            flet.Row(
                controls=[
                    flet.Icon(flet.Icons.CHECK_CIRCLE_OUTLINE, color=Parameters.AppColors.PrimaryFontColor),
                    MyLabel.Text(message, color=Parameters.AppColors.PrimaryFontColor)
                ],
            ),
            bgcolor=Parameters.AppColors.PrimaryBackGround,
        )
    )

def ToastError(message: str):
    Rout.Rout.page.open(
        flet.SnackBar(
            flet.Row(
                controls=[
                    flet.Icon(flet.Icons.REMOVE_CIRCLE_OUTLINE, color=Parameters.AppColors.PrimaryFontColor),
                    MyLabel.Text(message, color=Parameters.AppColors.PrimaryFontColor)
                ],
            ),
            bgcolor=Parameters.AppColors.PrimaryBackGround,
        )
    )

def CancelToast(message: str, cancel_action):
    Rout.Rout.page.open(
        flet.SnackBar(
            flet.Row(
                controls=[
                    flet.Icon(flet.Icons.CHECK_CIRCLE_OUTLINE, color=Parameters.AppColors.PrimaryFontColor),
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
