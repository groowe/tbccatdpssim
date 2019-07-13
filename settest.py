from cx_Freeze import setup,Executable

executables = [Executable("testfont.py")]
build_exe_options = {"packages": ["pygame"]}

setup( name = "testfont",
        options = {"build_exe": build_exe_options},
        executables = executables
        )
