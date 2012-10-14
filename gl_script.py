
import datetime
import numpy as np
from pandas.io.data import DataReader
import matplotlib
matplotlib.use("Agg")


import matplotlib.pyplot as plt
from gl_tools import *

from graphical_lasso import graphical_lasso

np.set_printoptions( precision = 5, suppress=True)


symbols = ['AAC', 'AACC', 'AAON', 'ACAT', 'ABMD', 'MSFT','GOOG', 'AAPL', '^GSPC']
start_data = start=datetime.datetime(2009, 01, 03)
data = dict( (sym, DataReader(sym, "yahoo") ) for sym in symbols )
close_data = np.concatenate( [ absolute_daily_returns( data[ts] )[:,None] for ts in data.keys() ], axis=1 )

gl_cov, gl_pre = graphical_lasso( close_data, 0.00015 )
save_network_graph( gl_pre, data.keys(), "Test", "test.pdf" )
print gl_cov
print
print gl_pre




