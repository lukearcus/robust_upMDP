import numpy as np

def fixed(val):
    def func(_):
        return val
    return func

def linear_multi(ind):
    def linear_fun(params):
        return min(max(params[ind],0),1)
    def one_minus_linear_fun(param):
        return min(max(1-param[ind],0),1)
    return linear_fun, one_minus_linear_fun

def softmax_multi(ind):
    def softmax(params):
        return float((np.exp(params)/sum(np.exp(params)))[ind])
    return softmax

def softmax_filler(inds):
    def softmax(params):
        return float(sum((np.exp(params)/sum(np.exp(params)))[inds]))
    return softmax

def linear(param):
    return min(max(param,0),1)

def one_minus_linear(param):
    return min(max(1-param,0),1)
