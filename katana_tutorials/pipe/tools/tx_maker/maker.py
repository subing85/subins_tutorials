import os

IMAGE_FORMATS = [
    '.TIFF',
    '.OpenEXR',
    '.JPEG',
    '.SGI',
    '.TGA',
    '.MayaIFF',
    '.DPX',
    '.BMP',
    '.HDR',
    '.PNG',
    '.GIF',
    '.PPM',
    '.XPM',
    '.TEX'
    ]


def converts(txmake, source_images, output_dirname):
    for source_image in source_images:
        convert(txmake, source_image, output_dirname)


def convert(txmake, source_image, output_dirname):
    name = os.path.splitext(os.path.basename(source_image))[0]
    tx_image = os.path.join(output_dirname, '%s.tx' % name)
    if not os.path.isdir(output_dirname):
        os.makedirs(output_dirname)
    
    if os.path.isfile(tx_image):
        try:
            os.remove(tx_image)
        except Exception as error:
            print '#error:', error
        
    command = '%s %s %s' % (txmake, source_image, tx_image)
    os.system(command)
    print 'source:'.rjust(10), source_image
    print 'tx:'.rjust(10), tx_image
    return tx_image
