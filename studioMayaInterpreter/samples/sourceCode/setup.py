from cx_Freeze import setup, Executable
setup(
    name = "Smart Maya v0.1",
    version = "0.1",
    description = "Maya File edit, quary and create",
    executables = [Executable("smartMaya.py")],
    )
