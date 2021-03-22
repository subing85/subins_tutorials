//Maya ASCII 2018ff09 scene
//Name: 1003.ma
//Last modified: Thu, Jun 11, 2020 12:57:12 PM
//Codeset: UTF-8
file -rdi 1 -ns "lookthrough" -rfn "lookthroughRN" -op "v=0;" -typ "mayaAscii"
		 "/venture/shows/katana_tutorials//asset/camera/lookthrough/puppet/0.0.0/lookthrough.ma";
file -rdi 1 -ns "batman" -rfn "batmanRN" -op "v=0;" -typ "mayaAscii" "/venture/shows/katana_tutorials//asset/character/batman/puppet/2.1.0/batman.ma";
file -rdi 1 -ns "jasmin" -rfn "jasminRN" -op "v=0;" -typ "mayaAscii" "/venture/shows/katana_tutorials//asset/character/jasmin/puppet//0.1.0/jasmin.ma";
file -rdi 1 -ns "motorcycle" -rfn "motorcycleRN" -op "v=0;" -typ "mayaAscii"
		 "/venture/shows/katana_tutorials//asset/prop/motorcycle/puppet/0.0.0/motorcycle.ma";
file -rdi 1 -ns "southcity" -rfn "southcityRN" -op "v=0;" -typ "mayaAscii" "/venture/shows/katana_tutorials//asset/set/southcity/puppet/0.0.1/southcity.ma";
file -r -ns "lookthrough" -dr 1 -rfn "lookthroughRN" -op "v=0;" -typ "mayaAscii"
		 "/venture/shows/katana_tutorials//asset/camera/lookthrough/puppet/0.0.0/lookthrough.ma";
file -r -ns "batman" -dr 1 -rfn "batmanRN" -op "v=0;" -typ "mayaAscii" "/venture/shows/katana_tutorials//asset/character/batman/puppet/2.1.0/batman.ma";
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
createNode fosterParent -n "batmanRNfosterParent1";
	rename -uid "FF350940-0000-4E35-5EE2-626600000C06";
createNode parentConstraint -n "world_parentConstraint1" -p "batmanRNfosterParent1";
	rename -uid "5CC52940-0000-4B3C-5ED4-198600000C9E";
	addAttr -dcb 0 -ci true -k true -sn "w0" -ln "worldW0" -dv 1 -min 0 -at "double";
	setAttr -k on ".nds";
	setAttr -k off ".v";
	setAttr -k off ".tx";
	setAttr -k off ".ty";
	setAttr -k off ".tz";
	setAttr -k off ".rx";
	setAttr -k off ".ry";
	setAttr -k off ".rz";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".erp" yes;
	setAttr ".tg[0].tot" -type "double3" 0.83946657005604919 1.3539444709729931 -2.114483054615552 ;
	setAttr ".tg[0].tor" -type "double3" 0 3.4467990919685039 0 ;
	setAttr ".lr" -type "double3" 0 -19.305098445329918 0 ;
	setAttr ".rst" -type "double3" 1.5919044898325796 1.3539444709729931 -1.6252946827418275 ;
	setAttr ".rsrr" -type "double3" 0 -19.305098445329918 0 ;
	setAttr -k on ".w0";
createNode fosterParent -n "jasminRNfosterParent1";
	rename -uid "FF350940-0000-4E35-5EE2-626700000C07";
