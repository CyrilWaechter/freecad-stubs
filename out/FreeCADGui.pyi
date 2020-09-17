from typing import Any

from typing import overload
import Base
ActiveDocument: Any
Control: Any
Snapper: Any
draftToolBar: Any

def SendMsgToActiveView(*args, **kwargs) -> Any: ...
def activateView(type) -> Any: ...
def activateWorkbench(string) -> None: ...
def activeDocument(*args, **kwargs) -> Any: ...
def activeView(typename = ...) -> objectorNone: ...
def activeWorkbench(*args, **kwargs) -> Any: ...
def addCommand(string, object) -> None: ...
def addDocumentObserver(*args, **kwargs) -> Any: ...
def addIcon(string, stringorlist) -> None: ...
def addIconPath(string) -> None: ...
def addLanguagePath(string) -> None: ...
def addModule(string) -> None: ...
def addPreferencePage(*args, **kwargs) -> Any: ...
def addResourcePath(string) -> None: ...
def addWorkbench(string, object) -> None: ...
def coinRemoveAllChildren(*args, **kwargs) -> Any: ...
def createDialog(string) -> Any: ...
def createViewer(*args, **kwargs) -> Any: ...
def doCommand(string) -> None: ...
def doCommandGui(string) -> None: ...
def editDocument(*args, **kwargs) -> Any: ...
def embedToWindow(*args, **kwargs) -> Any: ...
def exec_loop(*args, **kwargs) -> Any: ...
def export(*args, **kwargs) -> Any: ...
def exportSubgraph(*args, **kwargs) -> Any: ...
def getDocument(string) -> object: ...
def getIcon(string) -> QIcon: ...
def getLocale(*args, **kwargs) -> Any: ...
def getMainWindow(*args, **kwargs) -> Any: ...
def getMarkerIndex(*args, **kwargs) -> Any: ...
def getSoDBVersion(*args, **kwargs) -> Any: ...
def getWorkbench(string) -> object: ...
def hide(*args, **kwargs) -> Any: ...
def hideObject(object) -> None: ...
def insert(*args, **kwargs) -> Any: ...
def isIconCached(String) -> Bool: ...
def listCommands(*args, **kwargs) -> Any: ...
def listWorkbenches(*args, **kwargs) -> Any: ...
def loadFile(*args, **kwargs) -> Any: ...
def open(*args, **kwargs) -> Any: ...
def reload(name) -> doc: ...
def removeDocumentObserver(*args, **kwargs) -> Any: ...
def removeWorkbench(string) -> None: ...
def runCommand(string) -> None: ...
def sendMsgToFocusView(*args, **kwargs) -> Any: ...
def setActiveDocument(*args, **kwargs) -> Any: ...
def setLocale(*args, **kwargs) -> Any: ...
def setupWithoutGUI(*args, **kwargs) -> Any: ...
def show(*args, **kwargs) -> Any: ...
def showDownloads(*args, **kwargs) -> Any: ...
def showMainWindow(*args, **kwargs) -> Any: ...
def showObject(object) -> None: ...
def showPreferences(*args, **kwargs) -> Any: ...
def subgraphFromObject(object) -> Node: ...
def supportedLocales(*args, **kwargs) -> Any: ...
def updateGui(*args, **kwargs) -> Any: ...
def updateLocale(*args, **kwargs) -> Any: ...

class AxisOrigin(Base.BaseClass):
    AxisLength: Any = ...
    Labels: Any = ...
    LineWidth: Any = ...
    Node: Any = ...
    Plane: Any = ...
    PointSize: Any = ...
    Scale: Any = ...
    def __init__(self, *args, **kwargs) -> None: ...
    def getDetailPath(subname, path) -> Any: ...
    def getElementPicked(pickPoint) -> Any: ...
    def __delattr__(self, name) -> Any: ...
    def __setattr__(self, name, value) -> Any: ...

class Command(PyObjectBase):
    def __init__(self, *args, **kwargs) -> None: ...
    def get(self, *args, **kwargs) -> Any: ...
    def getInfo(self, *args, **kwargs) -> Any: ...
    def getShortcut(self, *args, **kwargs) -> Any: ...
    def isActive(self, *args, **kwargs) -> Any: ...
    def listAll(self, *args, **kwargs) -> Any: ...
    def listByShortcut(self, *args, **kwargs) -> Any: ...
    def resetShortcut(self, *args, **kwargs) -> Any: ...
    def run(self, *args, **kwargs) -> Any: ...
    def setShortcut(string) -> bool: ...
    def update(self, *args, **kwargs) -> Any: ...
    def __delattr__(self, name) -> Any: ...
    def __setattr__(self, name, value) -> Any: ...

class ExpressionBinding:
    @classmethod
    def __init__(self, *args, **kwargs) -> None: ...

class LinkView(Base.BaseClass):
    Count: Any = ...
    LinkedView: Any = ...
    Owner: Any = ...
    RootNode: Any = ...
    SubNames: Any = ...
    Visibilities: Any = ...
    def __init__(self, *args, **kwargs) -> None: ...
    def getBoundBox(vobj = ...) -> Any: ...
    def getChildren(self, *args, **kwargs) -> Any: ...
    def getDetailPath(element) -> Any: ...
    def getElementPicked(pickPoint) -> Any: ...
    def reset(self, *args, **kwargs) -> Any: ...
    def setChildren(self, *args, **kwargs) -> Any: ...
    @overload
    def setLink(object) -> Any: ...
    @overload
    def setLink(object, subname) -> Any: ...
    def setMaterial(Material) -> Any: ...
    def setTransform(matrix) -> Any: ...
    def setType(type, sublink = ...) -> Any: ...
    def __delattr__(self, name) -> Any: ...
    def __setattr__(self, name, value) -> Any: ...

class UiLoader:
    @classmethod
    def __init__(self, *args, **kwargs) -> None: ...

class Workbench:
    ContextMenu: Any = ...
    GetClassName: Any = ...
    Initialize: Any = ...
    MenuText: Any = ...
    ToolTip: Any = ...
    appendCommandbar: Any = ...
    appendContextMenu: Any = ...
    appendMenu: Any = ...
    appendToolbar: Any = ...
    getToolbarItems: Any = ...
    listCommandbars: Any = ...
    listMenus: Any = ...
    listToolbars: Any = ...
    name: Any = ...
    removeCommandbar: Any = ...
    removeContextMenu: Any = ...
    removeMenu: Any = ...
    removeToolbar: Any = ...