import flet
import Views.Rout as Rout
import DataSource.DataSource as DataSource

async def main(page: flet.Page):
    #logging.basicConfig(level=logging.DEBUG)
    page.window.width  = 1080 / 2  # window's width is 200 px
    page.window.height = 2400 / 2  # window's height is 200 px

    await DataSource.DataSource.Initialize(Rout.Rout.refresh)

    Rout.Rout.InitRouter(page)

flet.app(main, assets_dir="assets", view=flet.AppView.WEB_BROWSER)
