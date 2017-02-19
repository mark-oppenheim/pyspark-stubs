from typing import Any, Iterable, Optional, Tuple, TypeVar, Union
from pyspark.mllib.linalg import Vector
from numpy import ndarray  # type: ignore

VectorLike = Union[ndarray, Vector, List[float], Tuple[float, ...]]
