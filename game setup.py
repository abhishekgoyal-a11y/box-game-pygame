import cx_Freeze
executables = [cx_Freeze.Executable("game1.py")]

cx_Freeze.setup(
    name="BOX GAME",
    options={"build_exe": {"packages":["pygame"],
                            "include_files": ["background.jpg", "player.png",
                                               "background.wav", "gameover.wav",
                                               "hit.wav", "point.wav"]}},
    executables = executables
    )
