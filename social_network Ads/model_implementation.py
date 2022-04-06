# -*- coding: utf-8 -*-
"""
Created on Thu Mar 31 13:51:42 2022

@author: uarvi
"""

import pickle

import numpy as np 

local_classifier = pickle.load(open('classifier.pickle', 'rb'))

local_scaler = pickle.load(open('sc.pickle', 'rb'))

local_classifier = pickle.load(open('classifier.pickle', 'rb'))

new_pred = local_classifier.predict_proba(local_scaler.transform(np.array([[20,40000]])))[:, -1]

