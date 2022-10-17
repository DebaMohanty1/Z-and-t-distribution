# -*- coding: utf-8 -*-
"""
Created on Mon Oct 17 05:46:38 2022

@author: D
"""

import scipy.stats as stats

# The Z distribution is a special case of the normal distribution 
# with a mean of 0 and standard deviation of 1. 
# The t-distribution is similar to the Z-distribution, 
# but is sensitive to sample size and is used for small or moderate
#  samples when the population standard deviation is unknown.

# z-distribution
# cdf => cumulative distributive function; # similar to pnorm in R
# The syntax is scipy.stats.norm.CDF(data,loc,size,moments,scale)
# Where parameters are:
# data: It is a set of points or values that represent evenly 
# sampled data in the form of array data.
# loc: It is used to specify the mean, by default it is 0.
# moments: It is used to calculate statistics like standard deviation, kurtosis and mean.
# scale: It is used to specify the standard deviation, by default it is 1.
stats.norm.cdf(740, 711, 29)  # Given a value, find the probability

# ppf => Percent point function; # similar to qnorm in R
# Syntax: scipy.stats.norm.ppf(q,loc,scale)
# Where parameters are:
# q: It is used to specify the quantiles.
# loc: It is used to specify the mean, by default it is 0.
# scale: It is used to specify the standard deviation, by default it is 1.
stats.norm.ppf(0.975, 0, 1) # Given probability, find the Z value

# t-distribution
stats.t.cdf(1.98, 139) # Given a value, find the probability; # similar to pt in R
stats.t.ppf(0.975, 139) # Given probability, find the t value; # similar to qt in R