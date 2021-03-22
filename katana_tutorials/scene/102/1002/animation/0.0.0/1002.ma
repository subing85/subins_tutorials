//Maya ASCII 2018ff09 scene
//Name: 1002.ma
//Last modified: Thu, Jun 11, 2020 12:55:58 PM
//Codeset: UTF-8
file -rdi 1 -ns "lookthrough" -rfn "lookthroughRN" -op "v=0;" -typ "mayaAscii"
		 "/venture/shows/katana_tutorials//asset/camera/lookthrough/puppet/0.0.0/lookthrough.ma";
file -rdi 1 -ns "batman" -rfn "batmanRN" -op "v=0;" -typ "mayaAscii" "/venture/shows/katana_tutorials//asset/character/batman/puppet/0.0.2/batman.ma";
file -rdi 1 -ns "jasmin" -rfn "jasminRN" -op "v=0;" -typ "mayaAscii" "/venture/shows/katana_tutorials//asset/character/jasmin/puppet//0.1.0/jasmin.ma";
file -rdi 1 -ns "motorcycle" -rfn "motorcycleRN" -op "v=0;" -typ "mayaAscii"
		 "/venture/shows/katana_tutorials//asset/prop/motorcycle/puppet/0.0.0/motorcycle.ma";
file -rdi 1 -ns "southcity" -rfn "southcityRN" -op "v=0;" -typ "mayaAscii" "/venture/shows/katana_tutorials//asset/set/southcity/puppet/0.0.1/southcity.ma";
file -r -ns "lookthrough" -dr 1 -rfn "lookthroughRN" -op "v=0;" -typ "mayaAscii"
		 "/venture/shows/katana_tutorials//asset/camera/lookthrough/puppet/0.0.0/lookthrough.ma";
file -r -ns "batman" -dr 1 -rfn "batmanRN" -op "v=0;" -typ "mayaAscii" "/venture/shows/katana_tutorials//asset/character/batman/puppet/0.0.2/batman.ma";
file -r -ns "jasmin" -dr 1 -rfn "jasminRN" -op "v=0;" -typ "mayaAscii" "/venture/shows/katana_tutorials//asset/character/jasmin/puppet//0.1.0/jasmin.ma";
file -r -ns "motorcycle" -dr 1 -rfn "motorcycleRN" -op "v=0;" -typ "mayaAscii" "/venture/shows/katana_tutorials//asset/prop/motorcycle/puppet/0.0.0/motorcycle.ma";
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
	setAttr ".phl[1]" 0;
	setAttr ".phl[2]" 0;
	setAttr ".phl[3]" 0;
	setAttr ".phl[4]" 0;
	setAttr ".phl[5]" 0;
	setAttr ".phl[6]" 0;
	setAttr ".ed" -type "dataReferenceEdits" 
		"lookthroughRN"
		"lookthroughRN" 2
		2 "|lookthrough:lookthrough|lookthrough:world" "visibility" " 1"
		2 "|lookthrough:lookthrough|lookthrough:world" "scale" " -type \"double3\" 1 1 1"
		
		"lookthroughRN" 25
		1 |lookthrough:lookthrough "min" "min" " -ci 1 -dt \"string\""
		1 |lookthrough:lookthrough "max" "max" " -ci 1 -dt \"string\""
		1 |lookthrough:lookthrough "latest_lookdev" "latest_lookdev" " -ci 1 -dt \"string\""
		
		2 "|lookthrough:lookthrough" "min" " -type \"string\" \"1001\""
		2 "|lookthrough:lookthrough" "max" " -type \"string\" \"1025\""
		2 "|lookthrough:lookthrough" "latest_lookdev" " -type \"string\" \"None\""
		
		2 "|lookthrough:lookthrough|lookthrough:world" "translate" " -type \"double3\" 6.82333738241549437 4.05396370144347884 -5.18339756370333493"
		
		2 "|lookthrough:lookthrough|lookthrough:world" "translateX" " -av"
		2 "|lookthrough:lookthrough|lookthrough:world" "translateY" " -av"
		2 "|lookthrough:lookthrough|lookthrough:world" "translateZ" " -av"
		2 "|lookthrough:lookthrough|lookthrough:world" "rotate" " -type \"double3\" 1.79999999999937921 123.39999999999984936 0"
		
		2 "|lookthrough:lookthrough|lookthrough:world" "rotateX" " -av"
		2 "|lookthrough:lookthrough|lookthrough:world" "rotateY" " -av"
		2 "|lookthrough:lookthrough|lookthrough:world|lookthrough:camera" "rotatePivot" 
		" -type \"double3\" 0 0 0"
		2 "|lookthrough:lookthrough|lookthrough:world|lookthrough:camera|lookthrough:cameraShape" 
		"overscan" " 1.3"
		2 "|lookthrough:lookthrough|lookthrough:world|lookthrough:camera|lookthrough:cameraShape" 
		"centerOfInterest" " 65.04100370707635648"
		2 "|lookthrough:lookthrough|lookthrough:world|lookthrough:camera|lookthrough:cameraShape" 
		"displayFilmGate" " 0"
		2 "|lookthrough:lookthrough|lookthrough:world|lookthrough:camera|lookthrough:cameraShape" 
		"displayResolution" " 1"
		4 "|lookthrough:lookthrough" "shader" ""
		5 4 "lookthroughRN" "|lookthrough:lookthrough|lookthrough:world.translateX" 
		"lookthroughRN.placeHolderList[1]" ""
		5 4 "lookthroughRN" "|lookthrough:lookthrough|lookthrough:world.translateY" 
		"lookthroughRN.placeHolderList[2]" ""
		5 4 "lookthroughRN" "|lookthrough:lookthrough|lookthrough:world.translateZ" 
		"lookthroughRN.placeHolderList[3]" ""
		5 4 "lookthroughRN" "|lookthrough:lookthrough|lookthrough:world.rotateX" 
		"lookthroughRN.placeHolderList[4]" ""
		5 4 "lookthroughRN" "|lookthrough:lookthrough|lookthrough:world.rotateY" 
		"lookthroughRN.placeHolderList[5]" ""
		5 4 "lookthroughRN" "|lookthrough:lookthrough|lookthrough:world.rotateZ" 
		"lookthroughRN.placeHolderList[6]" "";
	setAttr ".ptag" -type "string" "";
