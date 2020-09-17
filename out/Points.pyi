from typing import Any

import Data

def export(*args, **kwargs) -> Any: ...
def insert(*args, **kwargs) -> Any: ...
def open(*args, **kwargs) -> Any: ...
def show(*args, **kwargs) -> Any: ...

class Points(Data.ComplexGeoData):
    CountPoints: Any = ...
    Points: Any = ...
    def __init__(self, *args, **kwargs) -> None: ...
    def addPoints(self, *args, **kwargs) -> Any: ...
    def copy(self, *args, **kwargs) -> Any: ...
    def fromSegment(self, *args, **kwargs) -> Any: ...
    def fromValid(self, *args, **kwargs) -> Any: ...
    def read(self, *args, **kwargs) -> Any: ...
    def write(self, *args, **kwargs) -> Any: ...
    def writeInventor(self, *args, **kwargs) -> Any: ...
    def __delattr__(self, name) -> Any: ...
    def __setattr__(self, name, value) -> Any: ...