createNode parentConstraint -n "world_parentConstraint2" -p "jasminRNfosterParent1";
	rename -uid "5CC52940-0000-4B3C-5ED4-198D00000CA3";
	addAttr -dcb 0 -ci true -k true -sn "w0" -ln "worldW0" -dv 1 -min 0 -at "double";
	setAttr -k on ".nds";
	setAttr -k off ".v";
	setAttr -k off ".tx";
	setAttr -k off ".ty";
	setAttr -k off ".tz";
	setAttr -k off ".rx";
	setAttr -k off ".ry";
	setAttr -k off ".rz";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".erp" yes;
	setAttr ".tg[0].tot" -type "double3" 0.88513552024813213 1.0306677720882036 -0.20493443560826655 ;
	setAttr ".tg[0].tor" -type "double3" 0 18.387662857015631 0 ;
	setAttr ".lr" -type "double3" 0 -4.3642346802827952 0 ;
	setAttr ".rst" -type "double3" 0.89551815194808604 1.0306677720882036 0.15333053066657967 ;
	setAttr ".rsrr" -type "double3" 0 -4.3642346802827952 0 ;
	setAttr -k on ".w0";
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
		
		2 "|lookthrough:lookthrough|lookthrough:world" "translate" " -type \"double3\" 3.92888797200439477 1.16148144225701078 -2.04762438010679393"
		
		2 "|lookthrough:lookthrough|lookthrough:world" "translateX" " -av"
		2 "|lookthrough:lookthrough|lookthrough:world" "translateY" " -av"
		2 "|lookthrough:lookthrough|lookthrough:world" "translateZ" " -av"
		2 "|lookthrough:lookthrough|lookthrough:world" "rotate" " -type \"double3\" 6.8616472703974809 123.79999999999962768 0"
		
		2 "|lookthrough:lookthrough|lookthrough:world" "rotateX" " -av"
		2 "|lookthrough:lookthrough|lookthrough:world" "rotateY" " -av"
		2 "|lookthrough:lookthrough|lookthrough:world" "rotateZ" " -av"
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
	setAttr -s 2 ".fn";
	setAttr ".fn[0]" -type "string" "/venture/shows/katana_tutorials//asset/character/batman/puppet/0.0.2/batman.ma";
	setAttr ".fn[1]" -type "string" "/venture/shows/katana_tutorials//assets/character/batman/0.0.0/batman.ma";
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
		"batmanRN" 49
		0 "|batmanRNfosterParent1|world_parentConstraint1" "|batman:batman|batman:world" 
		"-s -r "
		1 |batman:batman "min" "min" " -ci 1 -dt \"string\""
		1 |batman:batman "max" "max" " -ci 1 -dt \"string\""
		1 |batman:batman "latest_lookdev" "latest_lookdev" " -ci 1 -dt \"string\""
		
		2 "|batman:batman" "min" " -type \"string\" \"1001\""
		2 "|batman:batman" "max" " -type \"string\" \"1025\""
		2 "|batman:batman" "latest_lookdev" " -type \"string\" \"2.0.1\""
		2 "|batman:batman|batman:world" "visibility" " -av 1"
		2 "|batman:batman|batman:world" "translate" " -type \"double3\" 1.59190448983257959 1.35394447097299309 -1.62529468274182753"
		
		2 "|batman:batman|batman:world" "translateX" " -av"
		2 "|batman:batman|batman:world" "translateY" " -av"
		2 "|batman:batman|batman:world" "translateZ" " -av"
		2 "|batman:batman|batman:world" "rotate" " -type \"double3\" 0 -19.30509844532991792 0"
		
		2 "|batman:batman|batman:world" "rotateX" " -av"
		2 "|batman:batman|batman:world" "rotateY" " -av"
		2 "|batman:batman|batman:world" "rotateZ" " -av"
		2 "|batman:batman|batman:world" "scale" " -type \"double3\" 1 1 1"
		2 "|batman:batman|batman:world" "scaleX" " -av"
		2 "|batman:batman|batman:world" "scaleY" " -av"
		2 "|batman:batman|batman:world" "scaleZ" " -av"
		2 "|batman:batman|batman:world|batman:face_geo|batman:face_geoShape" "dispResolution" 
		" 1"
		2 "|batman:batman|batman:world|batman:face_geo|batman:face_geoShape" "displaySmoothMesh" 
		" 0"
		2 "|batman:batman|batman:world|batman:body_geo" "visibility" " -av 1"
		2 "|batman:batman|batman:world|batman:body_geo|batman:body_geoShape" "dispResolution" 
		" 1"
		2 "|batman:batman|batman:world|batman:body_geo|batman:body_geoShape" "displaySmoothMesh" 
		" 0"
		2 "|batman:batman|batman:world|batman:bat_logo_geo|batman:bat_logo_geoShape" 
		"dispResolution" " 1"
		2 "|batman:batman|batman:world|batman:bat_logo_geo|batman:bat_logo_geoShape" 
		"displaySmoothMesh" " 0"
		2 "|batman:batman|batman:world|batman:boot_geo|batman:boot_geoShape" "dispResolution" 
		" 1"
		2 "|batman:batman|batman:world|batman:boot_geo|batman:boot_geoShape" "displaySmoothMesh" 
		" 0"
		2 "|batman:batman|batman:world|batman:hand_geo|batman:hand_geoShape" "dispResolution" 
		" 1"
		2 "|batman:batman|batman:world|batman:hand_geo|batman:hand_geoShape" "displaySmoothMesh" 
		" 0"
		2 "|batman:batman|batman:world|batman:belt_geo|batman:belt_geoShape" "dispResolution" 
		" 1"
		2 "|batman:batman|batman:world|batman:belt_geo|batman:belt_geoShape" "displaySmoothMesh" 
		" 0"
		2 "|batman:batman|batman:world|batman:eye_geo|batman:eye_geoShape" "dispResolution" 
		" 1"
		2 "|batman:batman|batman:world|batman:eye_geo|batman:eye_geoShape" "displaySmoothMesh" 
		" 0"
		2 "|batman:batman|batman:world|batman:teeth_geo|batman:teeth_geoShape" "dispResolution" 
		" 1"
		2 "|batman:batman|batman:world|batman:teeth_geo|batman:teeth_geoShape" "displaySmoothMesh" 
		" 0"
		2 "|batman:batman|batman:world|batman:tounge_geo|batman:tounge_geoShape" 
		"dispResolution" " 1"
		2 "|batman:batman|batman:world|batman:tounge_geo|batman:tounge_geoShape" 
		"displaySmoothMesh" " 0"
		5 4 "batmanRN" "|batman:batman|batman:world.translateX" "batmanRN.placeHolderList[1]" 
		""
		5 4 "batmanRN" "|batman:batman|batman:world.translateY" "batmanRN.placeHolderList[2]" 
		""
		5 4 "batmanRN" "|batman:batman|batman:world.translateZ" "batmanRN.placeHolderList[3]" 
		""
		5 4 "batmanRN" "|batman:batman|batman:world.rotateX" "batmanRN.placeHolderList[4]" 
		""
		5 4 "batmanRN" "|batman:batman|batman:world.rotateY" "batmanRN.placeHolderList[5]" 
		""
		5 4 "batmanRN" "|batman:batman|batman:world.rotateZ" "batmanRN.placeHolderList[6]" 
		""
		5 3 "batmanRN" "|batman:batman|batman:world.rotateOrder" "batmanRN.placeHolderList[7]" 
		""
		5 3 "batmanRN" "|batman:batman|batman:world.parentInverseMatrix" "batmanRN.placeHolderList[8]" 
		""
		5 3 "batmanRN" "|batman:batman|batman:world.rotatePivot" "batmanRN.placeHolderList[9]" 
		""
		5 3 "batmanRN" "|batman:batman|batman:world.rotatePivotTranslate" "batmanRN.placeHolderList[10]" 
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
		"jasminRN" 28
		2 "|jasmin:jasmin|jasmin:world|jasmin:Jasmine_body|jasmin:Jasmine_bodyShape" 
		"dispResolution" " 1"
		2 "|jasmin:jasmin|jasmin:world|jasmin:Jasmine_body|jasmin:Jasmine_bodyShape" 
		"displaySmoothMesh" " 0"
		2 "|jasmin:jasmin|jasmin:world|jasmin:blendShape9|jasmin:blendShape9Shape" 
		"dispResolution" " 1"
		2 "|jasmin:jasmin|jasmin:world|jasmin:blendShape9|jasmin:blendShape9Shape" 
		"displaySmoothMesh" " 0"
		2 "|jasmin:jasmin|jasmin:world|jasmin:Jasmine_HairBuckles|jasmin:Jasmine_HairBucklesShape" 
		"dispResolution" " 1"
		2 "|jasmin:jasmin|jasmin:world|jasmin:Jasmine_HairBuckles|jasmin:Jasmine_HairBucklesShape" 
		"displaySmoothMesh" " 0"
		2 "|jasmin:jasmin|jasmin:world|jasmin:Jasmine_Shoes|jasmin:Jasmine_ShoesShape" 
		"dispResolution" " 1"
		2 "|jasmin:jasmin|jasmin:world|jasmin:Jasmine_Shoes|jasmin:Jasmine_ShoesShape" 
		"displaySmoothMesh" " 0"
		2 "|jasmin:jasmin|jasmin:world|jasmin:Jasmine_tshirt|jasmin:Jasmine_tshirtShape" 
		"dispResolution" " 1"
		2 "|jasmin:jasmin|jasmin:world|jasmin:Jasmine_tshirt|jasmin:Jasmine_tshirtShape" 
		"displaySmoothMesh" " 0"
		2 "|jasmin:jasmin|jasmin:world|jasmin:Jasmine_short|jasmin:Jasmine_shortShape" 
		"dispResolution" " 1"
		2 "|jasmin:jasmin|jasmin:world|jasmin:Jasmine_short|jasmin:Jasmine_shortShape" 
		"displaySmoothMesh" " 0"
		2 "|jasmin:jasmin|jasmin:world|jasmin:Jasmine_socks|jasmin:Jasmine_socksShape" 
		"dispResolution" " 1"
		2 "|jasmin:jasmin|jasmin:world|jasmin:Jasmine_socks|jasmin:Jasmine_socksShape" 
		"displaySmoothMesh" " 0"
		2 "|jasmin:jasmin|jasmin:world|jasmin:Jasmine_Tongue|jasmin:Jasmine_TongueShape" 
		"dispResolution" " 1"
		2 "|jasmin:jasmin|jasmin:world|jasmin:Jasmine_Tongue|jasmin:Jasmine_TongueShape" 
		"displaySmoothMesh" " 0"
		2 "|jasmin:jasmin|jasmin:world|jasmin:Head_Hair|jasmin:Head_HairShape" "dispResolution" 
		" 1"
		2 "|jasmin:jasmin|jasmin:world|jasmin:Head_Hair|jasmin:Head_HairShape" "displaySmoothMesh" 
		" 0"
		2 "|jasmin:jasmin|jasmin:world|jasmin:Jasmine_LoTeeth|jasmin:Jasmine_LoTeethShape" 
		"dispResolution" " 1"
		2 "|jasmin:jasmin|jasmin:world|jasmin:Jasmine_LoTeeth|jasmin:Jasmine_LoTeethShape" 
		"displaySmoothMesh" " 0"
		2 "|jasmin:jasmin|jasmin:world|jasmin:Jasmine_UpTeeth|jasmin:Jasmine_UpTeethShape" 
		"dispResolution" " 1"
		2 "|jasmin:jasmin|jasmin:world|jasmin:Jasmine_UpTeeth|jasmin:Jasmine_UpTeethShape" 
		"displaySmoothMesh" " 0"
		2 "|jasmin:jasmin|jasmin:world|jasmin:Jasmine_Lt_Eye|jasmin:Jasmine_Lt_EyeShape" 
		"dispResolution" " 1"
		2 "|jasmin:jasmin|jasmin:world|jasmin:Jasmine_Lt_Eye|jasmin:Jasmine_Lt_EyeShape" 
		"displaySmoothMesh" " 0"
		2 "|jasmin:jasmin|jasmin:world|jasmin:Braid|jasmin:BraidShape" "dispResolution" 
		" 1"
		2 "|jasmin:jasmin|jasmin:world|jasmin:Braid|jasmin:BraidShape" "displaySmoothMesh" 
		" 0"
		2 "|jasmin:jasmin|jasmin:world|jasmin:Jasmine_Rt_Eye|jasmin:Jasmine_Rt_EyeShape" 
		"dispResolution" " 1"
		2 "|jasmin:jasmin|jasmin:world|jasmin:Jasmine_Rt_Eye|jasmin:Jasmine_Rt_EyeShape" 
		"displaySmoothMesh" " 0"
		"jasminRN" 24
		0 "|jasminRNfosterParent1|world_parentConstraint2" "|jasmin:jasmin|jasmin:world" 
		"-s -r "
		1 |jasmin:jasmin "min" "min" " -ci 1 -dt \"string\""
		1 |jasmin:jasmin "max" "max" " -ci 1 -dt \"string\""
		1 |jasmin:jasmin "latest_lookdev" "latest_lookdev" " -ci 1 -dt \"string\""
		
		2 "|jasmin:jasmin" "min" " -type \"string\" \"1001\""
		2 "|jasmin:jasmin" "max" " -type \"string\" \"1025\""
		2 "|jasmin:jasmin" "latest_lookdev" " -type \"string\" \"0.0.1\""
		2 "|jasmin:jasmin|jasmin:world" "visibility" " 1"
		2 "|jasmin:jasmin|jasmin:world" "translate" " -type \"double3\" 0.89551815194808604 1.03066777208820359 0.15333053066657967"
		
		2 "|jasmin:jasmin|jasmin:world" "translateX" " -av"
		2 "|jasmin:jasmin|jasmin:world" "translateZ" " -av"
		2 "|jasmin:jasmin|jasmin:world" "rotate" " -type \"double3\" 0 -4.36423468028279515 0"
		
		2 "|jasmin:jasmin|jasmin:world" "rotateY" " -av"
		2 "|jasmin:jasmin|jasmin:world" "scale" " -type \"double3\" 1 1 1"
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
		5 3 "jasminRN" "|jasmin:jasmin|jasmin:world.rotateOrder" "jasminRN.placeHolderList[7]" 
		""
		5 3 "jasminRN" "|jasmin:jasmin|jasmin:world.parentInverseMatrix" "jasminRN.placeHolderList[8]" 
		""
		5 3 "jasminRN" "|jasmin:jasmin|jasmin:world.rotatePivot" "jasminRN.placeHolderList[9]" 
		""
		5 3 "jasminRN" "|jasmin:jasmin|jasmin:world.rotatePivotTranslate" "jasminRN.placeHolderList[10]" 
		"";
	setAttr ".ptag" -type "string" "";