lockNode -l 1 ;
createNode reference -n "batmanRN";
	rename -uid "5CC52940-0000-4B3C-5ED4-12D90000032A";
	setAttr ".ed" -type "dataReferenceEdits" 
		"batmanRN"
		"batmanRN" 0
		"batmanRN" 20
		1 |batman:batman "min" "min" " -ci 1 -dt \"string\""
		1 |batman:batman "max" "max" " -ci 1 -dt \"string\""
		1 |batman:batman "latest_lookdev" "latest_lookdev" " -ci 1 -dt \"string\""
		
		2 "|batman:batman" "min" " -type \"string\" \"1001\""
		2 "|batman:batman" "max" " -type \"string\" \"1025\""
		2 "|batman:batman" "latest_lookdev" " -type \"string\" \"2.0.2\""
		2 "|batman:batman|batman:world" "visibility" " -av 1"
		2 "|batman:batman|batman:world" "translate" " -type \"double3\" -3.52825773680144561 0 1.31645725065796571"
		
		2 "|batman:batman|batman:world" "translateX" " -av"
		2 "|batman:batman|batman:world" "translateY" " -av"
		2 "|batman:batman|batman:world" "translateZ" " -av"
		2 "|batman:batman|batman:world" "rotate" " -type \"double3\" 0 105.35413841516538014 0"
		
		2 "|batman:batman|batman:world" "rotateX" " -av"
		2 "|batman:batman|batman:world" "rotateY" " -av"
		2 "|batman:batman|batman:world" "rotateZ" " -av"
		2 "|batman:batman|batman:world" "scale" " -type \"double3\" 1 1 1"
		2 "|batman:batman|batman:world" "scaleX" " -av"
		2 "|batman:batman|batman:world" "scaleY" " -av"
		2 "|batman:batman|batman:world" "scaleZ" " -av"
		2 "|batman:batman|batman:world|batman:body_geo" "visibility" " -av 1";
	setAttr ".ptag" -type "string" "";
lockNode -l 1 ;
createNode reference -n "jasminRN";
	rename -uid "5CC52940-0000-4B3C-5ED4-12E100000340";
	setAttr ".ed" -type "dataReferenceEdits" 
		"jasminRN"
		"jasminRN" 0
		"jasminRN" 13
		1 |jasmin:jasmin "min" "min" " -ci 1 -dt \"string\""
		1 |jasmin:jasmin "max" "max" " -ci 1 -dt \"string\""
		1 |jasmin:jasmin "latest_lookdev" "latest_lookdev" " -ci 1 -dt \"string\""
		
		2 "|jasmin:jasmin" "min" " -type \"string\" \"1001\""
		2 "|jasmin:jasmin" "max" " -type \"string\" \"1025\""
		2 "|jasmin:jasmin" "latest_lookdev" " -type \"string\" \"0.0.1\""
		2 "|jasmin:jasmin|jasmin:world" "visibility" " 1"
		2 "|jasmin:jasmin|jasmin:world" "translate" " -type \"double3\" -2.69590685213338865 0 -1.90298377978215227"
		
		2 "|jasmin:jasmin|jasmin:world" "translateX" " -av"
		2 "|jasmin:jasmin|jasmin:world" "translateZ" " -av"
		2 "|jasmin:jasmin|jasmin:world" "rotate" " -type \"double3\" 0 58.61759649823003571 0"
		
		2 "|jasmin:jasmin|jasmin:world" "rotateY" " -av"
		2 "|jasmin:jasmin|jasmin:world" "scale" " -type \"double3\" 1 1 1";
	setAttr ".ptag" -type "string" "";
