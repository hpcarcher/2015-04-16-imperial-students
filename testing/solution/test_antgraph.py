from antgraph import AntGraph
from nose.tools import assert_equals 
import numpy as np


def test_ones_distance_etha():
    distances  = [[1 for x in range(3)] for y in range(3)]
    graph = AntGraph(3, distances)
    assert_equals(graph.etha(0,1), 1)


def test_general_distance_etha():
    distances  = [[6, 5, 4],[5, 0, 2],[4, 2, 0]]
    graph = AntGraph(3, distances) 
    np.testing.assert_allclose(0.2, graph.etha(0,1), rtol=0.0, atol=0.01)



