//Maya ASCII 2018ff09 scene
//Name: 1001.ma
//Last modified: Thu, Jun 11, 2020 12:54:43 PM
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
		2 "|lookthrough:lookthrough" "max" " -type \"string\" \"1020\""
		2 "|lookthrough:lookthrough" "latest_lookdev" " -type \"string\" \"None\""
		
		2 "|lookthrough:lookthrough|lookthrough:world" "translate" " -type \"double3\" 11.99875374884822143 2.29187808262276116 -16.08016833218534458"
		
		2 "|lookthrough:lookthrough|lookthrough:world" "translateX" " -av"
		2 "|lookthrough:lookthrough|lookthrough:world" "translateY" " -av"
		2 "|lookthrough:lookthrough|lookthrough:world" "translateZ" " -av"
		2 "|lookthrough:lookthrough|lookthrough:world" "rotate" " -type \"double3\" 1.1999999999995945 120.39999999999866986 0"
		
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
		"batmanRN" 30
		1 |batman:batman "min" "min" " -ci 1 -dt \"string\""
		1 |batman:batman "max" "max" " -ci 1 -dt \"string\""
		1 |batman:batman "latest_lookdev" "latest_lookdev" " -ci 1 -dt \"string\""
		
		2 "|batman:batman" "min" " -type \"string\" \"1001\""
		2 "|batman:batman" "max" " -type \"string\" \"1020\""
		2 "|batman:batman" "latest_lookdev" " -type \"string\" \"2.0.2\""
		2 "|batman:batman|batman:world" "visibility" " -av 1"
		2 "|batman:batman|batman:world" "translate" " -type \"double3\" -20.84567968375277047 0 6.07156009150464726"
		
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
		2 "|batman:batman|batman:world|batman:body_geo" "visibility" " -av 1"
		5 4 "batmanRN" "|batman:batman|batman:world.visibility" "batmanRN.placeHolderList[1]" 
		""
		5 4 "batmanRN" "|batman:batman|batman:world.translateX" "batmanRN.placeHolderList[2]" 
		""
		5 4 "batmanRN" "|batman:batman|batman:world.translateY" "batmanRN.placeHolderList[3]" 
		""
		5 4 "batmanRN" "|batman:batman|batman:world.translateZ" "batmanRN.placeHolderList[4]" 
		""
		5 4 "batmanRN" "|batman:batman|batman:world.rotateX" "batmanRN.placeHolderList[5]" 
		""
		5 4 "batmanRN" "|batman:batman|batman:world.rotateY" "batmanRN.placeHolderList[6]" 
		""
		5 4 "batmanRN" "|batman:batman|batman:world.rotateZ" "batmanRN.placeHolderList[7]" 
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
		2 "|jasmin:jasmin" "max" " -type \"string\" \"1020\""
		2 "|jasmin:jasmin" "latest_lookdev" " -type \"string\" \"0.0.1\""
		2 "|jasmin:jasmin|jasmin:world" "translate" " -type \"double3\" -16.39268917770279188 0 -10.25776267797571251"
		
		2 "|jasmin:jasmin|jasmin:world" "translateX" " -av"
		2 "|jasmin:jasmin|jasmin:world" "translateZ" " -av"
		2 "|jasmin:jasmin|jasmin:world" "rotate" " -type \"double3\" 0 58.61759649823003571 0"
		
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
		2 "|motorcycle:motorcycle" "max" " -type \"string\" \"1020\""
		2 "|motorcycle:motorcycle" "latest_lookdev" " -type \"string\" \"0.1.0\""
		
		2 "|motorcycle:motorcycle|motorcycle:world" "rotate" " -type \"double3\" 0 -22.75189753729842579 0";
	setAttr ".ptag" -type "string" "";
