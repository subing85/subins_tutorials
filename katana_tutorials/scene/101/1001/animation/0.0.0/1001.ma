//Maya ASCII 2018ff09 scene
//Name: 1001.ma
//Last modified: Thu, Jun 11, 2020 12:49:59 PM
//Codeset: UTF-8
file -rdi 1 -ns "lookthrough" -rfn "lookthroughRN" -op "v=0;" -typ "mayaAscii"
		 "/venture/shows/katana_tutorials//asset/camera/lookthrough/puppet/0.0.0/lookthrough.ma";
file -rdi 1 -ns "batman" -rfn "batmanRN" -op "v=0;" -typ "mayaAscii" "/venture/shows/katana_tutorials//asset/character/batman/puppet/0.0.2/batman.ma";
file -rdi 1 -ns "jasmin" -rfn "jasminRN" -op "v=0;" -typ "mayaAscii" "/venture/shows/katana_tutorials//asset/character/jasmin/puppet//0.1.0/jasmin.ma";
file -rdi 1 -ns "southcity" -rfn "southcityRN" -op "v=0;" -typ "mayaAscii" "/venture/shows/katana_tutorials//asset/set/southcity/puppet/0.0.1/southcity.ma";
file -r -ns "lookthrough" -dr 1 -rfn "lookthroughRN" -op "v=0;" -typ "mayaAscii"
		 "/venture/shows/katana_tutorials//asset/camera/lookthrough/puppet/0.0.0/lookthrough.ma";
file -r -ns "batman" -dr 1 -rfn "batmanRN" -op "v=0;" -typ "mayaAscii" "/venture/shows/katana_tutorials//asset/character/batman/puppet/0.0.2/batman.ma";
file -r -ns "jasmin" -dr 1 -rfn "jasminRN" -op "v=0;" -typ "mayaAscii" "/venture/shows/katana_tutorials//asset/character/jasmin/puppet//0.1.0/jasmin.ma";
file -r -ns "southcity" -dr 1 -rfn "southcityRN" -op "v=0;" -typ "mayaAscii" "/venture/shows/katana_tutorials//asset/set/southcity/puppet/0.0.1/southcity.ma";
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
createNode reference -n "lookthroughRN";
	rename -uid "5CC52940-0000-4B3C-5ED4-12CE00000324";
	setAttr -s 6 ".phl";
	setAttr ".phl[11]" 0;
	setAttr ".phl[12]" 0;
	setAttr ".phl[13]" 0;
	setAttr ".phl[14]" 0;
	setAttr ".phl[15]" 0;
	setAttr ".phl[16]" 0;
	setAttr ".ed" -type "dataReferenceEdits" 
		"lookthroughRN"
		"lookthroughRN" 4
		5 4 "lookthroughRN" "|lookthrough:lookthrough|lookthrough:world.scaleX" 
		"lookthroughRN.placeHolderList[7]" ""
		5 4 "lookthroughRN" "|lookthrough:lookthrough|lookthrough:world.scaleY" 
		"lookthroughRN.placeHolderList[8]" ""
		5 4 "lookthroughRN" "|lookthrough:lookthrough|lookthrough:world.scaleZ" 
		"lookthroughRN.placeHolderList[9]" ""
		5 4 "lookthroughRN" "|lookthrough:lookthrough|lookthrough:world.visibility" 
		"lookthroughRN.placeHolderList[10]" ""
		"lookthroughRN" 24
		1 |lookthrough:lookthrough "min" "min" " -ci 1 -dt \"string\""
		1 |lookthrough:lookthrough "max" "max" " -ci 1 -dt \"string\""
		1 |lookthrough:lookthrough "latest_lookdev" "latest_lookdev" " -ci 1 -dt \"string\""
		
		2 "|lookthrough:lookthrough" "min" " -type \"string\" \"1001\""
		2 "|lookthrough:lookthrough" "max" " -type \"string\" \"1050\""
		2 "|lookthrough:lookthrough" "latest_lookdev" " -type \"string\" \"None\""
		
		2 "|lookthrough:lookthrough|lookthrough:world" "translate" " -type \"double3\" 11.04 4.668 32.716"
		
		2 "|lookthrough:lookthrough|lookthrough:world" "translateX" " -av"
		2 "|lookthrough:lookthrough|lookthrough:world" "translateY" " -av"
		2 "|lookthrough:lookthrough|lookthrough:world" "translateZ" " -av"
		2 "|lookthrough:lookthrough|lookthrough:world" "rotate" " -type \"double3\" -1.8 20.4 0"
		
		2 "|lookthrough:lookthrough|lookthrough:world" "rotateX" " -av"
		2 "|lookthrough:lookthrough|lookthrough:world" "rotateY" " -av"
		2 "|lookthrough:lookthrough|lookthrough:world|lookthrough:camera|lookthrough:cameraShape" 
		"overscan" " 1.3"
		2 "|lookthrough:lookthrough|lookthrough:world|lookthrough:camera|lookthrough:cameraShape" 
		"centerOfInterest" " 12.41888190748606924"
		2 "|lookthrough:lookthrough|lookthrough:world|lookthrough:camera|lookthrough:cameraShape" 
		"displayFilmGate" " 0"
		2 "|lookthrough:lookthrough|lookthrough:world|lookthrough:camera|lookthrough:cameraShape" 
		"displayResolution" " 1"
		4 "|lookthrough:lookthrough" "shader" ""
		5 4 "lookthroughRN" "|lookthrough:lookthrough|lookthrough:world.translateX" 
		"lookthroughRN.placeHolderList[11]" ""
		5 4 "lookthroughRN" "|lookthrough:lookthrough|lookthrough:world.translateY" 
		"lookthroughRN.placeHolderList[12]" ""
		5 4 "lookthroughRN" "|lookthrough:lookthrough|lookthrough:world.translateZ" 
		"lookthroughRN.placeHolderList[13]" ""
		5 4 "lookthroughRN" "|lookthrough:lookthrough|lookthrough:world.rotateX" 
		"lookthroughRN.placeHolderList[14]" ""
		5 4 "lookthroughRN" "|lookthrough:lookthrough|lookthrough:world.rotateY" 
		"lookthroughRN.placeHolderList[15]" ""
		5 4 "lookthroughRN" "|lookthrough:lookthrough|lookthrough:world.rotateZ" 
		"lookthroughRN.placeHolderList[16]" "";
	setAttr ".ptag" -type "string" "";
