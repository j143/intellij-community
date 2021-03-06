# Stubs for concurrent.futures (Python 2)

from typing import TypeVar, Generic, Any, Iterable, Iterator, Callable, Optional, Set, Tuple, Union
from types import TracebackType

_T = TypeVar('_T')

class Error(Exception): ...
class CancelledError(Error): ...
class TimeoutError(Error): ...

class Future(Generic[_T]):
    def cancel(self) -> bool: ...
    def cancelled(self) -> bool: ...
    def running(self) -> bool: ...
    def done(self) -> bool: ...
    def result(self, timeout: Optional[float] = ...) -> _T: ...
    def exception(self, timeout: Optional[float] = ...) -> Any: ...
    def exception_info(self, timeout: Optional[float] = ...) -> Tuple[Any, Optional[TracebackType]]: ...
    def add_done_callback(self, fn: Callable[[Future], Any]) -> None: ...

    def set_running_or_notify_cancel(self) -> bool: ...
    def set_result(self, result: _T) -> None: ...
    def set_exception(self, exception: Any) -> None: ...
    def set_exception_info(self, exception: Any, traceback: TracebackType) -> None: ...

class Executor:
    def submit(self, fn: Callable[..., _T], *args: Any, **kwargs: Any) -> Future[_T]: ...
    def map(self, func: Callable[..., _T], *iterables: Iterable[Any], timeout: Optional[float] = ...) -> Iterator[_T]: ...
    def shutdown(self, wait: bool = ...) -> None: ...
    def __enter__(self) -> Executor: ...
    def __exit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> bool: ...

class ThreadPoolExecutor(Executor):
    def __init__(self, max_workers: Optional[int] = ...) -> None: ...

class ProcessPoolExecutor(Executor):
    def __init__(self, max_workers: Optional[int] = ...) -> None: ...

def wait(fs: Iterable[Future], timeout: Optional[float] = ..., return_when: str = ...) -> Tuple[Set[Future], Set[Future]]: ...

FIRST_COMPLETED = ...  # type: str
FIRST_EXCEPTION = ...  # type: str
ALL_COMPLETED = ...  # type: str

def as_completed(fs: Iterable[Future], timeout: Optional[float] = ...) -> Iterator[Future]: ...
