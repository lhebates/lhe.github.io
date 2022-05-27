---
title: Pystata Mac Example Notebook
layout: post
project: true
permalink: "/projects/:title/"
image: /assets/images/ds.jpg
source:
tags:
  - data-science
  - machine-learning
  - project
---

```python
# setup stata from python
import stata_setup
stata_setup.config('/Applications/Stata/', 'se')
```

    
      ___  ____  ____  ____  ____ ®
     /__    /   ____/   /   ____/      17.0
    ___/   /   /___/   /   /___/       SE—Standard Edition
    
     Statistics and Data Science       Copyright 1985-2021 StataCorp LLC
                                       StataCorp
                                       4905 Lakeway Drive
                                       College Station, Texas 77845 USA
                                       800-STATA-PC        https://www.stata.com
                                       979-696-4600        stata@stata.com
    
    Stata license: 50-student lab perpetual
    Serial number: 401706320249
      Licensed to: batesladmin
                   Bates College
    
    Notes:
          1. Unicode is supported; see help unicode_advice.
          2. Maximum number of variables is set to 5,000; see help set_maxvar.



```python
# load pystata (located in stata utility folder)
from pystata import stata
```


```python
# use stata cell magic, starting with %%stata
%%stata
sysuse auto, clear
```

    (1978 automobile data)



```python
# use stata line magic, starting with %%stata
%stata des
```

    
    Contains data from /Applications/Stata/ado/base/a/auto.dta
     Observations:            74                  1978 automobile data
        Variables:            12                  13 Apr 2020 17:45
                                                  (_dta has notes)
    -------------------------------------------------------------------------------
    Variable      Storage   Display    Value
        name         type    format    label      Variable label
    -------------------------------------------------------------------------------
    make            str18   %-18s                 Make and model
    price           int     %8.0gc                Price
    mpg             int     %8.0g                 Mileage (mpg)
    rep78           int     %8.0g                 Repair record 1978
    headroom        float   %6.1f                 Headroom (in.)
    trunk           int     %8.0g                 Trunk space (cu. ft.)
    weight          int     %8.0gc                Weight (lbs.)
    length          int     %8.0g                 Length (in.)
    turn            int     %8.0g                 Turn circle (ft.)
    displacement    int     %8.0g                 Displacement (cu. in.)
    gear_ratio      float   %6.2f                 Gear ratio
    foreign         byte    %8.0g      origin     Car origin
    -------------------------------------------------------------------------------
    Sorted by: foreign



```python
%stata scatter mpg price
```


![png](/assets/images/PyStata-mac-example-notebook_files/PyStata-mac-example-notebook_4_0.svg)



```python
%%stata
scatter mpg price, name(a, replace)
histogram rep78, name(b, replace)
```

    
    . scatter mpg price, name(a, replace)
    
    . histogram rep78, name(b, replace)
    (bin=8, start=1, width=.5)
    
    . 



![png](/assets/images/PyStata-mac-example-notebook_files/PyStata-mac-example-notebook_5_1.svg)



![png](/assets/images/PyStata-mac-example-notebook_files/PyStata-mac-example-notebook_5_2.svg)



```python

```