lockNode -l 1 ;
createNode reference -n "motorcycleRN";
	rename -uid "5CC52940-0000-4B3C-5ED4-15A300000413";
	setAttr -s 24 ".phl";
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
	setAttr ".phl[11]" 0;
	setAttr ".phl[12]" 0;
	setAttr ".phl[13]" 0;
	setAttr ".phl[14]" 0;
	setAttr ".phl[15]" 0;
	setAttr ".phl[16]" 0;
	setAttr ".phl[17]" 0;
	setAttr ".phl[18]" 0;
	setAttr ".phl[19]" 0;
	setAttr ".phl[20]" 0;
	setAttr ".phl[21]" 0;
	setAttr ".phl[22]" 0;
	setAttr ".phl[23]" 0;
	setAttr ".phl[24]" 0;
	setAttr ".ed" -type "dataReferenceEdits" 
		"motorcycleRN"
		"motorcycleRN" 388
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:polySurface117|motorcycle:polySurfaceShape117" 
		"dispResolution" " 1"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:polySurface117|motorcycle:polySurfaceShape117" 
		"displaySmoothMesh" " 0"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:polySurface118|motorcycle:polySurfaceShape118" 
		"dispResolution" " 1"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:polySurface118|motorcycle:polySurfaceShape118" 
		"displaySmoothMesh" " 0"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:pPipe93|motorcycle:pPipeShape93" 
		"dispResolution" " 1"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:pPipe93|motorcycle:pPipeShape93" 
		"displaySmoothMesh" " 0"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:polySurface119|motorcycle:polySurfaceShape119" 
		"dispResolution" " 1"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:polySurface119|motorcycle:polySurfaceShape119" 
		"displaySmoothMesh" " 0"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:pCube45|motorcycle:pCubeShape45" 
		"dispResolution" " 1"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:pCube45|motorcycle:pCubeShape45" 
		"displaySmoothMesh" " 0"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:polySurface120|motorcycle:polySurfaceShape120" 
		"dispResolution" " 1"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:polySurface120|motorcycle:polySurfaceShape120" 
		"displaySmoothMesh" " 0"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:polySurface121|motorcycle:polySurfaceShape121" 
		"dispResolution" " 1"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:polySurface121|motorcycle:polySurfaceShape121" 
		"displaySmoothMesh" " 0"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:polySurface122|motorcycle:polySurfaceShape122" 
		"dispResolution" " 1"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:polySurface122|motorcycle:polySurfaceShape122" 
		"displaySmoothMesh" " 0"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:polySurface123|motorcycle:polySurfaceShape123" 
		"dispResolution" " 1"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:polySurface123|motorcycle:polySurfaceShape123" 
		"displaySmoothMesh" " 0"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:pPipe94|motorcycle:pPipeShape94" 
		"dispResolution" " 1"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:pPipe94|motorcycle:pPipeShape94" 
		"displaySmoothMesh" " 0"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:polySurface124|motorcycle:polySurfaceShape124" 
		"dispResolution" " 1"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:polySurface124|motorcycle:polySurfaceShape124" 
		"displaySmoothMesh" " 0"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:pPipe95|motorcycle:pPipeShape95" 
		"dispResolution" " 1"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:pPipe95|motorcycle:pPipeShape95" 
		"displaySmoothMesh" " 0"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:pPipe96|motorcycle:pPipeShape96" 
		"dispResolution" " 1"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:pPipe96|motorcycle:pPipeShape96" 
		"displaySmoothMesh" " 0"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:pPipe97|motorcycle:pPipeShape97" 
		"dispResolution" " 1"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:pPipe97|motorcycle:pPipeShape97" 
		"displaySmoothMesh" " 0"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:pPipe98|motorcycle:pPipeShape98" 
		"dispResolution" " 1"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:pPipe98|motorcycle:pPipeShape98" 
		"displaySmoothMesh" " 0"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:polySurface125|motorcycle:polySurfaceShape125" 
		"dispResolution" " 1"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:polySurface125|motorcycle:polySurfaceShape125" 
		"displaySmoothMesh" " 0"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:polySurface126|motorcycle:polySurfaceShape126" 
		"dispResolution" " 1"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:polySurface126|motorcycle:polySurfaceShape126" 
		"displaySmoothMesh" " 0"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:polySurface127|motorcycle:polySurfaceShape127" 
		"dispResolution" " 1"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:polySurface127|motorcycle:polySurfaceShape127" 
		"displaySmoothMesh" " 0"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:polySurface116|motorcycle:polySurfaceShape116" 
		"dispResolution" " 1"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:polySurface116|motorcycle:polySurfaceShape116" 
		"displaySmoothMesh" " 0"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:polySurface115|motorcycle:polySurfaceShape115" 
		"dispResolution" " 1"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:polySurface115|motorcycle:polySurfaceShape115" 
		"displaySmoothMesh" " 0"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:polySurface114|motorcycle:polySurfaceShape114" 
		"dispResolution" " 1"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:polySurface114|motorcycle:polySurfaceShape114" 
		"displaySmoothMesh" " 0"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:polySurface113|motorcycle:polySurfaceShape113" 
		"dispResolution" " 1"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:polySurface113|motorcycle:polySurfaceShape113" 
		"displaySmoothMesh" " 0"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:polySurface112|motorcycle:polySurfaceShape112" 
		"dispResolution" " 1"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:polySurface112|motorcycle:polySurfaceShape112" 
		"displaySmoothMesh" " 0"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:polySurface111|motorcycle:polySurfaceShape111" 
		"dispResolution" " 1"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:polySurface111|motorcycle:polySurfaceShape111" 
		"displaySmoothMesh" " 0"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:polySurface110|motorcycle:polySurfaceShape110" 
		"dispResolution" " 1"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:polySurface110|motorcycle:polySurfaceShape110" 
		"displaySmoothMesh" " 0"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:polySurface109|motorcycle:polySurfaceShape109" 
		"dispResolution" " 1"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:polySurface109|motorcycle:polySurfaceShape109" 
		"displaySmoothMesh" " 0"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:polySurface108|motorcycle:polySurfaceShape108" 
		"dispResolution" " 1"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:polySurface108|motorcycle:polySurfaceShape108" 
		"displaySmoothMesh" " 0"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:polySurface107|motorcycle:polySurfaceShape107" 
		"dispResolution" " 1"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:polySurface107|motorcycle:polySurfaceShape107" 
		"displaySmoothMesh" " 0"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:polySurface106|motorcycle:polySurfaceShape106" 
		"dispResolution" " 1"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:polySurface106|motorcycle:polySurfaceShape106" 
		"displaySmoothMesh" " 0"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:polySurface105|motorcycle:polySurfaceShape105" 
		"dispResolution" " 1"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:polySurface105|motorcycle:polySurfaceShape105" 
		"displaySmoothMesh" " 0"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:polySurface104|motorcycle:polySurfaceShape104" 
		"dispResolution" " 1"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:polySurface104|motorcycle:polySurfaceShape104" 
		"displaySmoothMesh" " 0"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:pPipe92|motorcycle:pPipeShape92" 
		"dispResolution" " 1"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:pPipe92|motorcycle:pPipeShape92" 
		"displaySmoothMesh" " 0"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:polySurface103|motorcycle:polySurfaceShape103" 
		"dispResolution" " 1"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:polySurface103|motorcycle:polySurfaceShape103" 
		"displaySmoothMesh" " 0"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:polySurface102|motorcycle:polySurfaceShape102" 
		"dispResolution" " 1"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:polySurface102|motorcycle:polySurfaceShape102" 
		"displaySmoothMesh" " 0"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:polySurface101|motorcycle:polySurfaceShape101" 
		"dispResolution" " 1"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:polySurface101|motorcycle:polySurfaceShape101" 
		"displaySmoothMesh" " 0"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:polySurface100|motorcycle:polySurfaceShape100" 
		"dispResolution" " 1"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:polySurface100|motorcycle:polySurfaceShape100" 
		"displaySmoothMesh" " 0"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:polySurface99|motorcycle:polySurfaceShape99" 
		"dispResolution" " 1"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:polySurface99|motorcycle:polySurfaceShape99" 
		"displaySmoothMesh" " 0"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:polySurface98|motorcycle:polySurfaceShape98" 
		"dispResolution" " 1"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:polySurface98|motorcycle:polySurfaceShape98" 
		"displaySmoothMesh" " 0"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:polySurface97|motorcycle:polySurfaceShape97" 
		"dispResolution" " 1"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:polySurface97|motorcycle:polySurfaceShape97" 
		"displaySmoothMesh" " 0"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:polySurface96|motorcycle:polySurfaceShape96" 
		"dispResolution" " 1"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:polySurface96|motorcycle:polySurfaceShape96" 
		"displaySmoothMesh" " 0"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:polySurface95|motorcycle:polySurfaceShape95" 
		"dispResolution" " 1"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:polySurface95|motorcycle:polySurfaceShape95" 
		"displaySmoothMesh" " 0"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:pCylinder94|motorcycle:pCylinderShape94" 
		"dispResolution" " 1"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:pCylinder94|motorcycle:pCylinderShape94" 
		"displaySmoothMesh" " 0"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:polySurface94|motorcycle:polySurfaceShape94" 
		"dispResolution" " 1"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:polySurface94|motorcycle:polySurfaceShape94" 
		"displaySmoothMesh" " 0"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:polySurface93|motorcycle:polySurfaceShape93" 
		"dispResolution" " 1"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:polySurface93|motorcycle:polySurfaceShape93" 
		"displaySmoothMesh" " 0"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:polySurface92|motorcycle:polySurfaceShape92" 
		"dispResolution" " 1"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:polySurface92|motorcycle:polySurfaceShape92" 
		"displaySmoothMesh" " 0"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:polySurface91|motorcycle:polySurfaceShape91" 
		"dispResolution" " 1"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:polySurface91|motorcycle:polySurfaceShape91" 
		"displaySmoothMesh" " 0"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:polySurface90|motorcycle:polySurfaceShape90" 
		"dispResolution" " 1"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:polySurface90|motorcycle:polySurfaceShape90" 
		"displaySmoothMesh" " 0"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:polySurface89|motorcycle:polySurfaceShape89" 
		"dispResolution" " 1"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:polySurface89|motorcycle:polySurfaceShape89" 
		"displaySmoothMesh" " 0"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:polySurface88|motorcycle:polySurfaceShape88" 
		"dispResolution" " 1"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:polySurface88|motorcycle:polySurfaceShape88" 
		"displaySmoothMesh" " 0"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:polySurface87|motorcycle:polySurfaceShape87" 
		"dispResolution" " 1"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:polySurface87|motorcycle:polySurfaceShape87" 
		"displaySmoothMesh" " 0"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:polySurface86|motorcycle:polySurfaceShape86" 
		"dispResolution" " 1"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:polySurface86|motorcycle:polySurfaceShape86" 
		"displaySmoothMesh" " 0"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:polySurface85|motorcycle:polySurfaceShape85" 
		"dispResolution" " 1"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:polySurface85|motorcycle:polySurfaceShape85" 
		"displaySmoothMesh" " 0"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:polySurface84|motorcycle:polySurfaceShape84" 
		"dispResolution" " 1"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:polySurface84|motorcycle:polySurfaceShape84" 
		"displaySmoothMesh" " 0"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:polySurface83|motorcycle:polySurfaceShape83" 
		"dispResolution" " 1"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:polySurface83|motorcycle:polySurfaceShape83" 
		"displaySmoothMesh" " 0"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:polySurface82|motorcycle:polySurfaceShape82" 
		"dispResolution" " 1"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:polySurface82|motorcycle:polySurfaceShape82" 
		"displaySmoothMesh" " 0"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:polySurface81|motorcycle:polySurfaceShape81" 
		"dispResolution" " 1"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:polySurface81|motorcycle:polySurfaceShape81" 
		"displaySmoothMesh" " 0"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:polySurface80|motorcycle:polySurfaceShape80" 
		"dispResolution" " 1"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:polySurface80|motorcycle:polySurfaceShape80" 
		"displaySmoothMesh" " 0"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:polySurface79|motorcycle:polySurfaceShape79" 
		"dispResolution" " 1"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:polySurface79|motorcycle:polySurfaceShape79" 
		"displaySmoothMesh" " 0"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:polySurface78|motorcycle:polySurfaceShape78" 
		"dispResolution" " 1"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:polySurface78|motorcycle:polySurfaceShape78" 
		"displaySmoothMesh" " 0"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:polySurface77|motorcycle:polySurfaceShape77" 
		"dispResolution" " 1"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:polySurface77|motorcycle:polySurfaceShape77" 
		"displaySmoothMesh" " 0"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:polySurface76|motorcycle:polySurfaceShape76" 
		"dispResolution" " 1"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:polySurface76|motorcycle:polySurfaceShape76" 
		"displaySmoothMesh" " 0"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:polySurface75|motorcycle:polySurfaceShape75" 
		"dispResolution" " 1"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:polySurface75|motorcycle:polySurfaceShape75" 
		"displaySmoothMesh" " 0"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:polySurface74|motorcycle:polySurfaceShape74" 
		"dispResolution" " 1"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:polySurface74|motorcycle:polySurfaceShape74" 
		"displaySmoothMesh" " 0"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:polySurface73|motorcycle:polySurfaceShape73" 
		"dispResolution" " 1"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:polySurface73|motorcycle:polySurfaceShape73" 
		"displaySmoothMesh" " 0"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:polySurface72|motorcycle:polySurfaceShape72" 
		"dispResolution" " 1"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:polySurface72|motorcycle:polySurfaceShape72" 
		"displaySmoothMesh" " 0"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:polySurface71|motorcycle:polySurfaceShape71" 
		"dispResolution" " 1"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:polySurface71|motorcycle:polySurfaceShape71" 
		"displaySmoothMesh" " 0"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:polySurface70|motorcycle:polySurfaceShape70" 
		"dispResolution" " 1"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:polySurface70|motorcycle:polySurfaceShape70" 
		"displaySmoothMesh" " 0"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:polySurface69|motorcycle:polySurfaceShape69" 
		"dispResolution" " 1"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:polySurface69|motorcycle:polySurfaceShape69" 
		"displaySmoothMesh" " 0"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:polySurface68|motorcycle:polySurfaceShape68" 
		"dispResolution" " 1"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:polySurface68|motorcycle:polySurfaceShape68" 
		"displaySmoothMesh" " 0"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:polySurface67|motorcycle:polySurfaceShape67" 
		"dispResolution" " 1"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:polySurface67|motorcycle:polySurfaceShape67" 
		"displaySmoothMesh" " 0"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:polySurface66|motorcycle:polySurfaceShape66" 
		"dispResolution" " 1"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:polySurface66|motorcycle:polySurfaceShape66" 
		"displaySmoothMesh" " 0"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:pCube44|motorcycle:pCubeShape44" 
		"dispResolution" " 1"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:pCube44|motorcycle:pCubeShape44" 
		"displaySmoothMesh" " 0"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:polySurface65|motorcycle:polySurfaceShape65" 
		"dispResolution" " 1"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:polySurface65|motorcycle:polySurfaceShape65" 
		"displaySmoothMesh" " 0"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:pCube43|motorcycle:pCubeShape43" 
		"dispResolution" " 1"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:pCube43|motorcycle:pCubeShape43" 
		"displaySmoothMesh" " 0"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:pCube42|motorcycle:pCubeShape42" 
		"dispResolution" " 1"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:pCube42|motorcycle:pCubeShape42" 
		"displaySmoothMesh" " 0"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:pPlane14|motorcycle:pPlaneShape14" 
		"dispResolution" " 1"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:pPlane14|motorcycle:pPlaneShape14" 
		"displaySmoothMesh" " 0"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:pPlane13|motorcycle:pPlaneShape13" 
		"dispResolution" " 1"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:pPlane13|motorcycle:pPlaneShape13" 
		"displaySmoothMesh" " 0"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:pPlane12|motorcycle:pPlaneShape12" 
		"dispResolution" " 1"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:pPlane12|motorcycle:pPlaneShape12" 
		"displaySmoothMesh" " 0"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:pPlane11|motorcycle:pPlaneShape11" 
		"dispResolution" " 1"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:pPlane11|motorcycle:pPlaneShape11" 
		"displaySmoothMesh" " 0"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:pPipe91|motorcycle:pPipeShape91" 
		"dispResolution" " 1"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:pPipe91|motorcycle:pPipeShape91" 
		"displaySmoothMesh" " 0"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:pPipe90|motorcycle:pPipeShape90" 
		"dispResolution" " 1"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:pPipe90|motorcycle:pPipeShape90" 
		"displaySmoothMesh" " 0"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:pPipe89|motorcycle:pPipeShape89" 
		"dispResolution" " 1"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:pPipe89|motorcycle:pPipeShape89" 
		"displaySmoothMesh" " 0"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:pPipe88|motorcycle:pPipeShape88" 
		"dispResolution" " 1"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:pPipe88|motorcycle:pPipeShape88" 
		"displaySmoothMesh" " 0"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:pPipe87|motorcycle:pPipeShape87" 
		"dispResolution" " 1"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:pPipe87|motorcycle:pPipeShape87" 
		"displaySmoothMesh" " 0"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:pPipe86|motorcycle:pPipeShape86" 
		"dispResolution" " 1"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:pPipe86|motorcycle:pPipeShape86" 
		"displaySmoothMesh" " 0"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:pPipe85|motorcycle:pPipeShape85" 
		"dispResolution" " 1"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:pPipe85|motorcycle:pPipeShape85" 
		"displaySmoothMesh" " 0"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:pPipe84|motorcycle:pPipeShape84" 
		"dispResolution" " 1"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:pPipe84|motorcycle:pPipeShape84" 
		"displaySmoothMesh" " 0"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:pPipe83|motorcycle:pPipeShape83" 
		"dispResolution" " 1"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:pPipe83|motorcycle:pPipeShape83" 
		"displaySmoothMesh" " 0"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:pPipe82|motorcycle:pPipeShape82" 
		"dispResolution" " 1"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:pPipe82|motorcycle:pPipeShape82" 
		"displaySmoothMesh" " 0"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:pPipe81|motorcycle:pPipeShape81" 
		"dispResolution" " 1"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:pPipe81|motorcycle:pPipeShape81" 
		"displaySmoothMesh" " 0"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:pPipe80|motorcycle:pPipeShape80" 
		"dispResolution" " 1"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:pPipe80|motorcycle:pPipeShape80" 
		"displaySmoothMesh" " 0"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:pPipe79|motorcycle:pPipeShape79" 
		"dispResolution" " 1"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:pPipe79|motorcycle:pPipeShape79" 
		"displaySmoothMesh" " 0"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:pPipe78|motorcycle:pPipeShape78" 
		"dispResolution" " 1"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:pPipe78|motorcycle:pPipeShape78" 
		"displaySmoothMesh" " 0"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:pPipe77|motorcycle:pPipeShape77" 
		"dispResolution" " 1"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:pPipe77|motorcycle:pPipeShape77" 
		"displaySmoothMesh" " 0"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:pPipe76|motorcycle:pPipeShape76" 
		"dispResolution" " 1"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:pPipe76|motorcycle:pPipeShape76" 
		"displaySmoothMesh" " 0"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:pPipe75|motorcycle:pPipeShape75" 
		"dispResolution" " 1"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:pPipe75|motorcycle:pPipeShape75" 
		"displaySmoothMesh" " 0"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:pPipe74|motorcycle:pPipeShape74" 
		"dispResolution" " 1"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:pPipe74|motorcycle:pPipeShape74" 
		"displaySmoothMesh" " 0"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:pPipe73|motorcycle:pPipeShape73" 
		"dispResolution" " 1"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:pPipe73|motorcycle:pPipeShape73" 
		"displaySmoothMesh" " 0"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:pPipe72|motorcycle:pPipeShape72" 
		"dispResolution" " 1"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:pPipe72|motorcycle:pPipeShape72" 
		"displaySmoothMesh" " 0"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:pPipe71|motorcycle:pPipeShape71" 
		"dispResolution" " 1"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:pPipe71|motorcycle:pPipeShape71" 
		"displaySmoothMesh" " 0"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:pPipe70|motorcycle:pPipeShape70" 
		"dispResolution" " 1"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:pPipe70|motorcycle:pPipeShape70" 
		"displaySmoothMesh" " 0"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:pPipe69|motorcycle:pPipeShape69" 
		"dispResolution" " 1"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:pPipe69|motorcycle:pPipeShape69" 
		"displaySmoothMesh" " 0"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:pPipe68|motorcycle:pPipeShape68" 
		"dispResolution" " 1"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:pPipe68|motorcycle:pPipeShape68" 
		"displaySmoothMesh" " 0"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:pPipe67|motorcycle:pPipeShape67" 
		"dispResolution" " 1"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:pPipe67|motorcycle:pPipeShape67" 
		"displaySmoothMesh" " 0"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:pPipe66|motorcycle:pPipeShape66" 
		"dispResolution" " 1"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:pPipe66|motorcycle:pPipeShape66" 
		"displaySmoothMesh" " 0"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:pPipe65|motorcycle:pPipeShape65" 
		"dispResolution" " 1"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:pPipe65|motorcycle:pPipeShape65" 
		"displaySmoothMesh" " 0"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:pPipe64|motorcycle:pPipeShape64" 
		"dispResolution" " 1"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:pPipe64|motorcycle:pPipeShape64" 
		"displaySmoothMesh" " 0"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:pPipe63|motorcycle:pPipeShape63" 
		"dispResolution" " 1"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:pPipe63|motorcycle:pPipeShape63" 
		"displaySmoothMesh" " 0"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:pPipe62|motorcycle:pPipeShape62" 
		"dispResolution" " 1"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:pPipe62|motorcycle:pPipeShape62" 
		"displaySmoothMesh" " 0"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:pPipe61|motorcycle:pPipeShape61" 
		"dispResolution" " 1"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:pPipe61|motorcycle:pPipeShape61" 
		"displaySmoothMesh" " 0"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:pPipe60|motorcycle:pPipeShape60" 
		"dispResolution" " 1"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:pPipe60|motorcycle:pPipeShape60" 
		"displaySmoothMesh" " 0"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:pPipe59|motorcycle:pPipeShape59" 
		"dispResolution" " 1"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:pPipe59|motorcycle:pPipeShape59" 
		"displaySmoothMesh" " 0"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:pPipe58|motorcycle:pPipeShape58" 
		"dispResolution" " 1"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:pPipe58|motorcycle:pPipeShape58" 
		"displaySmoothMesh" " 0"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:pPipe57|motorcycle:pPipeShape57" 
		"dispResolution" " 1"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:pPipe57|motorcycle:pPipeShape57" 
		"displaySmoothMesh" " 0"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:pPipe56|motorcycle:pPipeShape56" 
		"dispResolution" " 1"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:pPipe56|motorcycle:pPipeShape56" 
		"displaySmoothMesh" " 0"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:pPipe55|motorcycle:pPipeShape55" 
		"dispResolution" " 1"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:pPipe55|motorcycle:pPipeShape55" 
		"displaySmoothMesh" " 0"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:pPipe54|motorcycle:pPipeShape54" 
		"dispResolution" " 1"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:pPipe54|motorcycle:pPipeShape54" 
		"displaySmoothMesh" " 0"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:pPipe53|motorcycle:pPipeShape53" 
		"dispResolution" " 1"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:pPipe53|motorcycle:pPipeShape53" 
		"displaySmoothMesh" " 0"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:pPipe52|motorcycle:pPipeShape52" 
		"dispResolution" " 1"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:pPipe52|motorcycle:pPipeShape52" 
		"displaySmoothMesh" " 0"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:pPipe51|motorcycle:pPipeShape51" 
		"dispResolution" " 1"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:pPipe51|motorcycle:pPipeShape51" 
		"displaySmoothMesh" " 0"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:pPipe50|motorcycle:pPipeShape50" 
		"dispResolution" " 1"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:pPipe50|motorcycle:pPipeShape50" 
		"displaySmoothMesh" " 0"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:pPipe49|motorcycle:pPipeShape49" 
		"dispResolution" " 1"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:pPipe49|motorcycle:pPipeShape49" 
		"displaySmoothMesh" " 0"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:pPipe48|motorcycle:pPipeShape48" 
		"dispResolution" " 1"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:pPipe48|motorcycle:pPipeShape48" 
		"displaySmoothMesh" " 0"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:pPipe47|motorcycle:pPipeShape47" 
		"dispResolution" " 1"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:pPipe47|motorcycle:pPipeShape47" 
		"displaySmoothMesh" " 0"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:pPipe46|motorcycle:pPipeShape46" 
		"dispResolution" " 1"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:pPipe46|motorcycle:pPipeShape46" 
		"displaySmoothMesh" " 0"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:pPipe45|motorcycle:pPipeShape45" 
		"dispResolution" " 1"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:pPipe45|motorcycle:pPipeShape45" 
		"displaySmoothMesh" " 0"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:pPipe44|motorcycle:pPipeShape44" 
		"dispResolution" " 1"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:pPipe44|motorcycle:pPipeShape44" 
		"displaySmoothMesh" " 0"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:pPipe43|motorcycle:pPipeShape43" 
		"dispResolution" " 1"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:pPipe43|motorcycle:pPipeShape43" 
		"displaySmoothMesh" " 0"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:pPipe42|motorcycle:pPipeShape42" 
		"dispResolution" " 1"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:pPipe42|motorcycle:pPipeShape42" 
		"displaySmoothMesh" " 0"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:pPipe41|motorcycle:pPipeShape41" 
		"dispResolution" " 1"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:pPipe41|motorcycle:pPipeShape41" 
		"displaySmoothMesh" " 0"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:pPipe40|motorcycle:pPipeShape40" 
		"dispResolution" " 1"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:pPipe40|motorcycle:pPipeShape40" 
		"displaySmoothMesh" " 0"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:pPipe39|motorcycle:pPipeShape39" 
		"dispResolution" " 1"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:pPipe39|motorcycle:pPipeShape39" 
		"displaySmoothMesh" " 0"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:pPipe38|motorcycle:pPipeShape38" 
		"dispResolution" " 1"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:pPipe38|motorcycle:pPipeShape38" 
		"displaySmoothMesh" " 0"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:pPipe37|motorcycle:pPipeShape37" 
		"dispResolution" " 1"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:pPipe37|motorcycle:pPipeShape37" 
		"displaySmoothMesh" " 0"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:pHelix11|motorcycle:pHelixShape11" 
		"dispResolution" " 1"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:pHelix11|motorcycle:pHelixShape11" 
		"displaySmoothMesh" " 0"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:pHelix10|motorcycle:pHelixShape10" 
		"dispResolution" " 1"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:pHelix10|motorcycle:pHelixShape10" 
		"displaySmoothMesh" " 0"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:pHelix9|motorcycle:pHelixShape9" 
		"dispResolution" " 1"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:pHelix9|motorcycle:pHelixShape9" 
		"displaySmoothMesh" " 0"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:pHelix8|motorcycle:pHelixShape8" 
		"dispResolution" " 1"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:pHelix8|motorcycle:pHelixShape8" 
		"displaySmoothMesh" " 0"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:pHelix7|motorcycle:pHelixShape7" 
		"dispResolution" " 1"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:pHelix7|motorcycle:pHelixShape7" 
		"displaySmoothMesh" " 0"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:pCylinder93|motorcycle:pCylinderShape93" 
		"dispResolution" " 1"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:pCylinder93|motorcycle:pCylinderShape93" 
		"displaySmoothMesh" " 0"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:pCylinder92|motorcycle:pCylinderShape92" 
		"dispResolution" " 1"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:pCylinder92|motorcycle:pCylinderShape92" 
		"displaySmoothMesh" " 0"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:pCylinder91|motorcycle:pCylinderShape91" 
		"dispResolution" " 1"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:pCylinder91|motorcycle:pCylinderShape91" 
		"displaySmoothMesh" " 0"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:pCylinder90|motorcycle:pCylinderShape90" 
		"dispResolution" " 1"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:pCylinder90|motorcycle:pCylinderShape90" 
		"displaySmoothMesh" " 0"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:pCylinder89|motorcycle:pCylinderShape89" 
		"dispResolution" " 1"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:pCylinder89|motorcycle:pCylinderShape89" 
		"displaySmoothMesh" " 0"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:pCylinder88|motorcycle:pCylinderShape88" 
		"dispResolution" " 1"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:pCylinder88|motorcycle:pCylinderShape88" 
		"displaySmoothMesh" " 0"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:pCylinder87|motorcycle:pCylinderShape87" 
		"dispResolution" " 1"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:pCylinder87|motorcycle:pCylinderShape87" 
		"displaySmoothMesh" " 0"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:pCylinder86|motorcycle:pCylinderShape86" 
		"dispResolution" " 1"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:pCylinder86|motorcycle:pCylinderShape86" 
		"displaySmoothMesh" " 0"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:pCylinder85|motorcycle:pCylinderShape85" 
		"dispResolution" " 1"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:pCylinder85|motorcycle:pCylinderShape85" 
		"displaySmoothMesh" " 0"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:pCylinder84|motorcycle:pCylinderShape84" 
		"dispResolution" " 1"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:pCylinder84|motorcycle:pCylinderShape84" 
		"displaySmoothMesh" " 0"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:pCylinder83|motorcycle:pCylinderShape83" 
		"dispResolution" " 1"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:pCylinder83|motorcycle:pCylinderShape83" 
		"displaySmoothMesh" " 0"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:pCylinder82|motorcycle:pCylinderShape82" 
		"dispResolution" " 1"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:pCylinder82|motorcycle:pCylinderShape82" 
		"displaySmoothMesh" " 0"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:pCylinder81|motorcycle:pCylinderShape81" 
		"dispResolution" " 1"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:pCylinder81|motorcycle:pCylinderShape81" 
		"displaySmoothMesh" " 0"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:pCylinder80|motorcycle:pCylinderShape80" 
		"dispResolution" " 1"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:pCylinder80|motorcycle:pCylinderShape80" 
		"displaySmoothMesh" " 0"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:pCylinder79|motorcycle:pCylinderShape79" 
		"dispResolution" " 1"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:pCylinder79|motorcycle:pCylinderShape79" 
		"displaySmoothMesh" " 0"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:pCylinder78|motorcycle:pCylinderShape78" 
		"dispResolution" " 1"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:pCylinder78|motorcycle:pCylinderShape78" 
		"displaySmoothMesh" " 0"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:pCylinder77|motorcycle:pCylinderShape77" 
		"dispResolution" " 1"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:pCylinder77|motorcycle:pCylinderShape77" 
		"displaySmoothMesh" " 0"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:pCylinder76|motorcycle:pCylinderShape76" 
		"dispResolution" " 1"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:pCylinder76|motorcycle:pCylinderShape76" 
		"displaySmoothMesh" " 0"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:pCylinder75|motorcycle:pCylinderShape75" 
		"dispResolution" " 1"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:pCylinder75|motorcycle:pCylinderShape75" 
		"displaySmoothMesh" " 0"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:pCylinder74|motorcycle:pCylinderShape74" 
		"dispResolution" " 1"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:pCylinder74|motorcycle:pCylinderShape74" 
		"displaySmoothMesh" " 0"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:pCylinder73|motorcycle:pCylinderShape73" 
		"dispResolution" " 1"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:pCylinder73|motorcycle:pCylinderShape73" 
		"displaySmoothMesh" " 0"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:pCylinder72|motorcycle:pCylinderShape72" 
		"dispResolution" " 1"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:pCylinder72|motorcycle:pCylinderShape72" 
		"displaySmoothMesh" " 0"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:pCylinder71|motorcycle:pCylinderShape71" 
		"dispResolution" " 1"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:pCylinder71|motorcycle:pCylinderShape71" 
		"displaySmoothMesh" " 0"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:pCylinder70|motorcycle:pCylinderShape70" 
		"dispResolution" " 1"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:pCylinder70|motorcycle:pCylinderShape70" 
		"displaySmoothMesh" " 0"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:pCylinder69|motorcycle:pCylinderShape69" 
		"dispResolution" " 1"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:pCylinder69|motorcycle:pCylinderShape69" 
		"displaySmoothMesh" " 0"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:pCylinder68|motorcycle:pCylinderShape68" 
		"dispResolution" " 1"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:pCylinder68|motorcycle:pCylinderShape68" 
		"displaySmoothMesh" " 0"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:pCylinder67|motorcycle:pCylinderShape67" 
		"dispResolution" " 1"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:pCylinder67|motorcycle:pCylinderShape67" 
		"displaySmoothMesh" " 0"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:pCylinder66|motorcycle:pCylinderShape66" 
		"dispResolution" " 1"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:pCylinder66|motorcycle:pCylinderShape66" 
		"displaySmoothMesh" " 0"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:pCylinder65|motorcycle:pCylinderShape65" 
		"dispResolution" " 1"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:pCylinder65|motorcycle:pCylinderShape65" 
		"displaySmoothMesh" " 0"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:pCylinder64|motorcycle:pCylinderShape64" 
		"dispResolution" " 1"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:pCylinder64|motorcycle:pCylinderShape64" 
		"displaySmoothMesh" " 0"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:pCylinder63|motorcycle:pCylinderShape63" 
		"dispResolution" " 1"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:pCylinder63|motorcycle:pCylinderShape63" 
		"displaySmoothMesh" " 0"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:pCylinder62|motorcycle:pCylinderShape62" 
		"dispResolution" " 1"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:pCylinder62|motorcycle:pCylinderShape62" 
		"displaySmoothMesh" " 0"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:pCylinder61|motorcycle:pCylinderShape61" 
		"dispResolution" " 1"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:pCylinder61|motorcycle:pCylinderShape61" 
		"displaySmoothMesh" " 0"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:pCylinder60|motorcycle:pCylinderShape60" 
		"dispResolution" " 1"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:pCylinder60|motorcycle:pCylinderShape60" 
		"displaySmoothMesh" " 0"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:pCylinder59|motorcycle:pCylinderShape59" 
		"dispResolution" " 1"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:pCylinder59|motorcycle:pCylinderShape59" 
		"displaySmoothMesh" " 0"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:pCube41|motorcycle:pCubeShape41" 
		"dispResolution" " 1"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:pCube41|motorcycle:pCubeShape41" 
		"displaySmoothMesh" " 0"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:pCube40|motorcycle:pCubeShape40" 
		"dispResolution" " 1"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:pCube40|motorcycle:pCubeShape40" 
		"displaySmoothMesh" " 0"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:pCube39|motorcycle:pCubeShape39" 
		"dispResolution" " 1"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:pCube39|motorcycle:pCubeShape39" 
		"displaySmoothMesh" " 0"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:pCube38|motorcycle:pCubeShape38" 
		"dispResolution" " 1"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:pCube38|motorcycle:pCubeShape38" 
		"displaySmoothMesh" " 0"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:pCube37|motorcycle:pCubeShape37" 
		"dispResolution" " 1"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:pCube37|motorcycle:pCubeShape37" 
		"displaySmoothMesh" " 0"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:pCube36|motorcycle:pCubeShape36" 
		"dispResolution" " 1"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:pCube36|motorcycle:pCubeShape36" 
		"displaySmoothMesh" " 0"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:pCube35|motorcycle:pCubeShape35" 
		"dispResolution" " 1"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:pCube35|motorcycle:pCubeShape35" 
		"displaySmoothMesh" " 0"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:pCube34|motorcycle:pCubeShape34" 
		"dispResolution" " 1"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:pCube34|motorcycle:pCubeShape34" 
		"displaySmoothMesh" " 0"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:pCube33|motorcycle:pCubeShape33" 
		"dispResolution" " 1"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:pCube33|motorcycle:pCubeShape33" 
		"displaySmoothMesh" " 0"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:pCube32|motorcycle:pCubeShape32" 
		"dispResolution" " 1"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:pCube32|motorcycle:pCubeShape32" 
		"displaySmoothMesh" " 0"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:pCube31|motorcycle:pCubeShape31" 
		"dispResolution" " 1"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:pCube31|motorcycle:pCubeShape31" 
		"displaySmoothMesh" " 0"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:pCube30|motorcycle:pCubeShape30" 
		"dispResolution" " 1"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:pCube30|motorcycle:pCubeShape30" 
		"displaySmoothMesh" " 0"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:pCube29|motorcycle:pCubeShape29" 
		"dispResolution" " 1"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:pCube29|motorcycle:pCubeShape29" 
		"displaySmoothMesh" " 0"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:pCube28|motorcycle:pCubeShape28" 
		"dispResolution" " 1"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:pCube28|motorcycle:pCubeShape28" 
		"displaySmoothMesh" " 0"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:pCube27|motorcycle:pCubeShape27" 
		"dispResolution" " 1"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:pCube27|motorcycle:pCubeShape27" 
		"displaySmoothMesh" " 0"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:hd_lght2|motorcycle:hd_lght2Shape" 
		"dispResolution" " 1"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:hd_lght2|motorcycle:hd_lght2Shape" 
		"displaySmoothMesh" " 0"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:engn1|motorcycle:engn1Shape" 
		"dispResolution" " 1"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:engn1|motorcycle:engn1Shape" 
		"displaySmoothMesh" " 0"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:chn1|motorcycle:chn1Shape" 
		"dispResolution" " 1"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:chn1|motorcycle:chn1Shape" 
		"displaySmoothMesh" " 0"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:cee_t1|motorcycle:cee_t1Shape" 
		"dispResolution" " 1"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:cee_t1|motorcycle:cee_t1Shape" 
		"displaySmoothMesh" " 0"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:bar_a1|motorcycle:bar_a1Shape" 
		"dispResolution" " 1"
		2 "|motorcycle:motorcycle|motorcycle:world|motorcycle:bar_a1|motorcycle:bar_a1Shape" 
		"displaySmoothMesh" " 0"
		"motorcycleRN" 36
		1 |motorcycle:motorcycle "min" "min" " -ci 1 -dt \"string\""
		1 |motorcycle:motorcycle "max" "max" " -ci 1 -dt \"string\""
		1 |motorcycle:motorcycle "latest_lookdev" "latest_lookdev" " -ci 1 -dt \"string\""
		
		2 "|motorcycle:motorcycle" "min" " -type \"string\" \"1001\""
		2 "|motorcycle:motorcycle" "max" " -type \"string\" \"1025\""
		2 "|motorcycle:motorcycle" "latest_lookdev" " -type \"string\" \"0.1.0\""
		
		2 "|motorcycle:motorcycle|motorcycle:world" "translate" " -type \"double3\" 0 0 0"
		
		2 "|motorcycle:motorcycle|motorcycle:world" "translateX" " -av"
		2 "|motorcycle:motorcycle|motorcycle:world" "translateY" " -av"
		2 "|motorcycle:motorcycle|motorcycle:world" "translateZ" " -av"
		2 "|motorcycle:motorcycle|motorcycle:world" "rotate" " -type \"double3\" 0 -22.75189753729842579 0"
		
		2 "|motorcycle:motorcycle|motorcycle:world" "rotateY" " -av"
		5 3 "motorcycleRN" "|motorcycle:motorcycle|motorcycle:world.translate" 
		"motorcycleRN.placeHolderList[1]" ""
		5 3 "motorcycleRN" "|motorcycle:motorcycle|motorcycle:world.translate" 
		"motorcycleRN.placeHolderList[2]" ""
		5 4 "motorcycleRN" "|motorcycle:motorcycle|motorcycle:world.translateX" 
		"motorcycleRN.placeHolderList[3]" ""
		5 4 "motorcycleRN" "|motorcycle:motorcycle|motorcycle:world.translateY" 
		"motorcycleRN.placeHolderList[4]" ""
		5 4 "motorcycleRN" "|motorcycle:motorcycle|motorcycle:world.translateZ" 
		"motorcycleRN.placeHolderList[5]" ""
		5 3 "motorcycleRN" "|motorcycle:motorcycle|motorcycle:world.rotate" 
		"motorcycleRN.placeHolderList[6]" ""
		5 3 "motorcycleRN" "|motorcycle:motorcycle|motorcycle:world.rotate" 
		"motorcycleRN.placeHolderList[7]" ""
		5 4 "motorcycleRN" "|motorcycle:motorcycle|motorcycle:world.rotateX" 
		"motorcycleRN.placeHolderList[8]" ""
		5 4 "motorcycleRN" "|motorcycle:motorcycle|motorcycle:world.rotateY" 
		"motorcycleRN.placeHolderList[9]" ""
		5 4 "motorcycleRN" "|motorcycle:motorcycle|motorcycle:world.rotateZ" 
		"motorcycleRN.placeHolderList[10]" ""
		5 3 "motorcycleRN" "|motorcycle:motorcycle|motorcycle:world.rotatePivot" 
		"motorcycleRN.placeHolderList[11]" ""
		5 3 "motorcycleRN" "|motorcycle:motorcycle|motorcycle:world.rotatePivot" 
		"motorcycleRN.placeHolderList[12]" ""
		5 3 "motorcycleRN" "|motorcycle:motorcycle|motorcycle:world.rotatePivotTranslate" 
		"motorcycleRN.placeHolderList[13]" ""
		5 3 "motorcycleRN" "|motorcycle:motorcycle|motorcycle:world.rotatePivotTranslate" 
		"motorcycleRN.placeHolderList[14]" ""
		5 3 "motorcycleRN" "|motorcycle:motorcycle|motorcycle:world.rotateOrder" 
		"motorcycleRN.placeHolderList[15]" ""
		5 3 "motorcycleRN" "|motorcycle:motorcycle|motorcycle:world.rotateOrder" 
		"motorcycleRN.placeHolderList[16]" ""
		5 3 "motorcycleRN" "|motorcycle:motorcycle|motorcycle:world.scale" "motorcycleRN.placeHolderList[17]" 
		""
		5 3 "motorcycleRN" "|motorcycle:motorcycle|motorcycle:world.scale" "motorcycleRN.placeHolderList[18]" 
		""
		5 4 "motorcycleRN" "|motorcycle:motorcycle|motorcycle:world.scaleX" 
		"motorcycleRN.placeHolderList[19]" ""
		5 4 "motorcycleRN" "|motorcycle:motorcycle|motorcycle:world.scaleY" 
		"motorcycleRN.placeHolderList[20]" ""
		5 4 "motorcycleRN" "|motorcycle:motorcycle|motorcycle:world.scaleZ" 
		"motorcycleRN.placeHolderList[21]" ""
		5 3 "motorcycleRN" "|motorcycle:motorcycle|motorcycle:world.parentMatrix" 
		"motorcycleRN.placeHolderList[22]" ""
		5 3 "motorcycleRN" "|motorcycle:motorcycle|motorcycle:world.parentMatrix" 
		"motorcycleRN.placeHolderList[23]" ""
		5 4 "motorcycleRN" "|motorcycle:motorcycle|motorcycle:world.visibility" 
		"motorcycleRN.placeHolderList[24]" "";
	setAttr ".ptag" -type "string" "";