lockNode -l 1 ;
createNode reference -n "motorcycleRN";
	rename -uid "5CC52940-0000-4B3C-5ED4-15A300000413";
	setAttr ".ed" -type "dataReferenceEdits" 
		"motorcycleRN"
		"motorcycleRN" 0
		"motorcycleRN" 7
		1 |motorcycle:motorcycle "min" "min" " -ci 1 -dt \"string\""
		1 |motorcycle:motorcycle "max" "max" " -ci 1 -dt \"string\""
		1 |motorcycle:motorcycle "latest_lookdev" "latest_lookdev" " -ci 1 -dt \"string\""
		
		2 "|motorcycle:motorcycle" "min" " -type \"string\" \"1001\""
		2 "|motorcycle:motorcycle" "max" " -type \"string\" \"1025\""
		2 "|motorcycle:motorcycle" "latest_lookdev" " -type \"string\" \"0.1.0\""
		
		2 "|motorcycle:motorcycle|motorcycle:world" "rotate" " -type \"double3\" 0 -22.75189753729842579 0";
	setAttr ".ptag" -type "string" "";
lockNode -l 1 ;
createNode reference -n "southcityRN";
	rename -uid "4A26E940-0000-4677-5EE1-0B00000012F8";
	setAttr ".ed" -type "dataReferenceEdits" 
		"southcityRN"
		"southcityRN" 0
		"southcityRN" 6
		1 |southcity:southcity "min" "min" " -ci 1 -dt \"string\""
		1 |southcity:southcity "max" "max" " -ci 1 -dt \"string\""
		1 |southcity:southcity "latest_lookdev" "latest_lookdev" " -ci 1 -dt \"string\""
		
		2 "|southcity:southcity" "min" " -type \"string\" \"1001\""
		2 "|southcity:southcity" "max" " -type \"string\" \"1025\""
		2 "|southcity:southcity" "latest_lookdev" " -type \"string\" \"0.1.0\"";
lockNode -l 1 ;
createNode animCurveTL -n "world_translateX";
	rename -uid "5CC52940-0000-4B3C-5ED4-185B0000062C";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  1001 6.8233373824154944;
createNode animCurveTL -n "world_translateY";
	rename -uid "5CC52940-0000-4B3C-5ED4-185B0000062D";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  1001 4.0539637014434788;
createNode animCurveTL -n "world_translateZ";
	rename -uid "5CC52940-0000-4B3C-5ED4-185B0000062E";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  1001 -5.1833975637033349;
createNode animCurveTA -n "world_rotateX";
	rename -uid "5CC52940-0000-4B3C-5ED4-185B0000062F";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  1001 1.7999999999993792;
createNode animCurveTA -n "world_rotateY";
	rename -uid "5CC52940-0000-4B3C-5ED4-185B00000630";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  1001 123.39999999999985;
createNode animCurveTA -n "world_rotateZ";
	rename -uid "5CC52940-0000-4B3C-5ED4-185B00000631";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  1001 0;
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
	setAttr -s 27 ".dsm";
	setAttr -k on ".mwc";
	setAttr -cb on ".an";
	setAttr -cb on ".il";
	setAttr -cb on ".vo";
	setAttr -cb on ".eo";
	setAttr -cb on ".fo";
	setAttr -cb on ".epo";
	setAttr -k on ".ro" yes;
	setAttr -s 3 ".gn";
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
connectAttr "world_translateX.o" "lookthroughRN.phl[1]";
connectAttr "world_translateY.o" "lookthroughRN.phl[2]";
connectAttr "world_translateZ.o" "lookthroughRN.phl[3]";
connectAttr "world_rotateX.o" "lookthroughRN.phl[4]";
connectAttr "world_rotateY.o" "lookthroughRN.phl[5]";
connectAttr "world_rotateZ.o" "lookthroughRN.phl[6]";
// End of 1002.ma
