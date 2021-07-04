import pytest
import numpy as np

X = np.random.rand(20, 2)
y = np.random.rand(20)

X_new = np.random.rand(40, 2)


def common(model):
    model.fit(X, y)
    y_new = model.predict(X_new)

    assert y_new.size == 40
    print(repr(model), 'Passed')


def test_basic():
    from polire import IDW, Spline, Trend, GP, Kriging, NaturalNeighbors, SpatialAverage, CustomInterpolator
    from sklearn.linear_model import LinearRegression

    common(IDW())
    common(Spline())
    common(Trend())
    common(GP())
    common(Kriging())
    common(NaturalNeighbors())
    common(SpatialAverage())
    common(CustomInterpolator(LinearRegression,
           reg_kwargs={"normalize": True}))