lockNode -l 1 ;
createNode reference -n "southcityRN";
	rename -uid "4A26E940-0000-4677-5EE1-0A2A00001148";
	setAttr ".ed" -type "dataReferenceEdits" 
		"southcityRN"
		"southcityRN" 0
		"southcityRN" 8
		1 |southcity:southcity "min" "min" " -ci 1 -dt \"string\""
		1 |southcity:southcity "max" "max" " -ci 1 -dt \"string\""
		1 |southcity:southcity "latest_lookdev" "latest_lookdev" " -ci 1 -dt \"string\""
		
		2 "|southcity:southcity" "min" " -type \"string\" \"1001\""
		2 "|southcity:southcity" "max" " -type \"string\" \"1025\""
		2 "|southcity:southcity" "latest_lookdev" " -type \"string\" \"0.1.0\""
		2 "|southcity:southcity|southcity:world|southcity:geometry|southcity:building_1_ctrl" 
		"translate" " -type \"double3\" -32.29084542884027087 0 14.94726617902720811"
		2 "|southcity:southcity|southcity:world|southcity:geometry|southcity:building_3_ctrl" 
		"translate" " -type \"double3\" -31.86983827246820056 0 41.7929288324734074";
lockNode -l 1 ;
createNode animCurveTL -n "world_translateX";
	rename -uid "5CC52940-0000-4B3C-5ED4-185B0000062C";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 3 ".ktv[0:2]"  1001 3.9288879720043948 1010 3.9288879720043948 1020 -3.8256113285156483;
	setAttr -s 3 ".kit[1:2]"  1 18;
	setAttr -s 3 ".kot[1:2]"  1 18;
	setAttr -s 3 ".kix[1:2]"  1 1;
	setAttr -s 3 ".kiy[1:2]"  0 0;
	setAttr -s 3 ".kox[1:2]"  1 1;
	setAttr -s 3 ".koy[1:2]"  0 0;
