from typing import Any, Optional

__title__: str
__author__: str
__url__: str
long = int
params: Any

def precision(): ...
def typecheck(args_and_types: Any, name: str = ...) -> None: ...
def toString(u: Any): ...
def tup(u: Any, array: bool = ...): ...
def neg(u: Any): ...
def equals(u: Any, v: Any): ...
def scale(u: Any, scalar: Any): ...
def scaleTo(u: Any, l: Any): ...
def dist(u: Any, v: Any): ...
def angle(u: Any, v: Any = ..., normal: Any = ...): ...
def project(u: Any, v: Any): ...
def rotate2D(u: Any, angle: Any): ...
def rotate(u: Any, angle: Any, axis: Any = ...): ...
def getRotation(vector: Any, reference: Any = ...): ...
def isNull(vector: Any): ...
def find(vector: Any, vlist: Any): ...
def closest(vector: Any, vlist: Any): ...
def isColinear(vlist: Any): ...
def rounded(v: Any, d: Optional[Any] = ...): ...
def getPlaneRotation(u: Any, v: Any, w: Optional[Any] = ...): ...
def removeDoubles(vlist: Any): ...
