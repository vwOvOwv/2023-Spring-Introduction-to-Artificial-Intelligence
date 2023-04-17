'''
对神经网络进行反向传播
'''
import numpy as np
from numpy.random import randn
from autograd.utils import parse
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("filename")
parser.add_argument("--debug", action="store_true")
args = parser.parse_args()


debug = args.debug

filename = args.filename
varnames, graph, nodes, expressions = parse(filename)
rootname = varnames[-1]
X = np.random.randn(100, 10)
value = graph.forward(X, debug)[-1]
graph.eval()
graph.flush()
value = graph.forward(X, debug)[-1]
xgrad = graph.backward(debug=debug)

params = graph.parameters()
grads = graph.grads()


print("numerical grad, backward grad")
t = 1e-7

graph.flush()
dx = randn(*X.shape)
X += t*dx
newvalue = graph.forward(X)[-1]
print((newvalue - value) / t, np.sum(np.multiply(dx, xgrad)))
X -= t * dx

for i, param in enumerate(params):
    graph.flush()
    dx = randn(*grads[i].shape)
    param += t * dx
    newvalue = graph.forward(X)[-1]
    print((newvalue - value) / t, np.sum(np.multiply(dx, grads[i])))
    param -= t * dx