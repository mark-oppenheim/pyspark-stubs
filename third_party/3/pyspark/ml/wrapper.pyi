# Stubs for pyspark.ml.wrapper (Python 3)

import abc
from typing import Any, Generic, Optional, Type, TypeVar
from pyspark.ml._typing import P, T, JM

from pyspark.ml import Estimator, Model, Transformer
from pyspark.ml.param import Params
from pyspark.ml.param.shared import HasFeaturesCol, HasLabelCol, HasPredictionCol

xrange = range

class JavaWrapper:
    def __init__(self, java_obj: Optional[Any] = ...) -> None: ...
    def __del__(self) -> None: ...

class JavaParams(JavaWrapper, Params):
    __metaclass__: Type[abc.ABCMeta]
    def copy(self, extra: Optional[Any] = ...): ...

class JavaEstimator(JavaParams, Estimator[JM]):
    __metaclass__: Type[abc.ABCMeta]

class JavaTransformer(JavaParams, Transformer):
    __metaclass__: Type[abc.ABCMeta]

class JavaModel(JavaTransformer, Model):
    __metaclass__: Type[abc.ABCMeta] = ...
    def __init__(self, java_model: Optional[Any] = ...) -> None: ...

class JavaPredictorParams(HasLabelCol, HasFeaturesCol, HasPredictionCol): ...

class JavaPredictor(JavaEstimator[JM], JavaPredictorParams, metaclass=abc.ABCMeta):
    def setLabelCol(self: P, value: str) -> P: ...
    def setFeaturesCol(self: P, value: str) -> P: ...
    def setPredictionCol(self: P, value: str) -> P: ...

class JavaPredictionModel(Generic[T], JavaModel, JavaPredictorParams):
    def setFeaturesCol(self: P, value: str) -> P: ...
    def setPredictionCol(self: P, value: str) -> P: ...
    @property
    def numFeatures(self) -> int: ...
    def predict(self, value: T) -> float: ...
