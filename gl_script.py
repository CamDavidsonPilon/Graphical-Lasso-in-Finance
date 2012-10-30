
import datetime
import numpy as np
from sklearn.covariance import GraphLasso
from pandas.io.data import DataReader
import matplotlib
matplotlib.use("Agg")
from sklearn.preprocessing import scale
import community
import matplotlib.pyplot as plt
from gl_tools import *
import networkx as nx
from graphical_lasso import graphical_lasso
from sklearn.cluster import AffinityPropagation
np.set_printoptions( precision = 5, suppress=True)


def get_data( symbols, start_date):
	data = {}
	new_symbols = []
	for sym in symbols:
		try:
			data[sym] = DataReader( sym, "yahoo", start = start_date)
			new_symbols.append( sym )
			print data[sym].shape
		except:
			print "Error %s"%sym
	return new_symbols,data

symbols =['ACE', 'ANF', 'ADBE','ALXN','ALL','AMZN','AXP','BBY','BA','COG', 'CPB','CAT', 'CHK', 'KO','CSC', 'COST', 'DVN','DOW','DD', 'ETFC', 'EA', 'ESRX', 'XOM','FDX', 'GPS', 'GE', 'GIS', 'GS', 'HAL','HPQ', 'HD', 'JNJ','JOY', 'LMT', 'MRK', 'TAP', 'NKE','NE','PG','RHT', 'SPLS', 'TEL', 'TE', 'V',  'MS','TOT','F', 'TM', 'MTU', 'TWX', 'CVX', 'MAR', 'MMM', 'HMC', 'SNE', 'CAJ', 'VL0','BAC','K','PFE', 'XRX', 'AIG', 'PEP', 'KO', 'PG', 'MCD', 'WMT', 'JPM','C', 'WFC', 'GE', 'T', 'VZ', 'IBM', 'MSFT','GOOG', 'AAPL', 'RIMM', "^GSPC", "^DJA", "CSCO", "YHOO","ORCL","SNDK","DELL", "NVDA", "EBAY", "CSMCSA", "AMD", "S", "INTC", "VXX" ]
symbols = set(symbols)

start_data = datetime.datetime(2010, 01, 03)
symbols, data = get_data( symbols, start_data)
close_data = np.concatenate( [ absolute_daily_returns( data[ts] )[:,None] for ts in symbols ], axis=1 )
alpha = 0.52
print "alpha: ", alpha



gl = GraphLasso(alpha)
nclose_data = scale(close_data)
gl.fit( nclose_data)
G = nx.Graph( gl.covariance_ )
partition = community.best_partition( G )
for i in set(partition.values() ):
	print "Community: ",i
	members = [ symbols[node] for node  in partition.keys() if parition[node] == i]
	print members


print
print "Affinity cluster"
ap = AffinityPropagation()
ap.fit( gl.covariance_)
labels = np.array(  ap.labels_ )
for i in set(ap.labels_):
	print "Community: ",i
	members = [ symbols[node] for node in np.nonzero( labels == i )]
	print members 

save_network_graph( -gl.precision_ + np.diag( np.diagonal( gl.precision_) ), symbols, "LargeNetwork.png", layout="spring", scale= 1)


#save_network_graph( gl.covariance_, symbols, "diagram.pdf", scale = 8, layout = "spring" )
#save_network_graph( gl_pre, symbols, "Precision Matrix Network", "test.pdf" )
#print gl_cov
#print
#print gl_pre






