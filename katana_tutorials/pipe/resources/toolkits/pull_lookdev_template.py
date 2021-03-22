KEY = 'toolkit'
NAME = 'Pull Lookdev Template'
ORDER = 8
ENABLE = True
ICON = 'pull_lookdev_template.png'
LAST_MODIFIED = 'Jun 26, 2020'
OWNER = 'Subin Gopi'
DESCRIPTION = 'pull lookdev template from latest publish'


def execute():
    from resources.studio_nodes import lookdev_template
    lookdev_template.create()   
