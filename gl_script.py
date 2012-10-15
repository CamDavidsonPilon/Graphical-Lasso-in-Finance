
import datetime
import numpy as np
from sklearn.covariance import GraphLasso
from pandas.io.data import DataReader
import matplotlib
matplotlib.use("Agg")
from sklearn.preprocessing import scale

import matplotlib.pyplot as plt
from gl_tools import *

from graphical_lasso import graphical_lasso

np.set_printoptions( precision = 5, suppress=True)


def get_data( symbols, start_date):
	data = {}
	new_symbols = []
	for sym in symbols:
		try:
			data[sym] = DataReader( sym, "yahoo", start = start_date)
			new_symbols.append( sym )
		except:
			pass
	return new_symbols,data

symbols =['MS','TOT','F', 'TM', 'MTU', 'TWX', 'CVX', 'MAR', '3M', 'HMC', 'PG', 'SNE', 'CAJ', 'VL0','BAC','K','PFE', 'XRX', 'AIG', 'PEP', 'KO', 'PG', 'MCD', 'WMT', 'JPM','C', 'WFC', 'GE', 'T', 'VZ', 'IBM', 'MSFT','GOOG', 'AAPL', 'RIMM']
start_data = datetime.datetime(2010, 01, 03)
symbols, data = get_data( symbols, start_data)
close_data = np.concatenate( [ absolute_daily_returns( data[ts] )[:,None] for ts in symbols ], axis=1 )
alpha = 0.38

gl = GraphLasso(alpha)
nclose_data = scale(close_data)
#save_network_graph( gl_pre, symbols, "Precision Matrix Network", "test.pdf" )
#print gl_cov
#print
#print gl_pre




