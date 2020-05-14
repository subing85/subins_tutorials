https://www.subins-toolkits.com

Maya plug-in for Export and Import UV Sets


Free Maya Plug-in for any kind use such as students, commercial purposes, independent film makers, etc.
Supprt to Maya 2016, Maya 2017, Maya 2018, Maya 2019

Create Date:   1 Augustr 2019

Author: Subin. Gopi
mail id: subing85@gmail.com

https://www.subins-toolkits.com

Copyright 2019, Subin Gopi All rights reserved. https://www.subins-toolkits.com/

​

Description

    This plugin demonstrates how to Export and Import UV Sets. And the exported data contain only uv set information, (no geometries) so that data contain very less size compare to any maya build-in data format.  

    In pipeline environment, better way to manage the export and import the uv's for example in the case of uv publish, most of the production practices geometry to publish, instead of any uv data, because Maya not provide any build-in pulgin to export and import uv's. 

    Free Maya Plug-in for any kind use.

    This is easy way to interchanging uv's between Maya instances.  
    
    


How to Configure the Studio UV Plug-in?.​

    1. configure the env variable called PYTHONPATH and MAYA_PLUG_IN_PATH.
    
        For example, if it is the below folder structure.
            /home/user/subins_toolkits
            
                    └── studio_uv
                        ├── core
                        │   ├── 
                        ├── doc
                        │   └──
                        ├── plug-in
                        │   └── 
                        ├── resources.py            
                        └── toolkit
                            ├──    
            in linux        
               export PYTHONPATH="/home/user/subins_toolkits"                

               export MAYA_PLUG_IN_PATH="/home/user/subins_toolkits/studio_uv/plug-in"    
                /usr/autodesk/maya2016/bin/maya
            
            in wind        
                set PYTHONPATH="/home/user/subins_toolkits"
                set MAYA_PLUG_IN_PATH="/home/user/subins_toolkits/studio_uv/plug-in"
                start "" "/usr/autodesk/maya2016/bin/maya"                
                
    2. Copy the sg_studio_uv.py file and studio_uv folder.
    
            a. _/_/_/studio_uv/plug-in/sg_studio_uv.py file copy.
                to build-in "MAYA_PLUG_IN_PATH" env variable locations, for example find the  below directories.
                        /home/user/maya/2016/plug-ins
                        /home/user/maya/plug-ins:
                        /usr/autodesk/maya2016/bin/plug-ins    
                            
                to find the build-in MAYA_PLUG_IN_PATH locations use below python code
                run in the maya python interpreter.
                       import os
                       print os.environ['MAYA_PLUG_IN_PATH']
                    
            b. _/_/_/studio_uv folder copy                        
                to build-in "PYTHONPATH" env variable locations, or below directories
                     /home/shreya/maya/scripts/
                     /home/shreya/maya/2016/scripts/     

                  
                    
How to use the studioUV plug-in?. 

    plugin name : studioUV

        mel command
            studioUV

        python command
            maya.cmds.studioUV
            pymel.core.studioUV

​


Help on function studioUV in module pymel.internal.pmcmds:


studioUV(*args, **kwargs)

    Flags:
        - directory : dir                (unicode or str)       create, edit and query
               Set the type of the export output or import inputs directory.​

        - objects : obj                  (unicode or str)       create and edit
              Set the type of the export or import inputs polygon as s sting format.
        
        - repeat : rp                    (bool)          edit
              Set the uv import type to multiple assign the uv sets.
              Able to assign the uv sets to duplicated or repeated polygons.
             
        - select : s                     (unicode or str)       create and edit
              Set the type of the export or import inputs polygon.
              export "selected" or "all" 
              import "selected" or "all" or "matching" ​

        - type : typ                     (unicode or str)       create and edit
              create and edit              
            Set the type of process called "export" or "import"     
    
    Derived from mel command `maya.cmds.studioUV`
    

​

Examples
​

    # Export All 
        export all polygons from the scene
    maya.cmds.studioUV(typ='export', s='all', dir='/tmp/my_uv_test.muv')
    
    # Export Selected 
        export selected polygons from the scene)
    maya.cmds.studioUV(typ='export', s='selected', dir='/tmp/my_uv_test.muv')
    
    # Import All 
        import to all available polygons only matchs with exported data
    maya.cmds.studioUV(typ='import', s='all', rp=False, dir='/tmp/my_uv_test.muv')
    
    # Import All Duplicated
        import to all available polygons only matchs with exported data and the same name space (multi assign)
    maya.cmds.studioUV(typ='import', s='all', rp=True, dir='/tmp/my_uv_test.muv')    
    
    # Import Selected
        import only to selected polygons
    maya.cmds.studioUV(typ='import', s='selected', rp=False, dir='/tmp/my_uv_test.muv')
    
    # Import All Selected
        import only to selected polygons with the same name space  (multi assign)
    maya.cmds.studioUV(typ='import', s='selected', rp=True, dir='/tmp/my_uv_test.muv')
    
    # Import To All Matching Polygons
        import to all available polygons with the same polygon counts (multi assign)
    maya.cmds.studioUV(typ='import', s='matching', rp=True, dir='/tmp/my_uv_test.muv')
    
    # Import To Matching Polygons
        import to available polygons with the same polygon counts (single assign)
    maya.cmds.studioUV(typ='import', s='matching', rp=False, dir='/tmp/my_uv_test.muv')
    
    # Query (get the polygon list from the exportd data)
    maya.cmds.studioUV(q=True, obj=True, dir='/tmp/my_uv_test.muv')
    
    # Export the specific polygons
    maya.cmds.studioUV(typ='export', obj='ball, bat', dir='/tmp/my_uv_test.muv')