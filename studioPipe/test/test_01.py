from PySide import QtGui
from PySide import QtCore
im = '/home/shreya/Documents/studio_pipe/batman.jpg'
out = '/home/shreya/Documents/studio_pipe/new.jpg'

print 'ssssssssssssss'
image = QtGui.QImage(im)
image.save('/home/shreya/Documents/studio_pipe/pipe_data_base/shows/abc.png', 'jpg')
