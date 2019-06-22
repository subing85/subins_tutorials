//Maya ASCII 2017 scene
//Name: walk.ma
//Last modified: Wed, May 15, 2019 09:12:38 PM
//Codeset: UTF-8
file -rdi 1 -ns "normal_walk_cycle" -rfn "normal_walk_cycleRN" -op "v=0;p=17;f=0"
		 -typ "mayaAscii" "/mnt/bkp/assets/walk_cycle/normal_walk_cycle.ma";
file -r -ns "normal_walk_cycle" -dr 1 -rfn "normal_walk_cycleRN" -op "v=0;p=17;f=0"
		 -typ "mayaAscii" "/mnt/bkp/assets/walk_cycle/normal_walk_cycle.ma";
requires maya "2017";
currentUnit -l centimeter -a degree -t pal;
fileInfo "application" "maya";
fileInfo "product" "Maya 2017";
fileInfo "version" "2017";
fileInfo "cutIdentifier" "201606150345-997974";
fileInfo "osv" "Linux 3.10.0-957.5.1.el7.x86_64 #1 SMP Fri Feb 1 14:54:57 UTC 2019 x86_64";
fileInfo "license" "student";
createNode transform -s -n "persp";
	rename -uid "D9161900-0000-5F5D-5CDC-0CE00000022F";
	setAttr ".v" no;
	setAttr ".t" -type "double3" 15.807425569015853 41.029339218935249 19.994605374750741 ;
	setAttr ".r" -type "double3" -52.538352729601222 19.799999999999681 0 ;
createNode camera -s -n "perspShape" -p "persp";
	rename -uid "D9161900-0000-5F5D-5CDC-0CE000000230";
	setAttr -k off ".v" no;
	setAttr ".fl" 34.999999999999993;
	setAttr ".coi" 45.102005438363776;
	setAttr ".imn" -type "string" "persp";
	setAttr ".den" -type "string" "persp_depth";
	setAttr ".man" -type "string" "persp_mask";
	setAttr ".hc" -type "string" "viewSet -p %camera";
	setAttr ".ai_translator" -type "string" "perspective";
createNode transform -s -n "top";
	rename -uid "D9161900-0000-5F5D-5CDC-0CE000000231";
	setAttr ".v" no;
	setAttr ".t" -type "double3" 0 1000.1 0 ;
	setAttr ".r" -type "double3" -89.999999999999986 0 0 ;
createNode camera -s -n "topShape" -p "top";
	rename -uid "D9161900-0000-5F5D-5CDC-0CE000000232";
	setAttr -k off ".v" no;
	setAttr ".rnd" no;
	setAttr ".coi" 1000.1;
	setAttr ".ow" 30;
	setAttr ".imn" -type "string" "top";
	setAttr ".den" -type "string" "top_depth";
	setAttr ".man" -type "string" "top_mask";
	setAttr ".hc" -type "string" "viewSet -t %camera";
	setAttr ".o" yes;
	setAttr ".ai_translator" -type "string" "orthographic";
createNode transform -s -n "front";
	rename -uid "D9161900-0000-5F5D-5CDC-0CE000000233";
	setAttr ".v" no;
	setAttr ".t" -type "double3" 0 0 1000.1 ;
createNode camera -s -n "frontShape" -p "front";
	rename -uid "D9161900-0000-5F5D-5CDC-0CE000000234";
	setAttr -k off ".v" no;
	setAttr ".rnd" no;
	setAttr ".coi" 1000.1;
	setAttr ".ow" 30;
	setAttr ".imn" -type "string" "front";
	setAttr ".den" -type "string" "front_depth";
	setAttr ".man" -type "string" "front_mask";
	setAttr ".hc" -type "string" "viewSet -f %camera";
	setAttr ".o" yes;
	setAttr ".ai_translator" -type "string" "orthographic";
createNode transform -s -n "side";
	rename -uid "D9161900-0000-5F5D-5CDC-0CE000000235";
	setAttr ".v" no;
	setAttr ".t" -type "double3" 1000.1 14.068477596296624 0 ;
	setAttr ".r" -type "double3" 0 89.999999999999986 0 ;
createNode camera -s -n "sideShape" -p "side";
	rename -uid "D9161900-0000-5F5D-5CDC-0CE000000236";
	setAttr -k off ".v" no;
	setAttr ".rnd" no;
	setAttr ".coi" 1000.1;
	setAttr ".ow" 43.588231868867751;
	setAttr ".imn" -type "string" "side";
	setAttr ".den" -type "string" "side_depth";
	setAttr ".man" -type "string" "side_mask";
	setAttr ".hc" -type "string" "viewSet -s %camera";
	setAttr ".o" yes;
	setAttr ".ai_translator" -type "string" "orthographic";
createNode transform -n "world";
	rename -uid "D9161900-0000-5F5D-5CDC-0E86000002ED";
	setAttr ".s" -type "double3" 1.5230470024090725 1.5230470024090725 1.5230470024090725 ;
createNode transform -n "controls" -p "|world";
	rename -uid "D9161900-0000-5F5D-5CDC-0E86000002EE";
createNode transform -n "ik_ctrl_group" -p "controls";
	rename -uid "D9161900-0000-5F5D-5CDC-0E86000002CF";
createNode transform -n "lt_wrist_ik_ctrl_group" -p "ik_ctrl_group";
	rename -uid "D9161900-0000-5F5D-5CDC-0E86000002D5";
	setAttr -l on -k off ".v";
	setAttr ".t" -type "double3" 6.9999999999997362 14 1.1490548658355607e-06 ;
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode transform -n "lt_wrist_ik_ctrl" -p "lt_wrist_ik_ctrl_group";
	rename -uid "D9161900-0000-5F5D-5CDC-0E86000002D4";
	addAttr -ci true -k true -sn "twist" -ln "twist" -at "double";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr -k on ".twist";
createNode nurbsCurve -n "lt_wrist_ik_ctrlShape" -p "lt_wrist_ik_ctrl";
	rename -uid "D9161900-0000-5F5D-5CDC-0E86000002D3";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 15 0 no 3
		16 0 1 2 3 4 5 6 7 8 9 10
		 11 12 13 14 15
		16
		0.75 0.75 0.75
		0.75 0.75 -0.75
		-0.75 0.75 -0.75
		-0.75 -0.75 -0.75
		0.75 -0.75 -0.75
		0.75 -0.75 0.75
		-0.75 -0.75 0.75
		-0.75 0.75 0.75
		0.75 0.75 0.75
		0.75 -0.75 0.75
		0.75 -0.75 -0.75
		0.75 0.75 -0.75
		-0.75 0.75 -0.75
		-0.75 0.75 0.75
		-0.75 -0.75 0.75
		-0.75 -0.75 -0.75
		;
createNode parentConstraint -n "lt_wrist_ik_ctrl_parentConstraint1" -p "lt_wrist_ik_ctrl";
	rename -uid "D9161900-0000-5F5D-5CDC-0FBB00000D39";
	addAttr -dcb 0 -ci true -k true -sn "w0" -ln "ctrlFK_Lf_ArmCW0" -dv 1 -min 0 -at "double";
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
	setAttr ".lr" -type "double3" 132.47369633677266 -8.8091638180251302 -98.989351251828325 ;
	setAttr ".rst" -type "double3" -5.6289205607748096 -4.9533665257504325 1.9819071383712288 ;
	setAttr ".rsrr" -type "double3" 132.47369633677266 -8.8091638180251302 -98.989351251828325 ;
	setAttr -k on ".w0";
createNode transform -n "rt_wrist_ik_ctrl_group" -p "ik_ctrl_group";
	rename -uid "D9161900-0000-5F5D-5CDC-0E86000002DC";
	setAttr -l on -k off ".v";
	setAttr ".t" -type "double3" -6.9999999999997362 14 1.1490548658355607e-06 ;
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode transform -n "rt_wrist_ik_ctrl" -p "rt_wrist_ik_ctrl_group";
	rename -uid "D9161900-0000-5F5D-5CDC-0E86000002DB";
	addAttr -ci true -k true -sn "twist" -ln "twist" -at "double";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr -k on ".twist";
createNode nurbsCurve -n "rt_wrist_ik_ctrlShape" -p "rt_wrist_ik_ctrl";
	rename -uid "D9161900-0000-5F5D-5CDC-0E86000002DA";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 15 0 no 3
		16 0 1 2 3 4 5 6 7 8 9 10
		 11 12 13 14 15
		16
		0.75 0.75 0.75
		0.75 0.75 -0.75
		-0.75 0.75 -0.75
		-0.75 -0.75 -0.75
		0.75 -0.75 -0.75
		0.75 -0.75 0.75
		-0.75 -0.75 0.75
		-0.75 0.75 0.75
		0.75 0.75 0.75
		0.75 -0.75 0.75
		0.75 -0.75 -0.75
		0.75 0.75 -0.75
		-0.75 0.75 -0.75
		-0.75 0.75 0.75
		-0.75 -0.75 0.75
		-0.75 -0.75 -0.75
		;
createNode parentConstraint -n "rt_wrist_ik_ctrl_parentConstraint1" -p "rt_wrist_ik_ctrl";
	rename -uid "D9161900-0000-5F5D-5CDC-0FC300000D3A";
	addAttr -dcb 0 -ci true -k true -sn "w0" -ln "ctrlFK_Rt_ArmCW0" -dv 1 -min 0 -at "double";
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
	setAttr ".lr" -type "double3" -109.28978331776798 6.8253478555962603 84.887575628140937 ;
	setAttr ".rst" -type "double3" 5.1549386237663999 -5.2681910078419492 -1.0419766831798347 ;
	setAttr ".rsrr" -type "double3" -109.28978331776798 6.8253478555962603 84.887575628140937 ;
	setAttr -k on ".w0";
createNode transform -n "lt_ankle_ik_ctrl_group" -p "ik_ctrl_group";
	rename -uid "D9161900-0000-5F5D-5CDC-0E86000002E3";
	setAttr -l on -k off ".v";
	setAttr ".t" -type "double3" 1.0000000000000004 1.0000000000003006 -2.751500343539659e-09 ;
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode transform -n "lt_ankle_ik_ctrl" -p "lt_ankle_ik_ctrl_group";
	rename -uid "D9161900-0000-5F5D-5CDC-0E86000002E2";
	addAttr -ci true -k true -sn "twist" -ln "twist" -at "double";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr -k on ".twist";
createNode nurbsCurve -n "lt_ankle_ik_ctrlShape" -p "lt_ankle_ik_ctrl";
	rename -uid "D9161900-0000-5F5D-5CDC-0E86000002E1";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 15 0 no 3
		16 0 1 2 3 4 5 6 7 8 9 10
		 11 12 13 14 15
		16
		0.75 0.75 0.75
		0.75 0.75 -0.75
		-0.75 0.75 -0.75
		-0.75 -0.75 -0.75
		0.75 -0.75 -0.75
		0.75 -0.75 0.75
		-0.75 -0.75 0.75
		-0.75 0.75 0.75
		0.75 0.75 0.75
		0.75 -0.75 0.75
		0.75 -0.75 -0.75
		0.75 0.75 -0.75
		-0.75 0.75 -0.75
		-0.75 0.75 0.75
		-0.75 -0.75 0.75
		-0.75 -0.75 -0.75
		;
createNode parentConstraint -n "lt_ankle_ik_ctrl_parentConstraint1" -p "lt_ankle_ik_ctrl";
	rename -uid "D9161900-0000-5F5D-5CDC-0F3300000C41";
	addAttr -dcb 0 -ci true -k true -sn "w0" -ln "ctrlIK_Lf_LegIKW0" -dv 1 -min 0 -at "double";
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
	setAttr ".lr" -type "double3" 0 10 0 ;
	setAttr ".rst" -type "double3" -0.45575863505733882 -0.31161581702158458 -4.2943375540420634 ;
	setAttr ".rsrr" -type "double3" 0 10 0 ;
	setAttr -k on ".w0";
createNode transform -n "rt_ankle_ik_ctrl_group" -p "ik_ctrl_group";
	rename -uid "D9161900-0000-5F5D-5CDC-0E86000002EA";
	setAttr -l on -k off ".v";
	setAttr ".t" -type "double3" -1 1.0000000000003002 9.1528166616422077e-10 ;
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode transform -n "rt_ankle_ik_ctrl" -p "rt_ankle_ik_ctrl_group";
	rename -uid "D9161900-0000-5F5D-5CDC-0E86000002E9";
	addAttr -ci true -k true -sn "twist" -ln "twist" -at "double";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr -k on ".twist";
createNode nurbsCurve -n "rt_ankle_ik_ctrlShape" -p "rt_ankle_ik_ctrl";
	rename -uid "D9161900-0000-5F5D-5CDC-0E86000002E8";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 15 0 no 3
		16 0 1 2 3 4 5 6 7 8 9 10
		 11 12 13 14 15
		16
		0.75 0.75 0.75
		0.75 0.75 -0.75
		-0.75 0.75 -0.75
		-0.75 -0.75 -0.75
		0.75 -0.75 -0.75
		0.75 -0.75 0.75
		-0.75 -0.75 0.75
		-0.75 0.75 0.75
		0.75 0.75 0.75
		0.75 -0.75 0.75
		0.75 -0.75 -0.75
		0.75 0.75 -0.75
		-0.75 0.75 -0.75
		-0.75 0.75 0.75
		-0.75 -0.75 0.75
		-0.75 -0.75 -0.75
		;
createNode parentConstraint -n "rt_ankle_ik_ctrl_parentConstraint1" -p "rt_ankle_ik_ctrl";
	rename -uid "D9161900-0000-5F5D-5CDC-0F3700000C46";
	addAttr -dcb 0 -ci true -k true -sn "w0" -ln "ctrlIK_Rt_LegIKW0" -dv 1 -min 0 -at "double";
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
	setAttr ".lr" -type "double3" -6.7188357526851945 -18.583088992239333 20.28784492144398 ;
	setAttr ".rst" -type "double3" 0.28082668899390351 -0.31044806999499086 2.9766372763968163 ;
	setAttr ".rsrr" -type "double3" -6.7188357526851945 -18.583088992239333 20.28784492144398 ;
	setAttr -k on ".w0";
createNode transform -n "fk_ctrl_group" -p "controls";
	rename -uid "D9161900-0000-5F5D-5CDC-0E860000029E";
createNode transform -n "ct_root_ctrl_group" -p "fk_ctrl_group";
	rename -uid "D9161900-0000-5F5D-5CDC-0E86000002A2";
	setAttr ".t" -type "double3" 0 10 0 ;
	setAttr ".r" -type "double3" 0 0 89.999999999999986 ;
createNode transform -n "ct_root_ctrl" -p "ct_root_ctrl_group";
	rename -uid "D9161900-0000-5F5D-5CDC-0E86000002A1";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode nurbsCurve -n "ct_root_ctrlShape" -p "ct_root_ctrl";
	rename -uid "D9161900-0000-5F5D-5CDC-0E86000002A0";
	setAttr -k off ".v";
	setAttr ".tw" yes;
createNode parentConstraint -n "ct_root_ctrl_parentConstraint1" -p "ct_root_ctrl";
	rename -uid "D9161900-0000-5F5D-5CDC-0F7A00000C58";
	addAttr -dcb 0 -ci true -k true -sn "w0" -ln "ctrl_RootW0" -dv 1 -min 0 -at "double";
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
	setAttr ".tg[0].tot" -type "double3" 0.012771392556049924 2.4532393780418715e-05 0.0017934612346524742 ;
	setAttr ".tg[0].tor" -type "double3" -7.993646425925486 0.015156409003657707 90.107930165636844 ;
	setAttr ".lr" -type "double3" 4.5517924518327741e-16 6.6931664641545875e-16 -1.2722218725854067e-14 ;
	setAttr ".rst" -type "double3" 0.19616288384140645 -8.6339704883107964e-19 -0.036029191484944698 ;
	setAttr ".rsrr" -type "double3" 4.5517924518327741e-16 6.6931664641545875e-16 -1.2722218725854067e-14 ;
	setAttr -k on ".w0";
createNode transform -n "ct_spine_ctrl_group" -p "fk_ctrl_group";
	rename -uid "D9161900-0000-5F5D-5CDC-0E86000002A8";
createNode transform -n "ct_spine_ctrl" -p "ct_spine_ctrl_group";
	rename -uid "D9161900-0000-5F5D-5CDC-0E86000002A7";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode nurbsCurve -n "ct_spine_ctrlShape" -p "ct_spine_ctrl";
	rename -uid "D9161900-0000-5F5D-5CDC-0E86000002A6";
	setAttr -k off ".v";
	setAttr ".tw" yes;
createNode orientConstraint -n "ct_spine_ctrl_orientConstraint1" -p "ct_spine_ctrl";
	rename -uid "D9161900-0000-5F5D-5CDC-0FE700000DC0";
	addAttr -dcb 0 -ci true -k true -sn "w0" -ln "ctrlFK_Cn_SpineBW0" -dv 1 -min 0 
		-at "double";
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
	setAttr ".lr" -type "double3" 92.016931248841004 3.8852743697011087 0.13661047069356852 ;
	setAttr ".o" -type "double3" -92.012293880214031 0.00011066872296489676 3.8876716325271916 ;
	setAttr ".rsrr" -type "double3" -5.5173828725626996e-33 -1.5902773407317584e-15 3.975693351829396e-16 ;
	setAttr -k on ".w0";
createNode parentConstraint -n "ct_spine_ctrl_group_parent_constraint" -p "ct_spine_ctrl_group";
	rename -uid "D9161900-0000-5F5D-5CDC-0E86000002C8";
	addAttr -dcb 0 -ci true -k true -sn "w0" -ln "ct_root_ctrlW0" -dv 1 -min 0 -at "double";
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
	setAttr ".tg[0].tot" -type "double3" 1.5 3.3306690738754696e-16 0 ;
	setAttr ".lr" -type "double3" 0 0 89.999999999999986 ;
	setAttr ".rst" -type "double3" 0 11.5 0 ;
	setAttr ".rsrr" -type "double3" 0 0 89.999999999999986 ;
	setAttr -k on ".w0";
createNode transform -n "ct_chest_ctrl_group" -p "fk_ctrl_group";
	rename -uid "D9161900-0000-5F5D-5CDC-0E86000002AD";
createNode transform -n "ct_chest_ctrl" -p "ct_chest_ctrl_group";
	rename -uid "D9161900-0000-5F5D-5CDC-0E86000002AC";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode nurbsCurve -n "ct_chest_ctrlShape" -p "ct_chest_ctrl";
	rename -uid "D9161900-0000-5F5D-5CDC-0E86000002AB";
	setAttr -k off ".v";
	setAttr ".tw" yes;
createNode orientConstraint -n "ct_chest_ctrl_orientConstraint1" -p "ct_chest_ctrl";
	rename -uid "D9161900-0000-5F5D-5CDC-0FEB00000DC1";
	addAttr -dcb 0 -ci true -k true -sn "w0" -ln "ctrlFK_Cn_SpineCW0" -dv 1 -min 0 
		-at "double";
	addAttr -dcb 0 -ci true -k true -sn "w1" -ln "ctrlFK_Cn_SpineDW1" -dv 1 -min 0 -at "double";
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
	setAttr -s 2 ".tg";
	setAttr ".lr" -type "double3" 87.538314116167285 0.67620364490347828 0.31639786158338917 ;
	setAttr ".o" -type "double3" -87.538440969406778 -0.34514907308849263 0.66199074508293076 ;
	setAttr ".rsrr" -type "double3" -6.3620799911867586e-15 4.2241741863187339e-16 9.9392333795734899e-17 ;
	setAttr -k on ".w0";
	setAttr -k on ".w1";
createNode parentConstraint -n "ct_chest_ctrl_group_parent_constraint" -p "ct_chest_ctrl_group";
	rename -uid "D9161900-0000-5F5D-5CDC-0E86000002C9";
	addAttr -dcb 0 -ci true -k true -sn "w0" -ln "ct_spine_ctrlW0" -dv 1 -min 0 -at "double";
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
	setAttr ".tg[0].tot" -type "double3" 1.5 3.3306690738754696e-16 0 ;
	setAttr ".lr" -type "double3" 0 0 89.999999999999986 ;
	setAttr ".rst" -type "double3" 0 13 0 ;
	setAttr ".rsrr" -type "double3" 0 0 89.999999999999986 ;
	setAttr -k on ".w0";
createNode transform -n "ct_neck_ctrl_group" -p "fk_ctrl_group";
	rename -uid "D9161900-0000-5F5D-5CDC-0E86000002B2";
createNode transform -n "ct_neck_ctrl" -p "ct_neck_ctrl_group";
	rename -uid "D9161900-0000-5F5D-5CDC-0E86000002B1";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode nurbsCurve -n "ct_neck_ctrlShape" -p "ct_neck_ctrl";
	rename -uid "D9161900-0000-5F5D-5CDC-0E86000002B0";
	setAttr -k off ".v";
	setAttr ".tw" yes;
createNode parentConstraint -n "ct_neck_ctrl_group_parent_constraint" -p "ct_neck_ctrl_group";
	rename -uid "D9161900-0000-5F5D-5CDC-0E86000002CA";
	addAttr -dcb 0 -ci true -k true -sn "w0" -ln "ct_chest_ctrlW0" -dv 1 -min 0 -at "double";
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
	setAttr ".tg[0].tot" -type "double3" 1.5 3.3306690738754696e-16 0 ;
	setAttr ".lr" -type "double3" 0 0 89.999999999999986 ;
	setAttr ".rst" -type "double3" 0 14.5 0 ;
	setAttr ".rsrr" -type "double3" 0 0 89.999999999999986 ;
	setAttr -k on ".w0";
createNode transform -n "ct_head_ctrl_group" -p "fk_ctrl_group";
	rename -uid "D9161900-0000-5F5D-5CDC-0E86000002B7";
createNode transform -n "ct_head_ctrl" -p "ct_head_ctrl_group";
	rename -uid "D9161900-0000-5F5D-5CDC-0E86000002B6";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode nurbsCurve -n "ct_head_ctrlShape" -p "ct_head_ctrl";
	rename -uid "D9161900-0000-5F5D-5CDC-0E86000002B5";
	setAttr -k off ".v";
	setAttr ".tw" yes;
createNode orientConstraint -n "ct_head_ctrl_orientConstraint1" -p "ct_head_ctrl";
	rename -uid "D9161900-0000-5F5D-5CDC-0FA500000CF6";
	addAttr -dcb 0 -ci true -k true -sn "w0" -ln "ctrlFK_Cn_SpineFW0" -dv 1 -min 0 
		-at "double";
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
	setAttr ".lr" -type "double3" 86.048547504421663 0.78554274120350687 0.10897845670423448 ;
	setAttr ".o" -type "double3" -86.048903485813625 -0.16285044495802889 0.77616642093950561 ;
	setAttr ".rsrr" -type "double3" -1.2723383479765733e-14 -2.9817700138720465e-16 -1.4908850069360227e-16 ;
	setAttr -k on ".w0";
createNode parentConstraint -n "ct_head_ctrl_group_parent_constraint" -p "ct_head_ctrl_group";
	rename -uid "D9161900-0000-5F5D-5CDC-0E86000002CB";
	addAttr -dcb 0 -ci true -k true -sn "w0" -ln "ct_neck_ctrlW0" -dv 1 -min 0 -at "double";
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
	setAttr ".tg[0].tot" -type "double3" 1 2.2204460492503131e-16 0 ;
	setAttr ".lr" -type "double3" 0 0 89.999999999999986 ;
	setAttr ".rst" -type "double3" 0 15.5 0 ;
	setAttr ".rsrr" -type "double3" 0 0 89.999999999999986 ;
	setAttr -k on ".w0";
createNode transform -n "ct_hip_ctrl_group" -p "fk_ctrl_group";
	rename -uid "D9161900-0000-5F5D-5CDC-0E86000002BC";
createNode transform -n "ct_hip_ctrl" -p "ct_hip_ctrl_group";
	rename -uid "D9161900-0000-5F5D-5CDC-0E86000002BB";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode nurbsCurve -n "ct_hip_ctrlShape" -p "ct_hip_ctrl";
	rename -uid "D9161900-0000-5F5D-5CDC-0E86000002BA";
	setAttr -k off ".v";
	setAttr ".tw" yes;
createNode parentConstraint -n "ct_hip_ctrl_group_parent_constraint" -p "ct_hip_ctrl_group";
	rename -uid "D9161900-0000-5F5D-5CDC-0E86000002CC";
	addAttr -dcb 0 -ci true -k true -sn "w0" -ln "ct_root_ctrlW0" -dv 1 -min 0 -at "double";
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
	setAttr ".tg[0].tot" -type "double3" -1 -2.2204460492503131e-16 0 ;
	setAttr ".tg[0].tor" -type "double3" 180 -7.016709298534876e-15 2.5444437451708134e-14 ;
	setAttr ".lr" -type "double3" 180 0 89.999999999999986 ;
	setAttr ".rst" -type "double3" 0 9 0 ;
	setAttr ".rsrr" -type "double3" 180 0 89.999999999999986 ;
	setAttr -k on ".w0";
createNode transform -n "lt_clavicle_ctrl_group" -p "fk_ctrl_group";
	rename -uid "D9161900-0000-5F5D-5CDC-0E86000002C1";
createNode transform -n "lt_clavicle_ctrl" -p "lt_clavicle_ctrl_group";
	rename -uid "D9161900-0000-5F5D-5CDC-0E86000002C0";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode nurbsCurve -n "lt_clavicle_ctrlShape" -p "lt_clavicle_ctrl";
	rename -uid "D9161900-0000-5F5D-5CDC-0E86000002BF";
	setAttr -k off ".v";
	setAttr ".tw" yes;
createNode orientConstraint -n "lt_clavicle_ctrl_orientConstraint1" -p "lt_clavicle_ctrl";
	rename -uid "D9161900-0000-5F5D-5CDC-0FF400000DC2";
	addAttr -dcb 0 -ci true -k true -sn "w0" -ln "ctrlFK_Lf_ClavicleW0" -dv 1 -min 
		0 -at "double";
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
	setAttr ".lr" -type "double3" 90.090555642230143 9.4817122586116263 -1.2285884834958216 ;
	setAttr ".o" -type "double3" -90.08933953102482 1.2435044682897496 9.4797850787837454 ;
	setAttr ".rsrr" -type "double3" 1.2622826392058332e-14 -3.1805546814635168e-15 -7.9513867036587959e-16 ;
	setAttr -k on ".w0";
createNode parentConstraint -n "lt_clavicle_ctrl_group_parent_constraint" -p "lt_clavicle_ctrl_group";
	rename -uid "D9161900-0000-5F5D-5CDC-0E86000002CD";
	addAttr -dcb 0 -ci true -k true -sn "w0" -ln "ct_chest_ctrlW0" -dv 1 -min 0 -at "double";
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
	setAttr ".tg[0].tot" -type "double3" 1 -0.99999999999999978 0 ;
	setAttr ".tg[0].tor" -type "double3" 0 0 -89.999999999999986 ;
	setAttr ".rst" -type "double3" 1 14 0 ;
	setAttr -k on ".w0";
createNode transform -n "rt_clavicle_ctrl_group" -p "fk_ctrl_group";
	rename -uid "D9161900-0000-5F5D-5CDC-0E86000002C6";
createNode transform -n "rt_clavicle_ctrl" -p "rt_clavicle_ctrl_group";
	rename -uid "D9161900-0000-5F5D-5CDC-0E86000002C5";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode nurbsCurve -n "rt_clavicle_ctrlShape" -p "rt_clavicle_ctrl";
	rename -uid "D9161900-0000-5F5D-5CDC-0E86000002C4";
	setAttr -k off ".v";
	setAttr ".tw" yes;
createNode orientConstraint -n "rt_clavicle_ctrl_orientConstraint1" -p "rt_clavicle_ctrl";
	rename -uid "D9161900-0000-5F5D-5CDC-0FF900000DC3";
	addAttr -dcb 0 -ci true -k true -sn "w0" -ln "ctrlFK_Rt_ClavicleW0" -dv 1 -min 
		0 -at "double";
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
	setAttr ".lr" -type "double3" 90.101141008671433 17.381523067724164 -0.89519349766574841 ;
	setAttr ".o" -type "double3" -90.096535164623091 0.92540637499507084 17.379989407096833 ;
	setAttr ".rsrr" -type "double3" 1.9480897423964044e-14 -2.7035176075557231e-31 1.5902773407317584e-15 ;
	setAttr -k on ".w0";
createNode parentConstraint -n "rt_clavicle_ctrl_group_parent_constraint" -p "rt_clavicle_ctrl_group";
	rename -uid "D9161900-0000-5F5D-5CDC-0E86000002CE";
	addAttr -dcb 0 -ci true -k true -sn "w0" -ln "ct_chest_ctrlW0" -dv 1 -min 0 -at "double";
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
	setAttr ".tg[0].tot" -type "double3" 1 1.0000000000000002 0 ;
	setAttr ".tg[0].tor" -type "double3" -180 0 -89.999999999999986 ;
	setAttr ".lr" -type "double3" 180 0 0 ;
	setAttr ".rst" -type "double3" -1 14 0 ;
	setAttr ".rsrr" -type "double3" 180 0 0 ;
	setAttr -k on ".w0";
createNode transform -n "ik" -p "|world";
	rename -uid "D9161900-0000-5F5D-5CDC-0E86000002EF";
createNode transform -n "ik_handle_group" -p "ik";
	rename -uid "D9161900-0000-5F5D-5CDC-0E86000002D0";
	setAttr ".v" no;
createNode ikHandle -n "lt_wrist_ik_handle" -p "ik_handle_group";
	rename -uid "D9161900-0000-5F5D-5CDC-0E86000002D2";
	setAttr ".pv" -type "double3" 0.017453070996747869 0 -1.9999238461283426 ;
	setAttr ".roc" yes;
createNode parentConstraint -n "lt_wrist_parent_constraint" -p "lt_wrist_ik_handle";
	rename -uid "D9161900-0000-5F5D-5CDC-0E86000002D6";
	addAttr -dcb 0 -ci true -k true -sn "w0" -ln "lt_wrist_ik_ctrlW0" -dv 1 -min 0 
		-at "double";
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
	setAttr ".lr" -type "double3" 132.47369633677266 -8.8091638180251337 -98.989351251828325 ;
	setAttr ".rst" -type "double3" 6.9999999999997362 14 1.1490548658355607e-06 ;
	setAttr -k on ".w0";
createNode ikHandle -n "rt_wrist_ik_handle" -p "ik_handle_group";
	rename -uid "D9161900-0000-5F5D-5CDC-0E86000002D9";
	setAttr ".pv" -type "double3" -0.017453070996747869 2.4492003366995383e-16 -1.9999238461283426 ;
	setAttr ".roc" yes;
