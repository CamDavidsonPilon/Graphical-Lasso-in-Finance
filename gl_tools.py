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
	ax = plt.subplot( 111)
	cax = ax.imshow( matrix, interpolation = "nearest", vmax=1, vmin=0)
	ax.set_title( title)
	
	cbar = fig.colorbar( cax, ticks = [1,0] )
	cbar.ax.set_yticklabels( ["1", "0"] )
	
	plt.xticks( range(len(axis_labels) ), axis_labels, size="small", rotation = 90 ) 
	plt.yticks( range(len(axis_labels) ), axis_labels, size="small" ) 
	
	plt.savefig( filename )
	return 

def save_network_graph_old( matrix, labels, title, filename ):
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
		nx.draw_circular( D, scale = 4, node_size = 150, ax = ax, with_labels = True, labels = labels, font_size = 6 )
		#nx.draw_networkx_labels(D, pos_labels, ax=ax, labels= labels, font_size = 12)
		ax.set_title( r"$\alpha$ = %.2e"%alpha_seq[i])

	plt.savefig( filename )


def save_network_graph( matrix, labels, filename, title, scale=8, layout = "circular", weight = lambda x: abs(4*x)**(2.5) ):
	labels = dict( zip( range( len(labels) ), labels) )
	d = matrix.shape[0]
	D = nx.Graph(matrix)
	#D.add_nodes_from( range(d) )
	#for i in range(d):
	#	for j in range(i):
	#			if matrix[i,j] != 0:
	#				D.add_edge( i, j, weight = matrix[i,j])
	weights = [ D[x][y]['weight'] for x,y in D.edges() ] 
	#weights = weights/np.max( np.abs( weights ) ) 
	cmap = plt.get_cmap( "Reds" ) #or some other one
	
	fig = plt.figure(figsize=(50,50))
	ax = fig.add_subplot(111)
	if layout == "circular":
		pos = nx.circular_layout( D, scale =scale )
	elif layout == "spring":
		pos = nx.spring_layout( D ,scale = scale, iterations = 35 )
	#bweights = [ 1+100*(x-min(weights))/( max(weights)- min(weights) ) for x in weights ]
	bweights = [ 'k'*(z<0) + 'r'*(z>0) for z in weights ]
	width = [ weight(w) for w in weights]
	print bweights
	print width
	nx.draw_networkx_edges( D, pos, ax = ax,edge_vmin=-0.2, edge_vmax=4, edge_cmap=cmap, edge_color = width, width=width)
	nx.draw_networkx_nodes( D, pos, ax=ax, node_size = 0, node_color="red")
	nx.draw_networkx_labels( D, pos,font_size=15, labels = labels, ax = ax)
	plt.axis("off")
	plt.title(title)
	plt.savefig( filename, bbox_inches="tight")
	return
	
	
	
	
			
			
 



def absolute_daily_returns( ts) :
    return (ts['Close']/(ts['Close'].shift(1) )-1)[1:]
	
	
