NAME = 'Extract studio model'
ORDER = 1
VALID = True
TYPE = 'extractor'
KEY = 'studio_model'
OWNER = 'Subin Gopi'
COMMENTS = 'To create studio model (custom data) file'
VERSION = '0.0.0'
LAST_MODIFIED = 'April 14, 2020'



def execute(output_path=None, **kwargs):   
    values = []
    message = ''
    
    return True, values, message



def trail():    
    return True, [], 'trail run'
    