createNode animCurveTL -n "world_translateY";
	rename -uid "5CC52940-0000-4B3C-5ED4-185B0000062D";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 3 ".ktv[0:2]"  1001 1.1614814422570108 1010 1.1614814422570108 1020 2.3053434965795372;
	setAttr -s 3 ".kit[1:2]"  1 18;
	setAttr -s 3 ".kot[1:2]"  1 18;
	setAttr -s 3 ".kix[1:2]"  1 1;
	setAttr -s 3 ".kiy[1:2]"  0 0;
	setAttr -s 3 ".kox[1:2]"  1 1;
	setAttr -s 3 ".koy[1:2]"  0 0;
createNode animCurveTL -n "world_translateZ";
	rename -uid "5CC52940-0000-4B3C-5ED4-185B0000062E";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 3 ".ktv[0:2]"  1001 -2.0476243801067939 1010 -2.0476243801067939 1020 15.703880405169418;
	setAttr -s 3 ".kit[1:2]"  1 18;
	setAttr -s 3 ".kot[1:2]"  1 18;
	setAttr -s 3 ".kix[1:2]"  1 1;
	setAttr -s 3 ".kiy[1:2]"  0 0;
	setAttr -s 3 ".kox[1:2]"  1 1;
	setAttr -s 3 ".koy[1:2]"  0 0;