lockNode -l 1 ;
createNode reference -n "batmanRN";
	rename -uid "5CC52940-0000-4B3C-5ED4-12D90000032A";
	setAttr -s 10 ".phl";
	setAttr ".phl[1]" 0;
	setAttr ".phl[2]" 0;
	setAttr ".phl[3]" 0;
	setAttr ".phl[4]" 0;
	setAttr ".phl[5]" 0;
	setAttr ".phl[6]" 0;
	setAttr ".phl[7]" 0;
	setAttr ".phl[8]" 0;
	setAttr ".phl[9]" 0;
	setAttr ".phl[10]" 0;
	setAttr ".ed" -type "dataReferenceEdits" 
		"batmanRN"
		"batmanRN" 0
		"batmanRN" 19
		1 |batman:batman "min" "min" " -ci 1 -dt \"string\""
		1 |batman:batman "max" "max" " -ci 1 -dt \"string\""
		1 |batman:batman "latest_lookdev" "latest_lookdev" " -ci 1 -dt \"string\""
		
		2 "|batman:batman" "min" " -type \"string\" \"1001\""
		2 "|batman:batman" "max" " -type \"string\" \"1050\""
		2 "|batman:batman" "latest_lookdev" " -type \"string\" \"2.0.2\""
		2 "|batman:batman|batman:world" "translate" " -type \"double3\" -8.09905929773589328 0 0"
		
		2 "|batman:batman|batman:world" "translateX" " -av"
		2 "|batman:batman|batman:world" "translateZ" " -av"
		5 4 "batmanRN" "|batman:batman|batman:world.translateX" "batmanRN.placeHolderList[1]" 
		""
		5 4 "batmanRN" "|batman:batman|batman:world.translateY" "batmanRN.placeHolderList[2]" 
		""
		5 4 "batmanRN" "|batman:batman|batman:world.translateZ" "batmanRN.placeHolderList[3]" 
		""
		5 4 "batmanRN" "|batman:batman|batman:world.rotateY" "batmanRN.placeHolderList[4]" 
		""
		5 4 "batmanRN" "|batman:batman|batman:world.rotateX" "batmanRN.placeHolderList[5]" 
		""
		5 4 "batmanRN" "|batman:batman|batman:world.rotateZ" "batmanRN.placeHolderList[6]" 
		""
		5 4 "batmanRN" "|batman:batman|batman:world.visibility" "batmanRN.placeHolderList[7]" 
		""
		5 4 "batmanRN" "|batman:batman|batman:world.scaleX" "batmanRN.placeHolderList[8]" 
		""
		5 4 "batmanRN" "|batman:batman|batman:world.scaleY" "batmanRN.placeHolderList[9]" 
		""
		5 4 "batmanRN" "|batman:batman|batman:world.scaleZ" "batmanRN.placeHolderList[10]" 
		"";
	setAttr ".ptag" -type "string" "";
