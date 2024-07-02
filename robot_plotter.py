import numpy as np
import matplotlib.pyplot as plt

def plot_robot(policy, upMDP):
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
        print(r_pos)
        ax.plot([r_pos[0]],[r_pos[1]], 'o')
        ax.plot([j_pos[0]],[j_pos[1]], 'x')
        ax.set_xlim((-0.5,2.5))
        ax.set_ylim((-0.5,2.5))
        plt.savefig("robot_plots/{0:0=2d}.png".format(i))
        plt.clf()
        #ax.clear()
        #plt.close()