createNode parentConstraint -n "rt_wrist_parent_constraint" -p "rt_wrist_ik_handle";
	rename -uid "D9161900-0000-5F5D-5CDC-0E86000002DD";
	addAttr -dcb 0 -ci true -k true -sn "w0" -ln "rt_wrist_ik_ctrlW0" -dv 1 -min 0 
		-at "double";
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
	setAttr ".lr" -type "double3" -109.28978331776798 6.8253478555962603 84.887575628140937 ;
	setAttr ".rst" -type "double3" -6.9999999999997362 14 1.1490548658355607e-06 ;
	setAttr -k on ".w0";
createNode ikHandle -n "lt_ankle_ik_handle" -p "ik_handle_group";
	rename -uid "D9161900-0000-5F5D-5CDC-0E86000002E0";
	setAttr ".pv" -type "double3" -2.980147198425806e-08 -0.015271428035869604 1.9999416950215683 ;
	setAttr ".roc" yes;
createNode parentConstraint -n "lt_ankle_parent_constraint" -p "lt_ankle_ik_handle";
	rename -uid "D9161900-0000-5F5D-5CDC-0E86000002E4";
	addAttr -dcb 0 -ci true -k true -sn "w0" -ln "lt_ankle_ik_ctrlW0" -dv 1 -min 0 
		-at "double";
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
	setAttr ".lr" -type "double3" 0 10 0 ;
	setAttr ".rst" -type "double3" 1.0000000000000004 1.0000000000003006 -2.751500343539659e-09 ;
	setAttr -k on ".w0";
createNode ikHandle -n "rt_ankle_ik_handle" -p "ik_handle_group";
	rename -uid "D9161900-0000-5F5D-5CDC-0E86000002E7";
	setAttr ".pv" -type "double3" 2.9801459880691218e-08 -0.015271428035869601 1.9999416950215683 ;
	setAttr ".roc" yes;
createNode parentConstraint -n "rt_ankle_parent_constraint" -p "rt_ankle_ik_handle";
	rename -uid "D9161900-0000-5F5D-5CDC-0E86000002EB";
	addAttr -dcb 0 -ci true -k true -sn "w0" -ln "rt_ankle_ik_ctrlW0" -dv 1 -min 0 
		-at "double";
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
	setAttr ".lr" -type "double3" -6.7188357526851927 -18.583088992239333 20.287844921443984 ;
	setAttr ".rst" -type "double3" -1 1.0000000000003002 9.1528166616422077e-10 ;
	setAttr -k on ".w0";
createNode transform -n "joints" -p "|world";
	rename -uid "D9161900-0000-5F5D-5CDC-0E86000002F0";
createNode joint -n "C_Root_Joint" -p "joints";
	rename -uid "D9161900-0000-5F5D-5CDC-0E860000028E";
	setAttr ".ro" 1;
	setAttr ".jo" -type "double3" 0 0 89.999999999999986 ;
	setAttr ".typ" 18;
	setAttr ".otp" -type "string" "root";
	setAttr ".radi" 0.2;
createNode joint -n "C_Hip_Joint" -p "C_Root_Joint";
	rename -uid "D9161900-0000-5F5D-5CDC-0E8600000293";
	setAttr ".ro" 1;
	setAttr ".jo" -type "double3" -180 0 0 ;
	setAttr ".typ" 18;
	setAttr ".otp" -type "string" "hip";
	setAttr ".radi" 0.2;
createNode joint -n "R_Pelvis_Joint" -p "C_Hip_Joint";
	rename -uid "D9161900-0000-5F5D-5CDC-0E8600000296";
	setAttr ".t" -type "double3" 0 -1 1.2246467991473532e-16 ;
	setAttr ".r" -type "double3" -0.68539972808534078 2.0110967593310471 -19.480516672146173 ;
	setAttr ".ro" 1;
	setAttr ".jo" -type "double3" -90.000000000000028 0 0 ;
	setAttr ".sd" 2;
	setAttr ".typ" 18;
	setAttr ".otp" -type "string" "pelvis";
	setAttr ".radi" 0.2;
createNode joint -n "R_Knee_Joint" -p "R_Pelvis_Joint";
	rename -uid "D9161900-0000-5F5D-5CDC-0E860000029D";
	setAttr ".t" -type "double3" -4.5 -2.9582283945787943e-31 1.1102230246251565e-15 ;
	setAttr ".r" -type "double3" -2.4669664034058094e-16 3.2317978933514544e-15 3.1632746434652164e-05 ;
	setAttr ".ro" 1;
	setAttr ".jo" -type "double3" 5.7055094273191895e-15 0 0 ;
	setAttr ".pa" -type "double3" 0 0 1 ;
	setAttr ".sd" 2;
	setAttr ".typ" 18;
	setAttr ".otp" -type "string" "knee";
	setAttr ".radi" 0.2;
createNode joint -n "R_Ankle_Joint" -p "R_Knee_Joint";
	rename -uid "D9161900-0000-5F5D-5CDC-0E8600000298";
	setAttr ".t" -type "double3" -3.5 -1.4791141972893971e-31 6.6613381477509392e-16 ;
	setAttr ".ro" 1;
	setAttr ".jo" -type "double3" 90 -89.999999999999986 0 ;
	setAttr ".sd" 2;
	setAttr ".typ" 18;
	setAttr ".otp" -type "string" "ankle";
	setAttr ".radi" 0.2;
createNode joint -n "R_Ball_Joint" -p "R_Ankle_Joint";
	rename -uid "D9161900-0000-5F5D-5CDC-0E860000028A";
	setAttr ".t" -type "double3" 0 1.0000000000000002 -0.99999999999999989 ;
	setAttr ".r" -type "double3" 180 -90 0 ;
	setAttr ".ro" 1;
	setAttr ".sd" 2;
	setAttr ".typ" 18;
	setAttr ".otp" -type "string" "ball";
	setAttr ".radi" 0.2;
createNode joint -n "R_Toe_Joint" -p "R_Ball_Joint";
	rename -uid "D9161900-0000-5F5D-5CDC-0E860000028C";
	setAttr ".t" -type "double3" 1 -2.4492935982947064e-16 2.2204460492503131e-16 ;
	setAttr ".ro" 1;
	setAttr ".jo" -type "double3" 0 179.99999999999997 0 ;
	setAttr ".pa" -type "double3" 0 1 0 ;
	setAttr ".sd" 2;
	setAttr ".typ" 18;
	setAttr ".otp" -type "string" "toe";
	setAttr ".radi" 0.2;
createNode ikEffector -n "rt_ankle_ik_effector" -p "R_Knee_Joint";
	rename -uid "D9161900-0000-5F5D-5CDC-0E86000002E6";
	setAttr ".v" no;
	setAttr ".hd" yes;
createNode joint -n "L_Pelvis_Joint" -p "C_Hip_Joint";
	rename -uid "D9161900-0000-5F5D-5CDC-0E8600000299";
	setAttr ".t" -type "double3" 0 1 -1.2246467991473532e-16 ;
	setAttr ".r" -type "double3" 1.5189689744668218 3.414330511226578 26.51611560884292 ;
	setAttr ".ro" 1;
	setAttr ".jo" -type "double3" 90.000000000000028 -0.30999999999999561 179.99999999999997 ;
	setAttr ".sd" 1;
	setAttr ".typ" 18;
	setAttr ".otp" -type "string" "pelvis";
	setAttr ".radi" 0.2;
createNode joint -n "L_Knee_Joint" -p "L_Pelvis_Joint";
	rename -uid "D9161900-0000-5F5D-5CDC-0E860000029A";
	setAttr ".t" -type "double3" 4.4999341342590844 -0.024347224275886831 -1.5543122344752192e-15 ;
	setAttr ".r" -type "double3" -2.8956982108499759e-16 8.8873621201113798e-15 3.1632548384394526e-05 ;
	setAttr ".ro" 1;
	setAttr ".jo" -type "double3" 6.0385252350084901e-16 6.9802157759277829e-15 0.050000000000011063 ;
	setAttr ".pa" -type "double3" 0 0 1 ;
	setAttr ".sd" 1;
	setAttr ".typ" 18;
	setAttr ".otp" -type "string" "knee";
	setAttr ".radi" 0.2;
createNode joint -n "L_Ankle_Joint" -p "L_Knee_Joint";
	rename -uid "D9161900-0000-5F5D-5CDC-0E8600000291";
	setAttr ".t" -type "double3" 3.4999309129964802 -0.021991003879456746 -6.6613381477509392e-16 ;
	setAttr ".ro" 1;
	setAttr ".jo" -type "double3" 89.64 -90 0 ;
	setAttr ".sd" 1;
	setAttr ".typ" 18;
	setAttr ".otp" -type "string" "ankle";
	setAttr ".radi" 0.2;
createNode joint -n "L_Ball_Joint" -p "L_Ankle_Joint";
	rename -uid "D9161900-0000-5F5D-5CDC-0E8600000297";
	setAttr ".t" -type "double3" 5.5511151231257827e-16 -1 1 ;
	setAttr ".r" -type "double3" 180 -90 0 ;
	setAttr ".ro" 1;
	setAttr ".jo" -type "double3" -6.4108055298249026e-15 3.1806174628899376e-15 -6.3810932458810037e-15 ;
	setAttr ".sd" 1;
	setAttr ".typ" 18;
	setAttr ".otp" -type "string" "ball";
	setAttr ".radi" 0.2;
createNode joint -n "L_Toe_Joint" -p "L_Ball_Joint";
	rename -uid "D9161900-0000-5F5D-5CDC-0E860000029C";
	setAttr ".t" -type "double3" -0.99999999999999956 -9.2877774652720975e-16 4.4408920985006262e-16 ;
	setAttr ".ro" 1;
	setAttr ".jo" -type "double3" 0 179.99999999999997 0 ;
	setAttr ".sd" 1;
	setAttr ".typ" 18;
	setAttr ".otp" -type "string" "toe";
	setAttr ".radi" 0.2;
createNode ikEffector -n "lt_ankle_ik_effector" -p "L_Knee_Joint";
	rename -uid "D9161900-0000-5F5D-5CDC-0E86000002DF";
	setAttr ".v" no;
	setAttr ".hd" yes;
createNode parentConstraint -n "C_Hip_Joint_parent_constraint" -p "C_Hip_Joint";
	rename -uid "D9161900-0000-5F5D-5CDC-0E86000002BD";
	addAttr -dcb 0 -ci true -k true -sn "w0" -ln "ct_hip_ctrlW0" -dv 1 -min 0 -at "double";
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
	setAttr ".lr" -type "double3" -1.4033418597069752e-14 0 0 ;
	setAttr ".rst" -type "double3" -1 -2.2204460492503131e-16 0 ;
	setAttr ".rsrr" -type "double3" -1.4033418597069752e-14 0 0 ;
	setAttr -k on ".w0";
createNode joint -n "C_Spine_Joint" -p "C_Root_Joint";
	rename -uid "D9161900-0000-5F5D-5CDC-0E8600000295";
	setAttr ".ro" 1;
	setAttr ".typ" 18;
	setAttr ".otp" -type "string" "spine";
	setAttr ".radi" 0.2;
createNode joint -n "C_Chest_Joint" -p "C_Spine_Joint";
	rename -uid "D9161900-0000-5F5D-5CDC-0E8600000286";
	setAttr ".ro" 1;
	setAttr ".typ" 18;
	setAttr ".otp" -type "string" "chest";
	setAttr ".radi" 0.2;
createNode joint -n "R_Clavicle_Joint" -p "C_Chest_Joint";
	rename -uid "D9161900-0000-5F5D-5CDC-0E8600000287";
	setAttr ".ro" 1;
	setAttr ".jo" -type "double3" -180 0 -89.999999999999986 ;
	setAttr ".sd" 2;
	setAttr ".typ" 18;
	setAttr ".otp" -type "string" "clavicle";
	setAttr ".radi" 0.2;
createNode joint -n "R_Shoulder_Joint" -p "R_Clavicle_Joint";
	rename -uid "D9161900-0000-5F5D-5CDC-0E860000028F";
	setAttr ".t" -type "double3" -1 0 0 ;
	setAttr ".r" -type "double3" 163.76050708239498 -153.34074423987917 -88.212604314747011 ;
	setAttr ".ro" 1;
	setAttr ".sd" 2;
	setAttr ".typ" 18;
	setAttr ".otp" -type "string" "shoulder";
	setAttr ".radi" 0.2;
createNode joint -n "R_Elbow_Joint" -p "R_Shoulder_Joint";
	rename -uid "D9161900-0000-5F5D-5CDC-0E8600000292";
	setAttr ".t" -type "double3" -2.5 0 0 ;
	setAttr ".r" -type "double3" 0 -2.6334397696540398e-05 0 ;
	setAttr ".ro" 1;
	setAttr ".pa" -type "double3" 0 -1 0 ;
	setAttr ".sd" 2;
	setAttr ".typ" 18;
	setAttr ".otp" -type "string" "elbow";
	setAttr ".radi" 0.2;
createNode joint -n "R_Wrist_Joint" -p "R_Elbow_Joint";
	rename -uid "D9161900-0000-5F5D-5CDC-0E8600000285";
	setAttr ".t" -type "double3" -2.5 0 0 ;
	setAttr ".ro" 1;
	setAttr ".sd" 2;
	setAttr ".typ" 18;
	setAttr ".otp" -type "string" "wrist";
	setAttr ".radi" 0.2;
createNode ikEffector -n "rt_wrist_ik_effector" -p "R_Elbow_Joint";
	rename -uid "D9161900-0000-5F5D-5CDC-0E86000002D8";
	setAttr ".v" no;
	setAttr ".hd" yes;
createNode parentConstraint -n "R_Clavicle_Joint_parent_constraint" -p "R_Clavicle_Joint";
	rename -uid "D9161900-0000-5F5D-5CDC-0E86000002C7";
	addAttr -dcb 0 -ci true -k true -sn "w0" -ln "rt_clavicle_ctrlW0" -dv 1 -min 0 
		-at "double";
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
	setAttr ".lr" -type "double3" -1.4033418597069752e-14 0 0 ;
	setAttr ".rst" -type "double3" 1 1.0000000000000002 0 ;
	setAttr -k on ".w0";
createNode joint -n "C_Neck_Joint" -p "C_Chest_Joint";
	rename -uid "D9161900-0000-5F5D-5CDC-0E8600000289";
	setAttr ".ro" 1;
	setAttr ".typ" 18;
	setAttr ".otp" -type "string" "neck";
	setAttr ".radi" 0.2;
createNode joint -n "C_Head_Joint" -p "C_Neck_Joint";
	rename -uid "D9161900-0000-5F5D-5CDC-0E8600000290";
	setAttr ".ro" 1;
	setAttr ".typ" 18;
	setAttr ".otp" -type "string" "head";
	setAttr ".radi" 0.2;
createNode joint -n "C_Tip_Joint" -p "C_Head_Joint";
	rename -uid "D9161900-0000-5F5D-5CDC-0E8600000288";
	setAttr ".t" -type "double3" 2.5 5.5511151231257827e-16 0 ;
	setAttr ".ro" 1;
	setAttr ".typ" 18;
	setAttr ".otp" -type "string" "tip";
	setAttr ".radi" 0.2;
createNode parentConstraint -n "C_Head_Joint_parent_constraint" -p "C_Head_Joint";
	rename -uid "D9161900-0000-5F5D-5CDC-0E86000002B8";
	addAttr -dcb 0 -ci true -k true -sn "w0" -ln "ct_head_ctrlW0" -dv 1 -min 0 -at "double";
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
	setAttr ".rst" -type "double3" 1 2.2204460492503131e-16 0 ;
	setAttr -k on ".w0";
createNode parentConstraint -n "C_Neck_Joint_parent_constraint" -p "C_Neck_Joint";
	rename -uid "D9161900-0000-5F5D-5CDC-0E86000002B3";
	addAttr -dcb 0 -ci true -k true -sn "w0" -ln "ct_neck_ctrlW0" -dv 1 -min 0 -at "double";
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
	setAttr ".rst" -type "double3" 1.5 3.3306690738754696e-16 0 ;
	setAttr -k on ".w0";
createNode joint -n "L_Clavicle_Joint" -p "C_Chest_Joint";
	rename -uid "D9161900-0000-5F5D-5CDC-0E860000028B";
	setAttr ".ro" 1;
	setAttr ".jo" -type "double3" 0 0 -89.999999999999986 ;
	setAttr ".sd" 1;
	setAttr ".typ" 18;
	setAttr ".otp" -type "string" "clavicle";
	setAttr ".radi" 0.2;
createNode joint -n "L_Shoulder_Joint" -p "L_Clavicle_Joint";
	rename -uid "D9161900-0000-5F5D-5CDC-0E860000028D";
	setAttr ".t" -type "double3" 1 0 0 ;
	setAttr ".r" -type "double3" 175.79557741000542 162.91928843782352 -83.211895899548665 ;
	setAttr ".ro" 1;
	setAttr ".sd" 1;
	setAttr ".typ" 18;
	setAttr ".otp" -type "string" "shoulder";
	setAttr ".radi" 0.2;
createNode joint -n "L_Elbow_Joint" -p "L_Shoulder_Joint";
	rename -uid "D9161900-0000-5F5D-5CDC-0E860000029B";
	setAttr ".t" -type "double3" 2.5 0 0 ;
	setAttr ".r" -type "double3" 0 -2.6334397696540398e-05 0 ;
	setAttr ".ro" 1;
	setAttr ".pa" -type "double3" 0 -1 0 ;
	setAttr ".sd" 1;
	setAttr ".typ" 18;
	setAttr ".otp" -type "string" "elbow";
	setAttr ".radi" 0.2;
createNode joint -n "L_Wrist_Joint" -p "L_Elbow_Joint";
	rename -uid "D9161900-0000-5F5D-5CDC-0E8600000294";
	setAttr ".t" -type "double3" 2.5 0 0 ;
	setAttr ".ro" 1;
	setAttr ".sd" 1;
	setAttr ".typ" 18;
	setAttr ".otp" -type "string" "wrist";
	setAttr ".radi" 0.2;
createNode ikEffector -n "lt_wrist_ik_effector" -p "L_Elbow_Joint";
	rename -uid "D9161900-0000-5F5D-5CDC-0E86000002D1";
	setAttr ".v" no;
	setAttr ".hd" yes;
createNode parentConstraint -n "L_Clavicle_Joint_parent_constraint" -p "L_Clavicle_Joint";
	rename -uid "D9161900-0000-5F5D-5CDC-0E86000002C2";
	addAttr -dcb 0 -ci true -k true -sn "w0" -ln "lt_clavicle_ctrlW0" -dv 1 -min 0 
		-at "double";
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
	setAttr ".rst" -type "double3" 1 -0.99999999999999978 0 ;
	setAttr -k on ".w0";
createNode parentConstraint -n "C_Chest_Joint_parent_constraint" -p "C_Chest_Joint";
	rename -uid "D9161900-0000-5F5D-5CDC-0E86000002AE";
	addAttr -dcb 0 -ci true -k true -sn "w0" -ln "ct_chest_ctrlW0" -dv 1 -min 0 -at "double";
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
	setAttr ".rst" -type "double3" 1.5 3.3306690738754696e-16 0 ;
	setAttr -k on ".w0";
createNode parentConstraint -n "C_Spine_Joint_parent_constraint" -p "C_Spine_Joint";
	rename -uid "D9161900-0000-5F5D-5CDC-0E86000002A9";
	addAttr -dcb 0 -ci true -k true -sn "w0" -ln "ct_spine_ctrlW0" -dv 1 -min 0 -at "double";
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
	setAttr ".rst" -type "double3" 1.5 3.3306690738754696e-16 0 ;
	setAttr -k on ".w0";
createNode parentConstraint -n "C_Root_Joint_parent_constraint" -p "C_Root_Joint";
	rename -uid "D9161900-0000-5F5D-5CDC-0E86000002A3";
	addAttr -dcb 0 -ci true -k true -sn "w0" -ln "ct_root_ctrlW0" -dv 1 -min 0 -at "double";
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
	setAttr ".rst" -type "double3" 0 10 0 ;
	setAttr -k on ".w0";
createNode lightLinker -s -n "lightLinker1";
	rename -uid "D9161900-0000-5F5D-5CDC-0CE000000237";
	setAttr -s 27 ".lnk";
	setAttr -s 2 ".slnk";
createNode shapeEditorManager -n "shapeEditorManager";
	rename -uid "D9161900-0000-5F5D-5CDC-0CE00000024C";
createNode poseInterpolatorManager -n "poseInterpolatorManager";
	rename -uid "D9161900-0000-5F5D-5CDC-0CE00000024D";
createNode displayLayerManager -n "layerManager";
	rename -uid "D9161900-0000-5F5D-5CDC-0CE00000024E";
createNode displayLayer -n "defaultLayer";
	rename -uid "D9161900-0000-5F5D-5CDC-0CE00000024F";
createNode renderLayerManager -n "renderLayerManager";
	rename -uid "D9161900-0000-5F5D-5CDC-0CE000000250";
createNode renderLayer -n "defaultRenderLayer";
	rename -uid "D9161900-0000-5F5D-5CDC-0CE000000251";
	setAttr ".g" yes;
createNode ikRPsolver -n "ikRPsolver";
	rename -uid "D9161900-0000-5F5D-5CDC-0CE40000027B";
createNode makeNurbCircle -n "makeNurbCircle1";
	rename -uid "D9161900-0000-5F5D-5CDC-0E860000029F";
	setAttr ".nr" -type "double3" 1 0 0 ;
	setAttr ".r" 2;
createNode makeNurbCircle -n "makeNurbCircle2";
	rename -uid "D9161900-0000-5F5D-5CDC-0E86000002A5";
	setAttr ".nr" -type "double3" 1 0 0 ;
	setAttr ".r" 1.7;
createNode makeNurbCircle -n "makeNurbCircle3";
	rename -uid "D9161900-0000-5F5D-5CDC-0E86000002AA";
	setAttr ".nr" -type "double3" 1 0 0 ;
	setAttr ".r" 1.7;
createNode makeNurbCircle -n "makeNurbCircle4";
	rename -uid "D9161900-0000-5F5D-5CDC-0E86000002AF";
	setAttr ".nr" -type "double3" 1 0 0 ;
	setAttr ".r" 1.7;
createNode makeNurbCircle -n "makeNurbCircle5";
	rename -uid "D9161900-0000-5F5D-5CDC-0E86000002B4";
	setAttr ".nr" -type "double3" 1 0 0 ;
	setAttr ".r" 1.7;
createNode makeNurbCircle -n "makeNurbCircle6";
	rename -uid "D9161900-0000-5F5D-5CDC-0E86000002B9";
	setAttr ".nr" -type "double3" 1 0 0 ;
	setAttr ".r" 1.7;
createNode makeNurbCircle -n "makeNurbCircle7";
	rename -uid "D9161900-0000-5F5D-5CDC-0E86000002BE";
	setAttr ".nr" -type "double3" 1 0 0 ;
createNode makeNurbCircle -n "makeNurbCircle8";
	rename -uid "D9161900-0000-5F5D-5CDC-0E86000002C3";
	setAttr ".nr" -type "double3" 1 0 0 ;
createNode unitConversion -n "unitConversion1";
	rename -uid "D9161900-0000-5F5D-5CDC-0E86000002D7";
	setAttr ".cf" 0.017453292519943295;
createNode unitConversion -n "unitConversion2";
	rename -uid "D9161900-0000-5F5D-5CDC-0E86000002DE";
	setAttr ".cf" 0.017453292519943295;
createNode unitConversion -n "unitConversion3";
	rename -uid "D9161900-0000-5F5D-5CDC-0E86000002E5";
	setAttr ".cf" 0.017453292519943295;
createNode unitConversion -n "unitConversion4";
	rename -uid "D9161900-0000-5F5D-5CDC-0E86000002EC";
	setAttr ".cf" 0.017453292519943295;