lockNode -l 1 ;
createNode reference -n "jasminRN";
	rename -uid "5CC52940-0000-4B3C-5ED4-12E100000340";
	setAttr -s 10 ".phl";
	setAttr ".phl[1]" 0;
	setAttr ".phl[2]" 0;
	setAttr ".phl[3]" 0;
	setAttr ".phl[4]" 0;
	setAttr ".phl[5]" 0;
	setAttr ".phl[6]" 0;
	setAttr ".phl[7]" 0;
	setAttr ".phl[8]" 0;
	setAttr ".phl[9]" 0;
	setAttr ".phl[10]" 0;
	setAttr ".ed" -type "dataReferenceEdits" 
		"jasminRN"
		"jasminRN" 0
		"jasminRN" 21
		1 |jasmin:jasmin "min" "min" " -ci 1 -dt \"string\""
		1 |jasmin:jasmin "max" "max" " -ci 1 -dt \"string\""
		1 |jasmin:jasmin "latest_lookdev" "latest_lookdev" " -ci 1 -dt \"string\""
		
		2 "|jasmin:jasmin" "min" " -type \"string\" \"1001\""
		2 "|jasmin:jasmin" "max" " -type \"string\" \"1050\""
		2 "|jasmin:jasmin" "latest_lookdev" " -type \"string\" \"0.0.1\""
		2 "|jasmin:jasmin|jasmin:world" "translate" " -type \"double3\" 8.53414580075088836 0 0"
		
		2 "|jasmin:jasmin|jasmin:world" "translateX" " -av"
		2 "|jasmin:jasmin|jasmin:world" "translateZ" " -av"
		2 "|jasmin:jasmin|jasmin:world" "rotate" " -type \"double3\" 0 -72.48082273540114784 0"
		
		2 "|jasmin:jasmin|jasmin:world" "rotateY" " -av"
		5 4 "jasminRN" "|jasmin:jasmin|jasmin:world.translateX" "jasminRN.placeHolderList[1]" 
		""
		5 4 "jasminRN" "|jasmin:jasmin|jasmin:world.translateY" "jasminRN.placeHolderList[2]" 
		""
		5 4 "jasminRN" "|jasmin:jasmin|jasmin:world.translateZ" "jasminRN.placeHolderList[3]" 
		""
		5 4 "jasminRN" "|jasmin:jasmin|jasmin:world.rotateX" "jasminRN.placeHolderList[4]" 
		""
		5 4 "jasminRN" "|jasmin:jasmin|jasmin:world.rotateY" "jasminRN.placeHolderList[5]" 
		""
		5 4 "jasminRN" "|jasmin:jasmin|jasmin:world.rotateZ" "jasminRN.placeHolderList[6]" 
		""
		5 4 "jasminRN" "|jasmin:jasmin|jasmin:world.visibility" "jasminRN.placeHolderList[7]" 
		""
		5 4 "jasminRN" "|jasmin:jasmin|jasmin:world.scaleX" "jasminRN.placeHolderList[8]" 
		""
		5 4 "jasminRN" "|jasmin:jasmin|jasmin:world.scaleY" "jasminRN.placeHolderList[9]" 
		""
		5 4 "jasminRN" "|jasmin:jasmin|jasmin:world.scaleZ" "jasminRN.placeHolderList[10]" 
		"";
	setAttr ".ptag" -type "string" "";
