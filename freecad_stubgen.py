# coding: utf8
"""This module generate freecad stubs using mypy.stubgen. See README.md for further info.

© All rights reserved.
Cyril Waechter

See the LICENSE.TXT file for more details.

Author : Cyril Waechter
"""
import sys
import os
from mypy import stubgen
from mypy.stubgen import Options
import FreeCAD
import FreeCADGui

FC_MODULES = (
    "FreeCAD",
    "FreeCADGui",
    "FreeCAD.Base",
    "FreeCAD.Console",
    "FreeCAD.Units",
    "__FreeCADBase__",
    "__FreeCADConsole__",
    "__Translate__",
    "AddonManager",
    "DraftUtils",
    "DraftVecUtils",
    "Drawing",
    "DrawingGui",
    "Fem",
    "FemGui",
    "Image",
    "ImageGui",
    "Import",
    "ImportGui",
    "Inspection",
    "InspectionGui" "Measure",
    "Mesh",
    "MeshGui",
    "MeshPart",
    "MeshPartGui",
    "Part",
    "Part.BRepOffsetAPI",
    "Part.Geom2d",
    "PartGui",
    "PartDesign",
    "Path",
    "PathGui",
    "PathSimulator",
    "Points",
    "PointsGui",
    "QtUnitGui",
    "Raytracing",
    "RaytracingGui",
    "ReverseEngineering",
    "ReverseEngineeringGui",
    "Robot",
    "RobotGui",
    "Sketcher",
    "SketcherGui",
    "Spreadsheet",
    "SpreadsheetGui",
    "Start",
    "StartGui",
    "Surface",
    "SurfaceGui",
    "WorkingPlane",
    "TechDraw",
    "TechDrawGui",
    "Web",
    "WebGui",
    "Data",
    "Data.ImportPointFile",
)


def freecad_options() -> Options:
    """Create options which currently seems to generate the best stubs"""
    # Create the output folder if it doesn't already exist.
    output_dir = "/home/cyril/git/freecad-stubs/out"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    return Options(
        pyversion=sys.version_info[:2],
        no_import=False,
        doc_dir="",
        search_path="",
        interpreter="",
        ignore_errors=True,
        parse_only=False,
        include_private=True,
        output_dir=output_dir,
        modules=list(FC_MODULES),
        packages=[],
        files=[],
        verbose=False,
        quiet=True,
        export_less=False,
    )


def main() -> None:
    """Generate freecad stubs"""
    FreeCAD.newDocument()
    FreeCADGui.showMainWindow()  # Apparently it generate better stubs if Gui is up
    options = freecad_options()
    stubgen.generate_stubs(options)


if __name__ == "__main__":
    main()
