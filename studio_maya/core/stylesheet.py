'''
stylesheet.py 0.0.1 
Date: August 15, 2019
Last modified: August 27, 2019
Author: Subin. Gopi(subing85@gmail.com)

# Copyright(c) 2019, Subin Gopi
# All rights reserved.

# WARNING! All changes made in this file will be lost!

Description
    None.
'''

def connect():
    widget_stypes = [
        'QWidget {font:14pt;}',
        'QTextEdit {padding: 1px; border: 1px solid #ffaa00; border-radius: 2px;}',
        'QTextEdit::hover {border: 1px solid #55aaff;}'
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