createNode reference -n "normal_walk_cycleRN";
	rename -uid "D9161900-0000-5F5D-5CDC-0EDF000002F2";
	setAttr -s 65 ".phl";
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
	setAttr ".phl[25]" 0;
	setAttr ".phl[26]" 0;
	setAttr ".phl[27]" 0;
	setAttr ".phl[28]" 0;
	setAttr ".phl[29]" 0;
	setAttr ".phl[30]" 0;
	setAttr ".phl[31]" 0;
	setAttr ".phl[32]" 0;
	setAttr ".phl[33]" 0;
	setAttr ".phl[34]" 0;
	setAttr ".phl[35]" 0;
	setAttr ".phl[36]" 0;
	setAttr ".phl[37]" 0;
	setAttr ".phl[38]" 0;
	setAttr ".phl[39]" 0;
	setAttr ".phl[40]" 0;
	setAttr ".phl[41]" 0;
	setAttr ".phl[42]" 0;
	setAttr ".phl[43]" 0;
	setAttr ".phl[44]" 0;
	setAttr ".phl[45]" 0;
	setAttr ".phl[46]" 0;
	setAttr ".phl[47]" 0;
	setAttr ".phl[48]" 0;
	setAttr ".phl[49]" 0;
	setAttr ".phl[50]" 0;
	setAttr ".phl[51]" 0;
	setAttr ".phl[52]" 0;
	setAttr ".phl[53]" 0;
	setAttr ".phl[54]" 0;
	setAttr ".phl[55]" 0;
	setAttr ".phl[56]" 0;
	setAttr ".phl[57]" 0;
	setAttr ".phl[58]" 0;
	setAttr ".phl[59]" 0;
	setAttr ".phl[60]" 0;
	setAttr ".phl[61]" 0;
	setAttr ".phl[62]" 0;
	setAttr ".phl[63]" 0;
	setAttr ".phl[64]" 0;
	setAttr ".phl[65]" 0;
	setAttr ".ed" -type "dataReferenceEdits" 
		"normal_walk_cycleRN"
		"normal_walk_cycleRN" 0
		"normal_walk_cycleRN" 71
		2 "|normal_walk_cycle:Char_Norman_1" "visibility" " 1"
		2 "|normal_walk_cycle:Char_Norman_1|normal_walk_cycle:LocalSpace|normal_walk_cycle:masterCtrl_Norman|normal_walk_cycle:grLocal_All_Rig|normal_walk_cycle:grAll_Ctrl|normal_walk_cycle:ZGr_Root_Rig|normal_walk_cycle:jntRig_Root|normal_walk_cycle:ctrlFK_Cn_SpineA|normal_walk_cycle:ctrlFK_Cn_SpineB|normal_walk_cycle:ctrlFK_Cn_SpineC|normal_walk_cycle:ctrlFK_Cn_SpineD|normal_walk_cycle:jntCon_Cn_SpineE|normal_walk_cycle:ctrlFK_Cn_SpineE|normal_walk_cycle:jntCon_Cn_SpineF|normal_walk_cycle:ctrlFK_Cn_SpineF" 
		"rotate" " -type \"double3\" 0 0 -1.11620634745442771"
		2 "|normal_walk_cycle:Char_Norman_1|normal_walk_cycle:LocalSpace|normal_walk_cycle:masterCtrl_Norman|normal_walk_cycle:grLocal_All_Rig|normal_walk_cycle:grAll_Ctrl|normal_walk_cycle:ZGr_Root_Rig|normal_walk_cycle:jntRig_Root|normal_walk_cycle:ctrlFK_Cn_SpineA|normal_walk_cycle:ctrlFK_Cn_SpineB|normal_walk_cycle:ctrlFK_Cn_SpineC|normal_walk_cycle:ctrlFK_Cn_SpineD|normal_walk_cycle:jntCon_Cn_SpineE|normal_walk_cycle:ctrlFK_Cn_SpineE|normal_walk_cycle:jntCon_Cn_SpineF|normal_walk_cycle:ctrlFK_Cn_SpineF" 
		"rotateZ" " -av"
		2 "|normal_walk_cycle:Char_Norman_1|normal_walk_cycle:LocalSpace|normal_walk_cycle:masterCtrl_Norman|normal_walk_cycle:grLocal_All_Rig|normal_walk_cycle:grAll_Ctrl|normal_walk_cycle:ZGr_Root_Rig|normal_walk_cycle:jntRig_Root|normal_walk_cycle:ctrlFK_Cn_SpineA|normal_walk_cycle:ctrlFK_Cn_SpineB|normal_walk_cycle:ctrlFK_Cn_SpineC|normal_walk_cycle:ctrlFK_Cn_SpineD|normal_walk_cycle:jntCon_Cn_SpineE|normal_walk_cycle:ctrlFK_Cn_SpineE|normal_walk_cycle:jntCon_Cn_SpineF|normal_walk_cycle:ctrlFK_Cn_SpineF" 
		"segmentScaleCompensate" " 1"
		2 "|normal_walk_cycle:Char_Norman_1|normal_walk_cycle:LocalSpace|normal_walk_cycle:masterCtrl_Norman|normal_walk_cycle:grLocal_All_Rig|normal_walk_cycle:grAll_Ctrl|normal_walk_cycle:ctrl_Root" 
		"translate" " -type \"double3\" -0.012896727215044578 -0.084920935812680592 0"
		2 "|normal_walk_cycle:Char_Norman_1|normal_walk_cycle:LocalSpace|normal_walk_cycle:masterCtrl_Norman|normal_walk_cycle:grLocal_All_Rig|normal_walk_cycle:grAll_Ctrl|normal_walk_cycle:ctrl_Root" 
		"translateX" " -av"
		5 3 "normal_walk_cycleRN" "|normal_walk_cycle:Char_Norman_1|normal_walk_cycle:LocalSpace|normal_walk_cycle:masterCtrl_Norman|normal_walk_cycle:grLocal_All_Rig|normal_walk_cycle:grAll_Ctrl|normal_walk_cycle:gr_All_IK|normal_walk_cycle:grCon_Lf_FootIK|normal_walk_cycle:ctrlIK_Lf_LegIK.scale" 
		"normal_walk_cycleRN.placeHolderList[1]" ""
		5 3 "normal_walk_cycleRN" "|normal_walk_cycle:Char_Norman_1|normal_walk_cycle:LocalSpace|normal_walk_cycle:masterCtrl_Norman|normal_walk_cycle:grLocal_All_Rig|normal_walk_cycle:grAll_Ctrl|normal_walk_cycle:gr_All_IK|normal_walk_cycle:grCon_Lf_FootIK|normal_walk_cycle:ctrlIK_Lf_LegIK.translate" 
		"normal_walk_cycleRN.placeHolderList[2]" ""
		5 3 "normal_walk_cycleRN" "|normal_walk_cycle:Char_Norman_1|normal_walk_cycle:LocalSpace|normal_walk_cycle:masterCtrl_Norman|normal_walk_cycle:grLocal_All_Rig|normal_walk_cycle:grAll_Ctrl|normal_walk_cycle:gr_All_IK|normal_walk_cycle:grCon_Lf_FootIK|normal_walk_cycle:ctrlIK_Lf_LegIK.rotate" 
		"normal_walk_cycleRN.placeHolderList[3]" ""
		5 3 "normal_walk_cycleRN" "|normal_walk_cycle:Char_Norman_1|normal_walk_cycle:LocalSpace|normal_walk_cycle:masterCtrl_Norman|normal_walk_cycle:grLocal_All_Rig|normal_walk_cycle:grAll_Ctrl|normal_walk_cycle:gr_All_IK|normal_walk_cycle:grCon_Lf_FootIK|normal_walk_cycle:ctrlIK_Lf_LegIK.rotatePivot" 
		"normal_walk_cycleRN.placeHolderList[4]" ""
		5 3 "normal_walk_cycleRN" "|normal_walk_cycle:Char_Norman_1|normal_walk_cycle:LocalSpace|normal_walk_cycle:masterCtrl_Norman|normal_walk_cycle:grLocal_All_Rig|normal_walk_cycle:grAll_Ctrl|normal_walk_cycle:gr_All_IK|normal_walk_cycle:grCon_Lf_FootIK|normal_walk_cycle:ctrlIK_Lf_LegIK.rotatePivotTranslate" 
		"normal_walk_cycleRN.placeHolderList[5]" ""
		5 3 "normal_walk_cycleRN" "|normal_walk_cycle:Char_Norman_1|normal_walk_cycle:LocalSpace|normal_walk_cycle:masterCtrl_Norman|normal_walk_cycle:grLocal_All_Rig|normal_walk_cycle:grAll_Ctrl|normal_walk_cycle:gr_All_IK|normal_walk_cycle:grCon_Lf_FootIK|normal_walk_cycle:ctrlIK_Lf_LegIK.rotateOrder" 
		"normal_walk_cycleRN.placeHolderList[6]" ""
		5 3 "normal_walk_cycleRN" "|normal_walk_cycle:Char_Norman_1|normal_walk_cycle:LocalSpace|normal_walk_cycle:masterCtrl_Norman|normal_walk_cycle:grLocal_All_Rig|normal_walk_cycle:grAll_Ctrl|normal_walk_cycle:gr_All_IK|normal_walk_cycle:grCon_Lf_FootIK|normal_walk_cycle:ctrlIK_Lf_LegIK.parentMatrix" 
		"normal_walk_cycleRN.placeHolderList[7]" ""
		5 3 "normal_walk_cycleRN" "|normal_walk_cycle:Char_Norman_1|normal_walk_cycle:LocalSpace|normal_walk_cycle:masterCtrl_Norman|normal_walk_cycle:grLocal_All_Rig|normal_walk_cycle:grAll_Ctrl|normal_walk_cycle:gr_All_IK|normal_walk_cycle:grCon_Rt_FootIK|normal_walk_cycle:ctrlIK_Rt_LegIK.scale" 
		"normal_walk_cycleRN.placeHolderList[8]" ""
		5 3 "normal_walk_cycleRN" "|normal_walk_cycle:Char_Norman_1|normal_walk_cycle:LocalSpace|normal_walk_cycle:masterCtrl_Norman|normal_walk_cycle:grLocal_All_Rig|normal_walk_cycle:grAll_Ctrl|normal_walk_cycle:gr_All_IK|normal_walk_cycle:grCon_Rt_FootIK|normal_walk_cycle:ctrlIK_Rt_LegIK.translate" 
		"normal_walk_cycleRN.placeHolderList[9]" ""
		5 3 "normal_walk_cycleRN" "|normal_walk_cycle:Char_Norman_1|normal_walk_cycle:LocalSpace|normal_walk_cycle:masterCtrl_Norman|normal_walk_cycle:grLocal_All_Rig|normal_walk_cycle:grAll_Ctrl|normal_walk_cycle:gr_All_IK|normal_walk_cycle:grCon_Rt_FootIK|normal_walk_cycle:ctrlIK_Rt_LegIK.rotate" 
		"normal_walk_cycleRN.placeHolderList[10]" ""
		5 3 "normal_walk_cycleRN" "|normal_walk_cycle:Char_Norman_1|normal_walk_cycle:LocalSpace|normal_walk_cycle:masterCtrl_Norman|normal_walk_cycle:grLocal_All_Rig|normal_walk_cycle:grAll_Ctrl|normal_walk_cycle:gr_All_IK|normal_walk_cycle:grCon_Rt_FootIK|normal_walk_cycle:ctrlIK_Rt_LegIK.rotatePivot" 
		"normal_walk_cycleRN.placeHolderList[11]" ""
		5 3 "normal_walk_cycleRN" "|normal_walk_cycle:Char_Norman_1|normal_walk_cycle:LocalSpace|normal_walk_cycle:masterCtrl_Norman|normal_walk_cycle:grLocal_All_Rig|normal_walk_cycle:grAll_Ctrl|normal_walk_cycle:gr_All_IK|normal_walk_cycle:grCon_Rt_FootIK|normal_walk_cycle:ctrlIK_Rt_LegIK.rotatePivotTranslate" 
		"normal_walk_cycleRN.placeHolderList[12]" ""
		5 3 "normal_walk_cycleRN" "|normal_walk_cycle:Char_Norman_1|normal_walk_cycle:LocalSpace|normal_walk_cycle:masterCtrl_Norman|normal_walk_cycle:grLocal_All_Rig|normal_walk_cycle:grAll_Ctrl|normal_walk_cycle:gr_All_IK|normal_walk_cycle:grCon_Rt_FootIK|normal_walk_cycle:ctrlIK_Rt_LegIK.rotateOrder" 
		"normal_walk_cycleRN.placeHolderList[13]" ""
		5 3 "normal_walk_cycleRN" "|normal_walk_cycle:Char_Norman_1|normal_walk_cycle:LocalSpace|normal_walk_cycle:masterCtrl_Norman|normal_walk_cycle:grLocal_All_Rig|normal_walk_cycle:grAll_Ctrl|normal_walk_cycle:gr_All_IK|normal_walk_cycle:grCon_Rt_FootIK|normal_walk_cycle:ctrlIK_Rt_LegIK.parentMatrix" 
		"normal_walk_cycleRN.placeHolderList[14]" ""
		5 3 "normal_walk_cycleRN" "|normal_walk_cycle:Char_Norman_1|normal_walk_cycle:LocalSpace|normal_walk_cycle:masterCtrl_Norman|normal_walk_cycle:grLocal_All_Rig|normal_walk_cycle:grAll_Ctrl|normal_walk_cycle:ZGr_Root_Rig|normal_walk_cycle:jntRig_Root|normal_walk_cycle:ctrlFK_Cn_SpineA|normal_walk_cycle:ctrlFK_Cn_SpineB.rotate" 
		"normal_walk_cycleRN.placeHolderList[15]" ""
		5 3 "normal_walk_cycleRN" "|normal_walk_cycle:Char_Norman_1|normal_walk_cycle:LocalSpace|normal_walk_cycle:masterCtrl_Norman|normal_walk_cycle:grLocal_All_Rig|normal_walk_cycle:grAll_Ctrl|normal_walk_cycle:ZGr_Root_Rig|normal_walk_cycle:jntRig_Root|normal_walk_cycle:ctrlFK_Cn_SpineA|normal_walk_cycle:ctrlFK_Cn_SpineB.rotateOrder" 
		"normal_walk_cycleRN.placeHolderList[16]" ""
		5 3 "normal_walk_cycleRN" "|normal_walk_cycle:Char_Norman_1|normal_walk_cycle:LocalSpace|normal_walk_cycle:masterCtrl_Norman|normal_walk_cycle:grLocal_All_Rig|normal_walk_cycle:grAll_Ctrl|normal_walk_cycle:ZGr_Root_Rig|normal_walk_cycle:jntRig_Root|normal_walk_cycle:ctrlFK_Cn_SpineA|normal_walk_cycle:ctrlFK_Cn_SpineB.parentMatrix" 
		"normal_walk_cycleRN.placeHolderList[17]" ""
		5 3 "normal_walk_cycleRN" "|normal_walk_cycle:Char_Norman_1|normal_walk_cycle:LocalSpace|normal_walk_cycle:masterCtrl_Norman|normal_walk_cycle:grLocal_All_Rig|normal_walk_cycle:grAll_Ctrl|normal_walk_cycle:ZGr_Root_Rig|normal_walk_cycle:jntRig_Root|normal_walk_cycle:ctrlFK_Cn_SpineA|normal_walk_cycle:ctrlFK_Cn_SpineB.jointOrient" 
		"normal_walk_cycleRN.placeHolderList[18]" ""
		5 3 "normal_walk_cycleRN" "|normal_walk_cycle:Char_Norman_1|normal_walk_cycle:LocalSpace|normal_walk_cycle:masterCtrl_Norman|normal_walk_cycle:grLocal_All_Rig|normal_walk_cycle:grAll_Ctrl|normal_walk_cycle:ZGr_Root_Rig|normal_walk_cycle:jntRig_Root|normal_walk_cycle:ctrlFK_Cn_SpineA|normal_walk_cycle:ctrlFK_Cn_SpineB|normal_walk_cycle:ctrlFK_Cn_SpineC.rotate" 
		"normal_walk_cycleRN.placeHolderList[19]" ""
		5 3 "normal_walk_cycleRN" "|normal_walk_cycle:Char_Norman_1|normal_walk_cycle:LocalSpace|normal_walk_cycle:masterCtrl_Norman|normal_walk_cycle:grLocal_All_Rig|normal_walk_cycle:grAll_Ctrl|normal_walk_cycle:ZGr_Root_Rig|normal_walk_cycle:jntRig_Root|normal_walk_cycle:ctrlFK_Cn_SpineA|normal_walk_cycle:ctrlFK_Cn_SpineB|normal_walk_cycle:ctrlFK_Cn_SpineC.rotateOrder" 
		"normal_walk_cycleRN.placeHolderList[20]" ""
		5 3 "normal_walk_cycleRN" "|normal_walk_cycle:Char_Norman_1|normal_walk_cycle:LocalSpace|normal_walk_cycle:masterCtrl_Norman|normal_walk_cycle:grLocal_All_Rig|normal_walk_cycle:grAll_Ctrl|normal_walk_cycle:ZGr_Root_Rig|normal_walk_cycle:jntRig_Root|normal_walk_cycle:ctrlFK_Cn_SpineA|normal_walk_cycle:ctrlFK_Cn_SpineB|normal_walk_cycle:ctrlFK_Cn_SpineC.parentMatrix" 
		"normal_walk_cycleRN.placeHolderList[21]" ""
		5 3 "normal_walk_cycleRN" "|normal_walk_cycle:Char_Norman_1|normal_walk_cycle:LocalSpace|normal_walk_cycle:masterCtrl_Norman|normal_walk_cycle:grLocal_All_Rig|normal_walk_cycle:grAll_Ctrl|normal_walk_cycle:ZGr_Root_Rig|normal_walk_cycle:jntRig_Root|normal_walk_cycle:ctrlFK_Cn_SpineA|normal_walk_cycle:ctrlFK_Cn_SpineB|normal_walk_cycle:ctrlFK_Cn_SpineC.jointOrient" 
		"normal_walk_cycleRN.placeHolderList[22]" ""
		5 3 "normal_walk_cycleRN" "|normal_walk_cycle:Char_Norman_1|normal_walk_cycle:LocalSpace|normal_walk_cycle:masterCtrl_Norman|normal_walk_cycle:grLocal_All_Rig|normal_walk_cycle:grAll_Ctrl|normal_walk_cycle:ZGr_Root_Rig|normal_walk_cycle:jntRig_Root|normal_walk_cycle:ctrlFK_Cn_SpineA|normal_walk_cycle:ctrlFK_Cn_SpineB|normal_walk_cycle:ctrlFK_Cn_SpineC|normal_walk_cycle:ctrlFK_Cn_SpineD.rotate" 
		"normal_walk_cycleRN.placeHolderList[23]" ""
		5 3 "normal_walk_cycleRN" "|normal_walk_cycle:Char_Norman_1|normal_walk_cycle:LocalSpace|normal_walk_cycle:masterCtrl_Norman|normal_walk_cycle:grLocal_All_Rig|normal_walk_cycle:grAll_Ctrl|normal_walk_cycle:ZGr_Root_Rig|normal_walk_cycle:jntRig_Root|normal_walk_cycle:ctrlFK_Cn_SpineA|normal_walk_cycle:ctrlFK_Cn_SpineB|normal_walk_cycle:ctrlFK_Cn_SpineC|normal_walk_cycle:ctrlFK_Cn_SpineD.rotateOrder" 
		"normal_walk_cycleRN.placeHolderList[24]" ""
		5 3 "normal_walk_cycleRN" "|normal_walk_cycle:Char_Norman_1|normal_walk_cycle:LocalSpace|normal_walk_cycle:masterCtrl_Norman|normal_walk_cycle:grLocal_All_Rig|normal_walk_cycle:grAll_Ctrl|normal_walk_cycle:ZGr_Root_Rig|normal_walk_cycle:jntRig_Root|normal_walk_cycle:ctrlFK_Cn_SpineA|normal_walk_cycle:ctrlFK_Cn_SpineB|normal_walk_cycle:ctrlFK_Cn_SpineC|normal_walk_cycle:ctrlFK_Cn_SpineD.parentMatrix" 
		"normal_walk_cycleRN.placeHolderList[25]" ""
		5 3 "normal_walk_cycleRN" "|normal_walk_cycle:Char_Norman_1|normal_walk_cycle:LocalSpace|normal_walk_cycle:masterCtrl_Norman|normal_walk_cycle:grLocal_All_Rig|normal_walk_cycle:grAll_Ctrl|normal_walk_cycle:ZGr_Root_Rig|normal_walk_cycle:jntRig_Root|normal_walk_cycle:ctrlFK_Cn_SpineA|normal_walk_cycle:ctrlFK_Cn_SpineB|normal_walk_cycle:ctrlFK_Cn_SpineC|normal_walk_cycle:ctrlFK_Cn_SpineD.jointOrient" 
		"normal_walk_cycleRN.placeHolderList[26]" ""
		5 3 "normal_walk_cycleRN" "|normal_walk_cycle:Char_Norman_1|normal_walk_cycle:LocalSpace|normal_walk_cycle:masterCtrl_Norman|normal_walk_cycle:grLocal_All_Rig|normal_walk_cycle:grAll_Ctrl|normal_walk_cycle:ZGr_Root_Rig|normal_walk_cycle:jntRig_Root|normal_walk_cycle:ctrlFK_Cn_SpineA|normal_walk_cycle:ctrlFK_Cn_SpineB|normal_walk_cycle:ctrlFK_Cn_SpineC|normal_walk_cycle:ctrlFK_Cn_SpineD|normal_walk_cycle:jntCon_Cn_SpineE|normal_walk_cycle:ctrlFK_Cn_SpineE|normal_walk_cycle:jntCon_Cn_SpineF|normal_walk_cycle:ctrlFK_Cn_SpineF.rotate" 
		"normal_walk_cycleRN.placeHolderList[27]" ""
		5 3 "normal_walk_cycleRN" "|normal_walk_cycle:Char_Norman_1|normal_walk_cycle:LocalSpace|normal_walk_cycle:masterCtrl_Norman|normal_walk_cycle:grLocal_All_Rig|normal_walk_cycle:grAll_Ctrl|normal_walk_cycle:ZGr_Root_Rig|normal_walk_cycle:jntRig_Root|normal_walk_cycle:ctrlFK_Cn_SpineA|normal_walk_cycle:ctrlFK_Cn_SpineB|normal_walk_cycle:ctrlFK_Cn_SpineC|normal_walk_cycle:ctrlFK_Cn_SpineD|normal_walk_cycle:jntCon_Cn_SpineE|normal_walk_cycle:ctrlFK_Cn_SpineE|normal_walk_cycle:jntCon_Cn_SpineF|normal_walk_cycle:ctrlFK_Cn_SpineF.rotateOrder" 
		"normal_walk_cycleRN.placeHolderList[28]" ""
		5 3 "normal_walk_cycleRN" "|normal_walk_cycle:Char_Norman_1|normal_walk_cycle:LocalSpace|normal_walk_cycle:masterCtrl_Norman|normal_walk_cycle:grLocal_All_Rig|normal_walk_cycle:grAll_Ctrl|normal_walk_cycle:ZGr_Root_Rig|normal_walk_cycle:jntRig_Root|normal_walk_cycle:ctrlFK_Cn_SpineA|normal_walk_cycle:ctrlFK_Cn_SpineB|normal_walk_cycle:ctrlFK_Cn_SpineC|normal_walk_cycle:ctrlFK_Cn_SpineD|normal_walk_cycle:jntCon_Cn_SpineE|normal_walk_cycle:ctrlFK_Cn_SpineE|normal_walk_cycle:jntCon_Cn_SpineF|normal_walk_cycle:ctrlFK_Cn_SpineF.parentMatrix" 
		"normal_walk_cycleRN.placeHolderList[29]" ""
		5 3 "normal_walk_cycleRN" "|normal_walk_cycle:Char_Norman_1|normal_walk_cycle:LocalSpace|normal_walk_cycle:masterCtrl_Norman|normal_walk_cycle:grLocal_All_Rig|normal_walk_cycle:grAll_Ctrl|normal_walk_cycle:ZGr_Root_Rig|normal_walk_cycle:jntRig_Root|normal_walk_cycle:ctrlFK_Cn_SpineA|normal_walk_cycle:ctrlFK_Cn_SpineB|normal_walk_cycle:ctrlFK_Cn_SpineC|normal_walk_cycle:ctrlFK_Cn_SpineD|normal_walk_cycle:jntCon_Cn_SpineE|normal_walk_cycle:ctrlFK_Cn_SpineE|normal_walk_cycle:jntCon_Cn_SpineF|normal_walk_cycle:ctrlFK_Cn_SpineF.jointOrient" 
		"normal_walk_cycleRN.placeHolderList[30]" ""
		5 3 "normal_walk_cycleRN" "|normal_walk_cycle:Char_Norman_1|normal_walk_cycle:LocalSpace|normal_walk_cycle:masterCtrl_Norman|normal_walk_cycle:grLocal_All_Rig|normal_walk_cycle:grAll_Ctrl|normal_walk_cycle:ZGr_Root_Rig|normal_walk_cycle:jntRig_Root|normal_walk_cycle:ctrlFK_Cn_SpineA|normal_walk_cycle:ctrlFK_Cn_SpineB|normal_walk_cycle:ctrlFK_Cn_SpineC|normal_walk_cycle:ctrlFK_Cn_SpineD|normal_walk_cycle:Gr_All_Chest|normal_walk_cycle:ZGr_Rt_Clavicle_FK|normal_walk_cycle:ctrlFK_Rt_Clavicle.rotate" 
		"normal_walk_cycleRN.placeHolderList[31]" ""
		5 3 "normal_walk_cycleRN" "|normal_walk_cycle:Char_Norman_1|normal_walk_cycle:LocalSpace|normal_walk_cycle:masterCtrl_Norman|normal_walk_cycle:grLocal_All_Rig|normal_walk_cycle:grAll_Ctrl|normal_walk_cycle:ZGr_Root_Rig|normal_walk_cycle:jntRig_Root|normal_walk_cycle:ctrlFK_Cn_SpineA|normal_walk_cycle:ctrlFK_Cn_SpineB|normal_walk_cycle:ctrlFK_Cn_SpineC|normal_walk_cycle:ctrlFK_Cn_SpineD|normal_walk_cycle:Gr_All_Chest|normal_walk_cycle:ZGr_Rt_Clavicle_FK|normal_walk_cycle:ctrlFK_Rt_Clavicle.rotateOrder" 
		"normal_walk_cycleRN.placeHolderList[32]" ""
		5 3 "normal_walk_cycleRN" "|normal_walk_cycle:Char_Norman_1|normal_walk_cycle:LocalSpace|normal_walk_cycle:masterCtrl_Norman|normal_walk_cycle:grLocal_All_Rig|normal_walk_cycle:grAll_Ctrl|normal_walk_cycle:ZGr_Root_Rig|normal_walk_cycle:jntRig_Root|normal_walk_cycle:ctrlFK_Cn_SpineA|normal_walk_cycle:ctrlFK_Cn_SpineB|normal_walk_cycle:ctrlFK_Cn_SpineC|normal_walk_cycle:ctrlFK_Cn_SpineD|normal_walk_cycle:Gr_All_Chest|normal_walk_cycle:ZGr_Rt_Clavicle_FK|normal_walk_cycle:ctrlFK_Rt_Clavicle.parentMatrix" 
		"normal_walk_cycleRN.placeHolderList[33]" ""
		5 3 "normal_walk_cycleRN" "|normal_walk_cycle:Char_Norman_1|normal_walk_cycle:LocalSpace|normal_walk_cycle:masterCtrl_Norman|normal_walk_cycle:grLocal_All_Rig|normal_walk_cycle:grAll_Ctrl|normal_walk_cycle:ZGr_Root_Rig|normal_walk_cycle:jntRig_Root|normal_walk_cycle:ctrlFK_Cn_SpineA|normal_walk_cycle:ctrlFK_Cn_SpineB|normal_walk_cycle:ctrlFK_Cn_SpineC|normal_walk_cycle:ctrlFK_Cn_SpineD|normal_walk_cycle:Gr_All_Chest|normal_walk_cycle:ZGr_Rt_Clavicle_FK|normal_walk_cycle:ctrlFK_Rt_Clavicle.jointOrient" 
		"normal_walk_cycleRN.placeHolderList[34]" ""
		5 3 "normal_walk_cycleRN" "|normal_walk_cycle:Char_Norman_1|normal_walk_cycle:LocalSpace|normal_walk_cycle:masterCtrl_Norman|normal_walk_cycle:grLocal_All_Rig|normal_walk_cycle:grAll_Ctrl|normal_walk_cycle:ZGr_Root_Rig|normal_walk_cycle:jntRig_Root|normal_walk_cycle:ctrlFK_Cn_SpineA|normal_walk_cycle:ctrlFK_Cn_SpineB|normal_walk_cycle:ctrlFK_Cn_SpineC|normal_walk_cycle:ctrlFK_Cn_SpineD|normal_walk_cycle:Gr_All_Chest|normal_walk_cycle:ZGr_Lf_Clavicle_FK|normal_walk_cycle:ctrlFK_Lf_Clavicle.rotate" 
		"normal_walk_cycleRN.placeHolderList[35]" ""
		5 3 "normal_walk_cycleRN" "|normal_walk_cycle:Char_Norman_1|normal_walk_cycle:LocalSpace|normal_walk_cycle:masterCtrl_Norman|normal_walk_cycle:grLocal_All_Rig|normal_walk_cycle:grAll_Ctrl|normal_walk_cycle:ZGr_Root_Rig|normal_walk_cycle:jntRig_Root|normal_walk_cycle:ctrlFK_Cn_SpineA|normal_walk_cycle:ctrlFK_Cn_SpineB|normal_walk_cycle:ctrlFK_Cn_SpineC|normal_walk_cycle:ctrlFK_Cn_SpineD|normal_walk_cycle:Gr_All_Chest|normal_walk_cycle:ZGr_Lf_Clavicle_FK|normal_walk_cycle:ctrlFK_Lf_Clavicle.rotateOrder" 
		"normal_walk_cycleRN.placeHolderList[36]" ""
		5 3 "normal_walk_cycleRN" "|normal_walk_cycle:Char_Norman_1|normal_walk_cycle:LocalSpace|normal_walk_cycle:masterCtrl_Norman|normal_walk_cycle:grLocal_All_Rig|normal_walk_cycle:grAll_Ctrl|normal_walk_cycle:ZGr_Root_Rig|normal_walk_cycle:jntRig_Root|normal_walk_cycle:ctrlFK_Cn_SpineA|normal_walk_cycle:ctrlFK_Cn_SpineB|normal_walk_cycle:ctrlFK_Cn_SpineC|normal_walk_cycle:ctrlFK_Cn_SpineD|normal_walk_cycle:Gr_All_Chest|normal_walk_cycle:ZGr_Lf_Clavicle_FK|normal_walk_cycle:ctrlFK_Lf_Clavicle.parentMatrix" 
		"normal_walk_cycleRN.placeHolderList[37]" ""
		5 3 "normal_walk_cycleRN" "|normal_walk_cycle:Char_Norman_1|normal_walk_cycle:LocalSpace|normal_walk_cycle:masterCtrl_Norman|normal_walk_cycle:grLocal_All_Rig|normal_walk_cycle:grAll_Ctrl|normal_walk_cycle:ZGr_Root_Rig|normal_walk_cycle:jntRig_Root|normal_walk_cycle:ctrlFK_Cn_SpineA|normal_walk_cycle:ctrlFK_Cn_SpineB|normal_walk_cycle:ctrlFK_Cn_SpineC|normal_walk_cycle:ctrlFK_Cn_SpineD|normal_walk_cycle:Gr_All_Chest|normal_walk_cycle:ZGr_Lf_Clavicle_FK|normal_walk_cycle:ctrlFK_Lf_Clavicle.jointOrient" 
		"normal_walk_cycleRN.placeHolderList[38]" ""
		5 3 "normal_walk_cycleRN" "|normal_walk_cycle:Char_Norman_1|normal_walk_cycle:LocalSpace|normal_walk_cycle:masterCtrl_Norman|normal_walk_cycle:grLocal_All_Rig|normal_walk_cycle:grAll_Ctrl|normal_walk_cycle:ZGr_Lf_ArmA|normal_walk_cycle:jntCon_Lf_ArmA|normal_walk_cycle:ctrlGim_Lf_ArmA|normal_walk_cycle:ctrlFK_Lf_ArmA|normal_walk_cycle:ctrlFK_Lf_ArmB|normal_walk_cycle:ctrlFK_Lf_ArmC.translate" 
		"normal_walk_cycleRN.placeHolderList[39]" ""
		5 3 "normal_walk_cycleRN" "|normal_walk_cycle:Char_Norman_1|normal_walk_cycle:LocalSpace|normal_walk_cycle:masterCtrl_Norman|normal_walk_cycle:grLocal_All_Rig|normal_walk_cycle:grAll_Ctrl|normal_walk_cycle:ZGr_Lf_ArmA|normal_walk_cycle:jntCon_Lf_ArmA|normal_walk_cycle:ctrlGim_Lf_ArmA|normal_walk_cycle:ctrlFK_Lf_ArmA|normal_walk_cycle:ctrlFK_Lf_ArmB|normal_walk_cycle:ctrlFK_Lf_ArmC.scale" 
		"normal_walk_cycleRN.placeHolderList[40]" ""
		5 3 "normal_walk_cycleRN" "|normal_walk_cycle:Char_Norman_1|normal_walk_cycle:LocalSpace|normal_walk_cycle:masterCtrl_Norman|normal_walk_cycle:grLocal_All_Rig|normal_walk_cycle:grAll_Ctrl|normal_walk_cycle:ZGr_Lf_ArmA|normal_walk_cycle:jntCon_Lf_ArmA|normal_walk_cycle:ctrlGim_Lf_ArmA|normal_walk_cycle:ctrlFK_Lf_ArmA|normal_walk_cycle:ctrlFK_Lf_ArmB|normal_walk_cycle:ctrlFK_Lf_ArmC.inverseScale" 
		"normal_walk_cycleRN.placeHolderList[41]" ""
		5 3 "normal_walk_cycleRN" "|normal_walk_cycle:Char_Norman_1|normal_walk_cycle:LocalSpace|normal_walk_cycle:masterCtrl_Norman|normal_walk_cycle:grLocal_All_Rig|normal_walk_cycle:grAll_Ctrl|normal_walk_cycle:ZGr_Lf_ArmA|normal_walk_cycle:jntCon_Lf_ArmA|normal_walk_cycle:ctrlGim_Lf_ArmA|normal_walk_cycle:ctrlFK_Lf_ArmA|normal_walk_cycle:ctrlFK_Lf_ArmB|normal_walk_cycle:ctrlFK_Lf_ArmC.rotate" 
		"normal_walk_cycleRN.placeHolderList[42]" ""
		5 3 "normal_walk_cycleRN" "|normal_walk_cycle:Char_Norman_1|normal_walk_cycle:LocalSpace|normal_walk_cycle:masterCtrl_Norman|normal_walk_cycle:grLocal_All_Rig|normal_walk_cycle:grAll_Ctrl|normal_walk_cycle:ZGr_Lf_ArmA|normal_walk_cycle:jntCon_Lf_ArmA|normal_walk_cycle:ctrlGim_Lf_ArmA|normal_walk_cycle:ctrlFK_Lf_ArmA|normal_walk_cycle:ctrlFK_Lf_ArmB|normal_walk_cycle:ctrlFK_Lf_ArmC.rotatePivot" 
		"normal_walk_cycleRN.placeHolderList[43]" ""
		5 3 "normal_walk_cycleRN" "|normal_walk_cycle:Char_Norman_1|normal_walk_cycle:LocalSpace|normal_walk_cycle:masterCtrl_Norman|normal_walk_cycle:grLocal_All_Rig|normal_walk_cycle:grAll_Ctrl|normal_walk_cycle:ZGr_Lf_ArmA|normal_walk_cycle:jntCon_Lf_ArmA|normal_walk_cycle:ctrlGim_Lf_ArmA|normal_walk_cycle:ctrlFK_Lf_ArmA|normal_walk_cycle:ctrlFK_Lf_ArmB|normal_walk_cycle:ctrlFK_Lf_ArmC.rotatePivotTranslate" 
		"normal_walk_cycleRN.placeHolderList[44]" ""
		5 3 "normal_walk_cycleRN" "|normal_walk_cycle:Char_Norman_1|normal_walk_cycle:LocalSpace|normal_walk_cycle:masterCtrl_Norman|normal_walk_cycle:grLocal_All_Rig|normal_walk_cycle:grAll_Ctrl|normal_walk_cycle:ZGr_Lf_ArmA|normal_walk_cycle:jntCon_Lf_ArmA|normal_walk_cycle:ctrlGim_Lf_ArmA|normal_walk_cycle:ctrlFK_Lf_ArmA|normal_walk_cycle:ctrlFK_Lf_ArmB|normal_walk_cycle:ctrlFK_Lf_ArmC.rotateOrder" 
		"normal_walk_cycleRN.placeHolderList[45]" ""
		5 3 "normal_walk_cycleRN" "|normal_walk_cycle:Char_Norman_1|normal_walk_cycle:LocalSpace|normal_walk_cycle:masterCtrl_Norman|normal_walk_cycle:grLocal_All_Rig|normal_walk_cycle:grAll_Ctrl|normal_walk_cycle:ZGr_Lf_ArmA|normal_walk_cycle:jntCon_Lf_ArmA|normal_walk_cycle:ctrlGim_Lf_ArmA|normal_walk_cycle:ctrlFK_Lf_ArmA|normal_walk_cycle:ctrlFK_Lf_ArmB|normal_walk_cycle:ctrlFK_Lf_ArmC.parentMatrix" 
		"normal_walk_cycleRN.placeHolderList[46]" ""
		5 3 "normal_walk_cycleRN" "|normal_walk_cycle:Char_Norman_1|normal_walk_cycle:LocalSpace|normal_walk_cycle:masterCtrl_Norman|normal_walk_cycle:grLocal_All_Rig|normal_walk_cycle:grAll_Ctrl|normal_walk_cycle:ZGr_Lf_ArmA|normal_walk_cycle:jntCon_Lf_ArmA|normal_walk_cycle:ctrlGim_Lf_ArmA|normal_walk_cycle:ctrlFK_Lf_ArmA|normal_walk_cycle:ctrlFK_Lf_ArmB|normal_walk_cycle:ctrlFK_Lf_ArmC.jointOrient" 
		"normal_walk_cycleRN.placeHolderList[47]" ""
		5 3 "normal_walk_cycleRN" "|normal_walk_cycle:Char_Norman_1|normal_walk_cycle:LocalSpace|normal_walk_cycle:masterCtrl_Norman|normal_walk_cycle:grLocal_All_Rig|normal_walk_cycle:grAll_Ctrl|normal_walk_cycle:ZGr_Lf_ArmA|normal_walk_cycle:jntCon_Lf_ArmA|normal_walk_cycle:ctrlGim_Lf_ArmA|normal_walk_cycle:ctrlFK_Lf_ArmA|normal_walk_cycle:ctrlFK_Lf_ArmB|normal_walk_cycle:ctrlFK_Lf_ArmC.segmentScaleCompensate" 
		"normal_walk_cycleRN.placeHolderList[48]" ""
		5 3 "normal_walk_cycleRN" "|normal_walk_cycle:Char_Norman_1|normal_walk_cycle:LocalSpace|normal_walk_cycle:masterCtrl_Norman|normal_walk_cycle:grLocal_All_Rig|normal_walk_cycle:grAll_Ctrl|normal_walk_cycle:ZGr_Rt_ArmA|normal_walk_cycle:jntCon_Rt_ArmA|normal_walk_cycle:ctrlGim_Rt_ArmA|normal_walk_cycle:ctrlFK_Rt_ArmA|normal_walk_cycle:ctrlFK_Rt_ArmB|normal_walk_cycle:ctrlFK_Rt_ArmC.translate" 
		"normal_walk_cycleRN.placeHolderList[49]" ""
		5 3 "normal_walk_cycleRN" "|normal_walk_cycle:Char_Norman_1|normal_walk_cycle:LocalSpace|normal_walk_cycle:masterCtrl_Norman|normal_walk_cycle:grLocal_All_Rig|normal_walk_cycle:grAll_Ctrl|normal_walk_cycle:ZGr_Rt_ArmA|normal_walk_cycle:jntCon_Rt_ArmA|normal_walk_cycle:ctrlGim_Rt_ArmA|normal_walk_cycle:ctrlFK_Rt_ArmA|normal_walk_cycle:ctrlFK_Rt_ArmB|normal_walk_cycle:ctrlFK_Rt_ArmC.scale" 
		"normal_walk_cycleRN.placeHolderList[50]" ""
		5 3 "normal_walk_cycleRN" "|normal_walk_cycle:Char_Norman_1|normal_walk_cycle:LocalSpace|normal_walk_cycle:masterCtrl_Norman|normal_walk_cycle:grLocal_All_Rig|normal_walk_cycle:grAll_Ctrl|normal_walk_cycle:ZGr_Rt_ArmA|normal_walk_cycle:jntCon_Rt_ArmA|normal_walk_cycle:ctrlGim_Rt_ArmA|normal_walk_cycle:ctrlFK_Rt_ArmA|normal_walk_cycle:ctrlFK_Rt_ArmB|normal_walk_cycle:ctrlFK_Rt_ArmC.inverseScale" 
		"normal_walk_cycleRN.placeHolderList[51]" ""
		5 3 "normal_walk_cycleRN" "|normal_walk_cycle:Char_Norman_1|normal_walk_cycle:LocalSpace|normal_walk_cycle:masterCtrl_Norman|normal_walk_cycle:grLocal_All_Rig|normal_walk_cycle:grAll_Ctrl|normal_walk_cycle:ZGr_Rt_ArmA|normal_walk_cycle:jntCon_Rt_ArmA|normal_walk_cycle:ctrlGim_Rt_ArmA|normal_walk_cycle:ctrlFK_Rt_ArmA|normal_walk_cycle:ctrlFK_Rt_ArmB|normal_walk_cycle:ctrlFK_Rt_ArmC.rotate" 
		"normal_walk_cycleRN.placeHolderList[52]" ""
		5 3 "normal_walk_cycleRN" "|normal_walk_cycle:Char_Norman_1|normal_walk_cycle:LocalSpace|normal_walk_cycle:masterCtrl_Norman|normal_walk_cycle:grLocal_All_Rig|normal_walk_cycle:grAll_Ctrl|normal_walk_cycle:ZGr_Rt_ArmA|normal_walk_cycle:jntCon_Rt_ArmA|normal_walk_cycle:ctrlGim_Rt_ArmA|normal_walk_cycle:ctrlFK_Rt_ArmA|normal_walk_cycle:ctrlFK_Rt_ArmB|normal_walk_cycle:ctrlFK_Rt_ArmC.rotatePivot" 
		"normal_walk_cycleRN.placeHolderList[53]" ""
		5 3 "normal_walk_cycleRN" "|normal_walk_cycle:Char_Norman_1|normal_walk_cycle:LocalSpace|normal_walk_cycle:masterCtrl_Norman|normal_walk_cycle:grLocal_All_Rig|normal_walk_cycle:grAll_Ctrl|normal_walk_cycle:ZGr_Rt_ArmA|normal_walk_cycle:jntCon_Rt_ArmA|normal_walk_cycle:ctrlGim_Rt_ArmA|normal_walk_cycle:ctrlFK_Rt_ArmA|normal_walk_cycle:ctrlFK_Rt_ArmB|normal_walk_cycle:ctrlFK_Rt_ArmC.rotatePivotTranslate" 
		"normal_walk_cycleRN.placeHolderList[54]" ""
		5 3 "normal_walk_cycleRN" "|normal_walk_cycle:Char_Norman_1|normal_walk_cycle:LocalSpace|normal_walk_cycle:masterCtrl_Norman|normal_walk_cycle:grLocal_All_Rig|normal_walk_cycle:grAll_Ctrl|normal_walk_cycle:ZGr_Rt_ArmA|normal_walk_cycle:jntCon_Rt_ArmA|normal_walk_cycle:ctrlGim_Rt_ArmA|normal_walk_cycle:ctrlFK_Rt_ArmA|normal_walk_cycle:ctrlFK_Rt_ArmB|normal_walk_cycle:ctrlFK_Rt_ArmC.rotateOrder" 
		"normal_walk_cycleRN.placeHolderList[55]" ""
		5 3 "normal_walk_cycleRN" "|normal_walk_cycle:Char_Norman_1|normal_walk_cycle:LocalSpace|normal_walk_cycle:masterCtrl_Norman|normal_walk_cycle:grLocal_All_Rig|normal_walk_cycle:grAll_Ctrl|normal_walk_cycle:ZGr_Rt_ArmA|normal_walk_cycle:jntCon_Rt_ArmA|normal_walk_cycle:ctrlGim_Rt_ArmA|normal_walk_cycle:ctrlFK_Rt_ArmA|normal_walk_cycle:ctrlFK_Rt_ArmB|normal_walk_cycle:ctrlFK_Rt_ArmC.parentMatrix" 
		"normal_walk_cycleRN.placeHolderList[56]" ""
		5 3 "normal_walk_cycleRN" "|normal_walk_cycle:Char_Norman_1|normal_walk_cycle:LocalSpace|normal_walk_cycle:masterCtrl_Norman|normal_walk_cycle:grLocal_All_Rig|normal_walk_cycle:grAll_Ctrl|normal_walk_cycle:ZGr_Rt_ArmA|normal_walk_cycle:jntCon_Rt_ArmA|normal_walk_cycle:ctrlGim_Rt_ArmA|normal_walk_cycle:ctrlFK_Rt_ArmA|normal_walk_cycle:ctrlFK_Rt_ArmB|normal_walk_cycle:ctrlFK_Rt_ArmC.jointOrient" 
		"normal_walk_cycleRN.placeHolderList[57]" ""
		5 3 "normal_walk_cycleRN" "|normal_walk_cycle:Char_Norman_1|normal_walk_cycle:LocalSpace|normal_walk_cycle:masterCtrl_Norman|normal_walk_cycle:grLocal_All_Rig|normal_walk_cycle:grAll_Ctrl|normal_walk_cycle:ZGr_Rt_ArmA|normal_walk_cycle:jntCon_Rt_ArmA|normal_walk_cycle:ctrlGim_Rt_ArmA|normal_walk_cycle:ctrlFK_Rt_ArmA|normal_walk_cycle:ctrlFK_Rt_ArmB|normal_walk_cycle:ctrlFK_Rt_ArmC.segmentScaleCompensate" 
		"normal_walk_cycleRN.placeHolderList[58]" ""
		5 3 "normal_walk_cycleRN" "|normal_walk_cycle:Char_Norman_1|normal_walk_cycle:LocalSpace|normal_walk_cycle:masterCtrl_Norman|normal_walk_cycle:grLocal_All_Rig|normal_walk_cycle:grAll_Ctrl|normal_walk_cycle:ctrl_Root.scale" 
		"normal_walk_cycleRN.placeHolderList[59]" ""
		5 3 "normal_walk_cycleRN" "|normal_walk_cycle:Char_Norman_1|normal_walk_cycle:LocalSpace|normal_walk_cycle:masterCtrl_Norman|normal_walk_cycle:grLocal_All_Rig|normal_walk_cycle:grAll_Ctrl|normal_walk_cycle:ctrl_Root.translate" 
		"normal_walk_cycleRN.placeHolderList[60]" ""
		5 3 "normal_walk_cycleRN" "|normal_walk_cycle:Char_Norman_1|normal_walk_cycle:LocalSpace|normal_walk_cycle:masterCtrl_Norman|normal_walk_cycle:grLocal_All_Rig|normal_walk_cycle:grAll_Ctrl|normal_walk_cycle:ctrl_Root.rotate" 
		"normal_walk_cycleRN.placeHolderList[61]" ""
		5 3 "normal_walk_cycleRN" "|normal_walk_cycle:Char_Norman_1|normal_walk_cycle:LocalSpace|normal_walk_cycle:masterCtrl_Norman|normal_walk_cycle:grLocal_All_Rig|normal_walk_cycle:grAll_Ctrl|normal_walk_cycle:ctrl_Root.rotatePivot" 
		"normal_walk_cycleRN.placeHolderList[62]" ""
		5 3 "normal_walk_cycleRN" "|normal_walk_cycle:Char_Norman_1|normal_walk_cycle:LocalSpace|normal_walk_cycle:masterCtrl_Norman|normal_walk_cycle:grLocal_All_Rig|normal_walk_cycle:grAll_Ctrl|normal_walk_cycle:ctrl_Root.rotatePivotTranslate" 
		"normal_walk_cycleRN.placeHolderList[63]" ""
		5 3 "normal_walk_cycleRN" "|normal_walk_cycle:Char_Norman_1|normal_walk_cycle:LocalSpace|normal_walk_cycle:masterCtrl_Norman|normal_walk_cycle:grLocal_All_Rig|normal_walk_cycle:grAll_Ctrl|normal_walk_cycle:ctrl_Root.rotateOrder" 
		"normal_walk_cycleRN.placeHolderList[64]" ""
		5 3 "normal_walk_cycleRN" "|normal_walk_cycle:Char_Norman_1|normal_walk_cycle:LocalSpace|normal_walk_cycle:masterCtrl_Norman|normal_walk_cycle:grLocal_All_Rig|normal_walk_cycle:grAll_Ctrl|normal_walk_cycle:ctrl_Root.parentMatrix" 
		"normal_walk_cycleRN.placeHolderList[65]" "";
	setAttr ".ptag" -type "string" "";
