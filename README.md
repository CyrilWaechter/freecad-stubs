# freecad-stubs project
This project use [mypy.stubgen](https://github.com/python/mypy/blob/master/mypy/stubgen.py) to generate stubs for FreeCAD modules

# Usage
1. Clone repo : `git clone `
2. Make sure your IDE check `/out` for stubs. eg. for vscode/code-oss you can create an `.env` file
at workspace root to allow your linter / auto-completer (eg. pylint /  jedi) 
```shell
FREECAD_LIB=/usr/lib/freecad/lib
FREECAD_STUBS=/home/<user>/git/freecad-stubs/out
PYTHONPATH=${FREECAD_STUBS}:${FREECAD_LIB}:${PYTHONPATH}
```

# Known issues
* Do not generate stubs for some submodules :
    * FreeCAD.Units
* Generated types are mainly not accurate