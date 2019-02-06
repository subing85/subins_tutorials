def show_window():
    from smartDeformer.resources.ui import main
    my_window = main.MainWindow()
    if not my_window:
        return
    my_window.show()