lockNode -l 1 ;
createNode script -n "uiConfigurationScriptNode";
	rename -uid "D9161900-0000-5F5D-5CDC-104400000DDD";
	setAttr ".b" -type "string" (
		"// Maya Mel UI Configuration File.\n//\n//  This script is machine generated.  Edit at your own risk.\n//\n//\n\nglobal string $gMainPane;\nif (`paneLayout -exists $gMainPane`) {\n\n\tglobal int $gUseScenePanelConfig;\n\tint    $useSceneConfig = $gUseScenePanelConfig;\n\tint    $menusOkayInPanels = `optionVar -q allowMenusInPanels`;\tint    $nVisPanes = `paneLayout -q -nvp $gMainPane`;\n\tint    $nPanes = 0;\n\tstring $editorName;\n\tstring $panelName;\n\tstring $itemFilterName;\n\tstring $panelConfig;\n\n\t//\n\t//  get current state of the UI\n\t//\n\tsceneUIReplacement -update $gMainPane;\n\n\t$panelName = `sceneUIReplacement -getNextPanel \"modelPanel\" (localizedPanelLabel(\"Top View\")) `;\n\tif (\"\" == $panelName) {\n\t\tif ($useSceneConfig) {\n\t\t\t$panelName = `modelPanel -unParent -l (localizedPanelLabel(\"Top View\")) -mbv $menusOkayInPanels `;\n\t\t\t$editorName = $panelName;\n            modelEditor -e \n                -camera \"top\" \n                -useInteractiveMode 0\n                -displayLights \"default\" \n                -displayAppearance \"smoothShaded\" \n"
		+ "                -activeOnly 0\n                -ignorePanZoom 0\n                -wireframeOnShaded 0\n                -headsUpDisplay 1\n                -holdOuts 1\n                -selectionHiliteDisplay 1\n                -useDefaultMaterial 0\n                -bufferMode \"double\" \n                -twoSidedLighting 0\n                -backfaceCulling 0\n                -xray 0\n                -jointXray 0\n                -activeComponentsXray 0\n                -displayTextures 0\n                -smoothWireframe 0\n                -lineWidth 1\n                -textureAnisotropic 0\n                -textureHilight 1\n                -textureSampling 2\n                -textureDisplay \"modulate\" \n                -textureMaxSize 16384\n                -fogging 0\n                -fogSource \"fragment\" \n                -fogMode \"linear\" \n                -fogStart 0\n                -fogEnd 100\n                -fogDensity 0.1\n                -fogColor 0.5 0.5 0.5 1 \n                -depthOfFieldPreview 1\n                -maxConstantTransparency 1\n"
		+ "                -rendererName \"base_OpenGL_Renderer\" \n                -objectFilterShowInHUD 1\n                -isFiltered 0\n                -colorResolution 256 256 \n                -bumpResolution 512 512 \n                -textureCompression 0\n                -transparencyAlgorithm \"frontAndBackCull\" \n                -transpInShadows 0\n                -cullingOverride \"none\" \n                -lowQualityLighting 0\n                -maximumNumHardwareLights 1\n                -occlusionCulling 0\n                -shadingModel 0\n                -useBaseRenderer 0\n                -useReducedRenderer 0\n                -smallObjectCulling 0\n                -smallObjectThreshold -1 \n                -interactiveDisableShadows 0\n                -interactiveBackFaceCull 0\n                -sortTransparent 1\n                -nurbsCurves 1\n                -nurbsSurfaces 1\n                -polymeshes 1\n                -subdivSurfaces 1\n                -planes 1\n                -lights 1\n                -cameras 1\n                -controlVertices 1\n"
		+ "                -hulls 1\n                -grid 1\n                -imagePlane 1\n                -joints 1\n                -ikHandles 1\n                -deformers 1\n                -dynamics 1\n                -particleInstancers 1\n                -fluids 1\n                -hairSystems 1\n                -follicles 1\n                -nCloths 1\n                -nParticles 1\n                -nRigids 1\n                -dynamicConstraints 1\n                -locators 1\n                -manipulators 1\n                -pluginShapes 1\n                -dimensions 1\n                -handles 1\n                -pivots 1\n                -textures 1\n                -strokes 1\n                -motionTrails 1\n                -clipGhosts 1\n                -greasePencils 1\n                -shadows 0\n                -captureSequenceNumber -1\n                -width 1\n                -height 1\n                -sceneRenderFilter 0\n                $editorName;\n            modelEditor -e -viewSelected 0 $editorName;\n            modelEditor -e \n"
		+ "                -pluginObjects \"gpuCacheDisplayFilter\" 1 \n                $editorName;\n\t\t}\n\t} else {\n\t\t$label = `panel -q -label $panelName`;\n\t\tmodelPanel -edit -l (localizedPanelLabel(\"Top View\")) -mbv $menusOkayInPanels  $panelName;\n\t\t$editorName = $panelName;\n        modelEditor -e \n            -camera \"top\" \n            -useInteractiveMode 0\n            -displayLights \"default\" \n            -displayAppearance \"smoothShaded\" \n            -activeOnly 0\n            -ignorePanZoom 0\n            -wireframeOnShaded 0\n            -headsUpDisplay 1\n            -holdOuts 1\n            -selectionHiliteDisplay 1\n            -useDefaultMaterial 0\n            -bufferMode \"double\" \n            -twoSidedLighting 0\n            -backfaceCulling 0\n            -xray 0\n            -jointXray 0\n            -activeComponentsXray 0\n            -displayTextures 0\n            -smoothWireframe 0\n            -lineWidth 1\n            -textureAnisotropic 0\n            -textureHilight 1\n            -textureSampling 2\n            -textureDisplay \"modulate\" \n"
		+ "            -textureMaxSize 16384\n            -fogging 0\n            -fogSource \"fragment\" \n            -fogMode \"linear\" \n            -fogStart 0\n            -fogEnd 100\n            -fogDensity 0.1\n            -fogColor 0.5 0.5 0.5 1 \n            -depthOfFieldPreview 1\n            -maxConstantTransparency 1\n            -rendererName \"base_OpenGL_Renderer\" \n            -objectFilterShowInHUD 1\n            -isFiltered 0\n            -colorResolution 256 256 \n            -bumpResolution 512 512 \n            -textureCompression 0\n            -transparencyAlgorithm \"frontAndBackCull\" \n            -transpInShadows 0\n            -cullingOverride \"none\" \n            -lowQualityLighting 0\n            -maximumNumHardwareLights 1\n            -occlusionCulling 0\n            -shadingModel 0\n            -useBaseRenderer 0\n            -useReducedRenderer 0\n            -smallObjectCulling 0\n            -smallObjectThreshold -1 \n            -interactiveDisableShadows 0\n            -interactiveBackFaceCull 0\n            -sortTransparent 1\n"
		+ "            -nurbsCurves 1\n            -nurbsSurfaces 1\n            -polymeshes 1\n            -subdivSurfaces 1\n            -planes 1\n            -lights 1\n            -cameras 1\n            -controlVertices 1\n            -hulls 1\n            -grid 1\n            -imagePlane 1\n            -joints 1\n            -ikHandles 1\n            -deformers 1\n            -dynamics 1\n            -particleInstancers 1\n            -fluids 1\n            -hairSystems 1\n            -follicles 1\n            -nCloths 1\n            -nParticles 1\n            -nRigids 1\n            -dynamicConstraints 1\n            -locators 1\n            -manipulators 1\n            -pluginShapes 1\n            -dimensions 1\n            -handles 1\n            -pivots 1\n            -textures 1\n            -strokes 1\n            -motionTrails 1\n            -clipGhosts 1\n            -greasePencils 1\n            -shadows 0\n            -captureSequenceNumber -1\n            -width 1\n            -height 1\n            -sceneRenderFilter 0\n            $editorName;\n"
		+ "        modelEditor -e -viewSelected 0 $editorName;\n        modelEditor -e \n            -pluginObjects \"gpuCacheDisplayFilter\" 1 \n            $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextPanel \"modelPanel\" (localizedPanelLabel(\"Side View\")) `;\n\tif (\"\" == $panelName) {\n\t\tif ($useSceneConfig) {\n\t\t\t$panelName = `modelPanel -unParent -l (localizedPanelLabel(\"Side View\")) -mbv $menusOkayInPanels `;\n\t\t\t$editorName = $panelName;\n            modelEditor -e \n                -camera \"side\" \n                -useInteractiveMode 0\n                -displayLights \"default\" \n                -displayAppearance \"smoothShaded\" \n                -activeOnly 0\n                -ignorePanZoom 0\n                -wireframeOnShaded 0\n                -headsUpDisplay 1\n                -holdOuts 1\n                -selectionHiliteDisplay 1\n                -useDefaultMaterial 0\n                -bufferMode \"double\" \n                -twoSidedLighting 0\n                -backfaceCulling 0\n"
		+ "                -xray 0\n                -jointXray 0\n                -activeComponentsXray 0\n                -displayTextures 0\n                -smoothWireframe 0\n                -lineWidth 1\n                -textureAnisotropic 0\n                -textureHilight 1\n                -textureSampling 2\n                -textureDisplay \"modulate\" \n                -textureMaxSize 16384\n                -fogging 0\n                -fogSource \"fragment\" \n                -fogMode \"linear\" \n                -fogStart 0\n                -fogEnd 100\n                -fogDensity 0.1\n                -fogColor 0.5 0.5 0.5 1 \n                -depthOfFieldPreview 1\n                -maxConstantTransparency 1\n                -rendererName \"base_OpenGL_Renderer\" \n                -objectFilterShowInHUD 1\n                -isFiltered 0\n                -colorResolution 256 256 \n                -bumpResolution 512 512 \n                -textureCompression 0\n                -transparencyAlgorithm \"frontAndBackCull\" \n                -transpInShadows 0\n"
		+ "                -cullingOverride \"none\" \n                -lowQualityLighting 0\n                -maximumNumHardwareLights 1\n                -occlusionCulling 0\n                -shadingModel 0\n                -useBaseRenderer 0\n                -useReducedRenderer 0\n                -smallObjectCulling 0\n                -smallObjectThreshold -1 \n                -interactiveDisableShadows 0\n                -interactiveBackFaceCull 0\n                -sortTransparent 1\n                -nurbsCurves 1\n                -nurbsSurfaces 1\n                -polymeshes 1\n                -subdivSurfaces 1\n                -planes 1\n                -lights 1\n                -cameras 1\n                -controlVertices 1\n                -hulls 1\n                -grid 1\n                -imagePlane 1\n                -joints 1\n                -ikHandles 1\n                -deformers 1\n                -dynamics 1\n                -particleInstancers 1\n                -fluids 1\n                -hairSystems 1\n                -follicles 1\n                -nCloths 1\n"
		+ "                -nParticles 1\n                -nRigids 1\n                -dynamicConstraints 1\n                -locators 1\n                -manipulators 1\n                -pluginShapes 1\n                -dimensions 1\n                -handles 1\n                -pivots 1\n                -textures 1\n                -strokes 1\n                -motionTrails 1\n                -clipGhosts 1\n                -greasePencils 1\n                -shadows 0\n                -captureSequenceNumber -1\n                -width 1\n                -height 1\n                -sceneRenderFilter 0\n                $editorName;\n            modelEditor -e -viewSelected 0 $editorName;\n            modelEditor -e \n                -pluginObjects \"gpuCacheDisplayFilter\" 1 \n                $editorName;\n\t\t}\n\t} else {\n\t\t$label = `panel -q -label $panelName`;\n\t\tmodelPanel -edit -l (localizedPanelLabel(\"Side View\")) -mbv $menusOkayInPanels  $panelName;\n\t\t$editorName = $panelName;\n        modelEditor -e \n            -camera \"side\" \n            -useInteractiveMode 0\n"
		+ "            -displayLights \"default\" \n            -displayAppearance \"smoothShaded\" \n            -activeOnly 0\n            -ignorePanZoom 0\n            -wireframeOnShaded 0\n            -headsUpDisplay 1\n            -holdOuts 1\n            -selectionHiliteDisplay 1\n            -useDefaultMaterial 0\n            -bufferMode \"double\" \n            -twoSidedLighting 0\n            -backfaceCulling 0\n            -xray 0\n            -jointXray 0\n            -activeComponentsXray 0\n            -displayTextures 0\n            -smoothWireframe 0\n            -lineWidth 1\n            -textureAnisotropic 0\n            -textureHilight 1\n            -textureSampling 2\n            -textureDisplay \"modulate\" \n            -textureMaxSize 16384\n            -fogging 0\n            -fogSource \"fragment\" \n            -fogMode \"linear\" \n            -fogStart 0\n            -fogEnd 100\n            -fogDensity 0.1\n            -fogColor 0.5 0.5 0.5 1 \n            -depthOfFieldPreview 1\n            -maxConstantTransparency 1\n            -rendererName \"base_OpenGL_Renderer\" \n"
		+ "            -objectFilterShowInHUD 1\n            -isFiltered 0\n            -colorResolution 256 256 \n            -bumpResolution 512 512 \n            -textureCompression 0\n            -transparencyAlgorithm \"frontAndBackCull\" \n            -transpInShadows 0\n            -cullingOverride \"none\" \n            -lowQualityLighting 0\n            -maximumNumHardwareLights 1\n            -occlusionCulling 0\n            -shadingModel 0\n            -useBaseRenderer 0\n            -useReducedRenderer 0\n            -smallObjectCulling 0\n            -smallObjectThreshold -1 \n            -interactiveDisableShadows 0\n            -interactiveBackFaceCull 0\n            -sortTransparent 1\n            -nurbsCurves 1\n            -nurbsSurfaces 1\n            -polymeshes 1\n            -subdivSurfaces 1\n            -planes 1\n            -lights 1\n            -cameras 1\n            -controlVertices 1\n            -hulls 1\n            -grid 1\n            -imagePlane 1\n            -joints 1\n            -ikHandles 1\n            -deformers 1\n"
		+ "            -dynamics 1\n            -particleInstancers 1\n            -fluids 1\n            -hairSystems 1\n            -follicles 1\n            -nCloths 1\n            -nParticles 1\n            -nRigids 1\n            -dynamicConstraints 1\n            -locators 1\n            -manipulators 1\n            -pluginShapes 1\n            -dimensions 1\n            -handles 1\n            -pivots 1\n            -textures 1\n            -strokes 1\n            -motionTrails 1\n            -clipGhosts 1\n            -greasePencils 1\n            -shadows 0\n            -captureSequenceNumber -1\n            -width 1\n            -height 1\n            -sceneRenderFilter 0\n            $editorName;\n        modelEditor -e -viewSelected 0 $editorName;\n        modelEditor -e \n            -pluginObjects \"gpuCacheDisplayFilter\" 1 \n            $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextPanel \"modelPanel\" (localizedPanelLabel(\"Front View\")) `;\n\tif (\"\" == $panelName) {\n"
		+ "\t\tif ($useSceneConfig) {\n\t\t\t$panelName = `modelPanel -unParent -l (localizedPanelLabel(\"Front View\")) -mbv $menusOkayInPanels `;\n\t\t\t$editorName = $panelName;\n            modelEditor -e \n                -camera \"front\" \n                -useInteractiveMode 0\n                -displayLights \"default\" \n                -displayAppearance \"smoothShaded\" \n                -activeOnly 0\n                -ignorePanZoom 0\n                -wireframeOnShaded 0\n                -headsUpDisplay 1\n                -holdOuts 1\n                -selectionHiliteDisplay 1\n                -useDefaultMaterial 0\n                -bufferMode \"double\" \n                -twoSidedLighting 0\n                -backfaceCulling 0\n                -xray 0\n                -jointXray 0\n                -activeComponentsXray 0\n                -displayTextures 0\n                -smoothWireframe 0\n                -lineWidth 1\n                -textureAnisotropic 0\n                -textureHilight 1\n                -textureSampling 2\n                -textureDisplay \"modulate\" \n"
		+ "                -textureMaxSize 16384\n                -fogging 0\n                -fogSource \"fragment\" \n                -fogMode \"linear\" \n                -fogStart 0\n                -fogEnd 100\n                -fogDensity 0.1\n                -fogColor 0.5 0.5 0.5 1 \n                -depthOfFieldPreview 1\n                -maxConstantTransparency 1\n                -rendererName \"base_OpenGL_Renderer\" \n                -objectFilterShowInHUD 1\n                -isFiltered 0\n                -colorResolution 256 256 \n                -bumpResolution 512 512 \n                -textureCompression 0\n                -transparencyAlgorithm \"frontAndBackCull\" \n                -transpInShadows 0\n                -cullingOverride \"none\" \n                -lowQualityLighting 0\n                -maximumNumHardwareLights 1\n                -occlusionCulling 0\n                -shadingModel 0\n                -useBaseRenderer 0\n                -useReducedRenderer 0\n                -smallObjectCulling 0\n                -smallObjectThreshold -1 \n"
		+ "                -interactiveDisableShadows 0\n                -interactiveBackFaceCull 0\n                -sortTransparent 1\n                -nurbsCurves 1\n                -nurbsSurfaces 1\n                -polymeshes 1\n                -subdivSurfaces 1\n                -planes 1\n                -lights 1\n                -cameras 1\n                -controlVertices 1\n                -hulls 1\n                -grid 1\n                -imagePlane 1\n                -joints 1\n                -ikHandles 1\n                -deformers 1\n                -dynamics 1\n                -particleInstancers 1\n                -fluids 1\n                -hairSystems 1\n                -follicles 1\n                -nCloths 1\n                -nParticles 1\n                -nRigids 1\n                -dynamicConstraints 1\n                -locators 1\n                -manipulators 1\n                -pluginShapes 1\n                -dimensions 1\n                -handles 1\n                -pivots 1\n                -textures 1\n                -strokes 1\n"
		+ "                -motionTrails 1\n                -clipGhosts 1\n                -greasePencils 1\n                -shadows 0\n                -captureSequenceNumber -1\n                -width 1\n                -height 1\n                -sceneRenderFilter 0\n                $editorName;\n            modelEditor -e -viewSelected 0 $editorName;\n            modelEditor -e \n                -pluginObjects \"gpuCacheDisplayFilter\" 1 \n                $editorName;\n\t\t}\n\t} else {\n\t\t$label = `panel -q -label $panelName`;\n\t\tmodelPanel -edit -l (localizedPanelLabel(\"Front View\")) -mbv $menusOkayInPanels  $panelName;\n\t\t$editorName = $panelName;\n        modelEditor -e \n            -camera \"front\" \n            -useInteractiveMode 0\n            -displayLights \"default\" \n            -displayAppearance \"smoothShaded\" \n            -activeOnly 0\n            -ignorePanZoom 0\n            -wireframeOnShaded 0\n            -headsUpDisplay 1\n            -holdOuts 1\n            -selectionHiliteDisplay 1\n            -useDefaultMaterial 0\n            -bufferMode \"double\" \n"
		+ "            -twoSidedLighting 0\n            -backfaceCulling 0\n            -xray 0\n            -jointXray 0\n            -activeComponentsXray 0\n            -displayTextures 0\n            -smoothWireframe 0\n            -lineWidth 1\n            -textureAnisotropic 0\n            -textureHilight 1\n            -textureSampling 2\n            -textureDisplay \"modulate\" \n            -textureMaxSize 16384\n            -fogging 0\n            -fogSource \"fragment\" \n            -fogMode \"linear\" \n            -fogStart 0\n            -fogEnd 100\n            -fogDensity 0.1\n            -fogColor 0.5 0.5 0.5 1 \n            -depthOfFieldPreview 1\n            -maxConstantTransparency 1\n            -rendererName \"base_OpenGL_Renderer\" \n            -objectFilterShowInHUD 1\n            -isFiltered 0\n            -colorResolution 256 256 \n            -bumpResolution 512 512 \n            -textureCompression 0\n            -transparencyAlgorithm \"frontAndBackCull\" \n            -transpInShadows 0\n            -cullingOverride \"none\" \n            -lowQualityLighting 0\n"
		+ "            -maximumNumHardwareLights 1\n            -occlusionCulling 0\n            -shadingModel 0\n            -useBaseRenderer 0\n            -useReducedRenderer 0\n            -smallObjectCulling 0\n            -smallObjectThreshold -1 \n            -interactiveDisableShadows 0\n            -interactiveBackFaceCull 0\n            -sortTransparent 1\n            -nurbsCurves 1\n            -nurbsSurfaces 1\n            -polymeshes 1\n            -subdivSurfaces 1\n            -planes 1\n            -lights 1\n            -cameras 1\n            -controlVertices 1\n            -hulls 1\n            -grid 1\n            -imagePlane 1\n            -joints 1\n            -ikHandles 1\n            -deformers 1\n            -dynamics 1\n            -particleInstancers 1\n            -fluids 1\n            -hairSystems 1\n            -follicles 1\n            -nCloths 1\n            -nParticles 1\n            -nRigids 1\n            -dynamicConstraints 1\n            -locators 1\n            -manipulators 1\n            -pluginShapes 1\n            -dimensions 1\n"
		+ "            -handles 1\n            -pivots 1\n            -textures 1\n            -strokes 1\n            -motionTrails 1\n            -clipGhosts 1\n            -greasePencils 1\n            -shadows 0\n            -captureSequenceNumber -1\n            -width 1\n            -height 1\n            -sceneRenderFilter 0\n            $editorName;\n        modelEditor -e -viewSelected 0 $editorName;\n        modelEditor -e \n            -pluginObjects \"gpuCacheDisplayFilter\" 1 \n            $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextPanel \"modelPanel\" (localizedPanelLabel(\"Persp View\")) `;\n\tif (\"\" == $panelName) {\n\t\tif ($useSceneConfig) {\n\t\t\t$panelName = `modelPanel -unParent -l (localizedPanelLabel(\"Persp View\")) -mbv $menusOkayInPanels `;\n\t\t\t$editorName = $panelName;\n            modelEditor -e \n                -camera \"persp\" \n                -useInteractiveMode 0\n                -displayLights \"default\" \n                -displayAppearance \"wireframe\" \n"
		+ "                -activeOnly 0\n                -ignorePanZoom 0\n                -wireframeOnShaded 0\n                -headsUpDisplay 1\n                -holdOuts 1\n                -selectionHiliteDisplay 1\n                -useDefaultMaterial 0\n                -bufferMode \"double\" \n                -twoSidedLighting 0\n                -backfaceCulling 0\n                -xray 0\n                -jointXray 0\n                -activeComponentsXray 0\n                -displayTextures 0\n                -smoothWireframe 0\n                -lineWidth 1\n                -textureAnisotropic 0\n                -textureHilight 1\n                -textureSampling 2\n                -textureDisplay \"modulate\" \n                -textureMaxSize 16384\n                -fogging 0\n                -fogSource \"fragment\" \n                -fogMode \"linear\" \n                -fogStart 0\n                -fogEnd 100\n                -fogDensity 0.1\n                -fogColor 0.5 0.5 0.5 1 \n                -depthOfFieldPreview 1\n                -maxConstantTransparency 1\n"
		+ "                -rendererName \"base_OpenGL_Renderer\" \n                -objectFilterShowInHUD 1\n                -isFiltered 0\n                -colorResolution 256 256 \n                -bumpResolution 512 512 \n                -textureCompression 0\n                -transparencyAlgorithm \"frontAndBackCull\" \n                -transpInShadows 0\n                -cullingOverride \"none\" \n                -lowQualityLighting 0\n                -maximumNumHardwareLights 1\n                -occlusionCulling 0\n                -shadingModel 0\n                -useBaseRenderer 0\n                -useReducedRenderer 0\n                -smallObjectCulling 0\n                -smallObjectThreshold -1 \n                -interactiveDisableShadows 0\n                -interactiveBackFaceCull 0\n                -sortTransparent 1\n                -nurbsCurves 1\n                -nurbsSurfaces 1\n                -polymeshes 1\n                -subdivSurfaces 1\n                -planes 1\n                -lights 1\n                -cameras 1\n                -controlVertices 1\n"
		+ "                -hulls 1\n                -grid 1\n                -imagePlane 1\n                -joints 1\n                -ikHandles 1\n                -deformers 1\n                -dynamics 1\n                -particleInstancers 1\n                -fluids 1\n                -hairSystems 1\n                -follicles 1\n                -nCloths 1\n                -nParticles 1\n                -nRigids 1\n                -dynamicConstraints 1\n                -locators 1\n                -manipulators 1\n                -pluginShapes 1\n                -dimensions 1\n                -handles 1\n                -pivots 1\n                -textures 1\n                -strokes 1\n                -motionTrails 1\n                -clipGhosts 1\n                -greasePencils 1\n                -shadows 0\n                -captureSequenceNumber -1\n                -width 1284\n                -height 725\n                -sceneRenderFilter 0\n                $editorName;\n            modelEditor -e -viewSelected 0 $editorName;\n            modelEditor -e \n"
		+ "                -pluginObjects \"gpuCacheDisplayFilter\" 1 \n                $editorName;\n\t\t}\n\t} else {\n\t\t$label = `panel -q -label $panelName`;\n\t\tmodelPanel -edit -l (localizedPanelLabel(\"Persp View\")) -mbv $menusOkayInPanels  $panelName;\n\t\t$editorName = $panelName;\n        modelEditor -e \n            -camera \"persp\" \n            -useInteractiveMode 0\n            -displayLights \"default\" \n            -displayAppearance \"wireframe\" \n            -activeOnly 0\n            -ignorePanZoom 0\n            -wireframeOnShaded 0\n            -headsUpDisplay 1\n            -holdOuts 1\n            -selectionHiliteDisplay 1\n            -useDefaultMaterial 0\n            -bufferMode \"double\" \n            -twoSidedLighting 0\n            -backfaceCulling 0\n            -xray 0\n            -jointXray 0\n            -activeComponentsXray 0\n            -displayTextures 0\n            -smoothWireframe 0\n            -lineWidth 1\n            -textureAnisotropic 0\n            -textureHilight 1\n            -textureSampling 2\n            -textureDisplay \"modulate\" \n"
		+ "            -textureMaxSize 16384\n            -fogging 0\n            -fogSource \"fragment\" \n            -fogMode \"linear\" \n            -fogStart 0\n            -fogEnd 100\n            -fogDensity 0.1\n            -fogColor 0.5 0.5 0.5 1 \n            -depthOfFieldPreview 1\n            -maxConstantTransparency 1\n            -rendererName \"base_OpenGL_Renderer\" \n            -objectFilterShowInHUD 1\n            -isFiltered 0\n            -colorResolution 256 256 \n            -bumpResolution 512 512 \n            -textureCompression 0\n            -transparencyAlgorithm \"frontAndBackCull\" \n            -transpInShadows 0\n            -cullingOverride \"none\" \n            -lowQualityLighting 0\n            -maximumNumHardwareLights 1\n            -occlusionCulling 0\n            -shadingModel 0\n            -useBaseRenderer 0\n            -useReducedRenderer 0\n            -smallObjectCulling 0\n            -smallObjectThreshold -1 \n            -interactiveDisableShadows 0\n            -interactiveBackFaceCull 0\n            -sortTransparent 1\n"
		+ "            -nurbsCurves 1\n            -nurbsSurfaces 1\n            -polymeshes 1\n            -subdivSurfaces 1\n            -planes 1\n            -lights 1\n            -cameras 1\n            -controlVertices 1\n            -hulls 1\n            -grid 1\n            -imagePlane 1\n            -joints 1\n            -ikHandles 1\n            -deformers 1\n            -dynamics 1\n            -particleInstancers 1\n            -fluids 1\n            -hairSystems 1\n            -follicles 1\n            -nCloths 1\n            -nParticles 1\n            -nRigids 1\n            -dynamicConstraints 1\n            -locators 1\n            -manipulators 1\n            -pluginShapes 1\n            -dimensions 1\n            -handles 1\n            -pivots 1\n            -textures 1\n            -strokes 1\n            -motionTrails 1\n            -clipGhosts 1\n            -greasePencils 1\n            -shadows 0\n            -captureSequenceNumber -1\n            -width 1284\n            -height 725\n            -sceneRenderFilter 0\n            $editorName;\n"
		+ "        modelEditor -e -viewSelected 0 $editorName;\n        modelEditor -e \n            -pluginObjects \"gpuCacheDisplayFilter\" 1 \n            $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextPanel \"outlinerPanel\" (localizedPanelLabel(\"ToggledOutliner\")) `;\n\tif (\"\" == $panelName) {\n\t\tif ($useSceneConfig) {\n\t\t\t$panelName = `outlinerPanel -unParent -l (localizedPanelLabel(\"ToggledOutliner\")) -mbv $menusOkayInPanels `;\n\t\t\t$editorName = $panelName;\n            outlinerEditor -e \n                -showShapes 0\n                -showAssignedMaterials 0\n                -showTimeEditor 1\n                -showReferenceNodes 0\n                -showReferenceMembers 0\n                -showAttributes 0\n                -showConnected 0\n                -showAnimCurvesOnly 0\n                -showMuteInfo 0\n                -organizeByLayer 1\n                -showAnimLayerWeight 1\n                -autoExpandLayers 1\n                -autoExpand 0\n                -showDagOnly 1\n"
		+ "                -showAssets 1\n                -showContainedOnly 1\n                -showPublishedAsConnected 0\n                -showContainerContents 1\n                -ignoreDagHierarchy 0\n                -expandConnections 0\n                -showUpstreamCurves 1\n                -showUnitlessCurves 1\n                -showCompounds 1\n                -showLeafs 1\n                -showNumericAttrsOnly 0\n                -highlightActive 1\n                -autoSelectNewObjects 0\n                -doNotSelectNewObjects 0\n                -dropIsParent 1\n                -transmitFilters 0\n                -setFilter \"defaultSetFilter\" \n                -showSetMembers 1\n                -allowMultiSelection 1\n                -alwaysToggleSelect 0\n                -directSelect 0\n                -isSet 0\n                -isSetMember 0\n                -displayMode \"DAG\" \n                -expandObjects 0\n                -setsIgnoreFilters 1\n                -containersIgnoreFilters 0\n                -editAttrName 0\n                -showAttrValues 0\n"
		+ "                -highlightSecondary 0\n                -showUVAttrsOnly 0\n                -showTextureNodesOnly 0\n                -attrAlphaOrder \"default\" \n                -animLayerFilterOptions \"allAffecting\" \n                -sortOrder \"none\" \n                -longNames 0\n                -niceNames 1\n                -showNamespace 1\n                -showPinIcons 0\n                -mapMotionTrails 0\n                -ignoreHiddenAttribute 0\n                -ignoreOutlinerColor 0\n                -renderFilterVisible 0\n                -renderFilterIndex 0\n                -selectionOrder \"chronological\" \n                -expandAttribute 0\n                $editorName;\n\t\t}\n\t} else {\n\t\t$label = `panel -q -label $panelName`;\n\t\toutlinerPanel -edit -l (localizedPanelLabel(\"ToggledOutliner\")) -mbv $menusOkayInPanels  $panelName;\n\t\t$editorName = $panelName;\n        outlinerEditor -e \n            -showShapes 0\n            -showAssignedMaterials 0\n            -showTimeEditor 1\n            -showReferenceNodes 0\n            -showReferenceMembers 0\n"
		+ "            -showAttributes 0\n            -showConnected 0\n            -showAnimCurvesOnly 0\n            -showMuteInfo 0\n            -organizeByLayer 1\n            -showAnimLayerWeight 1\n            -autoExpandLayers 1\n            -autoExpand 0\n            -showDagOnly 1\n            -showAssets 1\n            -showContainedOnly 1\n            -showPublishedAsConnected 0\n            -showContainerContents 1\n            -ignoreDagHierarchy 0\n            -expandConnections 0\n            -showUpstreamCurves 1\n            -showUnitlessCurves 1\n            -showCompounds 1\n            -showLeafs 1\n            -showNumericAttrsOnly 0\n            -highlightActive 1\n            -autoSelectNewObjects 0\n            -doNotSelectNewObjects 0\n            -dropIsParent 1\n            -transmitFilters 0\n            -setFilter \"defaultSetFilter\" \n            -showSetMembers 1\n            -allowMultiSelection 1\n            -alwaysToggleSelect 0\n            -directSelect 0\n            -isSet 0\n            -isSetMember 0\n            -displayMode \"DAG\" \n"
		+ "            -expandObjects 0\n            -setsIgnoreFilters 1\n            -containersIgnoreFilters 0\n            -editAttrName 0\n            -showAttrValues 0\n            -highlightSecondary 0\n            -showUVAttrsOnly 0\n            -showTextureNodesOnly 0\n            -attrAlphaOrder \"default\" \n            -animLayerFilterOptions \"allAffecting\" \n            -sortOrder \"none\" \n            -longNames 0\n            -niceNames 1\n            -showNamespace 1\n            -showPinIcons 0\n            -mapMotionTrails 0\n            -ignoreHiddenAttribute 0\n            -ignoreOutlinerColor 0\n            -renderFilterVisible 0\n            -renderFilterIndex 0\n            -selectionOrder \"chronological\" \n            -expandAttribute 0\n            $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextPanel \"outlinerPanel\" (localizedPanelLabel(\"Outliner\")) `;\n\tif (\"\" == $panelName) {\n\t\tif ($useSceneConfig) {\n\t\t\t$panelName = `outlinerPanel -unParent -l (localizedPanelLabel(\"Outliner\")) -mbv $menusOkayInPanels `;\n"
		+ "\t\t\t$editorName = $panelName;\n            outlinerEditor -e \n                -showShapes 0\n                -showAssignedMaterials 0\n                -showTimeEditor 1\n                -showReferenceNodes 0\n                -showReferenceMembers 0\n                -showAttributes 0\n                -showConnected 0\n                -showAnimCurvesOnly 0\n                -showMuteInfo 0\n                -organizeByLayer 1\n                -showAnimLayerWeight 1\n                -autoExpandLayers 1\n                -autoExpand 0\n                -showDagOnly 1\n                -showAssets 1\n                -showContainedOnly 1\n                -showPublishedAsConnected 0\n                -showContainerContents 1\n                -ignoreDagHierarchy 0\n                -expandConnections 0\n                -showUpstreamCurves 1\n                -showUnitlessCurves 1\n                -showCompounds 1\n                -showLeafs 1\n                -showNumericAttrsOnly 0\n                -highlightActive 1\n                -autoSelectNewObjects 0\n"
		+ "                -doNotSelectNewObjects 0\n                -dropIsParent 1\n                -transmitFilters 0\n                -setFilter \"defaultSetFilter\" \n                -showSetMembers 1\n                -allowMultiSelection 1\n                -alwaysToggleSelect 0\n                -directSelect 0\n                -displayMode \"DAG\" \n                -expandObjects 0\n                -setsIgnoreFilters 1\n                -containersIgnoreFilters 0\n                -editAttrName 0\n                -showAttrValues 0\n                -highlightSecondary 0\n                -showUVAttrsOnly 0\n                -showTextureNodesOnly 0\n                -attrAlphaOrder \"default\" \n                -animLayerFilterOptions \"allAffecting\" \n                -sortOrder \"none\" \n                -longNames 0\n                -niceNames 1\n                -showNamespace 1\n                -showPinIcons 0\n                -mapMotionTrails 0\n                -ignoreHiddenAttribute 0\n                -ignoreOutlinerColor 0\n                -renderFilterVisible 0\n"
		+ "                $editorName;\n\t\t}\n\t} else {\n\t\t$label = `panel -q -label $panelName`;\n\t\toutlinerPanel -edit -l (localizedPanelLabel(\"Outliner\")) -mbv $menusOkayInPanels  $panelName;\n\t\t$editorName = $panelName;\n        outlinerEditor -e \n            -showShapes 0\n            -showAssignedMaterials 0\n            -showTimeEditor 1\n            -showReferenceNodes 0\n            -showReferenceMembers 0\n            -showAttributes 0\n            -showConnected 0\n            -showAnimCurvesOnly 0\n            -showMuteInfo 0\n            -organizeByLayer 1\n            -showAnimLayerWeight 1\n            -autoExpandLayers 1\n            -autoExpand 0\n            -showDagOnly 1\n            -showAssets 1\n            -showContainedOnly 1\n            -showPublishedAsConnected 0\n            -showContainerContents 1\n            -ignoreDagHierarchy 0\n            -expandConnections 0\n            -showUpstreamCurves 1\n            -showUnitlessCurves 1\n            -showCompounds 1\n            -showLeafs 1\n            -showNumericAttrsOnly 0\n"
		+ "            -highlightActive 1\n            -autoSelectNewObjects 0\n            -doNotSelectNewObjects 0\n            -dropIsParent 1\n            -transmitFilters 0\n            -setFilter \"defaultSetFilter\" \n            -showSetMembers 1\n            -allowMultiSelection 1\n            -alwaysToggleSelect 0\n            -directSelect 0\n            -displayMode \"DAG\" \n            -expandObjects 0\n            -setsIgnoreFilters 1\n            -containersIgnoreFilters 0\n            -editAttrName 0\n            -showAttrValues 0\n            -highlightSecondary 0\n            -showUVAttrsOnly 0\n            -showTextureNodesOnly 0\n            -attrAlphaOrder \"default\" \n            -animLayerFilterOptions \"allAffecting\" \n            -sortOrder \"none\" \n            -longNames 0\n            -niceNames 1\n            -showNamespace 1\n            -showPinIcons 0\n            -mapMotionTrails 0\n            -ignoreHiddenAttribute 0\n            -ignoreOutlinerColor 0\n            -renderFilterVisible 0\n            $editorName;\n\t\tif (!$useSceneConfig) {\n"
		+ "\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"graphEditor\" (localizedPanelLabel(\"Graph Editor\")) `;\n\tif (\"\" == $panelName) {\n\t\tif ($useSceneConfig) {\n\t\t\t$panelName = `scriptedPanel -unParent  -type \"graphEditor\" -l (localizedPanelLabel(\"Graph Editor\")) -mbv $menusOkayInPanels `;\n\n\t\t\t$editorName = ($panelName+\"OutlineEd\");\n            outlinerEditor -e \n                -showShapes 1\n                -showAssignedMaterials 0\n                -showTimeEditor 1\n                -showReferenceNodes 0\n                -showReferenceMembers 0\n                -showAttributes 1\n                -showConnected 1\n                -showAnimCurvesOnly 1\n                -showMuteInfo 0\n                -organizeByLayer 1\n                -showAnimLayerWeight 1\n                -autoExpandLayers 1\n                -autoExpand 1\n                -showDagOnly 0\n                -showAssets 1\n                -showContainedOnly 0\n                -showPublishedAsConnected 0\n                -showContainerContents 0\n"
		+ "                -ignoreDagHierarchy 0\n                -expandConnections 1\n                -showUpstreamCurves 1\n                -showUnitlessCurves 1\n                -showCompounds 0\n                -showLeafs 1\n                -showNumericAttrsOnly 1\n                -highlightActive 0\n                -autoSelectNewObjects 1\n                -doNotSelectNewObjects 0\n                -dropIsParent 1\n                -transmitFilters 1\n                -setFilter \"0\" \n                -showSetMembers 0\n                -allowMultiSelection 1\n                -alwaysToggleSelect 0\n                -directSelect 0\n                -displayMode \"DAG\" \n                -expandObjects 0\n                -setsIgnoreFilters 1\n                -containersIgnoreFilters 0\n                -editAttrName 0\n                -showAttrValues 0\n                -highlightSecondary 0\n                -showUVAttrsOnly 0\n                -showTextureNodesOnly 0\n                -attrAlphaOrder \"default\" \n                -animLayerFilterOptions \"allAffecting\" \n"
		+ "                -sortOrder \"none\" \n                -longNames 0\n                -niceNames 1\n                -showNamespace 1\n                -showPinIcons 1\n                -mapMotionTrails 1\n                -ignoreHiddenAttribute 0\n                -ignoreOutlinerColor 0\n                -renderFilterVisible 0\n                $editorName;\n\n\t\t\t$editorName = ($panelName+\"GraphEd\");\n            animCurveEditor -e \n                -displayKeys 1\n                -displayTangents 0\n                -displayActiveKeys 0\n                -displayActiveKeyTangents 1\n                -displayInfinities 0\n                -displayValues 0\n                -autoFit 1\n                -snapTime \"integer\" \n                -snapValue \"none\" \n                -showResults \"off\" \n                -showBufferCurves \"off\" \n                -smoothness \"fine\" \n                -resultSamples 1.041667\n                -resultScreenSamples 0\n                -resultUpdate \"delayed\" \n                -showUpstreamCurves 1\n                -showCurveNames 0\n"
		+ "                -showActiveCurveNames 0\n                -stackedCurves 0\n                -stackedCurvesMin -1\n                -stackedCurvesMax 1\n                -stackedCurvesSpace 0.2\n                -displayNormalized 0\n                -preSelectionHighlight 0\n                -constrainDrag 0\n                -classicMode 1\n                -valueLinesToggle 1\n                $editorName;\n\t\t}\n\t} else {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Graph Editor\")) -mbv $menusOkayInPanels  $panelName;\n\n\t\t\t$editorName = ($panelName+\"OutlineEd\");\n            outlinerEditor -e \n                -showShapes 1\n                -showAssignedMaterials 0\n                -showTimeEditor 1\n                -showReferenceNodes 0\n                -showReferenceMembers 0\n                -showAttributes 1\n                -showConnected 1\n                -showAnimCurvesOnly 1\n                -showMuteInfo 0\n                -organizeByLayer 1\n                -showAnimLayerWeight 1\n                -autoExpandLayers 1\n"
		+ "                -autoExpand 1\n                -showDagOnly 0\n                -showAssets 1\n                -showContainedOnly 0\n                -showPublishedAsConnected 0\n                -showContainerContents 0\n                -ignoreDagHierarchy 0\n                -expandConnections 1\n                -showUpstreamCurves 1\n                -showUnitlessCurves 1\n                -showCompounds 0\n                -showLeafs 1\n                -showNumericAttrsOnly 1\n                -highlightActive 0\n                -autoSelectNewObjects 1\n                -doNotSelectNewObjects 0\n                -dropIsParent 1\n                -transmitFilters 1\n                -setFilter \"0\" \n                -showSetMembers 0\n                -allowMultiSelection 1\n                -alwaysToggleSelect 0\n                -directSelect 0\n                -displayMode \"DAG\" \n                -expandObjects 0\n                -setsIgnoreFilters 1\n                -containersIgnoreFilters 0\n                -editAttrName 0\n                -showAttrValues 0\n"
		+ "                -highlightSecondary 0\n                -showUVAttrsOnly 0\n                -showTextureNodesOnly 0\n                -attrAlphaOrder \"default\" \n                -animLayerFilterOptions \"allAffecting\" \n                -sortOrder \"none\" \n                -longNames 0\n                -niceNames 1\n                -showNamespace 1\n                -showPinIcons 1\n                -mapMotionTrails 1\n                -ignoreHiddenAttribute 0\n                -ignoreOutlinerColor 0\n                -renderFilterVisible 0\n                $editorName;\n\n\t\t\t$editorName = ($panelName+\"GraphEd\");\n            animCurveEditor -e \n                -displayKeys 1\n                -displayTangents 0\n                -displayActiveKeys 0\n                -displayActiveKeyTangents 1\n                -displayInfinities 0\n                -displayValues 0\n                -autoFit 1\n                -snapTime \"integer\" \n                -snapValue \"none\" \n                -showResults \"off\" \n                -showBufferCurves \"off\" \n                -smoothness \"fine\" \n"
		+ "                -resultSamples 1.041667\n                -resultScreenSamples 0\n                -resultUpdate \"delayed\" \n                -showUpstreamCurves 1\n                -showCurveNames 0\n                -showActiveCurveNames 0\n                -stackedCurves 0\n                -stackedCurvesMin -1\n                -stackedCurvesMax 1\n                -stackedCurvesSpace 0.2\n                -displayNormalized 0\n                -preSelectionHighlight 0\n                -constrainDrag 0\n                -classicMode 1\n                -valueLinesToggle 1\n                $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"dopeSheetPanel\" (localizedPanelLabel(\"Dope Sheet\")) `;\n\tif (\"\" == $panelName) {\n\t\tif ($useSceneConfig) {\n\t\t\t$panelName = `scriptedPanel -unParent  -type \"dopeSheetPanel\" -l (localizedPanelLabel(\"Dope Sheet\")) -mbv $menusOkayInPanels `;\n\n\t\t\t$editorName = ($panelName+\"OutlineEd\");\n            outlinerEditor -e \n                -showShapes 1\n"
		+ "                -showAssignedMaterials 0\n                -showTimeEditor 1\n                -showReferenceNodes 0\n                -showReferenceMembers 0\n                -showAttributes 1\n                -showConnected 1\n                -showAnimCurvesOnly 1\n                -showMuteInfo 0\n                -organizeByLayer 1\n                -showAnimLayerWeight 1\n                -autoExpandLayers 1\n                -autoExpand 0\n                -showDagOnly 0\n                -showAssets 1\n                -showContainedOnly 0\n                -showPublishedAsConnected 0\n                -showContainerContents 0\n                -ignoreDagHierarchy 0\n                -expandConnections 1\n                -showUpstreamCurves 1\n                -showUnitlessCurves 0\n                -showCompounds 1\n                -showLeafs 1\n                -showNumericAttrsOnly 1\n                -highlightActive 0\n                -autoSelectNewObjects 0\n                -doNotSelectNewObjects 1\n                -dropIsParent 1\n                -transmitFilters 0\n"
		+ "                -setFilter \"0\" \n                -showSetMembers 0\n                -allowMultiSelection 1\n                -alwaysToggleSelect 0\n                -directSelect 0\n                -displayMode \"DAG\" \n                -expandObjects 0\n                -setsIgnoreFilters 1\n                -containersIgnoreFilters 0\n                -editAttrName 0\n                -showAttrValues 0\n                -highlightSecondary 0\n                -showUVAttrsOnly 0\n                -showTextureNodesOnly 0\n                -attrAlphaOrder \"default\" \n                -animLayerFilterOptions \"allAffecting\" \n                -sortOrder \"none\" \n                -longNames 0\n                -niceNames 1\n                -showNamespace 1\n                -showPinIcons 0\n                -mapMotionTrails 1\n                -ignoreHiddenAttribute 0\n                -ignoreOutlinerColor 0\n                -renderFilterVisible 0\n                $editorName;\n\n\t\t\t$editorName = ($panelName+\"DopeSheetEd\");\n            dopeSheetEditor -e \n                -displayKeys 1\n"
		+ "                -displayTangents 0\n                -displayActiveKeys 0\n                -displayActiveKeyTangents 0\n                -displayInfinities 0\n                -displayValues 0\n                -autoFit 0\n                -snapTime \"integer\" \n                -snapValue \"none\" \n                -outliner \"dopeSheetPanel1OutlineEd\" \n                -showSummary 1\n                -showScene 0\n                -hierarchyBelow 0\n                -showTicks 1\n                -selectionWindow 0 0 0 0 \n                $editorName;\n\t\t}\n\t} else {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Dope Sheet\")) -mbv $menusOkayInPanels  $panelName;\n\n\t\t\t$editorName = ($panelName+\"OutlineEd\");\n            outlinerEditor -e \n                -showShapes 1\n                -showAssignedMaterials 0\n                -showTimeEditor 1\n                -showReferenceNodes 0\n                -showReferenceMembers 0\n                -showAttributes 1\n                -showConnected 1\n                -showAnimCurvesOnly 1\n"
		+ "                -showMuteInfo 0\n                -organizeByLayer 1\n                -showAnimLayerWeight 1\n                -autoExpandLayers 1\n                -autoExpand 0\n                -showDagOnly 0\n                -showAssets 1\n                -showContainedOnly 0\n                -showPublishedAsConnected 0\n                -showContainerContents 0\n                -ignoreDagHierarchy 0\n                -expandConnections 1\n                -showUpstreamCurves 1\n                -showUnitlessCurves 0\n                -showCompounds 1\n                -showLeafs 1\n                -showNumericAttrsOnly 1\n                -highlightActive 0\n                -autoSelectNewObjects 0\n                -doNotSelectNewObjects 1\n                -dropIsParent 1\n                -transmitFilters 0\n                -setFilter \"0\" \n                -showSetMembers 0\n                -allowMultiSelection 1\n                -alwaysToggleSelect 0\n                -directSelect 0\n                -displayMode \"DAG\" \n                -expandObjects 0\n"
		+ "                -setsIgnoreFilters 1\n                -containersIgnoreFilters 0\n                -editAttrName 0\n                -showAttrValues 0\n                -highlightSecondary 0\n                -showUVAttrsOnly 0\n                -showTextureNodesOnly 0\n                -attrAlphaOrder \"default\" \n                -animLayerFilterOptions \"allAffecting\" \n                -sortOrder \"none\" \n                -longNames 0\n                -niceNames 1\n                -showNamespace 1\n                -showPinIcons 0\n                -mapMotionTrails 1\n                -ignoreHiddenAttribute 0\n                -ignoreOutlinerColor 0\n                -renderFilterVisible 0\n                $editorName;\n\n\t\t\t$editorName = ($panelName+\"DopeSheetEd\");\n            dopeSheetEditor -e \n                -displayKeys 1\n                -displayTangents 0\n                -displayActiveKeys 0\n                -displayActiveKeyTangents 0\n                -displayInfinities 0\n                -displayValues 0\n                -autoFit 0\n                -snapTime \"integer\" \n"
		+ "                -snapValue \"none\" \n                -outliner \"dopeSheetPanel1OutlineEd\" \n                -showSummary 1\n                -showScene 0\n                -hierarchyBelow 0\n                -showTicks 1\n                -selectionWindow 0 0 0 0 \n                $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"timeEditorPanel\" (localizedPanelLabel(\"Time Editor\")) `;\n\tif (\"\" == $panelName) {\n\t\tif ($useSceneConfig) {\n\t\t\t$panelName = `scriptedPanel -unParent  -type \"timeEditorPanel\" -l (localizedPanelLabel(\"Time Editor\")) -mbv $menusOkayInPanels `;\n\t\t}\n\t} else {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Time Editor\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"clipEditorPanel\" (localizedPanelLabel(\"Trax Editor\")) `;\n\tif (\"\" == $panelName) {\n\t\tif ($useSceneConfig) {\n"
		+ "\t\t\t$panelName = `scriptedPanel -unParent  -type \"clipEditorPanel\" -l (localizedPanelLabel(\"Trax Editor\")) -mbv $menusOkayInPanels `;\n\n\t\t\t$editorName = clipEditorNameFromPanel($panelName);\n            clipEditor -e \n                -displayKeys 0\n                -displayTangents 0\n                -displayActiveKeys 0\n                -displayActiveKeyTangents 0\n                -displayInfinities 0\n                -displayValues 0\n                -autoFit 0\n                -snapTime \"none\" \n                -snapValue \"none\" \n                -initialized 0\n                -manageSequencer 0 \n                $editorName;\n\t\t}\n\t} else {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Trax Editor\")) -mbv $menusOkayInPanels  $panelName;\n\n\t\t\t$editorName = clipEditorNameFromPanel($panelName);\n            clipEditor -e \n                -displayKeys 0\n                -displayTangents 0\n                -displayActiveKeys 0\n                -displayActiveKeyTangents 0\n                -displayInfinities 0\n"
		+ "                -displayValues 0\n                -autoFit 0\n                -snapTime \"none\" \n                -snapValue \"none\" \n                -initialized 0\n                -manageSequencer 0 \n                $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"sequenceEditorPanel\" (localizedPanelLabel(\"Camera Sequencer\")) `;\n\tif (\"\" == $panelName) {\n\t\tif ($useSceneConfig) {\n\t\t\t$panelName = `scriptedPanel -unParent  -type \"sequenceEditorPanel\" -l (localizedPanelLabel(\"Camera Sequencer\")) -mbv $menusOkayInPanels `;\n\n\t\t\t$editorName = sequenceEditorNameFromPanel($panelName);\n            clipEditor -e \n                -displayKeys 0\n                -displayTangents 0\n                -displayActiveKeys 0\n                -displayActiveKeyTangents 0\n                -displayInfinities 0\n                -displayValues 0\n                -autoFit 0\n                -snapTime \"none\" \n                -snapValue \"none\" \n                -initialized 0\n"
		+ "                -manageSequencer 1 \n                $editorName;\n\t\t}\n\t} else {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Camera Sequencer\")) -mbv $menusOkayInPanels  $panelName;\n\n\t\t\t$editorName = sequenceEditorNameFromPanel($panelName);\n            clipEditor -e \n                -displayKeys 0\n                -displayTangents 0\n                -displayActiveKeys 0\n                -displayActiveKeyTangents 0\n                -displayInfinities 0\n                -displayValues 0\n                -autoFit 0\n                -snapTime \"none\" \n                -snapValue \"none\" \n                -initialized 0\n                -manageSequencer 1 \n                $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"hyperGraphPanel\" (localizedPanelLabel(\"Hypergraph Hierarchy\")) `;\n\tif (\"\" == $panelName) {\n\t\tif ($useSceneConfig) {\n\t\t\t$panelName = `scriptedPanel -unParent  -type \"hyperGraphPanel\" -l (localizedPanelLabel(\"Hypergraph Hierarchy\")) -mbv $menusOkayInPanels `;\n"
		+ "\n\t\t\t$editorName = ($panelName+\"HyperGraphEd\");\n            hyperGraph -e \n                -graphLayoutStyle \"hierarchicalLayout\" \n                -orientation \"horiz\" \n                -mergeConnections 0\n                -zoom 1\n                -animateTransition 0\n                -showRelationships 1\n                -showShapes 0\n                -showDeformers 0\n                -showExpressions 0\n                -showConstraints 0\n                -showConnectionFromSelected 0\n                -showConnectionToSelected 0\n                -showConstraintLabels 0\n                -showUnderworld 0\n                -showInvisible 0\n                -transitionFrames 1\n                -opaqueContainers 0\n                -freeform 0\n                -imagePosition 0 0 \n                -imageScale 1\n                -imageEnabled 0\n                -graphType \"DAG\" \n                -heatMapDisplay 0\n                -updateSelection 1\n                -updateNodeAdded 1\n                -useDrawOverrideColor 0\n                -limitGraphTraversal -1\n"
		+ "                -range 0 0 \n                -iconSize \"smallIcons\" \n                -showCachedConnections 0\n                $editorName;\n\t\t}\n\t} else {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Hypergraph Hierarchy\")) -mbv $menusOkayInPanels  $panelName;\n\n\t\t\t$editorName = ($panelName+\"HyperGraphEd\");\n            hyperGraph -e \n                -graphLayoutStyle \"hierarchicalLayout\" \n                -orientation \"horiz\" \n                -mergeConnections 0\n                -zoom 1\n                -animateTransition 0\n                -showRelationships 1\n                -showShapes 0\n                -showDeformers 0\n                -showExpressions 0\n                -showConstraints 0\n                -showConnectionFromSelected 0\n                -showConnectionToSelected 0\n                -showConstraintLabels 0\n                -showUnderworld 0\n                -showInvisible 0\n                -transitionFrames 1\n                -opaqueContainers 0\n                -freeform 0\n"
		+ "                -imagePosition 0 0 \n                -imageScale 1\n                -imageEnabled 0\n                -graphType \"DAG\" \n                -heatMapDisplay 0\n                -updateSelection 1\n                -updateNodeAdded 1\n                -useDrawOverrideColor 0\n                -limitGraphTraversal -1\n                -range 0 0 \n                -iconSize \"smallIcons\" \n                -showCachedConnections 0\n                $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"hyperShadePanel\" (localizedPanelLabel(\"Hypershade\")) `;\n\tif (\"\" == $panelName) {\n\t\tif ($useSceneConfig) {\n\t\t\t$panelName = `scriptedPanel -unParent  -type \"hyperShadePanel\" -l (localizedPanelLabel(\"Hypershade\")) -mbv $menusOkayInPanels `;\n\t\t}\n\t} else {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Hypershade\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n"
		+ "\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"visorPanel\" (localizedPanelLabel(\"Visor\")) `;\n\tif (\"\" == $panelName) {\n\t\tif ($useSceneConfig) {\n\t\t\t$panelName = `scriptedPanel -unParent  -type \"visorPanel\" -l (localizedPanelLabel(\"Visor\")) -mbv $menusOkayInPanels `;\n\t\t}\n\t} else {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Visor\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"nodeEditorPanel\" (localizedPanelLabel(\"Node Editor\")) `;\n\tif (\"\" == $panelName) {\n\t\tif ($useSceneConfig) {\n\t\t\t$panelName = `scriptedPanel -unParent  -type \"nodeEditorPanel\" -l (localizedPanelLabel(\"Node Editor\")) -mbv $menusOkayInPanels `;\n\n\t\t\t$editorName = ($panelName+\"NodeEditorEd\");\n            nodeEditor -e \n                -allAttributes 0\n                -allNodes 0\n                -autoSizeNodes 1\n                -consistentNameSize 1\n                -createNodeCommand \"nodeEdCreateNodeCommand\" \n"
		+ "                -defaultPinnedState 0\n                -additiveGraphingMode 0\n                -settingsChangedCallback \"nodeEdSyncControls\" \n                -traversalDepthLimit -1\n                -keyPressCommand \"nodeEdKeyPressCommand\" \n                -nodeTitleMode \"name\" \n                -gridSnap 0\n                -gridVisibility 1\n                -popupMenuScript \"nodeEdBuildPanelMenus\" \n                -showNamespace 1\n                -showShapes 1\n                -showSGShapes 0\n                -showTransforms 1\n                -useAssets 1\n                -syncedSelection 1\n                -extendToShapes 1\n                -activeTab -1\n                -editorMode \"default\" \n                $editorName;\n\t\t}\n\t} else {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Node Editor\")) -mbv $menusOkayInPanels  $panelName;\n\n\t\t\t$editorName = ($panelName+\"NodeEditorEd\");\n            nodeEditor -e \n                -allAttributes 0\n                -allNodes 0\n                -autoSizeNodes 1\n"
		+ "                -consistentNameSize 1\n                -createNodeCommand \"nodeEdCreateNodeCommand\" \n                -defaultPinnedState 0\n                -additiveGraphingMode 0\n                -settingsChangedCallback \"nodeEdSyncControls\" \n                -traversalDepthLimit -1\n                -keyPressCommand \"nodeEdKeyPressCommand\" \n                -nodeTitleMode \"name\" \n                -gridSnap 0\n                -gridVisibility 1\n                -popupMenuScript \"nodeEdBuildPanelMenus\" \n                -showNamespace 1\n                -showShapes 1\n                -showSGShapes 0\n                -showTransforms 1\n                -useAssets 1\n                -syncedSelection 1\n                -extendToShapes 1\n                -activeTab -1\n                -editorMode \"default\" \n                $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"createNodePanel\" (localizedPanelLabel(\"Create Node\")) `;\n\tif (\"\" == $panelName) {\n"
		+ "\t\tif ($useSceneConfig) {\n\t\t\t$panelName = `scriptedPanel -unParent  -type \"createNodePanel\" -l (localizedPanelLabel(\"Create Node\")) -mbv $menusOkayInPanels `;\n\t\t}\n\t} else {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Create Node\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"polyTexturePlacementPanel\" (localizedPanelLabel(\"UV Editor\")) `;\n\tif (\"\" == $panelName) {\n\t\tif ($useSceneConfig) {\n\t\t\t$panelName = `scriptedPanel -unParent  -type \"polyTexturePlacementPanel\" -l (localizedPanelLabel(\"UV Editor\")) -mbv $menusOkayInPanels `;\n\t\t}\n\t} else {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"UV Editor\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"renderWindowPanel\" (localizedPanelLabel(\"Render View\")) `;\n"
		+ "\tif (\"\" == $panelName) {\n\t\tif ($useSceneConfig) {\n\t\t\t$panelName = `scriptedPanel -unParent  -type \"renderWindowPanel\" -l (localizedPanelLabel(\"Render View\")) -mbv $menusOkayInPanels `;\n\t\t}\n\t} else {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Render View\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextPanel \"shapePanel\" (localizedPanelLabel(\"Shape Editor\")) `;\n\tif (\"\" == $panelName) {\n\t\tif ($useSceneConfig) {\n\t\t\tshapePanel -unParent -l (localizedPanelLabel(\"Shape Editor\")) -mbv $menusOkayInPanels ;\n\t\t}\n\t} else {\n\t\t$label = `panel -q -label $panelName`;\n\t\tshapePanel -edit -l (localizedPanelLabel(\"Shape Editor\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextPanel \"posePanel\" (localizedPanelLabel(\"Pose Editor\")) `;\n\tif (\"\" == $panelName) {\n\t\tif ($useSceneConfig) {\n\t\t\tposePanel -unParent -l (localizedPanelLabel(\"Pose Editor\")) -mbv $menusOkayInPanels ;\n"
		+ "\t\t}\n\t} else {\n\t\t$label = `panel -q -label $panelName`;\n\t\tposePanel -edit -l (localizedPanelLabel(\"Pose Editor\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"dynRelEdPanel\" (localizedPanelLabel(\"Dynamic Relationships\")) `;\n\tif (\"\" == $panelName) {\n\t\tif ($useSceneConfig) {\n\t\t\t$panelName = `scriptedPanel -unParent  -type \"dynRelEdPanel\" -l (localizedPanelLabel(\"Dynamic Relationships\")) -mbv $menusOkayInPanels `;\n\t\t}\n\t} else {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Dynamic Relationships\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"relationshipPanel\" (localizedPanelLabel(\"Relationship Editor\")) `;\n\tif (\"\" == $panelName) {\n\t\tif ($useSceneConfig) {\n\t\t\t$panelName = `scriptedPanel -unParent  -type \"relationshipPanel\" -l (localizedPanelLabel(\"Relationship Editor\")) -mbv $menusOkayInPanels `;\n"
		+ "\t\t}\n\t} else {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Relationship Editor\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"referenceEditorPanel\" (localizedPanelLabel(\"Reference Editor\")) `;\n\tif (\"\" == $panelName) {\n\t\tif ($useSceneConfig) {\n\t\t\t$panelName = `scriptedPanel -unParent  -type \"referenceEditorPanel\" -l (localizedPanelLabel(\"Reference Editor\")) -mbv $menusOkayInPanels `;\n\t\t}\n\t} else {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Reference Editor\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"componentEditorPanel\" (localizedPanelLabel(\"Component Editor\")) `;\n\tif (\"\" == $panelName) {\n\t\tif ($useSceneConfig) {\n\t\t\t$panelName = `scriptedPanel -unParent  -type \"componentEditorPanel\" -l (localizedPanelLabel(\"Component Editor\")) -mbv $menusOkayInPanels `;\n"
		+ "\t\t}\n\t} else {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Component Editor\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"dynPaintScriptedPanelType\" (localizedPanelLabel(\"Paint Effects\")) `;\n\tif (\"\" == $panelName) {\n\t\tif ($useSceneConfig) {\n\t\t\t$panelName = `scriptedPanel -unParent  -type \"dynPaintScriptedPanelType\" -l (localizedPanelLabel(\"Paint Effects\")) -mbv $menusOkayInPanels `;\n\t\t}\n\t} else {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Paint Effects\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"scriptEditorPanel\" (localizedPanelLabel(\"Script Editor\")) `;\n\tif (\"\" == $panelName) {\n\t\tif ($useSceneConfig) {\n\t\t\t$panelName = `scriptedPanel -unParent  -type \"scriptEditorPanel\" -l (localizedPanelLabel(\"Script Editor\")) -mbv $menusOkayInPanels `;\n"
		+ "\t\t}\n\t} else {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Script Editor\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"profilerPanel\" (localizedPanelLabel(\"Profiler Tool\")) `;\n\tif (\"\" == $panelName) {\n\t\tif ($useSceneConfig) {\n\t\t\t$panelName = `scriptedPanel -unParent  -type \"profilerPanel\" -l (localizedPanelLabel(\"Profiler Tool\")) -mbv $menusOkayInPanels `;\n\t\t}\n\t} else {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Profiler Tool\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"contentBrowserPanel\" (localizedPanelLabel(\"Content Browser\")) `;\n\tif (\"\" == $panelName) {\n\t\tif ($useSceneConfig) {\n\t\t\t$panelName = `scriptedPanel -unParent  -type \"contentBrowserPanel\" -l (localizedPanelLabel(\"Content Browser\")) -mbv $menusOkayInPanels `;\n"
		+ "\t\t}\n\t} else {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Content Browser\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\tif ($useSceneConfig) {\n        string $configName = `getPanel -cwl (localizedPanelLabel(\"Current Layout\"))`;\n        if (\"\" != $configName) {\n\t\t\tpanelConfiguration -edit -label (localizedPanelLabel(\"Current Layout\")) \n\t\t\t\t-userCreated false\n\t\t\t\t-defaultImage \"\"\n\t\t\t\t-image \"\"\n\t\t\t\t-sc false\n\t\t\t\t-configString \"global string $gMainPane; paneLayout -e -cn \\\"single\\\" -ps 1 100 100 $gMainPane;\"\n\t\t\t\t-removeAllPanels\n\t\t\t\t-ap false\n\t\t\t\t\t(localizedPanelLabel(\"Persp View\")) \n\t\t\t\t\t\"modelPanel\"\n"
		+ "\t\t\t\t\t\"$panelName = `modelPanel -unParent -l (localizedPanelLabel(\\\"Persp View\\\")) -mbv $menusOkayInPanels `;\\n$editorName = $panelName;\\nmodelEditor -e \\n    -cam `findStartUpCamera persp` \\n    -useInteractiveMode 0\\n    -displayLights \\\"default\\\" \\n    -displayAppearance \\\"wireframe\\\" \\n    -activeOnly 0\\n    -ignorePanZoom 0\\n    -wireframeOnShaded 0\\n    -headsUpDisplay 1\\n    -holdOuts 1\\n    -selectionHiliteDisplay 1\\n    -useDefaultMaterial 0\\n    -bufferMode \\\"double\\\" \\n    -twoSidedLighting 0\\n    -backfaceCulling 0\\n    -xray 0\\n    -jointXray 0\\n    -activeComponentsXray 0\\n    -displayTextures 0\\n    -smoothWireframe 0\\n    -lineWidth 1\\n    -textureAnisotropic 0\\n    -textureHilight 1\\n    -textureSampling 2\\n    -textureDisplay \\\"modulate\\\" \\n    -textureMaxSize 16384\\n    -fogging 0\\n    -fogSource \\\"fragment\\\" \\n    -fogMode \\\"linear\\\" \\n    -fogStart 0\\n    -fogEnd 100\\n    -fogDensity 0.1\\n    -fogColor 0.5 0.5 0.5 1 \\n    -depthOfFieldPreview 1\\n    -maxConstantTransparency 1\\n    -rendererName \\\"base_OpenGL_Renderer\\\" \\n    -objectFilterShowInHUD 1\\n    -isFiltered 0\\n    -colorResolution 256 256 \\n    -bumpResolution 512 512 \\n    -textureCompression 0\\n    -transparencyAlgorithm \\\"frontAndBackCull\\\" \\n    -transpInShadows 0\\n    -cullingOverride \\\"none\\\" \\n    -lowQualityLighting 0\\n    -maximumNumHardwareLights 1\\n    -occlusionCulling 0\\n    -shadingModel 0\\n    -useBaseRenderer 0\\n    -useReducedRenderer 0\\n    -smallObjectCulling 0\\n    -smallObjectThreshold -1 \\n    -interactiveDisableShadows 0\\n    -interactiveBackFaceCull 0\\n    -sortTransparent 1\\n    -nurbsCurves 1\\n    -nurbsSurfaces 1\\n    -polymeshes 1\\n    -subdivSurfaces 1\\n    -planes 1\\n    -lights 1\\n    -cameras 1\\n    -controlVertices 1\\n    -hulls 1\\n    -grid 1\\n    -imagePlane 1\\n    -joints 1\\n    -ikHandles 1\\n    -deformers 1\\n    -dynamics 1\\n    -particleInstancers 1\\n    -fluids 1\\n    -hairSystems 1\\n    -follicles 1\\n    -nCloths 1\\n    -nParticles 1\\n    -nRigids 1\\n    -dynamicConstraints 1\\n    -locators 1\\n    -manipulators 1\\n    -pluginShapes 1\\n    -dimensions 1\\n    -handles 1\\n    -pivots 1\\n    -textures 1\\n    -strokes 1\\n    -motionTrails 1\\n    -clipGhosts 1\\n    -greasePencils 1\\n    -shadows 0\\n    -captureSequenceNumber -1\\n    -width 1284\\n    -height 725\\n    -sceneRenderFilter 0\\n    $editorName;\\nmodelEditor -e -viewSelected 0 $editorName;\\nmodelEditor -e \\n    -pluginObjects \\\"gpuCacheDisplayFilter\\\" 1 \\n    $editorName\"\n"
		+ "\t\t\t\t\t\"modelPanel -edit -l (localizedPanelLabel(\\\"Persp View\\\")) -mbv $menusOkayInPanels  $panelName;\\n$editorName = $panelName;\\nmodelEditor -e \\n    -cam `findStartUpCamera persp` \\n    -useInteractiveMode 0\\n    -displayLights \\\"default\\\" \\n    -displayAppearance \\\"wireframe\\\" \\n    -activeOnly 0\\n    -ignorePanZoom 0\\n    -wireframeOnShaded 0\\n    -headsUpDisplay 1\\n    -holdOuts 1\\n    -selectionHiliteDisplay 1\\n    -useDefaultMaterial 0\\n    -bufferMode \\\"double\\\" \\n    -twoSidedLighting 0\\n    -backfaceCulling 0\\n    -xray 0\\n    -jointXray 0\\n    -activeComponentsXray 0\\n    -displayTextures 0\\n    -smoothWireframe 0\\n    -lineWidth 1\\n    -textureAnisotropic 0\\n    -textureHilight 1\\n    -textureSampling 2\\n    -textureDisplay \\\"modulate\\\" \\n    -textureMaxSize 16384\\n    -fogging 0\\n    -fogSource \\\"fragment\\\" \\n    -fogMode \\\"linear\\\" \\n    -fogStart 0\\n    -fogEnd 100\\n    -fogDensity 0.1\\n    -fogColor 0.5 0.5 0.5 1 \\n    -depthOfFieldPreview 1\\n    -maxConstantTransparency 1\\n    -rendererName \\\"base_OpenGL_Renderer\\\" \\n    -objectFilterShowInHUD 1\\n    -isFiltered 0\\n    -colorResolution 256 256 \\n    -bumpResolution 512 512 \\n    -textureCompression 0\\n    -transparencyAlgorithm \\\"frontAndBackCull\\\" \\n    -transpInShadows 0\\n    -cullingOverride \\\"none\\\" \\n    -lowQualityLighting 0\\n    -maximumNumHardwareLights 1\\n    -occlusionCulling 0\\n    -shadingModel 0\\n    -useBaseRenderer 0\\n    -useReducedRenderer 0\\n    -smallObjectCulling 0\\n    -smallObjectThreshold -1 \\n    -interactiveDisableShadows 0\\n    -interactiveBackFaceCull 0\\n    -sortTransparent 1\\n    -nurbsCurves 1\\n    -nurbsSurfaces 1\\n    -polymeshes 1\\n    -subdivSurfaces 1\\n    -planes 1\\n    -lights 1\\n    -cameras 1\\n    -controlVertices 1\\n    -hulls 1\\n    -grid 1\\n    -imagePlane 1\\n    -joints 1\\n    -ikHandles 1\\n    -deformers 1\\n    -dynamics 1\\n    -particleInstancers 1\\n    -fluids 1\\n    -hairSystems 1\\n    -follicles 1\\n    -nCloths 1\\n    -nParticles 1\\n    -nRigids 1\\n    -dynamicConstraints 1\\n    -locators 1\\n    -manipulators 1\\n    -pluginShapes 1\\n    -dimensions 1\\n    -handles 1\\n    -pivots 1\\n    -textures 1\\n    -strokes 1\\n    -motionTrails 1\\n    -clipGhosts 1\\n    -greasePencils 1\\n    -shadows 0\\n    -captureSequenceNumber -1\\n    -width 1284\\n    -height 725\\n    -sceneRenderFilter 0\\n    $editorName;\\nmodelEditor -e -viewSelected 0 $editorName;\\nmodelEditor -e \\n    -pluginObjects \\\"gpuCacheDisplayFilter\\\" 1 \\n    $editorName\"\n"
		+ "\t\t\t\t$configName;\n\n            setNamedPanelLayout (localizedPanelLabel(\"Current Layout\"));\n        }\n\n        panelHistory -e -clear mainPanelHistory;\n        setFocus `paneLayout -q -p1 $gMainPane`;\n        sceneUIReplacement -deleteRemaining;\n        sceneUIReplacement -clear;\n\t}\n\n\ngrid -spacing 5 -size 12 -divisions 5 -displayAxes yes -displayGridLines yes -displayDivisionLines yes -displayPerspectiveLabels no -displayOrthographicLabels no -displayAxesBold yes -perspectiveLabelPosition axis -orthographicLabelPosition edge;\nviewManip -drawCompass 0 -compassAngle 0 -frontParameters \"\" -homeParameters \"\" -selectionLockParameters \"\";\n}\n");
	setAttr ".st" 3;
