import numpy as np
class Perceptron(object):
    """Perceptron Klassifizierer
    
    Parameter
    ---------
    eta : float
        Lernrate zwischen 0.0 und 1.0
        
    n_iter : int
        Anzahl der Fehlerklassifizierungen pro Epoche
    
    Attribute
    ---------
    w_ : ld-array
        Gewichtungen nach Anpassung
        
    errors_ : list
        Anzahl der Fehlerklassifizierungen pro Epoche
        
    """
    
    def __init__(self, eta=0.01, n_iter=10):
        self.eta = eta
        serf.n_iter = n_iter
    
    def fit(self, X, y)
    """ Anpassen an die Trainingsdaten
    
        Parameter
        ---------
        X : {array-like}, shape = [n_samples, n_features]
            Trainingsvektoren, n_samples is
            die Anzahl der Objekte und
            n_features ist die Anzahl der Merkmale
            
        y : array-like, shape = [n_samples]
        
        Rückgabewert
        ------------
        self : Object
        
        """
    
    
    
    return self
    
    def net_input(self, X) :
        """ Nettoeingabe berechnen
        return np.dot(X, self.w_[1:] + self.w[0]
