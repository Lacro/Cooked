import flet
from Rout import Rout

def main(page: flet.Page):
    page.window.width  = 1080 / 2  # window's width is 200 px
    page.window.height = 2400 / 2  # window's height is 200 px

    Rout.SetPage(page)

flet.app(main, assets_dir="assets", view=flet.AppView.WEB_BROWSER)
