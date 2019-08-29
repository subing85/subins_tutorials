set my_python_path=C:/Python27

set STUDIO_PATH=%cd%
set PYTHONPATH=%cd%;%my_python_path%;%PYTHONPATH%

echo PYTHONPATH

echo ""
echo "Studio Maya"
echo "0.0.1 Release"
echo "www.subins-toolkits.comm"
echo "subing85@gmail.com"
echo ""


"%my_python_path%/python.exe" %cd%"/studio_maya/__init__.py"
