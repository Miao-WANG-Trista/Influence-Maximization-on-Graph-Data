
import numpy as np
import networkx as nx
from numpy.linalg import solve
from tqdm import tqdm


###############################################################################

class ViralRank:
    
    def __init__(self,graph):
        self.graph = graph
       
        
    def value(self, inversetemp = 1e-4):
        """
        Compute the ViralRank centrality index from:
        F. Iannelli, M.S. Mariani, I.M. Sokolov 
        "Influencers identification in complex networks through reaction-diffusion dynamics"
        (https://arxiv.org/abs/1803.01212)
        Viralrank is defined as (note that the minus sign implies negative scores): 
        v(lambda) = - \sum_j (D_{ij} + D_{ji})/N
        where D_{ij} is the random-walk effective distance [Iannelli at al. Phys. Rev. E 95, 012313 (2017)] 
        from i to j and lambda is a parameter that plays the role of the inverse temperature (see next), 
        while N is the number of nodes.
        
        Parameters
        --------
                
            inversetemp : float
                numerical parameter (lambda) necessary for the computation of ViralRank centrality
                for metapopulation models. It is defined as:
                    lambda = log[ (beta-mu)/alpha ] - gamma
                where beta, mu and alpha are the infection, recovery and  
                diffusion rates, respectively, while gamma is the Euler constant.
                For contact networks its value is set equal to (approximately) zero corresponding
                to a high temperature expansion, while it can be specifically tuned 
                for metapopulation networks uisng the above definition.
                  
                
        Returns:
        --------
        
            nodes' ViralRank score : ndarray
                
        """           
        
        assert nx.is_connected(self.graph), "The network has to be connected" 
        assert inversetemp > 0, "Negative temperature"
        A = np.asarray(nx.to_numpy_matrix(self.graph, dtype=float, weight=None).T)
        #print("The graph is directed:", nx.is_directed(g))
        #N = g.number_of_nodes()
        s = A.sum(1)
        P = (A.T/s).T
        #print("sum over columns of P", P.sum(1))  
        s = A.sum(1)
        #assert np.all(s) > 0, "The network has to be connected"
        P = (A.T/s).T        
        assert np.all(np.isclose(P.sum(axis=1), 1, rtol=1e-10)), "Non valid transition matrix" 
        
        
        self.nodes = self.graph.number_of_nodes()
        targets = range(self.nodes)
               
        I = np.eye( self.nodes-1,self.nodes-1 )
        Z = np.ones( (self.nodes, self.nodes) )
        D = np.zeros( (self.nodes, self.nodes) )
        for j in tqdm(targets): 
            Pm = np.delete(P,j,0) 
            Pm = np.delete(Pm,j,1) 
            pm = P[:,j]  
            pm = np.delete(pm,j) 
            z = np.linalg.solve((np.exp(inversetemp)*I-Pm), pm)
            Z[:,j] = np.insert(z,j,1)
            D[:,j] = -np.log(Z[:,j])
        
        v = -1./self.nodes * (D.sum(1)+D.sum(0)) 
        
        return v  
    
    def rank(self, inversetemp = 1e-4):
        
        values = self.value()
        return np.argsort(values)
        


###############################################################################
    
# if __name__ == "__main__":
#
#     # CHECK VERSIONS
#     vers_python0 = '2.7.13'
#     vers_numpy0  = '1.11.0'
#     vers_netx0   = '1.14.5'
#
#     from networkx import __version__ as vers_netx
#     vers_python = '%s.%s.%s' % version_info[:3]
#     vers_numpy  = np.__version__
#
#
#     print '\n---------'
#     print '---------'
#     print '---------'
#     print '---------'
#     print '---------'
#     print 'Required modules:'
#     print 'Python:   tested for: %s.  Yours: %s'    % (vers_python0, vers_python)
#     print 'numpy:    tested for: %s.  Yours: %s'    % (vers_numpy0, vers_numpy)
#     print 'networkx: tested for: %s.  Yours: %s'    % (vers_netx0, vers_netx)
#     print '--------'
#     print '--------'
#     print '--------'
#     print '--------\n'
    