createNode script -n "sceneConfigurationScriptNode";
	rename -uid "D9161900-0000-5F5D-5CDC-104400000DDE";
	setAttr ".b" -type "string" "playbackOptions -min 1 -max 125 -ast 1 -aet 208.333333 ";
	setAttr ".st" 6;
select -ne :time1;
	setAttr ".o" 1;
	setAttr ".unw" 1;
select -ne :hardwareRenderingGlobals;
	setAttr ".otfna" -type "stringArray" 22 "NURBS Curves" "NURBS Surfaces" "Polygons" "Subdiv Surface" "Particles" "Particle Instance" "Fluids" "Strokes" "Image Planes" "UI" "Lights" "Cameras" "Locators" "Joints" "IK Handles" "Deformers" "Motion Trails" "Components" "Hair Systems" "Follicles" "Misc. UI" "Ornaments"  ;
	setAttr ".otfva" -type "Int32Array" 22 0 1 1 1 1 1
		 1 1 1 0 0 0 0 0 0 0 0 0
		 0 0 0 0 ;
select -ne :renderPartition;
	setAttr -s 27 ".st";
select -ne :renderGlobalsList1;
select -ne :defaultShaderList1;
	setAttr -s 10 ".s";
select -ne :postProcessList1;
	setAttr -s 2 ".p";
