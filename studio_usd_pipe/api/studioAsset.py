from studio_usd_pipe.core import database

class Asset(database.Connect):
    
    def __init__(self, parent='asset'):
        super(Asset, self).__init__(parent)
        
        print self.db
    
    
            

            
