from gdo.base.GDO_Module import GDO_Module
from gdo.ui.GDT_Page import GDT_Page


class module_jquery(GDO_Module):

    def __init__(self):
        super().__init__()
        self._priority = 25

    def gdo_load_scripts(self, page: 'GDT_Page'):
        self.add_bower_js("jquery/dist/jquery.js")
        self.add_bower_js("jquery-color/dist/jquery.color.js")
        self.add_js('js/gdo-effects.js')

    def gdo_licenses(self) -> list[str]:
        return [
            'node_modules/jquery/LICENSE.txt',
            'node_modules/jquery-color/LICENSE.txt',
            'LICENSE',
        ]
