# Stubs for pyspark.ml.image (Python 3.6)
#

from typing import Any, Dict, List

from pyspark.sql.dataframe import DataFrame
from pyspark.sql.types import Row, StructType

from numpy import ndarray  # type: ignore

class _ImageSchema:
    def __init__(self) -> None: ...
    @property
    def imageSchema(self) -> StructType: ...
    @property
    def ocvTypes(self) -> Dict[str, int]: ...
    @property
    def imageFields(self) -> List[str]: ...
    @property
    def undefinedImageType(self) -> str: ...
    def toNDArray(self, image: Row) -> ndarray: ...
    def toImage(self, array: ndarray, origin: str = ...) -> Row: ...
    def readImages(self, path: str, recursive: bool = ..., numPartitions: int = ..., dropImageFailures: bool = ..., sampleRatio: float = ..., seed: int = ...) -> DataFrame: ...

ImageSchema: _ImageSchema
