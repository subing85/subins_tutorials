from pymel import core

from crowd.core import biped
reload(biped)


def create_puppet(tag, root, inputs):
    if tag == 'biped':
        biped.create_puppet(root, inputs)
