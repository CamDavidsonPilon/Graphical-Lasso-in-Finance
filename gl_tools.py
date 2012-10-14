import numpy as np
#from matplotlib import rc
import matplotlib.pyplot as plt
import networkx as nx
from graphical_lasso import graphical_lasso
from sklearn.covariance import GraphLasso

#rc('text', usetex=True)


def save_covariance_matrix_heatmap( matrix, axis_labels, title, filename ):
	""" (matrix, axis_labels, title, filename )"""
	
	if matrix.shape[1] != matrix.shape[0]:
		print "Needs to be a square matrix"
		return

	if matrix.shape[1] != len( axis_labels ):
		print "number of labels does not equal shape of matrix"
		return

	fig = plt.figure()
	ax = fig.subplot( 111)
	cax = ax.imshow( matrix, interpolation = 'none')
	ax.set_title( title)
	
	cbar = fig.colorbar( cax, ticks = [-1,0,1] )
	cbar.ax.set_yticklabels( ["-1", "0", "1" ] )
	
	ax.xticks( range(len(axis_labels) ), axis_labels, size="small" ) 
	ax.yticks( range(len(axis_labels) ), axis_labels, size="small" ) 
	
	plt.savefig( filename )
	return 

def save_network_graph( matrix, labels, title, filename ):
	D = nx.Graph( matrix )
	fig = plt.figure()
	ax = fig.add_subplot(111)
        labels = dict( zip( range(len(labels) ), labels) )
	pos_labels = nx.circular_layout(D)
	for k,i in pos_labels.iteritems():
		pos_labels[k] = i+0.05	
	nx.draw_circular( D, ax=ax, with_labels=False, font_size = 14 )
	nx.draw_networkx_labels(D, pos_labels,ax=ax, labels=  labels)
	ax.set_title(title)
	plt.savefig( filename )

	return

def save_network_graph_sequence( data, alpha_seq, labels, filename):
	if len(alpha_seq)%2 != 0:
		print "make alpha an even number please."
		return

	n = len(alpha_seq)
	labels = dict( zip( range( len(labels) ), labels) )
	fig = plt.figure()
	for i in range(n):
		ax = fig.add_subplot(n/2,2,i+1)
		gl = GraphLasso( alpha = alpha_seq[i] )
		
		gl.fit( data )
		D = nx.Graph( gl.precision_ )
		pos_labels = nx.circular_layout( D )
		for k,item in pos_labels.iteritems():
			pos_labels[k] = item + 0.1
		nx.draw_circular( D, scale = 4, node_size = 150, ax = ax, with_labels = True, labels = labels, font_size = 8)
		#nx.draw_networkx_labels(D, pos_labels, ax=ax, labels= labels, font_size = 12)
		ax.set_title( "alpha = %.2e"%alpha_seq[i])

	plt.savefig( filename )


def absolute_daily_returns( ts) :
    return (ts['Adj Close']/(ts['Adj Close'].shift(1) )-1)[1:]
	
	
