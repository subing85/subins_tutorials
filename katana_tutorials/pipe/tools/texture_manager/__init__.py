import sys

print 'welcome to katana python tutorials <Texture Manager Tool>'


def show_window(standalone=False):
        
    if standalone:
        from PyQt4 import QtGui
        from tools.texture_manager import main        
        application = QtGui.QApplication(sys.argv)
        window = main.TextureManager(parent=None)
        window.show()
        sys.exit(application.exec_())
    
    if not standalone:
        from tools.texture_manager import main
        reload(main)
        window = main.TextureManager(parent=None)
        window.show()

            
if __name__ == '__main__':
    show_window(standalone=True)
