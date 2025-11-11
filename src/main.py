import flet
import Views.Rout as Rout
import logging

def main(page: flet.Page):
    #logging.basicConfig(level=logging.DEBUG)
    page.window.width  = 1080 / 2  # window's width is 200 px
    page.window.height = 2400 / 2  # window's height is 200 px

    Rout.Rout.SetPage(page)

flet.app(main, assets_dir="assets", view=flet.AppView.WEB_BROWSER)
