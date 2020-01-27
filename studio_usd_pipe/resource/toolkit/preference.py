NAME = 'Preference'
ORDER = 0
VALID = True
LAST_MODIFIED = 'January 25, 2020'
OWNER = 'Subin Gopi'
COMMENTS = 'Configure the subin\'s usd toolkit!...'
SEPARATOR = True

def execute():
    from studio_usd_pipe.gui import preference
    preference.show_window(standalone=False)
    

