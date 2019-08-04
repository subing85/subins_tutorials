from cx_Freeze import setup, Executable
includes = ["atexit", "PyQt4.QtCore"] 
exe = Executable(
	script = "example.pyw",
	base = "Win32GUI"
	)
 
setup(
	options = {"build_exe": {"includes": includes}},
	executables = [exe]
	)

#includes = ["sip","re","atexit","PyQt4.QtCore"]
