from gdo.base.GDO_Module import GDO_Module
from gdo.ui.GDT_Page import GDT_Page


class module_jquery(GDO_Module):

    async def gdo_load_scripts(self, page: 'GDT_Page'):
        dot_min = await self.get_minify_append()
        self.add_bower_js(f"jquery/dist/jquery{dot_min}.js")
        self.add_bower_js(f"jquery-color/dist/jquery.color{dot_min}.js")
        self.add_js('js/gdo-effects.js')

    def gdo_licenses(self) -> list[str]:
        return [
            'node_modules/jquery/LICENSE.txt',
            'node_modules/jquery-color/LICENSE.txt',
            'LICENSE',

        ]
