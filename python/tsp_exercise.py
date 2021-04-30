# -*- coding: utf-8 -*-
"""
@author: Gualandi
"""
import numpy as np
from math import sqrt


from pyomo.environ import ConcreteModel, Var, Objective, Constraint, SolverFactory
from pyomo.environ import maximize, Binary, RangeSet, PositiveReals, ConstraintList

# Residenza Collegiali a Pavia
Rs = [(45.1882789,9.1600456, 'Del Maino'),(45.2070857,9.1382623, 'Green Campus'),
      (45.1961107,9.1395709, 'Golgi'),(45.1851618,9.1506323, 'Senatore'),
      (45.1806049,9.1691651, 'Don Bosco'),(45.1857651,9.1473637, 'CSA'),
      (45.1802511,9.1591663, 'Borromeo'),(45.1877192,9.1578934, 'Cairoli'),
      (45.1870975,9.1588276, 'Castiglioni'),(45.1871301,9.1435067, 'Santa Caterina'),
      (45.1863927,9.15947, 'Ghislieri'),(45.2007148,9.1325475, 'Nuovo'),
      (45.1787292,9.1635482, 'Cardano'),(45.1864928,9.1560687, 'Fraccaro'),
      (45.1989668,9.1775168, 'Griziotti'),(45.1838819,9.161318, 'Spallanzani'),
      (45.1823523,9.1454315, 'Valla'),(45.2007816,9.1341354, 'Volta'),
      (45.2070857,9.1382623, 'Residence Campus'),(45.2070857,9.1382623, 'Residenza Biomedica')]
 
# INSTANCES TAKE FROM THE TSPLIB:
#   http://elib.zib.de/pub/mp-testdata/tsp/tsplib/tsp/

ULYSSES = [(38.24, 20.42), (39.57, 26.15), (40.56, 25.32), (36.26, 23.12),
           (33.48, 10.54), (37.56, 12.19), (38.42, 13.11), (37.52, 20.44),
           (41.23, 9.10), (41.17, 13.05), (36.08, -5.21), (38.47, 15.13), 
           (38.15, 15.35), (37.51, 15.17), (35.49, 14.32), (39.36, 19.56)]
     
BAVIERA = [(1150.0,  1760.0), (630.0,  1660.0),  (40.0,  2090.0),    (750.0,  1100.0), 
  (1030.0,  2070.0), (1650.0,   650.0), (1490.0,  1630.0),  (790.0,  2260.0),
  (710.0,  1310.0),  (840.0,   550.0),  (1170.0,  2300.0),  (970.0,  1340.0),
  (510.0,   700.0),  (750.0,   900.0),  (1280.0,  1200.0),  (230.0,   590.0),
  (460.0,   860.0),  (1040.0,   950.0), (590.0,  1390.0),   (830.0,  1770.0),
  (490.0,   500.0),  (1840.0,  1240.0), (1260.0,  1500.0),  (1280.0,  790.0),
  (490.0,  2130.0),  (1460.0,  1420.0), (1260.0,  1910.0),  (360.0,  1980.0),
  (750.0,  2030.0)]   

    
# Mixed Integre Programming Formulation
def TSP(C):
    # Number of places
    n, n = C.shape
    
    # TODO: Implement the model of your choice
    m = ConcreteModel()
    
    # 1. Data and ranges
    # .....
    
    # 2. Variables
    # .....
    
    # 3. Objective function
    # .....
    
    # 4. Constraints
    # .....
    
    # 5. Solution
    # .....
    
    # Return the solution in the correct format
    return [(i, i+1) for i in range(n-1)]
    


def PlotTour(Ps, Ls):
    # Report solution value
    import pylab as pl
    from matplotlib import collections  as mc

    lines = [[Ps[i], Ps[j]] for i,j in Ls]

    lc = mc.LineCollection(lines, linewidths=2)
    fig, ax = pl.subplots()
    ax.add_collection(lc)
    ax.scatter([i for i,j in Ps[1:]], [j for i,j in Ps[1:]], 
                s=20, alpha=0.8, color='red')
    
    ax.autoscale()
    ax.margins(0.1)


def CostMatrix(Ls):
    n = len(Ls)
    C = 100000*np.ones((n,n))
    for i, (a,b) in enumerate(Ls):
        for j, (c,d) in enumerate(Ls[i+1:]):
            C[i, i+j+1] = sqrt((a-c)**2 + (b-d)**2)
            C[i+j+1, i] = C[i, i+j+1]
            
    return C
 
    
def RandomTSP(n):
    from numpy import random
    return [(x,y) for x,y in zip(random.random(n), random.random(n))]


# -----------------------------------------------
#   MAIN function
# -----------------------------------------------
if __name__ == "__main__":

    Test = 0
    
    # Compute Cost Matrix
    if Test == 0:
        Ls = [(b,a) for a,b,_ in Rs]
    if Test == 1:
        Ls = ULYSSES
    if Test == 2:
        Ls = BAVIERA
    if Test == 3:
        N = 100
        Ls = RandomTSP(N)
        
    # Compute cost matrix
    C = CostMatrix(Ls)
        
    # Solve problem
    tour = TSP(C)
    PlotTour(Ls, tour)
    