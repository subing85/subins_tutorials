//Maya ASCII 2018ff09 scene
//Name: lookthrough.ma
//Last modified: Tue, Jun 09, 2020 08:00:53 AM
//Codeset: UTF-8
requires maya "2018ff09";
requires "stereoCamera" "10.0";
requires "mtoa" "3.1.2.1";
requires "stereoCamera" "10.0";
requires "mtoa" "3.1.2.1";
currentUnit -l centimeter -a degree -t film;
fileInfo "application" "maya";
fileInfo "product" "Maya 2018";
fileInfo "version" "2018";
fileInfo "cutIdentifier" "201903222215-65bada0e52";
fileInfo "osv" "Linux 3.10.0-957.el7.x86_64 #1 SMP Thu Nov 8 23:39:32 UTC 2018 x86_64";
fileInfo "license" "student";
createNode transform -n "lookthrough";
	rename -uid "5CC52940-0000-4B3C-5ED4-120B000002CB";
	addAttr -ci true -sn "shader" -ln "shader" -dt "string";
	addAttr -ci true -sn "name" -ln "name" -dt "string";
	addAttr -ci true -sn "category" -ln "category" -dt "string";
	addAttr -ci true -sn "type" -ln "type" -dt "string";
	addAttr -ci true -sn "version" -ln "version" -dt "string";
	addAttr -ci true -sn "model" -ln "model" -dt "string";
	addAttr -ci true -sn "lookdev" -ln "lookdev" -dt "string";
	setAttr ".shader" -type "string" "None";
	setAttr ".name" -type "string" "lookthrough";
	setAttr ".category" -type "string" "camera";
	setAttr ".type" -type "string" "puppet";
	setAttr ".version" -type "string" "0.0.0";
	setAttr ".model" -type "string" "0.0.0";
	setAttr ".lookdev" -type "string" "0.0.0";
createNode transform -n "world" -p "lookthrough";
	rename -uid "5CC52940-0000-4B3C-5ED4-118E000002AC";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode nurbsCurve -n "worldShape" -p "|lookthrough|world";
	rename -uid "5CC52940-0000-4B3C-5ED4-118E000002AB";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		3 8 0 no 3
		13 0 0 0 1 2 3 4 5 6 7 8
		 8 8
		11
		-2.5948531480629597 1.7136723134148542e-16 -1.0483887240083527
		-2.7646782685750284 1.7136723134148542e-16 -0.62805680084909354
		-2.897445259477414 1.5732460140538257e-16 0.31275141559267206
		-2.4079033443307338 9.9107480064292307e-17 1.639109231900538
		-1.3509005672870851 1.7484674227327241e-17 2.5813394966622014
		0.025422428098542942 -6.826462119988117e-17 2.9131217188214791
		1.3957454046358155 -1.379025911357746e-16 2.5573698803972107
		2.4361430094986822 -1.7493698140181252e-16 1.5968358797983617
		2.9024622293490627 -1.7079623151607965e-16 0.26213638973905162
		2.7532960921295864 -1.4080366910161993e-16 -0.67621143356776003
		2.5761610332443978 -1.2117493135472827e-16 -1.0935154811127612
		;
createNode transform -n "camera" -p "|lookthrough|world";
	rename -uid "5CC52940-0000-4B3C-5ED4-1192000002AD";
	setAttr -l on ".tx";
	setAttr -l on ".ty";
	setAttr -l on ".tz";
	setAttr -l on ".rx";
	setAttr -l on ".ry";
	setAttr -l on ".rz";
	setAttr ".s" -type "double3" 1.0000000000000002 1.0000000000000002 1.0000000000000002 ;
	setAttr -l on ".sx";
	setAttr -l on ".sy";
	setAttr -l on ".sz";
createNode camera -n "cameraShape" -p "camera";
	rename -uid "5CC52940-0000-4B3C-5ED4-1192000002AE";
	setAttr -k off ".v";
	setAttr ".rnd" no;
	setAttr ".cap" -type "double2" 1.41732 0.94488 ;
	setAttr ".ff" 0;
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
// End of lookthrough.ma
