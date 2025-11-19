import flet
import Settings.Parameters as Parameters

class Text(flet.Text):
    def __init__(self, text:str, **kwargs):
        if 'size'       not in kwargs: kwargs['size']       = Parameters.AppSizes.DefaultTextSize
        if 'color'      not in kwargs: kwargs['color']      = Parameters.AppColors.SecondaryFontColor
        if 'text_align' not in kwargs: kwargs['text_align'] = flet.TextAlign.CENTER,

        super().__init__(value=text, **kwargs)


class Title(flet.Text):
    def __init__(self, text:str, **kwargs):
        if 'size'       not in kwargs: kwargs['size']       = Parameters.AppSizes.TitleTextSize
        if 'color'      not in kwargs: kwargs['color']      = Parameters.AppColors.PrimaryFontColor
        if 'text_align' not in kwargs: kwargs['text_align'] = flet.TextAlign.CENTER,
        
        super().__init__(value=text, **kwargs)
