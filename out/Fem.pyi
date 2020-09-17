from typing import Any

import Data

def export(list, string) -> Any: ...
def insert(*args, **kwargs) -> Any: ...
def open(string) -> Any: ...
def read(*args, **kwargs) -> Any: ...
def readResult(*args, **kwargs) -> Any: ...
def show(*args, **kwargs) -> Any: ...
def writeResult(*args, **kwargs) -> Any: ...

class FemMesh(Data.ComplexGeoData):
    EdgeCount: Any = ...
    Edges: Any = ...
    EdgesOnly: Any = ...
    FaceCount: Any = ...
    Faces: Any = ...
    FacesOnly: Any = ...
    GroupCount: Any = ...
    Groups: Any = ...
    HexaCount: Any = ...
    NodeCount: Any = ...
    Nodes: Any = ...
    PolygonCount: Any = ...
    PolyhedronCount: Any = ...
    PrismCount: Any = ...
    PyramidCount: Any = ...
    QuadrangleCount: Any = ...
    SubMeshCount: Any = ...
    TetraCount: Any = ...
    TriangleCount: Any = ...
    Volume: Any = ...
    VolumeCount: Any = ...
    Volumes: Any = ...
    def __init__(self, *args, **kwargs) -> None: ...
    def addEdge(self, *args, **kwargs) -> Any: ...
    def addFace(self, *args, **kwargs) -> Any: ...
    def addGroup(self, *args, **kwargs) -> Any: ...
    def addGroupElements(groupid, list_of_elements) -> Any: ...
    def addHypothesis(self, *args, **kwargs) -> Any: ...
    def addNode(self, *args, **kwargs) -> Any: ...
    def addQuad(self, *args, **kwargs) -> Any: ...
    def addVolume(self, *args, **kwargs) -> Any: ...
    def compute(self, *args, **kwargs) -> Any: ...
    def copy(self, *args, **kwargs) -> Any: ...
    def getEdgesByEdge(self, *args, **kwargs) -> Any: ...
    def getElementNodes(self, *args, **kwargs) -> Any: ...
    def getElementType(self, *args, **kwargs) -> Any: ...
    def getFacesByFace(self, *args, **kwargs) -> Any: ...
    def getGroupElementType(self, *args, **kwargs) -> Any: ...
    def getGroupElements(self, *args, **kwargs) -> Any: ...
    def getGroupName(self, *args, **kwargs) -> Any: ...
    def getIdByElementType(self, *args, **kwargs) -> Any: ...
    def getNodeById(self, *args, **kwargs) -> Any: ...
    def getNodesByEdge(self, *args, **kwargs) -> Any: ...
    def getNodesByFace(self, *args, **kwargs) -> Any: ...
    def getNodesBySolid(self, *args, **kwargs) -> Any: ...
    def getNodesByVertex(self, *args, **kwargs) -> Any: ...
    def getVolumesByFace(self, *args, **kwargs) -> Any: ...
    def getccxVolumesByFace(self, *args, **kwargs) -> Any: ...
    def read(self, *args, **kwargs) -> Any: ...
    def removeGroup(groupid) -> Any: ...
    def setShape(self, *args, **kwargs) -> Any: ...
    def setStandardHypotheses(self, *args, **kwargs) -> Any: ...
    def setTransform(self, *args, **kwargs) -> Any: ...
    def write(self, *args, **kwargs) -> Any: ...
    def writeABAQUS(file, intelemParam, boolgroupParam) -> Any: ...
    def __delattr__(self, name) -> Any: ...
    def __setattr__(self, name, value) -> Any: ...

class StdMeshers_Arithmetic1D:
    @classmethod
    def __init__(self, *args, **kwargs) -> None: ...

class StdMeshers_AutomaticLength:
    @classmethod
    def __init__(self, *args, **kwargs) -> None: ...

class StdMeshers_CompositeSegment_1D:
    @classmethod
    def __init__(self, *args, **kwargs) -> None: ...

class StdMeshers_Deflection1D:
    @classmethod
    def __init__(self, *args, **kwargs) -> None: ...

class StdMeshers_Hexa_3D:
    @classmethod
    def __init__(self, *args, **kwargs) -> None: ...

class StdMeshers_LayerDistribution:
    @classmethod
    def __init__(self, *args, **kwargs) -> None: ...

class StdMeshers_LengthFromEdges:
    @classmethod
    def __init__(self, *args, **kwargs) -> None: ...

class StdMeshers_LocalLength:
    @classmethod
    def __init__(self, *args, **kwargs) -> None: ...

class StdMeshers_MEFISTO_2D:
    @classmethod
    def __init__(self, *args, **kwargs) -> None: ...

class StdMeshers_MaxElementArea:
    @classmethod
    def __init__(self, *args, **kwargs) -> None: ...

class StdMeshers_MaxElementVolume:
    @classmethod
    def __init__(self, *args, **kwargs) -> None: ...

class StdMeshers_MaxLength:
    @classmethod
    def __init__(self, *args, **kwargs) -> None: ...

class StdMeshers_NotConformAllowed:
    @classmethod
    def __init__(self, *args, **kwargs) -> None: ...

class StdMeshers_NumberOfLayers:
    @classmethod
    def __init__(self, *args, **kwargs) -> None: ...

class StdMeshers_NumberOfSegments:
    @classmethod
    def __init__(self, *args, **kwargs) -> None: ...

class StdMeshers_Prism_3D:
    @classmethod
    def __init__(self, *args, **kwargs) -> None: ...

class StdMeshers_ProjectionSource1D:
    @classmethod
    def __init__(self, *args, **kwargs) -> None: ...

class StdMeshers_ProjectionSource2D:
    @classmethod
    def __init__(self, *args, **kwargs) -> None: ...

class StdMeshers_ProjectionSource3D:
    @classmethod
    def __init__(self, *args, **kwargs) -> None: ...

class StdMeshers_Projection_1D:
    @classmethod
    def __init__(self, *args, **kwargs) -> None: ...

class StdMeshers_Projection_2D:
    @classmethod
    def __init__(self, *args, **kwargs) -> None: ...

class StdMeshers_Projection_3D:
    @classmethod
    def __init__(self, *args, **kwargs) -> None: ...

class StdMeshers_QuadranglePreference:
    @classmethod
    def __init__(self, *args, **kwargs) -> None: ...

class StdMeshers_Quadrangle_2D:
    @classmethod
    def __init__(self, *args, **kwargs) -> None: ...

class StdMeshers_QuadraticMesh:
    @classmethod
    def __init__(self, *args, **kwargs) -> None: ...

class StdMeshers_RadialPrism_3D:
    @classmethod
    def __init__(self, *args, **kwargs) -> None: ...

class StdMeshers_Regular_1D:
    @classmethod
    def __init__(self, *args, **kwargs) -> None: ...

class StdMeshers_SegmentAroundVertex_0D:
    @classmethod
    def __init__(self, *args, **kwargs) -> None: ...

class StdMeshers_SegmentLengthAroundVertex:
    @classmethod
    def __init__(self, *args, **kwargs) -> None: ...

class StdMeshers_StartEndLength:
    @classmethod
    def __init__(self, *args, **kwargs) -> None: ...

class StdMeshers_UseExisting_1D:
    @classmethod
    def __init__(self, *args, **kwargs) -> None: ...

class StdMeshers_UseExisting_2D:
    @classmethod
    def __init__(self, *args, **kwargs) -> None: ...