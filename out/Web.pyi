from typing import Any

def registerServerFirewall(*args, **kwargs) -> Any: ...
def startServer(address = ..., port = ...) -> Any: ...
def waitForConnection(address = ..., port = ..., timeout = ...) -> Any: ...
