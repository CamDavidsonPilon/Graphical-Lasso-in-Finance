
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
			print sym, data[sym].shape
		except:
			print "Error %s"%sym
	return new_symbols,data

symbols =['ACE', 'ANF', 'ADBE','ALXN','ALL','AMZN','AXP','BBY','BA','COG', 'CPB','CAT', 'CHK','CSC', 'COST', 'DVN','DOW','DD', 'ETFC', 'EA', 'ESRX', 'XOM','FDX', 'GPS', 'GIS', 'GS', 'HAL','HPQ', 'HD', 'JNJ','JOY', 'LMT', 'MRK', 'TAP', 'NKE','NE','RHT', 'SPLS', 'TEL', 'TE', 'V',  'MS','TOT','F', 'TM', 'MTU', 'TWX', 'CVX', 'MAR', 'MMM', 'HMC', 'SNE', 'CAJ', 'VLO','BAC','K','PFE', 'XRX', 'AIG', 'PEP', 'KO', 'PG', 'MCD', 'WMT', 'JPM','C', 'WFC', 'GE', 'T', 'VZ', 'IBM', 'MSFT','GOOG', 'AAPL', 'RIMM', "^DJA", "CSCO", "YHOO","ORCL","SNDK","DELL", "NVDA", "EBAY", "WIN", "WFM", "WHR", "WU", "WAG", "VMC", "UTX", "UNP", "USB", "TSN","TMO","TXT", "TXN", "TSO", "SYY","SBUX", "SWK", "LUV", "CMCSA", "AMD", "S", "INTC", "VXX", "^GSPC" ]


start_data = datetime.datetime(2010, 01, 03)
symbols, data = get_data( symbols, start_data)
close_data = np.concatenate( [ absolute_daily_returns( data[ts] )[:,None] for ts in symbols ], axis=1 )
alpha = 0.47
print "alpha: ", alpha


gl = GraphLasso(alpha)
nclose_data = scale(close_data)
gl.fit( nclose_data)

#remove the SP500
cov_sp = gl.covariance_[:, :-1].T[:,:-1]
prec_sp = gl.precision_[:, :-1].T[:,:-1]


def community_cluster(cov_sp, symbols):
	G = nx.Graph( cov_sp )
	partition = community.best_partition( G )
	for i in set(partition.values() ):
		print "Community: ",i
		members = [ symbols[node] for node  in partition.keys() if partition[node] == i]
		print members


def affinity_cluster( cov_sp, symbols):
	print "Affinity cluster"
	ap = AffinityPropagation()
	ap.fit( cov_sp )
	labels = np.array(  ap.labels_ )
	for i in set(ap.labels_):
		print "Community: ",i
		members = [ symbols[node] for node in np.nonzero( labels == i)[0]]
		print members 


#save_network_graph( -prec_sp + np.diag( np.diagonal( prec_sp) ), symbols[:-1], "LargeNetworkNo_SP.png", layout="spring", scale= 10, weight = lambda x: abs(5*x)**(2.5) )


#save_network_graph( gl.covariance_, symbols, "diagram.pdf", scale = 8, layout = "spring" )
#save_network_graph( gl_pre, symbols, "Precision Matrix Network", "test.pdf" )
#print gl_cov
#print
#print gl_pre






