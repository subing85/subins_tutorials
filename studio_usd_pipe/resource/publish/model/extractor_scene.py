NAME = 'Extract Maya Ascii'
ORDER = 3
VALID = True
TYPE = 'extractor'
KEY = 'maya_ascii'
OWNER = 'Subin Gopi'
COMMENTS = 'To create maya ascii file'
VERSION = '0.0.0'
LAST_MODIFIED = 'April 14, 2020'



def execute(output_path=None, **kwargs):   
    values = []
    message = ''
    
    return True, values, message



def trail():    
    return True, [], 'trail run'
    