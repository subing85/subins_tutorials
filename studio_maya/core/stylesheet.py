
def connect():
    widget_stypes = [
        'QWidget {font:14pt;}',
        #'QLabel {padding: 1px; border: 1px solid #ffaa00; border-radius: 2px;}',
        #'QLabel::hover {padding: 1px solid #55aaff;}'
        #'QTreeWidget {padding: 1px; border: 1px solid #ffaa00; border-radius: 2px;}',
        #'QTreeWidget::hover {border: 1px solid #55aaff;}'
        'QTextEdit {padding: 1px; border: 1px solid #ffaa00; border-radius: 2px;}',
        'QTextEdit::hover {border: 1px solid #55aaff;}'
        #'QToolBar {padding: 1px; border: 1px solid #ffaa00; border-radius: 2px;}',
        #'QToolBar::hover {border: 1px solid #55aaff;}'
        'QGroupBox {padding: 1px; border: 1px solid #ffaa00; border-radius: 2px;}',
        'QGroupBox::hover {border: 1px solid #55aaff;}'
        'QMenu {padding: 1px; border: 1px solid #ffaa00; border-radius: 2px;}',
        'QMenu::hover {border: 1px solid #55aaff;}'
        'QProgressBar {border: 1px solid grey; border-radius: 1px; text-align: right; font: 6pt}',
        'QProgressBar::chunk {background-color: #aaaa00;width: 3px;margin: 0.5px;}',
        'font: 8pt'
    ]
    data = ' '.join(widget_stypes)
    return data
