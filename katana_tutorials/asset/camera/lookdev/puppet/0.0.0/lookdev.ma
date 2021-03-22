//Maya ASCII 2018ff09 scene
//Name: lookdev.ma
//Last modified: Tue, Jun 09, 2020 07:58:12 AM
//Codeset: UTF-8
requires maya "2018ff09";
requires "stereoCamera" "10.0";
requires "mtoa" "3.1.2.1";
requires "Mayatomr" "2012.0m - 3.9.1.36 ";
currentUnit -l centimeter -a degree -t film;
fileInfo "application" "maya";
fileInfo "product" "Maya 2018";
fileInfo "version" "2018";
fileInfo "cutIdentifier" "201903222215-65bada0e52";
fileInfo "osv" "Linux 3.10.0-957.el7.x86_64 #1 SMP Thu Nov 8 23:39:32 UTC 2018 x86_64";
fileInfo "license" "student";
createNode transform -n "lookdev";
	rename -uid "E9ADC940-0000-677A-5ECB-EE89000007F9";
	addAttr -ci true -sn "name" -ln "name" -dt "string";
	addAttr -ci true -sn "category" -ln "category" -dt "string";
	addAttr -ci true -sn "type" -ln "type" -dt "string";
	addAttr -ci true -sn "version" -ln "version" -dt "string";
	addAttr -ci true -sn "model" -ln "model" -dt "string";
	addAttr -ci true -sn "lookdev" -ln "lookdev" -dt "string";
	setAttr ".name" -type "string" "lookdev";
	setAttr ".category" -type "string" "camera";
	setAttr ".type" -type "string" "puppet";
	setAttr ".version" -type "string" "0.0.0";
	setAttr ".model" -type "string" "0.0.0";
	setAttr ".lookdev" -type "string" "0.0.0";
createNode transform -n "camera" -p "lookdev";
	rename -uid "E9ADC940-0000-677A-5ECB-EBCB0000077D";
	setAttr ".t" -type "double3" 3.7742596295836233 6.0789414356666516 25.305541926716735 ;
	setAttr ".r" -type "double3" -7.8000000000000158 7.9999999999999458 -1.0036911916390714e-16 ;
createNode camera -n "cameraShape" -p "camera";
	rename -uid "E9ADC940-0000-677A-5ECB-EBCB0000077E";
	setAttr -k off ".v";
	setAttr ".rnd" no;
	setAttr ".cap" -type "double2" 1.41732 0.94488 ;
	setAttr ".ff" 0;
	setAttr ".coi" 31.059078717673906;
	setAttr ".ow" 30;
	setAttr ".imn" -type "string" "camera1";
	setAttr ".den" -type "string" "camera1_depth";
	setAttr ".man" -type "string" "camera1_mask";
	setAttr ".ai_translator" -type "string" "perspective";
select -ne :time1;
	setAttr ".o" 1;
	setAttr ".unw" 1;
select -ne :hardwareRenderingGlobals;
	setAttr ".otfna" -type "stringArray" 22 "NURBS Curves" "NURBS Surfaces" "Polygons" "Subdiv Surface" "Particles" "Particle Instance" "Fluids" "Strokes" "Image Planes" "UI" "Lights" "Cameras" "Locators" "Joints" "IK Handles" "Deformers" "Motion Trails" "Components" "Hair Systems" "Follicles" "Misc. UI" "Ornaments"  ;
	setAttr ".otfva" -type "Int32Array" 22 0 1 1 1 1 1
		 1 1 1 0 0 0 0 0 0 0 0 0
		 0 0 0 0 ;
select -ne :renderPartition;
	setAttr -s 2 ".st";
select -ne :renderGlobalsList1;
select -ne :defaultShaderList1;
	setAttr -s 4 ".s";
select -ne :postProcessList1;
	setAttr -s 2 ".p";
select -ne :defaultRenderingList1;
select -ne :initialShadingGroup;
	setAttr ".ro" yes;
select -ne :initialParticleSE;
	setAttr ".ro" yes;
select -ne :defaultRenderGlobals;
	setAttr ".ren" -type "string" "arnold";
select -ne :defaultResolution;
	setAttr ".pa" 1;
select -ne :defaultColorMgtGlobals;
	setAttr ".cme" no;
select -ne :hardwareRenderGlobals;
	setAttr ".ctrs" 256;
	setAttr ".btrs" 512;
// End of lookdev.ma