select -ne :defaultRenderUtilityList1;
	setAttr -s 68 ".u";
select -ne :defaultRenderingList1;
	setAttr -s 2 ".r";
select -ne :initialShadingGroup;
	setAttr -s 37 ".dsm";
	setAttr ".ro" yes;
select -ne :initialParticleSE;
	setAttr ".ro" yes;
select -ne :defaultRenderGlobals;
	setAttr ".mcfr" 25;
	setAttr ".ren" -type "string" "arnold";
select -ne :defaultResolution;
	setAttr ".pa" 1;
select -ne :defaultColorMgtGlobals;
	setAttr ".cme" no;
select -ne :hardwareRenderGlobals;
	setAttr ".ctrs" 256;
	setAttr ".btrs" 512;
	setAttr ".hwfr" 25;
select -ne :ikSystem;
	setAttr -s 7 ".sol";
connectAttr "normal_walk_cycleRN.phl[1]" "lt_ankle_ik_ctrl_parentConstraint1.tg[0].ts"
		;
connectAttr "normal_walk_cycleRN.phl[2]" "lt_ankle_ik_ctrl_parentConstraint1.tg[0].tt"
		;
connectAttr "normal_walk_cycleRN.phl[3]" "lt_ankle_ik_ctrl_parentConstraint1.tg[0].tr"
		;
connectAttr "normal_walk_cycleRN.phl[4]" "lt_ankle_ik_ctrl_parentConstraint1.tg[0].trp"
		;
connectAttr "normal_walk_cycleRN.phl[5]" "lt_ankle_ik_ctrl_parentConstraint1.tg[0].trt"
		;
connectAttr "normal_walk_cycleRN.phl[6]" "lt_ankle_ik_ctrl_parentConstraint1.tg[0].tro"
		;
connectAttr "normal_walk_cycleRN.phl[7]" "lt_ankle_ik_ctrl_parentConstraint1.tg[0].tpm"
		;
connectAttr "normal_walk_cycleRN.phl[8]" "rt_ankle_ik_ctrl_parentConstraint1.tg[0].ts"
		;
connectAttr "normal_walk_cycleRN.phl[9]" "rt_ankle_ik_ctrl_parentConstraint1.tg[0].tt"
		;
connectAttr "normal_walk_cycleRN.phl[10]" "rt_ankle_ik_ctrl_parentConstraint1.tg[0].tr"
		;
connectAttr "normal_walk_cycleRN.phl[11]" "rt_ankle_ik_ctrl_parentConstraint1.tg[0].trp"
		;
connectAttr "normal_walk_cycleRN.phl[12]" "rt_ankle_ik_ctrl_parentConstraint1.tg[0].trt"
		;
connectAttr "normal_walk_cycleRN.phl[13]" "rt_ankle_ik_ctrl_parentConstraint1.tg[0].tro"
		;
connectAttr "normal_walk_cycleRN.phl[14]" "rt_ankle_ik_ctrl_parentConstraint1.tg[0].tpm"
		;
connectAttr "normal_walk_cycleRN.phl[15]" "ct_spine_ctrl_orientConstraint1.tg[0].tr"
		;
connectAttr "normal_walk_cycleRN.phl[16]" "ct_spine_ctrl_orientConstraint1.tg[0].tro"
		;
connectAttr "normal_walk_cycleRN.phl[17]" "ct_spine_ctrl_orientConstraint1.tg[0].tpm"
		;
connectAttr "normal_walk_cycleRN.phl[18]" "ct_spine_ctrl_orientConstraint1.tg[0].tjo"
		;
connectAttr "normal_walk_cycleRN.phl[19]" "ct_chest_ctrl_orientConstraint1.tg[0].tr"
		;
connectAttr "normal_walk_cycleRN.phl[20]" "ct_chest_ctrl_orientConstraint1.tg[0].tro"
		;
connectAttr "normal_walk_cycleRN.phl[21]" "ct_chest_ctrl_orientConstraint1.tg[0].tpm"
		;
connectAttr "normal_walk_cycleRN.phl[22]" "ct_chest_ctrl_orientConstraint1.tg[0].tjo"
		;
connectAttr "normal_walk_cycleRN.phl[23]" "ct_chest_ctrl_orientConstraint1.tg[1].tr"
		;
connectAttr "normal_walk_cycleRN.phl[24]" "ct_chest_ctrl_orientConstraint1.tg[1].tro"
		;
connectAttr "normal_walk_cycleRN.phl[25]" "ct_chest_ctrl_orientConstraint1.tg[1].tpm"
		;
connectAttr "normal_walk_cycleRN.phl[26]" "ct_chest_ctrl_orientConstraint1.tg[1].tjo"
		;
connectAttr "normal_walk_cycleRN.phl[27]" "ct_head_ctrl_orientConstraint1.tg[0].tr"
		;
connectAttr "normal_walk_cycleRN.phl[28]" "ct_head_ctrl_orientConstraint1.tg[0].tro"
		;
connectAttr "normal_walk_cycleRN.phl[29]" "ct_head_ctrl_orientConstraint1.tg[0].tpm"
		;
connectAttr "normal_walk_cycleRN.phl[30]" "ct_head_ctrl_orientConstraint1.tg[0].tjo"
		;
connectAttr "normal_walk_cycleRN.phl[31]" "rt_clavicle_ctrl_orientConstraint1.tg[0].tr"
		;
connectAttr "normal_walk_cycleRN.phl[32]" "rt_clavicle_ctrl_orientConstraint1.tg[0].tro"
		;
