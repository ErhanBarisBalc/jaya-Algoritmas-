#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 12 13:07:56 2022

@author: barisbalci
"""

import math
from random import random 

for dongu in range(0,durma_kriteri):
    for j in range(0,pn):
        
#Başlangıç çözüm matrisinde amaç fonksiyonun minimum yapan (en iyi) çözüm ve bu çözüme ait tasarım değiişkenlerinin elde edilmesi

    i_deger=min(OPT[AF][:])
    i_sira=np.argmin(OPT[AF])
    
    X1geniyi=OPT[0][i_sira]
    X2geniyi=OPT[1][İ_sira]
    ....
    
#Başlangıç çözüm matrisinde amaç fonksiyonunu mamksimumu yapan (en kötü) çözüm ve bu çözüme ait tasarım değişkenlerinin elde edilmesi 

    k_deger=max(OPT[AF][:])
    k_sira=np.argmin(OPT[AF][:])
    
    X1genkotu=OPT[0][k_sira]
    X2genkotu=OPT[1][k_sira]
    .....
    
         X1new=OPT[0][j]+random()*(X1geniyi-abs(OPT[0][j]))-random()*
(X1genkotu-abs(OPT[0][j]))
         X2new=OPT[1][j]+random()*(X1geniyi-abs(OPT[1][j]))-random()*
(X1genkotu-abs(OPT[1][j]))
    
deger=min(OPT[AF][:])
sira=np.argmin(OPT[AF])
