from typing import Any

class ImportPointFile:
    Path: Any = ...
    IPFui: Any = ...
    CPGui: Any = ...
    Resources: Any = ...
    GroupList: Any = ...
    def __init__(self) -> None: ...
    def GetResources(self): ...
    def IsActive(self): ...
    def Activated(self) -> None: ...
    def AddFile(self) -> None: ...
    def RemoveFile(self) -> None: ...
    def ActivatePointGroups(self) -> None: ...
    def LoadCPGui(self) -> None: ...
    def CreatePointGroup(self) -> None: ...
    PointList: Any = ...
    def FileReader(self, File: Any, Operation: Any) -> None: ...
    def Preview(self) -> None: ...
    def ImportFile(self) -> None: ...