lockNode -l 1 ;
createNode reference -n "southcityRN";
	rename -uid "4A26E940-0000-4677-5EE0-FEEB0000094C";
	setAttr ".ed" -type "dataReferenceEdits" 
		"southcityRN"
		"southcityRN" 0
		"southcityRN" 8
		1 |southcity:southcity "min" "min" " -ci 1 -dt \"string\""
		1 |southcity:southcity "max" "max" " -ci 1 -dt \"string\""
		1 |southcity:southcity "latest_lookdev" "latest_lookdev" " -ci 1 -dt \"string\""
		
		2 "|southcity:southcity" "min" " -type \"string\" \"1001\""
		2 "|southcity:southcity" "max" " -type \"string\" \"1050\""
		2 "|southcity:southcity" "latest_lookdev" " -type \"string\" \"0.1.0\""
		2 "|southcity:southcity|southcity:world" "translate" " -type \"double3\" 0 0 0"
		
		2 "|southcity:southcity|southcity:world" "rotate" " -type \"double3\" 0 0 0";
	setAttr ".ptag" -type "string" "";
lockNode -l 1 ;
createNode animCurveTL -n "world_translateX2";
	rename -uid "5CC52940-0000-4B3C-5ED4-13CE000003BD";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  1001 11.04 1040 7.837;
createNode animCurveTL -n "world_translateY2";
	rename -uid "5CC52940-0000-4B3C-5ED4-13CE000003BE";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  1001 4.668 1040 4.379;
createNode animCurveTL -n "world_translateZ2";
	rename -uid "5CC52940-0000-4B3C-5ED4-13CE000003BF";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  1001 32.716 1040 24.104;
createNode animCurveTA -n "world_rotateX2";
	rename -uid "5CC52940-0000-4B3C-5ED4-13CE000003C1";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  1001 -1.8 1040 -1.8;
createNode animCurveTA -n "world_rotateY2";
	rename -uid "5CC52940-0000-4B3C-5ED4-13CE000003C2";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  1001 20.4 1040 20.4;
createNode animCurveTA -n "world_rotateZ2";
	rename -uid "5CC52940-0000-4B3C-5ED4-13CE000003C3";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  1001 0 1040 0;
createNode animCurveTL -n "world_translateX";
	rename -uid "5CC52940-0000-4B3C-5ED4-13600000038B";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  1001 -8.0990592977358933 1040 3.025753021655857;
createNode animCurveTL -n "world_translateY";
	rename -uid "5CC52940-0000-4B3C-5ED4-13600000038C";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  1001 0 1040 0;
createNode animCurveTL -n "world_translateZ";
	rename -uid "5CC52940-0000-4B3C-5ED4-13600000038D";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  1001 0 1040 2.4179818692403803;
createNode animCurveTA -n "world_rotateY";
	rename -uid "5CC52940-0000-4B3C-5ED4-136000000388";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  1001 77.737466824730248 1040 77.737466824730248;
createNode animCurveTA -n "world_rotateX";
	rename -uid "5CC52940-0000-4B3C-5ED4-136000000387";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  1001 0 1040 0;
createNode animCurveTA -n "world_rotateZ";
	rename -uid "5CC52940-0000-4B3C-5ED4-136000000389";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  1001 0 1040 0;
createNode animCurveTU -n "world_visibility";
	rename -uid "5CC52940-0000-4B3C-5ED4-13600000038A";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  1001 1 1040 1;
	setAttr -s 2 ".kot[0:1]"  5 5;
createNode animCurveTU -n "world_scaleX";
	rename -uid "5CC52940-0000-4B3C-5ED4-13600000038E";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  1001 1 1040 1;
createNode animCurveTU -n "world_scaleY";
	rename -uid "5CC52940-0000-4B3C-5ED4-13600000038F";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  1001 1 1040 1;
createNode animCurveTU -n "world_scaleZ";
	rename -uid "5CC52940-0000-4B3C-5ED4-136000000390";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  1001 1 1040 1;
createNode animCurveTL -n "world_translateX1";
	rename -uid "5CC52940-0000-4B3C-5ED4-136A00000395";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  1001 8.5341458007508884 1040 6.0094816949756673;
createNode animCurveTL -n "world_translateY1";
	rename -uid "5CC52940-0000-4B3C-5ED4-136A00000396";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  1001 0 1040 0;
createNode animCurveTL -n "world_translateZ1";
	rename -uid "5CC52940-0000-4B3C-5ED4-136A00000397";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  1001 0 1040 2.323827468879057;
