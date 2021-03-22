import sys

print 'welcome to katana python tutorials <Tempalte Publish Tool>'


def show_window(standalone=False):
        
    if standalone:
        from PyQt4 import QtGui
        from tools.template_publish import main        
        application = QtGui.QApplication(sys.argv)
        window = main.TemplatePublish(parent=None)
        window.show()
        sys.exit(application.exec_())
    
    if not standalone:
        from tools.template_publish import main
        reload(main)
        window = main.TemplatePublish(parent=None)
        window.show()

            
if __name__ == '__main__':
    show_window(standalone=True)
