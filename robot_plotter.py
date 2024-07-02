import numpy as np
import matplotlib.pyplot as plt
from svgpath2mpl import parse_path

smiley = parse_path("""m 739.01202,391.98936 c 13,26 13,57 9,85 -6,27 -18,52 -35,68 -21,20 -50,23 -77,18 -15,-4 -28,-12 -39,-23 -18,-17 -30,-40 -36,-67 -4,-20 -4,-41 0,-60 l 6,-21 z m -302,-1 c 2,3 6,20 7,29 5,28 1,57 -11,83 -15,30 -41,52 -72,60 -29,7 -57,0 -82,-15 -26,-17 -45,-49 -50,-82 -2,-12 -2,-33 0,-45 1,-10 5,-26 8,-30 z M 487.15488,66.132209 c 121,21 194,115.000001 212,233.000001 l 0,8 25,1 1,18 -481,0 c -6,-13 -10,-27 -13,-41 -13,-94 38,-146 114,-193.000001 45,-23 93,-29 142,-26 z m -47,18 c -52,6 -98,28.000001 -138,62.000001 -28,25 -46,56 -51,87 -4,20 -1,57 5,70 l 423,1 c 2,-56 -39,-118 -74,-157 -31,-34 -72,-54.000001 -116,-63.000001 -11,-2 -38,-2 -49,0 z m 138,324.000001 c -5,6 -6,40 -2,58 3,16 4,16 10,10 14,-14 38,-14 52,0 15,18 12,41 -6,55 -3,3 -5,5 -5,6 1,4 22,8 34,7 42,-4 57.6,-40 66.2,-77 3,-17 1,-53 -4,-59 l -145.2,0 z m -331,-1 c -4,5 -5,34 -4,50 2,14 6,24 8,24 1,0 3,-2 6,-5 17,-17 47,-13 58,9 7,16 4,31 -8,43 -4,4 -7,8 -7,9 0,0 4,2 8,3 51,17 105,-20 115,-80 3,-15 0,-43 -3,-53 z m 61,-266 c 0,0 46,-40 105,-53.000001 66,-15 114,7 114,7 0,0 -14,76.000001 -93,95.000001 -76,18 -126,-49 -126,-49 z""")
smiley.vertices -= smiley.vertices.mean(axis=0)

def plot_robot(policy, upMDP):
    ind = 0
    for j in range(10):
        MDP = upMDP.sample_MDP()
        state = upMDP.Init_state
        traj = [state]
        end_states = set(MDP.Labelled_states[1]+MDP.Labelled_states[2]+MDP.Labelled_states[3])
        for i in range(100):
            act_dist = policy[state]
            act = np.random.choice(range(len(MDP.Enabled_actions[state])), p=act_dist[MDP.Enabled_actions[state]])
            transitions = MDP.Transition_probs[state][act]
            transition_ids = MDP.trans_ids[state][act]
            next_state = np.random.choice(transition_ids, p=transitions)
            traj.append(next_state)
            state = next_state
            if state in end_states:
                break
        for i, s in enumerate(traj):
            n=3
            if s < n**4:
                robot = s//n**2
                jan = s-robot*n**2
            else:
                robot = (s-n**4)//n**2
                jan = (s-n**4)-robot*n**2
            r_pos = (robot-n*(robot//n), robot//n)
            j_pos = (jan-n*(jan//n), jan//n)

            ax = plt.subplot()
            #print(r_pos)
            ax.plot([r_pos[0]],[r_pos[1]], ms=24, marker=r'$\bigotimes$', color="blue")
            

            ax.plot([j_pos[0]],[j_pos[1]], marker=smiley, ms=24, color="red")
            ax.plot([2],[2], marker=r'$\star$', color="green", ms=24)
            ax.set_xlim((-0.5,2.5))
            ax.set_ylim((-0.5,2.5))
            plt.savefig("robot_plots/{0:0=3d}.png".format(ind+i))
            plt.clf()
            #ax.clear()
            #plt.close()
        ind += i
        print(ind)