createNode animCurveTA -n "world_rotateX1";
	rename -uid "5CC52940-0000-4B3C-5ED4-136A00000399";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  1001 0 1040 0;
createNode animCurveTA -n "world_rotateY1";
	rename -uid "5CC52940-0000-4B3C-5ED4-136A0000039A";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  1001 -72.480822735401148 1040 -47.371978351775127;
createNode animCurveTA -n "world_rotateZ1";
	rename -uid "5CC52940-0000-4B3C-5ED4-136A0000039B";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  1001 0 1040 0;
createNode animCurveTU -n "world_visibility1";
	rename -uid "5CC52940-0000-4B3C-5ED4-136A00000398";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  1001 1 1040 1;
	setAttr -s 2 ".kot[0:1]"  5 5;
createNode animCurveTU -n "world_scaleX1";
	rename -uid "5CC52940-0000-4B3C-5ED4-136A0000039C";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  1001 1 1040 1;
createNode animCurveTU -n "world_scaleY1";
	rename -uid "5CC52940-0000-4B3C-5ED4-136A0000039D";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  1001 1 1040 1;
createNode animCurveTU -n "world_scaleZ1";
	rename -uid "5CC52940-0000-4B3C-5ED4-136A0000039E";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  1001 1 1040 1;
select -ne :time1;
	setAttr -av -k on ".cch";
	setAttr -cb on ".ihi";
	setAttr -k on ".nds";
	setAttr -cb on ".bnm";
	setAttr -k on ".o" 1001;
	setAttr ".unw" 1001;
select -ne :hardwareRenderingGlobals;
	setAttr ".otfna" -type "stringArray" 22 "NURBS Curves" "NURBS Surfaces" "Polygons" "Subdiv Surface" "Particles" "Particle Instance" "Fluids" "Strokes" "Image Planes" "UI" "Lights" "Cameras" "Locators" "Joints" "IK Handles" "Deformers" "Motion Trails" "Components" "Hair Systems" "Follicles" "Misc. UI" "Ornaments"  ;
	setAttr ".otfva" -type "Int32Array" 22 0 1 1 1 1 1
		 1 1 1 0 0 0 0 0 0 0 0 0
		 0 0 0 0 ;
select -ne :renderPartition;
	setAttr -k on ".cch";
	setAttr -cb on ".ihi";
	setAttr -k on ".nds";
	setAttr -cb on ".bnm";
	setAttr -s 2 ".st";
	setAttr -cb on ".an";
	setAttr -cb on ".pt";
select -ne :renderGlobalsList1;
	setAttr -k on ".cch";
	setAttr -cb on ".ihi";
	setAttr -k on ".nds";
	setAttr -cb on ".bnm";
select -ne :defaultShaderList1;
	setAttr -k on ".cch";
	setAttr -cb on ".ihi";
	setAttr -k on ".nds";
	setAttr -cb on ".bnm";
	setAttr -s 4 ".s";
select -ne :postProcessList1;
	setAttr -k on ".cch";
	setAttr -cb on ".ihi";
	setAttr -k on ".nds";
	setAttr -cb on ".bnm";
	setAttr -s 2 ".p";
select -ne :defaultRenderingList1;
select -ne :initialShadingGroup;
	setAttr -k on ".cch";
	setAttr -cb on ".ihi";
	setAttr -av -k on ".nds";
	setAttr -cb on ".bnm";
	setAttr -s 24 ".dsm";
	setAttr -k on ".mwc";
	setAttr -cb on ".an";
	setAttr -cb on ".il";
	setAttr -cb on ".vo";
	setAttr -cb on ".eo";
	setAttr -cb on ".fo";
	setAttr -cb on ".epo";
	setAttr -k on ".ro" yes;
select -ne :initialParticleSE;
	setAttr -k on ".cch";
	setAttr -cb on ".ihi";
	setAttr -av -k on ".nds";
	setAttr -cb on ".bnm";
	setAttr -k on ".mwc";
	setAttr -cb on ".an";
	setAttr -cb on ".il";
	setAttr -cb on ".vo";
	setAttr -cb on ".eo";
	setAttr -cb on ".fo";
	setAttr -cb on ".epo";
	setAttr -k on ".ro" yes;
select -ne :defaultRenderGlobals;
	setAttr ".ren" -type "string" "arnold";
