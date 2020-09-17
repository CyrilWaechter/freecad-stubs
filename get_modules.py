# coding: utf8
"""Attempt to automatically generate modules list. No good result at the moment

© All rights reserved.
Cyril Waechter

See the LICENSE.TXT file for more details.

Author : Cyril Waechter
"""
import sys
import inspect
from typing import List
import FreeCAD
import FreeCADGui
import Part
import PartDesign


def generate_freecad_modules() -> List[str]:
    result = []
    for m_name, m in sys.modules.items():
        path = ""
        try:
            path = inspect.getfile(m)
        except TypeError:
            path = "python"
        except (NameError, AttributeError):
            pass
        if "python" in path:
            continue
        result.append(m_name)
    return result


if __name__ == "__main__":
    FreeCAD.newDocument()
    FreeCADGui.showMainWindow()
    print(generate_freecad_modules())
