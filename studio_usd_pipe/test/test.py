import sys




def runs(name):
  from maya import standalone
  standalone.initialize(name='python')
  from maya import cmds

  pulgins = [			
    "objExport",
    "pxrUsd",			
    "pxrUsdPreviewSurface",
    "pxrUsdTranslators"
    ]
  for plugin in pulgins:
      #try:        
      cmds.loadPlugin(plugin, quiet=True)
      print '{} loaded plugin'.format(plugin)
      #except ImportError as error:
      #print error
      
  print '\nsubin', name



runs(sys.argv)
print '##################'