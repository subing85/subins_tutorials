set STUDIO_PATH=%cd%
set PYTHONPATH=%cd%

echo ""
echo "Asset Library"
echo "0.0.1 Release"
echo "www.subins-toolkits.comm"
echo "subing85@gmail.com"
echo ""

"C:/Program Files/Autodesk/Maya2016/bin/mayapy.exe" %cd%"/assetLibrary/__init__.py"
