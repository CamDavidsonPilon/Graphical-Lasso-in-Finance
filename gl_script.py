
import datetime
import numpy as np
from sklearn.covariance import GraphLasso
from pandas.io.data import DataReader
import matplotlib
matplotlib.use("Agg")


import matplotlib.pyplot as plt
from gl_tools import *

from graphical_lasso import graphical_lasso

np.set_printoptions( precision = 5, suppress=True)


symbols =['MS','BAC','K','PEP', 'KO', 'PG', 'MCD', 'WMT', 'JPM','C', 'WFC', 'GE', 'T', 'VZ', 'MSFT','GOOG', 'AAPL', 'RIMM']
start_data = start=datetime.datetime(2009, 01, 03)
data = dict( (sym, DataReader(sym, "yahoo", start = start_data) ) for sym in symbols )
close_data = np.concatenate( [ absolute_daily_returns( data[ts] )[:,None] for ts in symbols ], axis=1 )
alpha = 0.00015

gl = GraphLasso( alpha = alpha )

gl.fit( close_data )

#save_network_graph( gl_pre, symbols, "Precision Matrix Network", "test.pdf" )
#print gl_cov
#print
#print gl_pre