lockNode -l 1 ;
createNode reference -n "southcityRN";
	rename -uid "4A26E940-0000-4677-5EE1-08F200001062";
	setAttr ".ed" -type "dataReferenceEdits" 
		"southcityRN"
		"southcityRN" 0
		"southcityRN" 11
		1 |southcity:southcity "min" "min" " -ci 1 -dt \"string\""
		1 |southcity:southcity "max" "max" " -ci 1 -dt \"string\""
		1 |southcity:southcity "latest_lookdev" "latest_lookdev" " -ci 1 -dt \"string\""
		
		2 "|southcity:southcity" "min" " -type \"string\" \"1001\""
		2 "|southcity:southcity" "max" " -type \"string\" \"1020\""
		2 "|southcity:southcity" "latest_lookdev" " -type \"string\" \"0.1.0\""
		2 "|southcity:southcity|southcity:world" "rotate" " -type \"double3\" 0 0 0"
		
		2 "|southcity:southcity|southcity:world|southcity:geometry|southcity:building_1_ctrl" 
		"translate" " -type \"double3\" -26.60599199648075341 0 -14.77946005342071167"
		2 "|southcity:southcity|southcity:world|southcity:geometry|southcity:building_2_ctrl" 
		"translate" " -type \"double3\" 27.71786014211598825 0 -21.3415522575378418"
		2 "|southcity:southcity|southcity:world|southcity:geometry|southcity:building_3_ctrl" 
		"translate" " -type \"double3\" -17.36419677734375 0 21.55198734411902706"
		2 "|southcity:southcity|southcity:world|southcity:geometry|southcity:building_4_ctrl" 
		"translate" " -type \"double3\" 23.68547630310058594 0 9.63313651084899902";
lockNode -l 1 ;
createNode animCurveTL -n "world_translateX2";
	rename -uid "5CC52940-0000-4B3C-5ED4-17C700000618";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  1001 11.998753748848221 1020 11.998753748848221;
createNode animCurveTL -n "world_translateY2";
	rename -uid "5CC52940-0000-4B3C-5ED4-17C700000619";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  1001 2.2918780826227612 1020 2.2918780826227612;
createNode animCurveTL -n "world_translateZ2";
	rename -uid "5CC52940-0000-4B3C-5ED4-17C70000061A";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  1001 -16.080168332185345 1020 -16.080168332185345;
createNode animCurveTA -n "world_rotateX2";
	rename -uid "5CC52940-0000-4B3C-5ED4-17C70000061B";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  1001 1.1999999999995945 1020 1.1999999999995945;
createNode animCurveTA -n "world_rotateY2";
	rename -uid "5CC52940-0000-4B3C-5ED4-17C70000061C";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  1001 120.39999999999867 1020 135;
createNode animCurveTA -n "world_rotateZ2";
	rename -uid "5CC52940-0000-4B3C-5ED4-17C70000061D";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  1001 0 1020 0;
createNode animCurveTU -n "world_visibility3";
	rename -uid "5CC52940-0000-4B3C-5ED4-1741000005F7";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  1001 1 1020 1;
	setAttr -s 2 ".kot[0:1]"  5 5;
createNode animCurveTL -n "world_translateX1";
	rename -uid "5CC52940-0000-4B3C-5ED4-1741000005F4";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  1001 -20.84567968375277 1020 -3.5282577368014456;
createNode animCurveTL -n "world_translateY1";
	rename -uid "5CC52940-0000-4B3C-5ED4-1741000005F5";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  1001 0 1020 0;
createNode animCurveTL -n "world_translateZ1";
	rename -uid "5CC52940-0000-4B3C-5ED4-1741000005F6";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  1001 6.0715600915046473 1020 1.3164572506579657;
createNode animCurveTA -n "world_rotateX1";
	rename -uid "5CC52940-0000-4B3C-5ED4-1741000005F8";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  1001 0 1020 0;
createNode animCurveTA -n "world_rotateY1";
	rename -uid "5CC52940-0000-4B3C-5ED4-1741000005F9";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  1001 105.35413841516538 1020 105.35413841516538;
createNode animCurveTA -n "world_rotateZ1";
	rename -uid "5CC52940-0000-4B3C-5ED4-1741000005FA";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  1001 0 1020 0;
createNode animCurveTU -n "world_scaleX3";
	rename -uid "5CC52940-0000-4B3C-5ED4-1741000005FB";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  1001 1 1020 1;
