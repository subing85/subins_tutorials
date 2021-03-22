KEY = 'toolkit'
NAME = 'Template Publish'
ORDER = 7
ENABLE = True
ICON = 'template_publish.png'
LAST_MODIFIED = 'Jun 25, 2020'
OWNER = 'Subin Gopi'
DESCRIPTION = 'katana scene template publish'


def execute():
    from tools import template_publish
    template_publish.show_window(standalone=False)

