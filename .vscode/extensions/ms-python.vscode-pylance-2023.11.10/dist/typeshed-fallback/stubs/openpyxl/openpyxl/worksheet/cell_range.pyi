from _typeshed import Incomplete, Unused
from collections.abc import Generator
from typing import overload
from typing_extensions import Literal

from openpyxl.descriptors import Strict
from openpyxl.descriptors.base import MinMax, _ConvertibleToInt
from openpyxl.descriptors.serialisable import Serialisable

class CellRange(Serialisable):
    min_col: MinMax[int, Literal[False]]
    min_row: MinMax[int, Literal[False]]
    max_col: MinMax[int, Literal[False]]
    max_row: MinMax[int, Literal[False]]
    title: str | None

    @overload
    def __init__(
        self,
        range_string: str | None,
        min_col: Unused = None,
        min_row: Unused = None,
        max_col: Unused = None,
        max_row: Unused = None,
        title: str | None = None,
    ) -> None: ...
    @overload
    def __init__(
        self,
        range_string: None = None,
        *,
        min_col: _ConvertibleToInt,
        min_row: _ConvertibleToInt,
        max_col: _ConvertibleToInt,
        max_row: _ConvertibleToInt,
        title: str | None = None,
    ) -> None: ...
    @property
    def bounds(self): ...
    @property
    def coord(self): ...
    @property
    def rows(self) -> Generator[Incomplete, None, None]: ...
    @property
    def cols(self) -> Generator[Incomplete, None, None]: ...
    @property
    def cells(self): ...
    def __copy__(self): ...
    def shift(self, col_shift: int = 0, row_shift: int = 0) -> None: ...
    def __ne__(self, other): ...
    def __eq__(self, other): ...
    def issubset(self, other): ...
    __le__ = issubset
    def __lt__(self, other): ...
    def issuperset(self, other): ...
    __ge__ = issuperset
    def __contains__(self, coord): ...
    def __gt__(self, other): ...
    def isdisjoint(self, other): ...
    def intersection(self, other): ...
    __and__ = intersection
    def union(self, other): ...
    __or__ = union
    def __iter__(self): ...
    def expand(self, right: int = 0, down: int = 0, left: int = 0, up: int = 0) -> None: ...
    def shrink(self, right: int = 0, bottom: int = 0, left: int = 0, top: int = 0) -> None: ...
    @property
    def size(self): ...
    @property
    def top(self): ...
    @property
    def bottom(self): ...
    @property
    def left(self): ...
    @property
    def right(self): ...

class MultiCellRange(Strict):
    ranges: Incomplete
    def __init__(self, ranges=...) -> None: ...
    def __contains__(self, coord): ...
    def sorted(self) -> list[CellRange]: ...
    def add(self, coord) -> None: ...
    def __iadd__(self, coord): ...
    def __eq__(self, other): ...
    def __ne__(self, other): ...
    def __bool__(self) -> bool: ...
    def remove(self, coord) -> None: ...
    def __iter__(self): ...
    def __copy__(self): ...
