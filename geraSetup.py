import cx_Freeze


executables = [
    cx_Freeze.Executable(script="main.py", icon="Recursos/logo.ico")
]

cx_Freeze.setup(
    name = "corrida Maluca",
    options = {
        "build_exe":{
            "packages":["pygame"],
            "include_files":["Recursos"]
        }
    }, executables = executables
)