createNode animCurveTA -n "world_rotateX";
	rename -uid "5CC52940-0000-4B3C-5ED4-185B0000062F";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 3 ".ktv[0:2]"  1001 6.8616472703974809 1010 6.8616472703974809 1020 5.8935054850324837;
	setAttr -s 3 ".kit[1:2]"  1 18;
	setAttr -s 3 ".kot[1:2]"  1 18;
	setAttr -s 3 ".kix[1:2]"  1 1;
	setAttr -s 3 ".kiy[1:2]"  0 0;
	setAttr -s 3 ".kox[1:2]"  1 1;
	setAttr -s 3 ".koy[1:2]"  0 0;
createNode animCurveTA -n "world_rotateY";
	rename -uid "5CC52940-0000-4B3C-5ED4-185B00000630";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 3 ".ktv[0:2]"  1001 123.79999999999963 1010 123.79999999999963 1020 153.04023936093321;
	setAttr -s 3 ".kit[1:2]"  1 18;
	setAttr -s 3 ".kot[1:2]"  1 18;
	setAttr -s 3 ".kix[1:2]"  1 1;
	setAttr -s 3 ".kiy[1:2]"  0 0;
	setAttr -s 3 ".kox[1:2]"  1 1;
	setAttr -s 3 ".koy[1:2]"  0 0;
