from maya import OpenMaya
from pymel import core
from maya import cmds

from alembic import Abc
from alembic import AbcCollection
from alembic import AbcCoreAbstract
from alembic import AbcGeom
from alembic import AbcMaterial
from alembic import Util


node = 'pSphereShape1'
path = '/venture/test_show/cache/alembic/ball_03.abc'

object = Abc.IObject()
dir(Abc)
object.
archive = Abc.IArchive(path)
top = archive.getTop()'
meta = top.getMetaData()

abc = AbcCoreAbstract.MetaData()
abc.set('name', 'subin')

meta.append(abc)



print meta.__str__()

for x in range (top.getNumChildren()):
    child = top.getChild(x)
    print 'child\t', child
    
mdata = top.getMetaData()


o_archive = Abc.OArchive(path, False)








