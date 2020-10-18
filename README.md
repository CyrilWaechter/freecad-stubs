# freecad-stubs project
This project use [mypy.stubgen](https://github.com/python/mypy/blob/master/mypy/stubgen.py) to generate stubs for FreeCAD modules

# Usage
1. Clone repo : `git clone https://github.com/CyrilWaechter/freecad-stubs.git`
2. Make sure your IDE check `/out` for stubs. eg. for vscode/code-oss you can create an `.env` file
at workspace root to allow your linter / auto-completer (eg. pylint /  jedi) 
```shell
FREECAD_LIB=/usr/lib/freecad/lib
FREECAD_STUBS=/home/<user>/git/freecad-stubs/out
PYTHONPATH=${FREECAD_STUBS}:${FREECAD_LIB}:${PYTHONPATH}
```

# Context
This stubs generator was developed as part of a FreeCAD community effort to make development 
around FreeCAD easier. See :
* [Type-checked Python](https://forum.freecadweb.org/viewtopic.php?t=49917)
* [Please demonstrate using a remote text editor to substitute the Python editor in FreeCAD](https://forum.freecadweb.org/viewtopic.php?f=8&t=40673)

You might also want to checkout [Vanuan / freecad-python-stubs](https://github.com/Vanuan/freecad-python-stubs) which might superseed this 
repository at some point.

# Known issues
* Do not generate stubs for some submodules :
    * FreeCAD.Units
* Generated types are mainly not accurate