createNode animCurveTA -n "world_rotateZ";
	rename -uid "5CC52940-0000-4B3C-5ED4-185B00000631";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 3 ".ktv[0:2]"  1001 0 1010 0 1020 -1.7435670774423093;
	setAttr -s 3 ".kit[1:2]"  1 18;
	setAttr -s 3 ".kot[1:2]"  1 18;
	setAttr -s 3 ".kix[1:2]"  1 1;
	setAttr -s 3 ".kiy[1:2]"  0 0;
	setAttr -s 3 ".kox[1:2]"  1 1;
	setAttr -s 3 ".koy[1:2]"  0 0;
createNode animCurveTL -n "world_translateX1";
	rename -uid "5CC52940-0000-4B3C-5ED4-19C000000CC4";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 3 ".ktv[0:2]"  1001 0 1010 0 1020 -7.2709811067419583;
	setAttr -s 3 ".kit[1:2]"  1 18;
	setAttr -s 3 ".kot[1:2]"  1 18;
	setAttr -s 3 ".kix[1:2]"  1 1;
	setAttr -s 3 ".kiy[1:2]"  0 0;
	setAttr -s 3 ".kox[1:2]"  1 1;
	setAttr -s 3 ".koy[1:2]"  0 0;
createNode animCurveTL -n "world_translateY1";
	rename -uid "5CC52940-0000-4B3C-5ED4-19C000000CC5";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 3 ".ktv[0:2]"  1001 0 1010 0 1020 0;
	setAttr -s 3 ".kit[1:2]"  1 18;
	setAttr -s 3 ".kot[1:2]"  1 18;
	setAttr -s 3 ".kix[1:2]"  1 1;
	setAttr -s 3 ".kiy[1:2]"  0 0;
	setAttr -s 3 ".kox[1:2]"  1 1;
	setAttr -s 3 ".koy[1:2]"  0 0;
