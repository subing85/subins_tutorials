KEY = 'toolkit'
NAME = 'TX-Maker'
ORDER = 1
ENABLE = True
ICON = 'txmaker.png'
LAST_MODIFIED = 'Jun 20, 2020'
OWNER = 'Subin Gopi'
DESCRIPTION = 'Convert imgaes to PRMAN tx formats'


def execute():
    from tools import tx_maker
    tx_maker.show_window(standalone=False)
