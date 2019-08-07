
def connect():
    
    widget_stypes = [
        'QWidget {font:14pt;}',
        'QLabel {padding: 1px; border: 1px solid #ffaa00; border-radius: 2px;}',
        'QLabel::hover {padding: 1px solid #55aaff;}'
        'QTreeWidget {padding: 1px; border: 1px solid #ffaa00; border-radius: 2px;}',
        'QTreeWidget::hover {border: 1px solid #55aaff;}'
        'QTextEdit {padding: 1px; border: 1px solid #ffaa00; border-radius: 2px;}',
        'QTextEdit::hover {border: 1px solid #55aaff;}' 
        
        'QToolBar {padding: 1px; border: 1px solid #ffaa00; border-radius: 2px;}',
        'QToolBar::hover {border: 1px solid #55aaff;}'
        
        'QMenu {padding: 1px; border: 1px solid #ffaa00; border-radius: 2px;}',
        'QMenu::hover {border: 1px solid #55aaff;}'
    ]
        
    # lineeit = 
    
    
    data = ' '.join(widget_stypes) 
    
    # print data   
    
    return data
    
    
'''
    
    
    
/* ==============================================
                QWidget
=============================================== */
QWidget
{
                font:10pt "Arial";
}
/* ==============================================
                QLineEdit
=============================================== */
QLineEdit
{
                padding: 1px;
                border: 1px solid #ffaa00;
                border-radius: 2px;
}
 
QLineEdit::hover
{
                border: 1px solid #55aaff;
}
 
/* ==============================================
                QPushButton
=============================================== */
QPushButton
{
                padding: 1px;
                border: 1px solid #ffaa00;
                border-radius: 2px;        
 
}
 
QPushButton::menu-indicator:open
{
                position: relative;          
                top: 2px; left: 2px;
}
QPushButton::hover
{
                border: 1px solid #55aaff;
}
/* ==============================================
                QLabel
=============================================== */
QLabel
{
                padding: 1px;
                border: 1px solid #ffaa00;
                border-radius: 2px;
}
 
QLabel::hover
{
                border: 1px solid #55aaff;
}
/* ==============================================
                QTreeWidget
=============================================== */
QTreeWidget
{
                padding: 1px;
                border: 1px solid #ffaa00;
                border-radius: 2px;
}
 
QTreeWidget::hover
{
                border: 1px solid #55aaff;
}
/* ==============================================
                QGroupBox
=============================================== */
QGroupBox
{
                padding: 1px;
                border: 1px solid #ffaa00;
                border-radius: 2px;
}
 
QGroupBox::hover
{
                border: 1px solid #55aaff;
}
/* ==============================================
                QProgressBar
=============================================== */
QProgressBar::hover
{
                border: 1px solid #55aaff;
}
/* ==============================================
                QTextEdit
=============================================== */
QTextEdit
{
                padding: 1px;
                border: 1px solid #ffaa00;
                border-radius: 2px;
}
 
QLabel::hover
{
                border: 1px solid #55aaff;
}
'''