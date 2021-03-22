import sys

print 'welcome to katana python tutorials <TX-Maker Tool>'


def show_window(standalone=False):
        
    if standalone:
        from PyQt4 import QtGui
        from tools.tx_maker import main        
        application = QtGui.QApplication(sys.argv)
        window = main.TxMaker(parent=None)
        window.show()
        sys.exit(application.exec_())
    
    if not standalone:
        from tools.tx_maker import main
        reload(main)
        window = main.TxMaker(parent=None)
        window.show()


if __name__ == '__main__':
    show_window(standalone=True)
