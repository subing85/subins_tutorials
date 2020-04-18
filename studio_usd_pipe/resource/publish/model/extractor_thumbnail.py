NAME = 'Extract Thumbnail'
ORDER = 0
VALID = True
TYPE = 'extractor'
KEY = 'thumbnail'
OWNER = 'Subin Gopi'
COMMENTS = 'To create model thumbnail file'
VERSION = '0.0.0'
LAST_MODIFIED = 'April 14, 2020'



def execute(output_path=None, **kwargs):   
    values = []
    message = ''
    
    return True, values, message



def trail():    
    return True, [], 'trail run'
    