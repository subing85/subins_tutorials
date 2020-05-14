Smart Copy - v0.1
Date : August 20, 2016
Last modified: August 20, 2016
Author: Subin. Gopi
subing85@gmail.com
Copyright 2016 Subin. Gopi - All Rights Reserved.


!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
!!!!!!Pose and Animation Copy Paste Tool (Smart Copy)!!!!!!
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

Smart Copy written in Python and Pymel.

This tool will help to duplicates the Pose and Animation with simple procedure.
Just like a basic copy paste concept, from one Scene file to any another files. 

Procedure

 	Copy		
		>- Select the controls or key nodes - click on copy button.

	Paste		
		>- Selected			- 	selected node only will get updated with pose or animation.			
								
Features

	>- This module will support from one scene file to any another scene files.
	>- Copying pose and animation from one rig to another identical rig.	
	>- Easy way to copy the pose and animation with two clicks.		
	
	https://vimeo.com/180073258
	

Support - Autodesk Maya2016.
OS 		- Windows 10

Installing 
	copy to smartCopy folder to  C:\Users\meera\Documents\maya\2016\scripts
	or
	update the mayaLaunch.bat line 19 to change with your smartCopy dirctory
		example 
			set PYTHONPATH=D:/MyScripts/pythonApplication/subinTutorials
			to set PYTHONPATH= C:/Users/abcd/Desktop/myScripts


# After that open the new maya and run following two lines in the PYTHON script editor.
import smartCopy 
reload(smartCopy)
smartCopy.main()

!thanks!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