createNode animCurveTL -n "world_translateZ1";
	rename -uid "5CC52940-0000-4B3C-5ED4-19C000000CC6";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 3 ".ktv[0:2]"  1001 0 1010 0 1020 17.337711786314578;
	setAttr -s 3 ".kit[1:2]"  1 18;
	setAttr -s 3 ".kot[1:2]"  1 18;
	setAttr -s 3 ".kix[1:2]"  1 1;
	setAttr -s 3 ".kiy[1:2]"  0 0;
	setAttr -s 3 ".kox[1:2]"  1 1;
	setAttr -s 3 ".koy[1:2]"  0 0;
createNode animCurveTA -n "world_rotateX1";
	rename -uid "5CC52940-0000-4B3C-5ED4-19C000000CC8";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 3 ".ktv[0:2]"  1001 0 1010 0 1020 0;
	setAttr -s 3 ".kit[1:2]"  1 18;
	setAttr -s 3 ".kot[1:2]"  1 18;
	setAttr -s 3 ".kix[1:2]"  1 1;
	setAttr -s 3 ".kiy[1:2]"  0 0;
	setAttr -s 3 ".kox[1:2]"  1 1;
	setAttr -s 3 ".koy[1:2]"  0 0;
createNode animCurveTA -n "world_rotateY1";
	rename -uid "5CC52940-0000-4B3C-5ED4-19C000000CC9";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 3 ".ktv[0:2]"  1001 -22.751897537298426 1010 -22.751897537298426 1020 0.33752913178289129;
	setAttr -s 3 ".kit[1:2]"  1 18;
	setAttr -s 3 ".kot[1:2]"  1 18;
	setAttr -s 3 ".kix[1:2]"  1 1;
	setAttr -s 3 ".kiy[1:2]"  0 0;
	setAttr -s 3 ".kox[1:2]"  1 1;
	setAttr -s 3 ".koy[1:2]"  0 0;
createNode animCurveTA -n "world_rotateZ1";
	rename -uid "5CC52940-0000-4B3C-5ED4-19C000000CCA";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 3 ".ktv[0:2]"  1001 0 1010 0 1020 0;
	setAttr -s 3 ".kit[1:2]"  1 18;
	setAttr -s 3 ".kot[1:2]"  1 18;
	setAttr -s 3 ".kix[1:2]"  1 1;
	setAttr -s 3 ".kiy[1:2]"  0 0;
	setAttr -s 3 ".kox[1:2]"  1 1;
	setAttr -s 3 ".koy[1:2]"  0 0;
createNode animCurveTU -n "world_scaleX";
	rename -uid "5CC52940-0000-4B3C-5ED4-19C000000CCB";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 3 ".ktv[0:2]"  1001 1 1010 1 1020 1;
	setAttr -s 3 ".kit[1:2]"  1 18;
	setAttr -s 3 ".kot[1:2]"  1 18;
	setAttr -s 3 ".kix[1:2]"  1 1;
	setAttr -s 3 ".kiy[1:2]"  0 0;
	setAttr -s 3 ".kox[1:2]"  1 1;
	setAttr -s 3 ".koy[1:2]"  0 0;
createNode animCurveTU -n "world_scaleY";
	rename -uid "5CC52940-0000-4B3C-5ED4-19C000000CCC";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 3 ".ktv[0:2]"  1001 1 1010 1 1020 1;
	setAttr -s 3 ".kit[1:2]"  1 18;
	setAttr -s 3 ".kot[1:2]"  1 18;
	setAttr -s 3 ".kix[1:2]"  1 1;
	setAttr -s 3 ".kiy[1:2]"  0 0;
	setAttr -s 3 ".kox[1:2]"  1 1;
	setAttr -s 3 ".koy[1:2]"  0 0;
createNode animCurveTU -n "world_scaleZ";
	rename -uid "5CC52940-0000-4B3C-5ED4-19C000000CCD";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 3 ".ktv[0:2]"  1001 1 1010 1 1020 1;
	setAttr -s 3 ".kit[1:2]"  1 18;
	setAttr -s 3 ".kot[1:2]"  1 18;
	setAttr -s 3 ".kix[1:2]"  1 1;
	setAttr -s 3 ".kiy[1:2]"  0 0;
	setAttr -s 3 ".kox[1:2]"  1 1;
	setAttr -s 3 ".koy[1:2]"  0 0;
createNode animCurveTU -n "world_visibility";
	rename -uid "5CC52940-0000-4B3C-5ED4-19C000000CC7";
	setAttr ".tan" 5;
	setAttr ".wgt" no;
	setAttr -s 3 ".ktv[0:2]"  1001 1 1010 1 1020 1;
	setAttr -s 3 ".kit[0:2]"  9 1 9;
	setAttr -s 3 ".kix[1:2]"  1 1;
	setAttr -s 3 ".kiy[1:2]"  0 0;
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
connectAttr "world_parentConstraint1.ctx" "batmanRN.phl[1]";
connectAttr "world_parentConstraint1.cty" "batmanRN.phl[2]";
connectAttr "world_parentConstraint1.ctz" "batmanRN.phl[3]";
connectAttr "world_parentConstraint1.crx" "batmanRN.phl[4]";
connectAttr "world_parentConstraint1.cry" "batmanRN.phl[5]";
connectAttr "world_parentConstraint1.crz" "batmanRN.phl[6]";
connectAttr "batmanRN.phl[7]" "world_parentConstraint1.cro";
connectAttr "batmanRN.phl[8]" "world_parentConstraint1.cpim";
connectAttr "batmanRN.phl[9]" "world_parentConstraint1.crp";
connectAttr "batmanRN.phl[10]" "world_parentConstraint1.crt";
connectAttr "world_parentConstraint2.ctx" "jasminRN.phl[1]";
connectAttr "world_parentConstraint2.cty" "jasminRN.phl[2]";
connectAttr "world_parentConstraint2.ctz" "jasminRN.phl[3]";
connectAttr "world_parentConstraint2.crx" "jasminRN.phl[4]";
connectAttr "world_parentConstraint2.cry" "jasminRN.phl[5]";
connectAttr "world_parentConstraint2.crz" "jasminRN.phl[6]";
connectAttr "jasminRN.phl[7]" "world_parentConstraint2.cro";
connectAttr "jasminRN.phl[8]" "world_parentConstraint2.cpim";
connectAttr "jasminRN.phl[9]" "world_parentConstraint2.crp";
connectAttr "jasminRN.phl[10]" "world_parentConstraint2.crt";
connectAttr "motorcycleRN.phl[1]" "world_parentConstraint1.tg[0].tt";
connectAttr "motorcycleRN.phl[2]" "world_parentConstraint2.tg[0].tt";
connectAttr "world_translateX1.o" "motorcycleRN.phl[3]";
connectAttr "world_translateY1.o" "motorcycleRN.phl[4]";
connectAttr "world_translateZ1.o" "motorcycleRN.phl[5]";
connectAttr "motorcycleRN.phl[6]" "world_parentConstraint1.tg[0].tr";
connectAttr "motorcycleRN.phl[7]" "world_parentConstraint2.tg[0].tr";
connectAttr "world_rotateX1.o" "motorcycleRN.phl[8]";
connectAttr "world_rotateY1.o" "motorcycleRN.phl[9]";
connectAttr "world_rotateZ1.o" "motorcycleRN.phl[10]";
connectAttr "motorcycleRN.phl[11]" "world_parentConstraint1.tg[0].trp";
connectAttr "motorcycleRN.phl[12]" "world_parentConstraint2.tg[0].trp";
connectAttr "motorcycleRN.phl[13]" "world_parentConstraint1.tg[0].trt";
connectAttr "motorcycleRN.phl[14]" "world_parentConstraint2.tg[0].trt";
connectAttr "motorcycleRN.phl[15]" "world_parentConstraint1.tg[0].tro";
connectAttr "motorcycleRN.phl[16]" "world_parentConstraint2.tg[0].tro";
connectAttr "motorcycleRN.phl[17]" "world_parentConstraint1.tg[0].ts";
connectAttr "motorcycleRN.phl[18]" "world_parentConstraint2.tg[0].ts";
connectAttr "world_scaleX.o" "motorcycleRN.phl[19]";
connectAttr "world_scaleY.o" "motorcycleRN.phl[20]";
connectAttr "world_scaleZ.o" "motorcycleRN.phl[21]";
connectAttr "motorcycleRN.phl[22]" "world_parentConstraint1.tg[0].tpm";
connectAttr "motorcycleRN.phl[23]" "world_parentConstraint2.tg[0].tpm";
connectAttr "world_visibility.o" "motorcycleRN.phl[24]";
connectAttr "world_parentConstraint1.w0" "world_parentConstraint1.tg[0].tw";
connectAttr "world_parentConstraint2.w0" "world_parentConstraint2.tg[0].tw";
connectAttr "batmanRNfosterParent1.msg" "batmanRN.fp";
connectAttr "jasminRNfosterParent1.msg" "jasminRN.fp";
// End of 1003.ma
