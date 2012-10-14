Graphica-Lasso-in-Finance
=========================

Implementations of the graphical lasso method to estimation of covariance matrices in finance.


Background
----------

The graphical lasso method is used to find a sparse inverse covariance matrix. Why is this useful? The (i,j)th element of the inverse covariance matrix is known as the partial-correlation between variable i and variable j. The [partial autocorrelation](http://en.wikipedia.org/wiki/Partial_correlation) is the correlation of two data, controlling for every other variable. If the variables are Gaussian, and the partial-correlation is 0, then the variables are conditionally independent. 

This is a very intuitive property in finance. Think: if the price of sheep increases, should the price of MSFT really increase too, even if there covariance is positive? Probably not, but both might be linked through a series of ETFs like the DJ-UBS and the SP500. The covariance matrix is a victim of causality! Sheep prices and MSFT have positive covariance because they are both dependent on another set of indices, but have (close to) zero conditional correlation.


Theory
------

Based on the paper [Sparse inverse covariance estimation with the grapical lasso](http://www-stat.stanford.edu/~tibs/ftp/graph.pdf) by Freidman et el. (2007).    