connectAttr "normal_walk_cycleRN.phl[33]" "rt_clavicle_ctrl_orientConstraint1.tg[0].tpm"
		;
connectAttr "normal_walk_cycleRN.phl[34]" "rt_clavicle_ctrl_orientConstraint1.tg[0].tjo"
		;
connectAttr "normal_walk_cycleRN.phl[35]" "lt_clavicle_ctrl_orientConstraint1.tg[0].tr"
		;
connectAttr "normal_walk_cycleRN.phl[36]" "lt_clavicle_ctrl_orientConstraint1.tg[0].tro"
		;
connectAttr "normal_walk_cycleRN.phl[37]" "lt_clavicle_ctrl_orientConstraint1.tg[0].tpm"
		;
connectAttr "normal_walk_cycleRN.phl[38]" "lt_clavicle_ctrl_orientConstraint1.tg[0].tjo"
		;
connectAttr "normal_walk_cycleRN.phl[39]" "lt_wrist_ik_ctrl_parentConstraint1.tg[0].tt"
		;
connectAttr "normal_walk_cycleRN.phl[40]" "lt_wrist_ik_ctrl_parentConstraint1.tg[0].ts"
		;
connectAttr "normal_walk_cycleRN.phl[41]" "lt_wrist_ik_ctrl_parentConstraint1.tg[0].tis"
		;
connectAttr "normal_walk_cycleRN.phl[42]" "lt_wrist_ik_ctrl_parentConstraint1.tg[0].tr"
		;
connectAttr "normal_walk_cycleRN.phl[43]" "lt_wrist_ik_ctrl_parentConstraint1.tg[0].trp"
		;
connectAttr "normal_walk_cycleRN.phl[44]" "lt_wrist_ik_ctrl_parentConstraint1.tg[0].trt"
		;
connectAttr "normal_walk_cycleRN.phl[45]" "lt_wrist_ik_ctrl_parentConstraint1.tg[0].tro"
		;
connectAttr "normal_walk_cycleRN.phl[46]" "lt_wrist_ik_ctrl_parentConstraint1.tg[0].tpm"
		;
connectAttr "normal_walk_cycleRN.phl[47]" "lt_wrist_ik_ctrl_parentConstraint1.tg[0].tjo"
		;
connectAttr "normal_walk_cycleRN.phl[48]" "lt_wrist_ik_ctrl_parentConstraint1.tg[0].tsc"
		;
connectAttr "normal_walk_cycleRN.phl[49]" "rt_wrist_ik_ctrl_parentConstraint1.tg[0].tt"
		;
connectAttr "normal_walk_cycleRN.phl[50]" "rt_wrist_ik_ctrl_parentConstraint1.tg[0].ts"
		;
connectAttr "normal_walk_cycleRN.phl[51]" "rt_wrist_ik_ctrl_parentConstraint1.tg[0].tis"
		;
connectAttr "normal_walk_cycleRN.phl[52]" "rt_wrist_ik_ctrl_parentConstraint1.tg[0].tr"
		;
connectAttr "normal_walk_cycleRN.phl[53]" "rt_wrist_ik_ctrl_parentConstraint1.tg[0].trp"
		;
connectAttr "normal_walk_cycleRN.phl[54]" "rt_wrist_ik_ctrl_parentConstraint1.tg[0].trt"
		;
connectAttr "normal_walk_cycleRN.phl[55]" "rt_wrist_ik_ctrl_parentConstraint1.tg[0].tro"
		;
connectAttr "normal_walk_cycleRN.phl[56]" "rt_wrist_ik_ctrl_parentConstraint1.tg[0].tpm"
		;
connectAttr "normal_walk_cycleRN.phl[57]" "rt_wrist_ik_ctrl_parentConstraint1.tg[0].tjo"
		;
connectAttr "normal_walk_cycleRN.phl[58]" "rt_wrist_ik_ctrl_parentConstraint1.tg[0].tsc"
		;
connectAttr "normal_walk_cycleRN.phl[59]" "ct_root_ctrl_parentConstraint1.tg[0].ts"
		;
connectAttr "normal_walk_cycleRN.phl[60]" "ct_root_ctrl_parentConstraint1.tg[0].tt"
		;
connectAttr "normal_walk_cycleRN.phl[61]" "ct_root_ctrl_parentConstraint1.tg[0].tr"
		;
connectAttr "normal_walk_cycleRN.phl[62]" "ct_root_ctrl_parentConstraint1.tg[0].trp"
		;
connectAttr "normal_walk_cycleRN.phl[63]" "ct_root_ctrl_parentConstraint1.tg[0].trt"
		;
connectAttr "normal_walk_cycleRN.phl[64]" "ct_root_ctrl_parentConstraint1.tg[0].tro"
		;
connectAttr "normal_walk_cycleRN.phl[65]" "ct_root_ctrl_parentConstraint1.tg[0].tpm"
		;
connectAttr "lt_wrist_ik_ctrl_parentConstraint1.ctx" "lt_wrist_ik_ctrl.tx";
connectAttr "lt_wrist_ik_ctrl_parentConstraint1.cty" "lt_wrist_ik_ctrl.ty";
connectAttr "lt_wrist_ik_ctrl_parentConstraint1.ctz" "lt_wrist_ik_ctrl.tz";
connectAttr "lt_wrist_ik_ctrl_parentConstraint1.crx" "lt_wrist_ik_ctrl.rx";
connectAttr "lt_wrist_ik_ctrl_parentConstraint1.cry" "lt_wrist_ik_ctrl.ry";
connectAttr "lt_wrist_ik_ctrl_parentConstraint1.crz" "lt_wrist_ik_ctrl.rz";
connectAttr "lt_wrist_ik_ctrl.ro" "lt_wrist_ik_ctrl_parentConstraint1.cro";
connectAttr "lt_wrist_ik_ctrl.pim" "lt_wrist_ik_ctrl_parentConstraint1.cpim";
connectAttr "lt_wrist_ik_ctrl.rp" "lt_wrist_ik_ctrl_parentConstraint1.crp";
connectAttr "lt_wrist_ik_ctrl.rpt" "lt_wrist_ik_ctrl_parentConstraint1.crt";
connectAttr "lt_wrist_ik_ctrl_parentConstraint1.w0" "lt_wrist_ik_ctrl_parentConstraint1.tg[0].tw"
		;
connectAttr "rt_wrist_ik_ctrl_parentConstraint1.ctx" "rt_wrist_ik_ctrl.tx";
connectAttr "rt_wrist_ik_ctrl_parentConstraint1.cty" "rt_wrist_ik_ctrl.ty";
connectAttr "rt_wrist_ik_ctrl_parentConstraint1.ctz" "rt_wrist_ik_ctrl.tz";
connectAttr "rt_wrist_ik_ctrl_parentConstraint1.crx" "rt_wrist_ik_ctrl.rx";
connectAttr "rt_wrist_ik_ctrl_parentConstraint1.cry" "rt_wrist_ik_ctrl.ry";
connectAttr "rt_wrist_ik_ctrl_parentConstraint1.crz" "rt_wrist_ik_ctrl.rz";
connectAttr "rt_wrist_ik_ctrl.ro" "rt_wrist_ik_ctrl_parentConstraint1.cro";
connectAttr "rt_wrist_ik_ctrl.pim" "rt_wrist_ik_ctrl_parentConstraint1.cpim";
connectAttr "rt_wrist_ik_ctrl.rp" "rt_wrist_ik_ctrl_parentConstraint1.crp";
connectAttr "rt_wrist_ik_ctrl.rpt" "rt_wrist_ik_ctrl_parentConstraint1.crt";
connectAttr "rt_wrist_ik_ctrl_parentConstraint1.w0" "rt_wrist_ik_ctrl_parentConstraint1.tg[0].tw"
		;
connectAttr "lt_ankle_ik_ctrl_parentConstraint1.ctz" "lt_ankle_ik_ctrl.tz";
connectAttr "lt_ankle_ik_ctrl_parentConstraint1.cty" "lt_ankle_ik_ctrl.ty";
connectAttr "lt_ankle_ik_ctrl_parentConstraint1.ctx" "lt_ankle_ik_ctrl.tx";
connectAttr "lt_ankle_ik_ctrl_parentConstraint1.crx" "lt_ankle_ik_ctrl.rx";
connectAttr "lt_ankle_ik_ctrl_parentConstraint1.cry" "lt_ankle_ik_ctrl.ry";
connectAttr "lt_ankle_ik_ctrl_parentConstraint1.crz" "lt_ankle_ik_ctrl.rz";
connectAttr "lt_ankle_ik_ctrl.ro" "lt_ankle_ik_ctrl_parentConstraint1.cro";
connectAttr "lt_ankle_ik_ctrl.pim" "lt_ankle_ik_ctrl_parentConstraint1.cpim";
connectAttr "lt_ankle_ik_ctrl.rp" "lt_ankle_ik_ctrl_parentConstraint1.crp";
connectAttr "lt_ankle_ik_ctrl.rpt" "lt_ankle_ik_ctrl_parentConstraint1.crt";
connectAttr "lt_ankle_ik_ctrl_parentConstraint1.w0" "lt_ankle_ik_ctrl_parentConstraint1.tg[0].tw"
		;
connectAttr "rt_ankle_ik_ctrl_parentConstraint1.ctx" "rt_ankle_ik_ctrl.tx";
connectAttr "rt_ankle_ik_ctrl_parentConstraint1.cty" "rt_ankle_ik_ctrl.ty";
connectAttr "rt_ankle_ik_ctrl_parentConstraint1.ctz" "rt_ankle_ik_ctrl.tz";
connectAttr "rt_ankle_ik_ctrl_parentConstraint1.crx" "rt_ankle_ik_ctrl.rx";
connectAttr "rt_ankle_ik_ctrl_parentConstraint1.cry" "rt_ankle_ik_ctrl.ry";
connectAttr "rt_ankle_ik_ctrl_parentConstraint1.crz" "rt_ankle_ik_ctrl.rz";
connectAttr "rt_ankle_ik_ctrl.ro" "rt_ankle_ik_ctrl_parentConstraint1.cro";
connectAttr "rt_ankle_ik_ctrl.pim" "rt_ankle_ik_ctrl_parentConstraint1.cpim";
connectAttr "rt_ankle_ik_ctrl.rp" "rt_ankle_ik_ctrl_parentConstraint1.crp";
connectAttr "rt_ankle_ik_ctrl.rpt" "rt_ankle_ik_ctrl_parentConstraint1.crt";
connectAttr "rt_ankle_ik_ctrl_parentConstraint1.w0" "rt_ankle_ik_ctrl_parentConstraint1.tg[0].tw"
		;
connectAttr "ct_root_ctrl_parentConstraint1.ctx" "ct_root_ctrl.tx";
connectAttr "ct_root_ctrl_parentConstraint1.cty" "ct_root_ctrl.ty";
connectAttr "ct_root_ctrl_parentConstraint1.ctz" "ct_root_ctrl.tz";
connectAttr "ct_root_ctrl_parentConstraint1.crx" "ct_root_ctrl.rx";
connectAttr "ct_root_ctrl_parentConstraint1.cry" "ct_root_ctrl.ry";
connectAttr "ct_root_ctrl_parentConstraint1.crz" "ct_root_ctrl.rz";
connectAttr "makeNurbCircle1.oc" "ct_root_ctrlShape.cr";
connectAttr "ct_root_ctrl.ro" "ct_root_ctrl_parentConstraint1.cro";
connectAttr "ct_root_ctrl.pim" "ct_root_ctrl_parentConstraint1.cpim";
connectAttr "ct_root_ctrl.rp" "ct_root_ctrl_parentConstraint1.crp";
connectAttr "ct_root_ctrl.rpt" "ct_root_ctrl_parentConstraint1.crt";
connectAttr "ct_root_ctrl_parentConstraint1.w0" "ct_root_ctrl_parentConstraint1.tg[0].tw"
		;
connectAttr "ct_spine_ctrl_group_parent_constraint.ctx" "ct_spine_ctrl_group.tx"
		;
connectAttr "ct_spine_ctrl_group_parent_constraint.cty" "ct_spine_ctrl_group.ty"
		;
connectAttr "ct_spine_ctrl_group_parent_constraint.ctz" "ct_spine_ctrl_group.tz"
		;
connectAttr "ct_spine_ctrl_group_parent_constraint.crx" "ct_spine_ctrl_group.rx"
		;
connectAttr "ct_spine_ctrl_group_parent_constraint.cry" "ct_spine_ctrl_group.ry"
		;
connectAttr "ct_spine_ctrl_group_parent_constraint.crz" "ct_spine_ctrl_group.rz"
		;
connectAttr "ct_spine_ctrl_orientConstraint1.crx" "ct_spine_ctrl.rx";
connectAttr "ct_spine_ctrl_orientConstraint1.cry" "ct_spine_ctrl.ry";
connectAttr "ct_spine_ctrl_orientConstraint1.crz" "ct_spine_ctrl.rz";
connectAttr "makeNurbCircle2.oc" "ct_spine_ctrlShape.cr";
connectAttr "ct_spine_ctrl.ro" "ct_spine_ctrl_orientConstraint1.cro";
connectAttr "ct_spine_ctrl.pim" "ct_spine_ctrl_orientConstraint1.cpim";
connectAttr "ct_spine_ctrl_orientConstraint1.w0" "ct_spine_ctrl_orientConstraint1.tg[0].tw"
		;
connectAttr "ct_spine_ctrl_group.ro" "ct_spine_ctrl_group_parent_constraint.cro"
		;
connectAttr "ct_spine_ctrl_group.pim" "ct_spine_ctrl_group_parent_constraint.cpim"
		;
connectAttr "ct_spine_ctrl_group.rp" "ct_spine_ctrl_group_parent_constraint.crp"
		;
connectAttr "ct_spine_ctrl_group.rpt" "ct_spine_ctrl_group_parent_constraint.crt"
		;
connectAttr "ct_root_ctrl.t" "ct_spine_ctrl_group_parent_constraint.tg[0].tt";
connectAttr "ct_root_ctrl.rp" "ct_spine_ctrl_group_parent_constraint.tg[0].trp";
connectAttr "ct_root_ctrl.rpt" "ct_spine_ctrl_group_parent_constraint.tg[0].trt"
		;
connectAttr "ct_root_ctrl.r" "ct_spine_ctrl_group_parent_constraint.tg[0].tr";
connectAttr "ct_root_ctrl.ro" "ct_spine_ctrl_group_parent_constraint.tg[0].tro";
connectAttr "ct_root_ctrl.s" "ct_spine_ctrl_group_parent_constraint.tg[0].ts";
connectAttr "ct_root_ctrl.pm" "ct_spine_ctrl_group_parent_constraint.tg[0].tpm";
connectAttr "ct_spine_ctrl_group_parent_constraint.w0" "ct_spine_ctrl_group_parent_constraint.tg[0].tw"
		;
connectAttr "ct_chest_ctrl_group_parent_constraint.ctx" "ct_chest_ctrl_group.tx"
		;
connectAttr "ct_chest_ctrl_group_parent_constraint.cty" "ct_chest_ctrl_group.ty"
		;
connectAttr "ct_chest_ctrl_group_parent_constraint.ctz" "ct_chest_ctrl_group.tz"
		;
connectAttr "ct_chest_ctrl_group_parent_constraint.crx" "ct_chest_ctrl_group.rx"
		;
connectAttr "ct_chest_ctrl_group_parent_constraint.cry" "ct_chest_ctrl_group.ry"
		;
connectAttr "ct_chest_ctrl_group_parent_constraint.crz" "ct_chest_ctrl_group.rz"
		;
connectAttr "ct_chest_ctrl_orientConstraint1.crx" "ct_chest_ctrl.rx";
connectAttr "ct_chest_ctrl_orientConstraint1.cry" "ct_chest_ctrl.ry";
connectAttr "ct_chest_ctrl_orientConstraint1.crz" "ct_chest_ctrl.rz";
connectAttr "makeNurbCircle3.oc" "ct_chest_ctrlShape.cr";
connectAttr "ct_chest_ctrl.ro" "ct_chest_ctrl_orientConstraint1.cro";
connectAttr "ct_chest_ctrl.pim" "ct_chest_ctrl_orientConstraint1.cpim";
connectAttr "ct_chest_ctrl_orientConstraint1.w0" "ct_chest_ctrl_orientConstraint1.tg[0].tw"
		;
connectAttr "ct_chest_ctrl_orientConstraint1.w1" "ct_chest_ctrl_orientConstraint1.tg[1].tw"
		;
connectAttr "ct_chest_ctrl_group.ro" "ct_chest_ctrl_group_parent_constraint.cro"
		;
connectAttr "ct_chest_ctrl_group.pim" "ct_chest_ctrl_group_parent_constraint.cpim"
		;
connectAttr "ct_chest_ctrl_group.rp" "ct_chest_ctrl_group_parent_constraint.crp"
		;
connectAttr "ct_chest_ctrl_group.rpt" "ct_chest_ctrl_group_parent_constraint.crt"
		;
connectAttr "ct_spine_ctrl.t" "ct_chest_ctrl_group_parent_constraint.tg[0].tt";
connectAttr "ct_spine_ctrl.rp" "ct_chest_ctrl_group_parent_constraint.tg[0].trp"
		;
connectAttr "ct_spine_ctrl.rpt" "ct_chest_ctrl_group_parent_constraint.tg[0].trt"
		;
connectAttr "ct_spine_ctrl.r" "ct_chest_ctrl_group_parent_constraint.tg[0].tr";
connectAttr "ct_spine_ctrl.ro" "ct_chest_ctrl_group_parent_constraint.tg[0].tro"
		;
connectAttr "ct_spine_ctrl.s" "ct_chest_ctrl_group_parent_constraint.tg[0].ts";
connectAttr "ct_spine_ctrl.pm" "ct_chest_ctrl_group_parent_constraint.tg[0].tpm"
		;
connectAttr "ct_chest_ctrl_group_parent_constraint.w0" "ct_chest_ctrl_group_parent_constraint.tg[0].tw"
		;
connectAttr "ct_neck_ctrl_group_parent_constraint.ctx" "ct_neck_ctrl_group.tx";
connectAttr "ct_neck_ctrl_group_parent_constraint.cty" "ct_neck_ctrl_group.ty";
connectAttr "ct_neck_ctrl_group_parent_constraint.ctz" "ct_neck_ctrl_group.tz";
connectAttr "ct_neck_ctrl_group_parent_constraint.crx" "ct_neck_ctrl_group.rx";
connectAttr "ct_neck_ctrl_group_parent_constraint.cry" "ct_neck_ctrl_group.ry";
connectAttr "ct_neck_ctrl_group_parent_constraint.crz" "ct_neck_ctrl_group.rz";
connectAttr "makeNurbCircle4.oc" "ct_neck_ctrlShape.cr";
connectAttr "ct_neck_ctrl_group.ro" "ct_neck_ctrl_group_parent_constraint.cro";
connectAttr "ct_neck_ctrl_group.pim" "ct_neck_ctrl_group_parent_constraint.cpim"
		;
connectAttr "ct_neck_ctrl_group.rp" "ct_neck_ctrl_group_parent_constraint.crp";
connectAttr "ct_neck_ctrl_group.rpt" "ct_neck_ctrl_group_parent_constraint.crt";
connectAttr "ct_chest_ctrl.t" "ct_neck_ctrl_group_parent_constraint.tg[0].tt";
connectAttr "ct_chest_ctrl.rp" "ct_neck_ctrl_group_parent_constraint.tg[0].trp";
connectAttr "ct_chest_ctrl.rpt" "ct_neck_ctrl_group_parent_constraint.tg[0].trt"
		;
connectAttr "ct_chest_ctrl.r" "ct_neck_ctrl_group_parent_constraint.tg[0].tr";
connectAttr "ct_chest_ctrl.ro" "ct_neck_ctrl_group_parent_constraint.tg[0].tro";
connectAttr "ct_chest_ctrl.s" "ct_neck_ctrl_group_parent_constraint.tg[0].ts";
connectAttr "ct_chest_ctrl.pm" "ct_neck_ctrl_group_parent_constraint.tg[0].tpm";
connectAttr "ct_neck_ctrl_group_parent_constraint.w0" "ct_neck_ctrl_group_parent_constraint.tg[0].tw"
		;
connectAttr "ct_head_ctrl_group_parent_constraint.ctx" "ct_head_ctrl_group.tx";
connectAttr "ct_head_ctrl_group_parent_constraint.cty" "ct_head_ctrl_group.ty";
connectAttr "ct_head_ctrl_group_parent_constraint.ctz" "ct_head_ctrl_group.tz";
connectAttr "ct_head_ctrl_group_parent_constraint.crx" "ct_head_ctrl_group.rx";
connectAttr "ct_head_ctrl_group_parent_constraint.cry" "ct_head_ctrl_group.ry";
connectAttr "ct_head_ctrl_group_parent_constraint.crz" "ct_head_ctrl_group.rz";
connectAttr "ct_head_ctrl_orientConstraint1.crx" "ct_head_ctrl.rx";
connectAttr "ct_head_ctrl_orientConstraint1.cry" "ct_head_ctrl.ry";
connectAttr "ct_head_ctrl_orientConstraint1.crz" "ct_head_ctrl.rz";
connectAttr "makeNurbCircle5.oc" "ct_head_ctrlShape.cr";
connectAttr "ct_head_ctrl.ro" "ct_head_ctrl_orientConstraint1.cro";
connectAttr "ct_head_ctrl.pim" "ct_head_ctrl_orientConstraint1.cpim";
connectAttr "ct_head_ctrl_orientConstraint1.w0" "ct_head_ctrl_orientConstraint1.tg[0].tw"
		;
connectAttr "ct_head_ctrl_group.ro" "ct_head_ctrl_group_parent_constraint.cro";
connectAttr "ct_head_ctrl_group.pim" "ct_head_ctrl_group_parent_constraint.cpim"
		;
connectAttr "ct_head_ctrl_group.rp" "ct_head_ctrl_group_parent_constraint.crp";
connectAttr "ct_head_ctrl_group.rpt" "ct_head_ctrl_group_parent_constraint.crt";
connectAttr "ct_neck_ctrl.t" "ct_head_ctrl_group_parent_constraint.tg[0].tt";
connectAttr "ct_neck_ctrl.rp" "ct_head_ctrl_group_parent_constraint.tg[0].trp";
connectAttr "ct_neck_ctrl.rpt" "ct_head_ctrl_group_parent_constraint.tg[0].trt";
connectAttr "ct_neck_ctrl.r" "ct_head_ctrl_group_parent_constraint.tg[0].tr";
connectAttr "ct_neck_ctrl.ro" "ct_head_ctrl_group_parent_constraint.tg[0].tro";
connectAttr "ct_neck_ctrl.s" "ct_head_ctrl_group_parent_constraint.tg[0].ts";
connectAttr "ct_neck_ctrl.pm" "ct_head_ctrl_group_parent_constraint.tg[0].tpm";
connectAttr "ct_head_ctrl_group_parent_constraint.w0" "ct_head_ctrl_group_parent_constraint.tg[0].tw"
		;
connectAttr "ct_hip_ctrl_group_parent_constraint.ctx" "ct_hip_ctrl_group.tx";
connectAttr "ct_hip_ctrl_group_parent_constraint.cty" "ct_hip_ctrl_group.ty";
connectAttr "ct_hip_ctrl_group_parent_constraint.ctz" "ct_hip_ctrl_group.tz";
connectAttr "ct_hip_ctrl_group_parent_constraint.crx" "ct_hip_ctrl_group.rx";
connectAttr "ct_hip_ctrl_group_parent_constraint.cry" "ct_hip_ctrl_group.ry";
connectAttr "ct_hip_ctrl_group_parent_constraint.crz" "ct_hip_ctrl_group.rz";
connectAttr "makeNurbCircle6.oc" "ct_hip_ctrlShape.cr";
connectAttr "ct_hip_ctrl_group.ro" "ct_hip_ctrl_group_parent_constraint.cro";
connectAttr "ct_hip_ctrl_group.pim" "ct_hip_ctrl_group_parent_constraint.cpim";
connectAttr "ct_hip_ctrl_group.rp" "ct_hip_ctrl_group_parent_constraint.crp";
connectAttr "ct_hip_ctrl_group.rpt" "ct_hip_ctrl_group_parent_constraint.crt";
connectAttr "ct_root_ctrl.t" "ct_hip_ctrl_group_parent_constraint.tg[0].tt";
connectAttr "ct_root_ctrl.rp" "ct_hip_ctrl_group_parent_constraint.tg[0].trp";
connectAttr "ct_root_ctrl.rpt" "ct_hip_ctrl_group_parent_constraint.tg[0].trt";
connectAttr "ct_root_ctrl.r" "ct_hip_ctrl_group_parent_constraint.tg[0].tr";
connectAttr "ct_root_ctrl.ro" "ct_hip_ctrl_group_parent_constraint.tg[0].tro";
connectAttr "ct_root_ctrl.s" "ct_hip_ctrl_group_parent_constraint.tg[0].ts";
connectAttr "ct_root_ctrl.pm" "ct_hip_ctrl_group_parent_constraint.tg[0].tpm";
connectAttr "ct_hip_ctrl_group_parent_constraint.w0" "ct_hip_ctrl_group_parent_constraint.tg[0].tw"
		;
connectAttr "lt_clavicle_ctrl_group_parent_constraint.ctx" "lt_clavicle_ctrl_group.tx"
		;
connectAttr "lt_clavicle_ctrl_group_parent_constraint.cty" "lt_clavicle_ctrl_group.ty"
		;
connectAttr "lt_clavicle_ctrl_group_parent_constraint.ctz" "lt_clavicle_ctrl_group.tz"
		;
connectAttr "lt_clavicle_ctrl_group_parent_constraint.crx" "lt_clavicle_ctrl_group.rx"
		;
connectAttr "lt_clavicle_ctrl_group_parent_constraint.cry" "lt_clavicle_ctrl_group.ry"
		;
connectAttr "lt_clavicle_ctrl_group_parent_constraint.crz" "lt_clavicle_ctrl_group.rz"
		;
connectAttr "lt_clavicle_ctrl_orientConstraint1.crx" "lt_clavicle_ctrl.rx";
connectAttr "lt_clavicle_ctrl_orientConstraint1.cry" "lt_clavicle_ctrl.ry";
connectAttr "lt_clavicle_ctrl_orientConstraint1.crz" "lt_clavicle_ctrl.rz";
connectAttr "makeNurbCircle7.oc" "lt_clavicle_ctrlShape.cr";
connectAttr "lt_clavicle_ctrl.ro" "lt_clavicle_ctrl_orientConstraint1.cro";
connectAttr "lt_clavicle_ctrl.pim" "lt_clavicle_ctrl_orientConstraint1.cpim";
connectAttr "lt_clavicle_ctrl_orientConstraint1.w0" "lt_clavicle_ctrl_orientConstraint1.tg[0].tw"
		;
connectAttr "lt_clavicle_ctrl_group.ro" "lt_clavicle_ctrl_group_parent_constraint.cro"
		;
connectAttr "lt_clavicle_ctrl_group.pim" "lt_clavicle_ctrl_group_parent_constraint.cpim"
		;
connectAttr "lt_clavicle_ctrl_group.rp" "lt_clavicle_ctrl_group_parent_constraint.crp"
		;
connectAttr "lt_clavicle_ctrl_group.rpt" "lt_clavicle_ctrl_group_parent_constraint.crt"
		;
connectAttr "ct_chest_ctrl.t" "lt_clavicle_ctrl_group_parent_constraint.tg[0].tt"
		;
connectAttr "ct_chest_ctrl.rp" "lt_clavicle_ctrl_group_parent_constraint.tg[0].trp"
		;
connectAttr "ct_chest_ctrl.rpt" "lt_clavicle_ctrl_group_parent_constraint.tg[0].trt"
		;
connectAttr "ct_chest_ctrl.r" "lt_clavicle_ctrl_group_parent_constraint.tg[0].tr"
		;
connectAttr "ct_chest_ctrl.ro" "lt_clavicle_ctrl_group_parent_constraint.tg[0].tro"
		;
connectAttr "ct_chest_ctrl.s" "lt_clavicle_ctrl_group_parent_constraint.tg[0].ts"
		;
connectAttr "ct_chest_ctrl.pm" "lt_clavicle_ctrl_group_parent_constraint.tg[0].tpm"
		;
connectAttr "lt_clavicle_ctrl_group_parent_constraint.w0" "lt_clavicle_ctrl_group_parent_constraint.tg[0].tw"
		;
connectAttr "rt_clavicle_ctrl_group_parent_constraint.ctx" "rt_clavicle_ctrl_group.tx"
		;
connectAttr "rt_clavicle_ctrl_group_parent_constraint.cty" "rt_clavicle_ctrl_group.ty"
		;
connectAttr "rt_clavicle_ctrl_group_parent_constraint.ctz" "rt_clavicle_ctrl_group.tz"
		;
connectAttr "rt_clavicle_ctrl_group_parent_constraint.crx" "rt_clavicle_ctrl_group.rx"
		;
connectAttr "rt_clavicle_ctrl_group_parent_constraint.cry" "rt_clavicle_ctrl_group.ry"
		;
connectAttr "rt_clavicle_ctrl_group_parent_constraint.crz" "rt_clavicle_ctrl_group.rz"
		;
connectAttr "rt_clavicle_ctrl_orientConstraint1.crx" "rt_clavicle_ctrl.rx";
connectAttr "rt_clavicle_ctrl_orientConstraint1.cry" "rt_clavicle_ctrl.ry";
connectAttr "rt_clavicle_ctrl_orientConstraint1.crz" "rt_clavicle_ctrl.rz";
connectAttr "makeNurbCircle8.oc" "rt_clavicle_ctrlShape.cr";
connectAttr "rt_clavicle_ctrl.ro" "rt_clavicle_ctrl_orientConstraint1.cro";
connectAttr "rt_clavicle_ctrl.pim" "rt_clavicle_ctrl_orientConstraint1.cpim";
connectAttr "rt_clavicle_ctrl_orientConstraint1.w0" "rt_clavicle_ctrl_orientConstraint1.tg[0].tw"
		;
connectAttr "rt_clavicle_ctrl_group.ro" "rt_clavicle_ctrl_group_parent_constraint.cro"
		;
connectAttr "rt_clavicle_ctrl_group.pim" "rt_clavicle_ctrl_group_parent_constraint.cpim"
		;
connectAttr "rt_clavicle_ctrl_group.rp" "rt_clavicle_ctrl_group_parent_constraint.crp"
		;
connectAttr "rt_clavicle_ctrl_group.rpt" "rt_clavicle_ctrl_group_parent_constraint.crt"
		;
connectAttr "ct_chest_ctrl.t" "rt_clavicle_ctrl_group_parent_constraint.tg[0].tt"
		;
