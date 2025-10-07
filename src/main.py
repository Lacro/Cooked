import flet
import Rout

def main(page: flet.Page):
    Rout.HomePageRouter.SetPage(page)

flet.app(main, assets_dir="assets", view=flet.AppView.WEB_BROWSER)
