from cx_Freeze import setup, Executable
base = None

executables = [Executable(script="TamaGoPy.py", base=base, icon="icon.ico")]
includefiles = ["playername.dat", "tama1.dat", "tama2.dat"]


setup(

    name = "TamaGoPy",
    author = "khyrthy",
    version = "0.1.4.0", # 0 for "Alpha"
    description = 'A tamagotchi displayed in command line',
    executables = executables,
    options = { 'build_exe':  {'include_files':includefiles}}
    
    )