select -ne :defaultResolution;
	setAttr -av -k on ".cch";
	setAttr -k on ".ihi";
	setAttr -av -k on ".nds";
	setAttr -k on ".bnm";
	setAttr -av ".w";
	setAttr -av ".h";
	setAttr -av -k on ".pa" 1;
	setAttr -av -k on ".al";
	setAttr -av ".dar";
	setAttr -av -k on ".ldar";
	setAttr -k on ".dpi";
	setAttr -av -k on ".off";
	setAttr -av -k on ".fld";
	setAttr -av -k on ".zsl";
	setAttr -k on ".isu";
	setAttr -k on ".pdu";
select -ne :defaultColorMgtGlobals;
	setAttr ".cme" no;
select -ne :hardwareRenderGlobals;
	setAttr -k on ".cch";
	setAttr -cb on ".ihi";
	setAttr -k on ".nds";
	setAttr -cb on ".bnm";
	setAttr ".ctrs" 256;
	setAttr ".btrs" 512;
	setAttr -k off ".fbfm";
	setAttr -k off -cb on ".ehql";
	setAttr -k off -cb on ".eams";
	setAttr -k off -cb on ".eeaa";
	setAttr -k off -cb on ".engm";
	setAttr -k off -cb on ".mes";
	setAttr -k off -cb on ".emb";
	setAttr -av -k off -cb on ".mbbf";
	setAttr -k off -cb on ".mbs";
	setAttr -k off -cb on ".trm";
	setAttr -k off -cb on ".tshc";
	setAttr -k off ".enpt";
	setAttr -k off -cb on ".clmt";
	setAttr -k off -cb on ".tcov";
	setAttr -k off -cb on ".lith";
	setAttr -k off -cb on ".sobc";
	setAttr -k off -cb on ".cuth";
	setAttr -k off -cb on ".hgcd";
	setAttr -k off -cb on ".hgci";
	setAttr -k off -cb on ".mgcs";
	setAttr -k off -cb on ".twa";
	setAttr -k off -cb on ".twz";
	setAttr -k on ".hwcc";
	setAttr -k on ".hwdp";
	setAttr -k on ".hwql";
	setAttr -k on ".hwfr";
	setAttr -k on ".soll";
	setAttr -k on ".sosl";
	setAttr -k on ".bswa";
	setAttr -k on ".shml";
	setAttr -k on ".hwel";
connectAttr "world_translateX2.o" "lookthroughRN.phl[11]";
connectAttr "world_translateY2.o" "lookthroughRN.phl[12]";
connectAttr "world_translateZ2.o" "lookthroughRN.phl[13]";
connectAttr "world_rotateX2.o" "lookthroughRN.phl[14]";
connectAttr "world_rotateY2.o" "lookthroughRN.phl[15]";
connectAttr "world_rotateZ2.o" "lookthroughRN.phl[16]";
connectAttr "world_translateX.o" "batmanRN.phl[1]";
connectAttr "world_translateY.o" "batmanRN.phl[2]";
connectAttr "world_translateZ.o" "batmanRN.phl[3]";
connectAttr "world_rotateY.o" "batmanRN.phl[4]";
connectAttr "world_rotateX.o" "batmanRN.phl[5]";
connectAttr "world_rotateZ.o" "batmanRN.phl[6]";
connectAttr "world_visibility.o" "batmanRN.phl[7]";
connectAttr "world_scaleX.o" "batmanRN.phl[8]";
connectAttr "world_scaleY.o" "batmanRN.phl[9]";
connectAttr "world_scaleZ.o" "batmanRN.phl[10]";
connectAttr "world_translateX1.o" "jasminRN.phl[1]";
connectAttr "world_translateY1.o" "jasminRN.phl[2]";
connectAttr "world_translateZ1.o" "jasminRN.phl[3]";
connectAttr "world_rotateX1.o" "jasminRN.phl[4]";
connectAttr "world_rotateY1.o" "jasminRN.phl[5]";
connectAttr "world_rotateZ1.o" "jasminRN.phl[6]";
connectAttr "world_visibility1.o" "jasminRN.phl[7]";
connectAttr "world_scaleX1.o" "jasminRN.phl[8]";
connectAttr "world_scaleY1.o" "jasminRN.phl[9]";
connectAttr "world_scaleZ1.o" "jasminRN.phl[10]";
// End of 1001.ma
