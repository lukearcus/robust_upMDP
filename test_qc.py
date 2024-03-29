from UI.get_args import run as get_args
from main.sampler import get_samples
import Markov.writer as writer
import Markov.models
from tqdm import tqdm
import numpy as np
from scipy.special import softmax

k = 100
k_inn = 10

softmax_mix = True

args = get_args()
model = args["model"]
sample = Markov.models.MDP(model.sample_MDP())
num_states = len(model.States)
num_acts = len(model.Actions)
q_convex = True
q_concave = True
for j in tqdm(range(k)):
    params_1 = np.ones((num_states, num_acts))*-np.infty
    params_2 = np.ones((num_states, num_acts))*-np.infty
    pol_1 = np.zeros((num_states, num_acts))
    pol_2 = np.zeros((num_states, num_acts))
    for s in model.States:
        for a in model.Enabled_actions[s]:
            params_1[s,a] = np.random.random()#1/len(model.Enabled_actions[s])
            params_2[s,a] = np.random.random()#1/len(model.Enabled_actions[s])
        pol_1[s,:] = softmax(params_1[s,:])
        pol_2[s,:] = softmax(params_2[s,:])
        #pol_1[s,:] /= np.sum(pol_1[s,:])
        #pol_2[s,:] /= np.sum(pol_2[s,:])

    sample_1 = sample.fix_pol(pol_1)
    sample_2 = sample.fix_pol(pol_2)
    
    IO = writer.stormpy_io(sample_1)
    IO.write()
    res_1, _, _ = IO.solve()
    
    IO = writer.stormpy_io(sample_2)
    IO.write()
    res_2, _, _ = IO.solve()
    
    min_res = min(res_1,res_2)
    max_res = max(res_1,res_2)
    for i in range(k_inn):
        mixer = np.random.random()
        mix_pol = mixer*pol_1+(1-mixer)*pol_2
        if softmax_mix:
            mix_params = mixer*params_1+(1-mixer)*params_2
            mix_pol = softmax(mix_params, axis=1)

        mix_sample = sample.fix_pol(mix_pol)
        IO = writer.stormpy_io(mix_sample)
        IO.write()
        mix_res, _, _ = IO.solve()
        
        if mix_res < min_res:
            q_concave = False
        
        if mix_res > max_res:
            q_convex = False
    if model.opt == "min":
        if not q_convex:
            break
    else:
        if not q_concave:
            break
    if (not q_concave) and (not q_convex):
        break

if q_concave and q_convex:
    print("Found no counterexamples")

if not q_convex:
    print("Found a counterexample disproving quasiconvexity")

if not q_concave:
    print("Found a counterexample disproving quasiconcavity")

