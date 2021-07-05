![example workflow](https://github.com/patel-zeel/polire/actions/workflows/python-package.yml/badge.svg)


Polire
------

The word "interpolation" has Latin origin and is composed of two words - Inter meaning between and Polire meaning to polish.

This repository is a collection of several spatial interpolation algorithms. 

Examples
---
### Minimal example of interpolation
```python
import numpy as np
from polire import Kriging

# Data
X = np.random.rand(10, 2) # Spatial 2D points
y = np.random.rand(10) # Observations
X_new = np.random.rand(100, 2) # New spatial points

# Fit
model = Kriging()
model.fit(X, y)

# Predict
y_new = model.predict(X_new)
```

### Supported Interpolation Methods
```python
from polire import (
    Kriging, # Best spatial unbiased predictor
    GP, # Gaussian process interpolator from GPy
    IDW, # Inverse distance weighting
    SpatialAverage,
    Spline,
    Trend,
    Random, # Predict uniformly within the observation range, a reasonable baseline
    NaturalNeighbors,
    CustomInterpolator # Supports any regressor from Scikit-learn
)
```

### Use GP kernels from GPy and regressors from sklearn
```python
from sklearn.linear_model import LinearRegression # or any Scikit-learn regressor
from GPy.kern import Matern32 # or any other GPy kernel

from polire import GP, CustomInterpolator

# GP model
model = GP(Matern32(input_dim=2))

# Sklearn model
model = CustomInterpolator(LinearRegression(normalize = True))
```

More info
---

Contributors:  [S Deepak Narayanan](https://github.com/sdeepaknarayanan), [Zeel B Patel](https://github.com/patel-zeel), [Apoorv Agnihotri](https://github.com/apoorvagnihotri), and [Nipun Batra](https://github.com/nipunbatra).

This project is a part of Sustainability Lab at IIT Gandhinagar.

Acknowledgement to sklearn template for helping to package into a PiPy package.

Citation
---
Please cite us if you are using our work:

```bibtex
@inproceedings{10.1145/3384419.3430407,
author = {Narayanan, S Deepak and Patel, Zeel B and Agnihotri, Apoorv and Batra, Nipun},
title = {A Toolkit for Spatial Interpolation and Sensor Placement: Poster Abstract},
year = {2020},
isbn = {9781450375900},
publisher = {Association for Computing Machinery},
address = {New York, NY, USA},
url = {https://doi.org/10.1145/3384419.3430407},
doi = {10.1145/3384419.3430407},
abstract = {Sensing is central to the SenSys and related communities. However, fine-grained spatial sensing remains a challenge despite recent advancements, owing to cost, maintenance, among other factors. Thus, estimating the sensed phenomenon at unmonitored locations and strategically installing sensors is of prime importance. In this work, we introduce Polire - an open-source tool that provides a suite of algorithms for spatial interpolation and near-field passive sensor placements. We replicate two existing papers on these two tasks to show the efficacy of Polire. We believe that Polire is an essential step towards lowering entry barriers towards sensing and scientific reproducibility.},
booktitle = {Proceedings of the 18th Conference on Embedded Networked Sensor Systems},
pages = {653–654},
numpages = {2},
location = {Virtual Event, Japan},
series = {SenSys '20}
}
```
