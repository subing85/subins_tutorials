
from pymel import core


def control_shapes():    
    return ['cricle', 'cube']


def control_types():
    control_type = {
        0: 'ct',
        1: "lt",
        2: 'rt'
    }
    return control_type


def create_shape(name, shape=None, orientation=[1,0,0], raduis=1.0):
    if shape == 'cricle':
        control_shape = core.circle(r=raduis, nr=orientation, ch=False)[0]
    elif shape == 'cube':
        control_shape = core.curve(
            d=1,
            p=[
                (1, 1, 1),
                (1, 1, -1),
                (-1, 1, -1),
                (-1, -1, -1),
                (1, -1, -1),
                (1, -1, 1),
                (-1, -1, 1),
                (-1, 1, 1),
                (1, 1, 1),
                (1, -1, 1),
                (1, -1, -1),
                (1, 1, -1),
                (-1, 1, -1),
                (-1, 1, 1),
                (-1, -1, 1),
                (-1, -1, -1)
            ],
            k=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
        )
        control_shape.setScale([raduis, raduis, raduis])
        core.makeIdentity(control_shape, a=True, t=0, r=0, s=1, n=0, pn=1)
    else:
        control_shape = core.group(em=True)
    
    control_shape.rename(name)        
    return control_shape


def create(name, shape=None, raduis=1.0):
    control_shape = create_shape(name, shape=shape, raduis=raduis)
    group = core.group(n='{}_group'.format(name), em=True)
    
    control_shape.setParent(group)
    return control_shape, group
