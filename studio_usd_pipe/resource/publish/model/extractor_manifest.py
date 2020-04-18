NAME = 'Extract Manifest'
ORDER = 4
VALID = True
TYPE = 'extractor'
KEY = 'manifest'
OWNER = 'Subin Gopi'
COMMENTS = 'To create manifest of the publish'
VERSION = '0.0.0'
LAST_MODIFIED = 'April 14, 2020'



def execute(output_path=None, **kwargs):   
    values = [output_path + '/tmp/man.txt']
    message = ''
    
    return True, values, message



def trail():    
    return True, [], 'trail run'
    