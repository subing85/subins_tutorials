KEY = 'toolkit'
NAME = 'Pull Lighting Template'
ORDER = 11
ENABLE = True
ICON = 'pull_lighting_template.png'
LAST_MODIFIED = 'Jun 28, 2020'
OWNER = 'Subin Gopi'
DESCRIPTION = 'pull lighting template from latest publish'


def execute():
    from resources.studio_nodes import lighting_template
    lighting_template.create()   