createNode animCurveTU -n "world_scaleY3";
	rename -uid "5CC52940-0000-4B3C-5ED4-1741000005FC";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  1001 1 1020 1;
createNode animCurveTU -n "world_scaleZ3";
	rename -uid "5CC52940-0000-4B3C-5ED4-1741000005FD";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  1001 1 1020 1;
createNode animCurveTL -n "world_translateX";
	rename -uid "5CC52940-0000-4B3C-5ED4-172B000005D9";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  1001 -16.392689177702792 1020 -2.6959068521333887;
createNode animCurveTL -n "world_translateY";
	rename -uid "5CC52940-0000-4B3C-5ED4-172B000005DA";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  1001 0 1020 0;
createNode animCurveTL -n "world_translateZ";
	rename -uid "5CC52940-0000-4B3C-5ED4-172B000005DB";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  1001 -10.257762677975713 1020 -1.9029837797821523;
createNode animCurveTA -n "world_rotateX";
	rename -uid "5CC52940-0000-4B3C-5ED4-172B000005DD";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  1001 0 1020 0;
createNode animCurveTA -n "world_rotateY";
	rename -uid "5CC52940-0000-4B3C-5ED4-172B000005DE";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  1001 58.617596498230036 1020 58.617596498230036;
createNode animCurveTA -n "world_rotateZ";
	rename -uid "5CC52940-0000-4B3C-5ED4-172B000005DF";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  1001 0 1020 0;
createNode animCurveTU -n "world_visibility";
	rename -uid "5CC52940-0000-4B3C-5ED4-172B000005DC";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  1001 1 1020 1;
	setAttr -s 2 ".kot[0:1]"  5 5;
createNode animCurveTU -n "world_scaleX";
	rename -uid "5CC52940-0000-4B3C-5ED4-172B000005E0";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  1001 1 1020 1;
createNode animCurveTU -n "world_scaleY";
	rename -uid "5CC52940-0000-4B3C-5ED4-172B000005E1";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  1001 1 1020 1;
createNode animCurveTU -n "world_scaleZ";
	rename -uid "5CC52940-0000-4B3C-5ED4-172B000005E2";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  1001 1 1020 1;
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
connectAttr "world_translateX2.o" "lookthroughRN.phl[1]";
connectAttr "world_translateY2.o" "lookthroughRN.phl[2]";
connectAttr "world_translateZ2.o" "lookthroughRN.phl[3]";
connectAttr "world_rotateX2.o" "lookthroughRN.phl[4]";
connectAttr "world_rotateY2.o" "lookthroughRN.phl[5]";
connectAttr "world_rotateZ2.o" "lookthroughRN.phl[6]";
connectAttr "world_visibility3.o" "batmanRN.phl[1]";
connectAttr "world_translateX1.o" "batmanRN.phl[2]";
connectAttr "world_translateY1.o" "batmanRN.phl[3]";
connectAttr "world_translateZ1.o" "batmanRN.phl[4]";
connectAttr "world_rotateX1.o" "batmanRN.phl[5]";
connectAttr "world_rotateY1.o" "batmanRN.phl[6]";
connectAttr "world_rotateZ1.o" "batmanRN.phl[7]";
connectAttr "world_scaleX3.o" "batmanRN.phl[8]";
connectAttr "world_scaleY3.o" "batmanRN.phl[9]";
connectAttr "world_scaleZ3.o" "batmanRN.phl[10]";
connectAttr "world_translateX.o" "jasminRN.phl[1]";
connectAttr "world_translateY.o" "jasminRN.phl[2]";
connectAttr "world_translateZ.o" "jasminRN.phl[3]";
connectAttr "world_rotateX.o" "jasminRN.phl[4]";
connectAttr "world_rotateY.o" "jasminRN.phl[5]";
connectAttr "world_rotateZ.o" "jasminRN.phl[6]";
connectAttr "world_visibility.o" "jasminRN.phl[7]";
connectAttr "world_scaleX.o" "jasminRN.phl[8]";
connectAttr "world_scaleY.o" "jasminRN.phl[9]";
connectAttr "world_scaleZ.o" "jasminRN.phl[10]";
// End of 1001.ma