connectAttr "ct_chest_ctrl.rp" "rt_clavicle_ctrl_group_parent_constraint.tg[0].trp"
		;
connectAttr "ct_chest_ctrl.rpt" "rt_clavicle_ctrl_group_parent_constraint.tg[0].trt"
		;
connectAttr "ct_chest_ctrl.r" "rt_clavicle_ctrl_group_parent_constraint.tg[0].tr"
		;
connectAttr "ct_chest_ctrl.ro" "rt_clavicle_ctrl_group_parent_constraint.tg[0].tro"
		;
connectAttr "ct_chest_ctrl.s" "rt_clavicle_ctrl_group_parent_constraint.tg[0].ts"
		;
connectAttr "ct_chest_ctrl.pm" "rt_clavicle_ctrl_group_parent_constraint.tg[0].tpm"
		;
connectAttr "rt_clavicle_ctrl_group_parent_constraint.w0" "rt_clavicle_ctrl_group_parent_constraint.tg[0].tw"
		;
connectAttr "L_Shoulder_Joint.msg" "lt_wrist_ik_handle.hsj";
connectAttr "lt_wrist_ik_effector.hp" "lt_wrist_ik_handle.hee";
connectAttr "ikRPsolver.msg" "lt_wrist_ik_handle.hsv";
connectAttr "lt_wrist_parent_constraint.ctx" "lt_wrist_ik_handle.tx";
connectAttr "lt_wrist_parent_constraint.cty" "lt_wrist_ik_handle.ty";
connectAttr "lt_wrist_parent_constraint.ctz" "lt_wrist_ik_handle.tz";
connectAttr "lt_wrist_parent_constraint.crx" "lt_wrist_ik_handle.rx";
connectAttr "lt_wrist_parent_constraint.cry" "lt_wrist_ik_handle.ry";
connectAttr "lt_wrist_parent_constraint.crz" "lt_wrist_ik_handle.rz";
connectAttr "unitConversion1.o" "lt_wrist_ik_handle.twi";
connectAttr "lt_wrist_ik_handle.ro" "lt_wrist_parent_constraint.cro";
connectAttr "lt_wrist_ik_handle.pim" "lt_wrist_parent_constraint.cpim";
connectAttr "lt_wrist_ik_handle.rp" "lt_wrist_parent_constraint.crp";
connectAttr "lt_wrist_ik_handle.rpt" "lt_wrist_parent_constraint.crt";
connectAttr "lt_wrist_ik_ctrl.t" "lt_wrist_parent_constraint.tg[0].tt";
connectAttr "lt_wrist_ik_ctrl.rp" "lt_wrist_parent_constraint.tg[0].trp";
connectAttr "lt_wrist_ik_ctrl.rpt" "lt_wrist_parent_constraint.tg[0].trt";
connectAttr "lt_wrist_ik_ctrl.r" "lt_wrist_parent_constraint.tg[0].tr";
connectAttr "lt_wrist_ik_ctrl.ro" "lt_wrist_parent_constraint.tg[0].tro";
connectAttr "lt_wrist_ik_ctrl.s" "lt_wrist_parent_constraint.tg[0].ts";
connectAttr "lt_wrist_ik_ctrl.pm" "lt_wrist_parent_constraint.tg[0].tpm";
connectAttr "lt_wrist_parent_constraint.w0" "lt_wrist_parent_constraint.tg[0].tw"
		;
connectAttr "R_Shoulder_Joint.msg" "rt_wrist_ik_handle.hsj";
connectAttr "rt_wrist_ik_effector.hp" "rt_wrist_ik_handle.hee";
connectAttr "ikRPsolver.msg" "rt_wrist_ik_handle.hsv";
connectAttr "rt_wrist_parent_constraint.ctx" "rt_wrist_ik_handle.tx";
connectAttr "rt_wrist_parent_constraint.cty" "rt_wrist_ik_handle.ty";
connectAttr "rt_wrist_parent_constraint.ctz" "rt_wrist_ik_handle.tz";
connectAttr "rt_wrist_parent_constraint.crx" "rt_wrist_ik_handle.rx";
connectAttr "rt_wrist_parent_constraint.cry" "rt_wrist_ik_handle.ry";
connectAttr "rt_wrist_parent_constraint.crz" "rt_wrist_ik_handle.rz";
connectAttr "unitConversion2.o" "rt_wrist_ik_handle.twi";
connectAttr "rt_wrist_ik_handle.ro" "rt_wrist_parent_constraint.cro";
connectAttr "rt_wrist_ik_handle.pim" "rt_wrist_parent_constraint.cpim";
connectAttr "rt_wrist_ik_handle.rp" "rt_wrist_parent_constraint.crp";
connectAttr "rt_wrist_ik_handle.rpt" "rt_wrist_parent_constraint.crt";
connectAttr "rt_wrist_ik_ctrl.t" "rt_wrist_parent_constraint.tg[0].tt";
connectAttr "rt_wrist_ik_ctrl.rp" "rt_wrist_parent_constraint.tg[0].trp";
connectAttr "rt_wrist_ik_ctrl.rpt" "rt_wrist_parent_constraint.tg[0].trt";
connectAttr "rt_wrist_ik_ctrl.r" "rt_wrist_parent_constraint.tg[0].tr";
connectAttr "rt_wrist_ik_ctrl.ro" "rt_wrist_parent_constraint.tg[0].tro";
connectAttr "rt_wrist_ik_ctrl.s" "rt_wrist_parent_constraint.tg[0].ts";
connectAttr "rt_wrist_ik_ctrl.pm" "rt_wrist_parent_constraint.tg[0].tpm";
connectAttr "rt_wrist_parent_constraint.w0" "rt_wrist_parent_constraint.tg[0].tw"
		;
connectAttr "L_Pelvis_Joint.msg" "lt_ankle_ik_handle.hsj";
connectAttr "lt_ankle_ik_effector.hp" "lt_ankle_ik_handle.hee";
connectAttr "ikRPsolver.msg" "lt_ankle_ik_handle.hsv";
connectAttr "lt_ankle_parent_constraint.ctx" "lt_ankle_ik_handle.tx";
connectAttr "lt_ankle_parent_constraint.cty" "lt_ankle_ik_handle.ty";
connectAttr "lt_ankle_parent_constraint.ctz" "lt_ankle_ik_handle.tz";
connectAttr "lt_ankle_parent_constraint.crx" "lt_ankle_ik_handle.rx";
connectAttr "lt_ankle_parent_constraint.cry" "lt_ankle_ik_handle.ry";
connectAttr "lt_ankle_parent_constraint.crz" "lt_ankle_ik_handle.rz";
connectAttr "unitConversion3.o" "lt_ankle_ik_handle.twi";
connectAttr "lt_ankle_ik_handle.ro" "lt_ankle_parent_constraint.cro";
connectAttr "lt_ankle_ik_handle.pim" "lt_ankle_parent_constraint.cpim";
connectAttr "lt_ankle_ik_handle.rp" "lt_ankle_parent_constraint.crp";
connectAttr "lt_ankle_ik_handle.rpt" "lt_ankle_parent_constraint.crt";
connectAttr "lt_ankle_ik_ctrl.t" "lt_ankle_parent_constraint.tg[0].tt";
connectAttr "lt_ankle_ik_ctrl.rp" "lt_ankle_parent_constraint.tg[0].trp";
connectAttr "lt_ankle_ik_ctrl.rpt" "lt_ankle_parent_constraint.tg[0].trt";
connectAttr "lt_ankle_ik_ctrl.r" "lt_ankle_parent_constraint.tg[0].tr";
connectAttr "lt_ankle_ik_ctrl.ro" "lt_ankle_parent_constraint.tg[0].tro";
connectAttr "lt_ankle_ik_ctrl.s" "lt_ankle_parent_constraint.tg[0].ts";
connectAttr "lt_ankle_ik_ctrl.pm" "lt_ankle_parent_constraint.tg[0].tpm";
connectAttr "lt_ankle_parent_constraint.w0" "lt_ankle_parent_constraint.tg[0].tw"
		;
connectAttr "R_Pelvis_Joint.msg" "rt_ankle_ik_handle.hsj";
connectAttr "rt_ankle_ik_effector.hp" "rt_ankle_ik_handle.hee";
connectAttr "ikRPsolver.msg" "rt_ankle_ik_handle.hsv";
connectAttr "rt_ankle_parent_constraint.ctx" "rt_ankle_ik_handle.tx";
connectAttr "rt_ankle_parent_constraint.cty" "rt_ankle_ik_handle.ty";
connectAttr "rt_ankle_parent_constraint.ctz" "rt_ankle_ik_handle.tz";
connectAttr "rt_ankle_parent_constraint.crx" "rt_ankle_ik_handle.rx";
connectAttr "rt_ankle_parent_constraint.cry" "rt_ankle_ik_handle.ry";
connectAttr "rt_ankle_parent_constraint.crz" "rt_ankle_ik_handle.rz";
connectAttr "unitConversion4.o" "rt_ankle_ik_handle.twi";
connectAttr "rt_ankle_ik_handle.ro" "rt_ankle_parent_constraint.cro";
connectAttr "rt_ankle_ik_handle.pim" "rt_ankle_parent_constraint.cpim";
connectAttr "rt_ankle_ik_handle.rp" "rt_ankle_parent_constraint.crp";
connectAttr "rt_ankle_ik_handle.rpt" "rt_ankle_parent_constraint.crt";
connectAttr "rt_ankle_ik_ctrl.t" "rt_ankle_parent_constraint.tg[0].tt";
connectAttr "rt_ankle_ik_ctrl.rp" "rt_ankle_parent_constraint.tg[0].trp";
connectAttr "rt_ankle_ik_ctrl.rpt" "rt_ankle_parent_constraint.tg[0].trt";
connectAttr "rt_ankle_ik_ctrl.r" "rt_ankle_parent_constraint.tg[0].tr";
connectAttr "rt_ankle_ik_ctrl.ro" "rt_ankle_parent_constraint.tg[0].tro";
connectAttr "rt_ankle_ik_ctrl.s" "rt_ankle_parent_constraint.tg[0].ts";
connectAttr "rt_ankle_ik_ctrl.pm" "rt_ankle_parent_constraint.tg[0].tpm";
connectAttr "rt_ankle_parent_constraint.w0" "rt_ankle_parent_constraint.tg[0].tw"
		;
connectAttr "C_Root_Joint_parent_constraint.ctx" "C_Root_Joint.tx";
connectAttr "C_Root_Joint_parent_constraint.cty" "C_Root_Joint.ty";
connectAttr "C_Root_Joint_parent_constraint.ctz" "C_Root_Joint.tz";
connectAttr "C_Root_Joint_parent_constraint.crx" "C_Root_Joint.rx";
connectAttr "C_Root_Joint_parent_constraint.cry" "C_Root_Joint.ry";
connectAttr "C_Root_Joint_parent_constraint.crz" "C_Root_Joint.rz";
connectAttr "C_Root_Joint.s" "C_Hip_Joint.is";
connectAttr "C_Hip_Joint_parent_constraint.ctx" "C_Hip_Joint.tx";
connectAttr "C_Hip_Joint_parent_constraint.cty" "C_Hip_Joint.ty";
connectAttr "C_Hip_Joint_parent_constraint.ctz" "C_Hip_Joint.tz";
connectAttr "C_Hip_Joint_parent_constraint.crx" "C_Hip_Joint.rx";
connectAttr "C_Hip_Joint_parent_constraint.cry" "C_Hip_Joint.ry";
connectAttr "C_Hip_Joint_parent_constraint.crz" "C_Hip_Joint.rz";
connectAttr "C_Hip_Joint.s" "R_Pelvis_Joint.is";
connectAttr "R_Pelvis_Joint.s" "R_Knee_Joint.is";
connectAttr "R_Knee_Joint.s" "R_Ankle_Joint.is";
connectAttr "R_Ankle_Joint.s" "R_Ball_Joint.is";
connectAttr "R_Ball_Joint.s" "R_Toe_Joint.is";
connectAttr "R_Ankle_Joint.tx" "rt_ankle_ik_effector.tx";
connectAttr "R_Ankle_Joint.ty" "rt_ankle_ik_effector.ty";
connectAttr "R_Ankle_Joint.tz" "rt_ankle_ik_effector.tz";
connectAttr "C_Hip_Joint.s" "L_Pelvis_Joint.is";
connectAttr "L_Pelvis_Joint.s" "L_Knee_Joint.is";
connectAttr "L_Knee_Joint.s" "L_Ankle_Joint.is";
connectAttr "L_Ankle_Joint.s" "L_Ball_Joint.is";
connectAttr "L_Ball_Joint.s" "L_Toe_Joint.is";
connectAttr "L_Ankle_Joint.tx" "lt_ankle_ik_effector.tx";
connectAttr "L_Ankle_Joint.ty" "lt_ankle_ik_effector.ty";
connectAttr "L_Ankle_Joint.tz" "lt_ankle_ik_effector.tz";
connectAttr "C_Hip_Joint.ro" "C_Hip_Joint_parent_constraint.cro";
connectAttr "C_Hip_Joint.pim" "C_Hip_Joint_parent_constraint.cpim";
connectAttr "C_Hip_Joint.rp" "C_Hip_Joint_parent_constraint.crp";
connectAttr "C_Hip_Joint.rpt" "C_Hip_Joint_parent_constraint.crt";
connectAttr "C_Hip_Joint.jo" "C_Hip_Joint_parent_constraint.cjo";
connectAttr "ct_hip_ctrl.t" "C_Hip_Joint_parent_constraint.tg[0].tt";
connectAttr "ct_hip_ctrl.rp" "C_Hip_Joint_parent_constraint.tg[0].trp";
connectAttr "ct_hip_ctrl.rpt" "C_Hip_Joint_parent_constraint.tg[0].trt";
connectAttr "ct_hip_ctrl.r" "C_Hip_Joint_parent_constraint.tg[0].tr";
connectAttr "ct_hip_ctrl.ro" "C_Hip_Joint_parent_constraint.tg[0].tro";
connectAttr "ct_hip_ctrl.s" "C_Hip_Joint_parent_constraint.tg[0].ts";
connectAttr "ct_hip_ctrl.pm" "C_Hip_Joint_parent_constraint.tg[0].tpm";
connectAttr "C_Hip_Joint_parent_constraint.w0" "C_Hip_Joint_parent_constraint.tg[0].tw"
		;
connectAttr "C_Root_Joint.s" "C_Spine_Joint.is";
connectAttr "C_Spine_Joint_parent_constraint.ctx" "C_Spine_Joint.tx";
connectAttr "C_Spine_Joint_parent_constraint.cty" "C_Spine_Joint.ty";
connectAttr "C_Spine_Joint_parent_constraint.ctz" "C_Spine_Joint.tz";
connectAttr "C_Spine_Joint_parent_constraint.crx" "C_Spine_Joint.rx";
connectAttr "C_Spine_Joint_parent_constraint.cry" "C_Spine_Joint.ry";
connectAttr "C_Spine_Joint_parent_constraint.crz" "C_Spine_Joint.rz";
connectAttr "C_Spine_Joint.s" "C_Chest_Joint.is";
connectAttr "C_Chest_Joint_parent_constraint.ctx" "C_Chest_Joint.tx";
connectAttr "C_Chest_Joint_parent_constraint.cty" "C_Chest_Joint.ty";
connectAttr "C_Chest_Joint_parent_constraint.ctz" "C_Chest_Joint.tz";
connectAttr "C_Chest_Joint_parent_constraint.crx" "C_Chest_Joint.rx";
connectAttr "C_Chest_Joint_parent_constraint.cry" "C_Chest_Joint.ry";
connectAttr "C_Chest_Joint_parent_constraint.crz" "C_Chest_Joint.rz";
connectAttr "C_Chest_Joint.s" "R_Clavicle_Joint.is";
connectAttr "R_Clavicle_Joint_parent_constraint.ctx" "R_Clavicle_Joint.tx";
connectAttr "R_Clavicle_Joint_parent_constraint.cty" "R_Clavicle_Joint.ty";
connectAttr "R_Clavicle_Joint_parent_constraint.ctz" "R_Clavicle_Joint.tz";
connectAttr "R_Clavicle_Joint_parent_constraint.crx" "R_Clavicle_Joint.rx";
connectAttr "R_Clavicle_Joint_parent_constraint.cry" "R_Clavicle_Joint.ry";
connectAttr "R_Clavicle_Joint_parent_constraint.crz" "R_Clavicle_Joint.rz";
connectAttr "R_Clavicle_Joint.s" "R_Shoulder_Joint.is";
connectAttr "R_Shoulder_Joint.s" "R_Elbow_Joint.is";
connectAttr "R_Elbow_Joint.s" "R_Wrist_Joint.is";
connectAttr "R_Wrist_Joint.tx" "rt_wrist_ik_effector.tx";
connectAttr "R_Wrist_Joint.ty" "rt_wrist_ik_effector.ty";
connectAttr "R_Wrist_Joint.tz" "rt_wrist_ik_effector.tz";
connectAttr "R_Clavicle_Joint.ro" "R_Clavicle_Joint_parent_constraint.cro";
connectAttr "R_Clavicle_Joint.pim" "R_Clavicle_Joint_parent_constraint.cpim";
connectAttr "R_Clavicle_Joint.rp" "R_Clavicle_Joint_parent_constraint.crp";
connectAttr "R_Clavicle_Joint.rpt" "R_Clavicle_Joint_parent_constraint.crt";
connectAttr "R_Clavicle_Joint.jo" "R_Clavicle_Joint_parent_constraint.cjo";
connectAttr "rt_clavicle_ctrl.t" "R_Clavicle_Joint_parent_constraint.tg[0].tt";
connectAttr "rt_clavicle_ctrl.rp" "R_Clavicle_Joint_parent_constraint.tg[0].trp"
		;
connectAttr "rt_clavicle_ctrl.rpt" "R_Clavicle_Joint_parent_constraint.tg[0].trt"
		;
connectAttr "rt_clavicle_ctrl.r" "R_Clavicle_Joint_parent_constraint.tg[0].tr";
connectAttr "rt_clavicle_ctrl.ro" "R_Clavicle_Joint_parent_constraint.tg[0].tro"
		;
connectAttr "rt_clavicle_ctrl.s" "R_Clavicle_Joint_parent_constraint.tg[0].ts";
connectAttr "rt_clavicle_ctrl.pm" "R_Clavicle_Joint_parent_constraint.tg[0].tpm"
		;
connectAttr "R_Clavicle_Joint_parent_constraint.w0" "R_Clavicle_Joint_parent_constraint.tg[0].tw"
		;
connectAttr "C_Chest_Joint.s" "C_Neck_Joint.is";
connectAttr "C_Neck_Joint_parent_constraint.ctx" "C_Neck_Joint.tx";
connectAttr "C_Neck_Joint_parent_constraint.cty" "C_Neck_Joint.ty";
connectAttr "C_Neck_Joint_parent_constraint.ctz" "C_Neck_Joint.tz";
connectAttr "C_Neck_Joint_parent_constraint.crx" "C_Neck_Joint.rx";
connectAttr "C_Neck_Joint_parent_constraint.cry" "C_Neck_Joint.ry";
connectAttr "C_Neck_Joint_parent_constraint.crz" "C_Neck_Joint.rz";
connectAttr "C_Neck_Joint.s" "C_Head_Joint.is";
connectAttr "C_Head_Joint_parent_constraint.ctx" "C_Head_Joint.tx";
connectAttr "C_Head_Joint_parent_constraint.cty" "C_Head_Joint.ty";
connectAttr "C_Head_Joint_parent_constraint.ctz" "C_Head_Joint.tz";
connectAttr "C_Head_Joint_parent_constraint.crx" "C_Head_Joint.rx";
connectAttr "C_Head_Joint_parent_constraint.cry" "C_Head_Joint.ry";
connectAttr "C_Head_Joint_parent_constraint.crz" "C_Head_Joint.rz";
connectAttr "C_Head_Joint.s" "C_Tip_Joint.is";
connectAttr "C_Head_Joint.ro" "C_Head_Joint_parent_constraint.cro";
connectAttr "C_Head_Joint.pim" "C_Head_Joint_parent_constraint.cpim";
connectAttr "C_Head_Joint.rp" "C_Head_Joint_parent_constraint.crp";
connectAttr "C_Head_Joint.rpt" "C_Head_Joint_parent_constraint.crt";
connectAttr "C_Head_Joint.jo" "C_Head_Joint_parent_constraint.cjo";
connectAttr "ct_head_ctrl.t" "C_Head_Joint_parent_constraint.tg[0].tt";
connectAttr "ct_head_ctrl.rp" "C_Head_Joint_parent_constraint.tg[0].trp";
connectAttr "ct_head_ctrl.rpt" "C_Head_Joint_parent_constraint.tg[0].trt";
connectAttr "ct_head_ctrl.r" "C_Head_Joint_parent_constraint.tg[0].tr";
connectAttr "ct_head_ctrl.ro" "C_Head_Joint_parent_constraint.tg[0].tro";
connectAttr "ct_head_ctrl.s" "C_Head_Joint_parent_constraint.tg[0].ts";
connectAttr "ct_head_ctrl.pm" "C_Head_Joint_parent_constraint.tg[0].tpm";
connectAttr "C_Head_Joint_parent_constraint.w0" "C_Head_Joint_parent_constraint.tg[0].tw"
		;
connectAttr "C_Neck_Joint.ro" "C_Neck_Joint_parent_constraint.cro";
connectAttr "C_Neck_Joint.pim" "C_Neck_Joint_parent_constraint.cpim";
connectAttr "C_Neck_Joint.rp" "C_Neck_Joint_parent_constraint.crp";
connectAttr "C_Neck_Joint.rpt" "C_Neck_Joint_parent_constraint.crt";
connectAttr "C_Neck_Joint.jo" "C_Neck_Joint_parent_constraint.cjo";
connectAttr "ct_neck_ctrl.t" "C_Neck_Joint_parent_constraint.tg[0].tt";
connectAttr "ct_neck_ctrl.rp" "C_Neck_Joint_parent_constraint.tg[0].trp";
connectAttr "ct_neck_ctrl.rpt" "C_Neck_Joint_parent_constraint.tg[0].trt";
connectAttr "ct_neck_ctrl.r" "C_Neck_Joint_parent_constraint.tg[0].tr";
connectAttr "ct_neck_ctrl.ro" "C_Neck_Joint_parent_constraint.tg[0].tro";
connectAttr "ct_neck_ctrl.s" "C_Neck_Joint_parent_constraint.tg[0].ts";
connectAttr "ct_neck_ctrl.pm" "C_Neck_Joint_parent_constraint.tg[0].tpm";
connectAttr "C_Neck_Joint_parent_constraint.w0" "C_Neck_Joint_parent_constraint.tg[0].tw"
		;
connectAttr "C_Chest_Joint.s" "L_Clavicle_Joint.is";
connectAttr "L_Clavicle_Joint_parent_constraint.ctx" "L_Clavicle_Joint.tx";
connectAttr "L_Clavicle_Joint_parent_constraint.cty" "L_Clavicle_Joint.ty";
connectAttr "L_Clavicle_Joint_parent_constraint.ctz" "L_Clavicle_Joint.tz";
connectAttr "L_Clavicle_Joint_parent_constraint.crx" "L_Clavicle_Joint.rx";
connectAttr "L_Clavicle_Joint_parent_constraint.cry" "L_Clavicle_Joint.ry";
connectAttr "L_Clavicle_Joint_parent_constraint.crz" "L_Clavicle_Joint.rz";
connectAttr "L_Clavicle_Joint.s" "L_Shoulder_Joint.is";
connectAttr "L_Shoulder_Joint.s" "L_Elbow_Joint.is";
connectAttr "L_Elbow_Joint.s" "L_Wrist_Joint.is";
connectAttr "L_Wrist_Joint.tx" "lt_wrist_ik_effector.tx";
connectAttr "L_Wrist_Joint.ty" "lt_wrist_ik_effector.ty";
connectAttr "L_Wrist_Joint.tz" "lt_wrist_ik_effector.tz";
connectAttr "L_Clavicle_Joint.ro" "L_Clavicle_Joint_parent_constraint.cro";
connectAttr "L_Clavicle_Joint.pim" "L_Clavicle_Joint_parent_constraint.cpim";
connectAttr "L_Clavicle_Joint.rp" "L_Clavicle_Joint_parent_constraint.crp";
connectAttr "L_Clavicle_Joint.rpt" "L_Clavicle_Joint_parent_constraint.crt";
connectAttr "L_Clavicle_Joint.jo" "L_Clavicle_Joint_parent_constraint.cjo";
connectAttr "lt_clavicle_ctrl.t" "L_Clavicle_Joint_parent_constraint.tg[0].tt";
connectAttr "lt_clavicle_ctrl.rp" "L_Clavicle_Joint_parent_constraint.tg[0].trp"
		;
connectAttr "lt_clavicle_ctrl.rpt" "L_Clavicle_Joint_parent_constraint.tg[0].trt"
		;
connectAttr "lt_clavicle_ctrl.r" "L_Clavicle_Joint_parent_constraint.tg[0].tr";
connectAttr "lt_clavicle_ctrl.ro" "L_Clavicle_Joint_parent_constraint.tg[0].tro"
		;
connectAttr "lt_clavicle_ctrl.s" "L_Clavicle_Joint_parent_constraint.tg[0].ts";
connectAttr "lt_clavicle_ctrl.pm" "L_Clavicle_Joint_parent_constraint.tg[0].tpm"
		;
connectAttr "L_Clavicle_Joint_parent_constraint.w0" "L_Clavicle_Joint_parent_constraint.tg[0].tw"
		;
connectAttr "C_Chest_Joint.ro" "C_Chest_Joint_parent_constraint.cro";
connectAttr "C_Chest_Joint.pim" "C_Chest_Joint_parent_constraint.cpim";
connectAttr "C_Chest_Joint.rp" "C_Chest_Joint_parent_constraint.crp";
connectAttr "C_Chest_Joint.rpt" "C_Chest_Joint_parent_constraint.crt";
connectAttr "C_Chest_Joint.jo" "C_Chest_Joint_parent_constraint.cjo";
connectAttr "ct_chest_ctrl.t" "C_Chest_Joint_parent_constraint.tg[0].tt";
connectAttr "ct_chest_ctrl.rp" "C_Chest_Joint_parent_constraint.tg[0].trp";
connectAttr "ct_chest_ctrl.rpt" "C_Chest_Joint_parent_constraint.tg[0].trt";
connectAttr "ct_chest_ctrl.r" "C_Chest_Joint_parent_constraint.tg[0].tr";
connectAttr "ct_chest_ctrl.ro" "C_Chest_Joint_parent_constraint.tg[0].tro";
connectAttr "ct_chest_ctrl.s" "C_Chest_Joint_parent_constraint.tg[0].ts";
connectAttr "ct_chest_ctrl.pm" "C_Chest_Joint_parent_constraint.tg[0].tpm";
connectAttr "C_Chest_Joint_parent_constraint.w0" "C_Chest_Joint_parent_constraint.tg[0].tw"
		;
connectAttr "C_Spine_Joint.ro" "C_Spine_Joint_parent_constraint.cro";
connectAttr "C_Spine_Joint.pim" "C_Spine_Joint_parent_constraint.cpim";
connectAttr "C_Spine_Joint.rp" "C_Spine_Joint_parent_constraint.crp";
connectAttr "C_Spine_Joint.rpt" "C_Spine_Joint_parent_constraint.crt";
connectAttr "C_Spine_Joint.jo" "C_Spine_Joint_parent_constraint.cjo";
connectAttr "ct_spine_ctrl.t" "C_Spine_Joint_parent_constraint.tg[0].tt";
connectAttr "ct_spine_ctrl.rp" "C_Spine_Joint_parent_constraint.tg[0].trp";
connectAttr "ct_spine_ctrl.rpt" "C_Spine_Joint_parent_constraint.tg[0].trt";
connectAttr "ct_spine_ctrl.r" "C_Spine_Joint_parent_constraint.tg[0].tr";
connectAttr "ct_spine_ctrl.ro" "C_Spine_Joint_parent_constraint.tg[0].tro";
connectAttr "ct_spine_ctrl.s" "C_Spine_Joint_parent_constraint.tg[0].ts";
connectAttr "ct_spine_ctrl.pm" "C_Spine_Joint_parent_constraint.tg[0].tpm";
connectAttr "C_Spine_Joint_parent_constraint.w0" "C_Spine_Joint_parent_constraint.tg[0].tw"
		;
connectAttr "C_Root_Joint.ro" "C_Root_Joint_parent_constraint.cro";
connectAttr "C_Root_Joint.pim" "C_Root_Joint_parent_constraint.cpim";
connectAttr "C_Root_Joint.rp" "C_Root_Joint_parent_constraint.crp";
connectAttr "C_Root_Joint.rpt" "C_Root_Joint_parent_constraint.crt";
connectAttr "C_Root_Joint.jo" "C_Root_Joint_parent_constraint.cjo";
connectAttr "ct_root_ctrl.t" "C_Root_Joint_parent_constraint.tg[0].tt";
connectAttr "ct_root_ctrl.rp" "C_Root_Joint_parent_constraint.tg[0].trp";
connectAttr "ct_root_ctrl.rpt" "C_Root_Joint_parent_constraint.tg[0].trt";
connectAttr "ct_root_ctrl.r" "C_Root_Joint_parent_constraint.tg[0].tr";
connectAttr "ct_root_ctrl.ro" "C_Root_Joint_parent_constraint.tg[0].tro";
connectAttr "ct_root_ctrl.s" "C_Root_Joint_parent_constraint.tg[0].ts";
connectAttr "ct_root_ctrl.pm" "C_Root_Joint_parent_constraint.tg[0].tpm";
connectAttr "C_Root_Joint_parent_constraint.w0" "C_Root_Joint_parent_constraint.tg[0].tw"
		;
relationship "link" ":lightLinker1" ":initialShadingGroup.message" ":defaultLightSet.message";
relationship "link" ":lightLinker1" ":initialParticleSE.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" ":initialShadingGroup.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" ":initialParticleSE.message" ":defaultLightSet.message";
connectAttr "layerManager.dli[0]" "defaultLayer.id";
connectAttr "renderLayerManager.rlmi[0]" "defaultRenderLayer.rlid";
connectAttr "lt_wrist_ik_ctrl.twist" "unitConversion1.i";
connectAttr "rt_wrist_ik_ctrl.twist" "unitConversion2.i";
connectAttr "lt_ankle_ik_ctrl.twist" "unitConversion3.i";
connectAttr "rt_ankle_ik_ctrl.twist" "unitConversion4.i";
connectAttr "defaultRenderLayer.msg" ":defaultRenderingList1.r" -na;
connectAttr "ikRPsolver.msg" ":ikSystem.sol" -na;
// End of walk.ma
