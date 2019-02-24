def show_window():
    from assetLibrary.resources.ui import main
    reload(main)
    my_window = main.MainWindow()
    my_window.show()