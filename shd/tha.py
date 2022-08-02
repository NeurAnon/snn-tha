# exp relaxation implementation of THA based on Eq (4)

def thr_annealing(config, network):
    alpha_thr1 = config['alpha_thr1']
    thr_final1 = config['thr_final1']

    alpha_thr2 = config['alpha_thr2']
    thr_final2 = config['thr_final2']

    network.lif1.threshold += (thr_final1 - network.lif1.threshold) * alpha_thr1
    network.lif2.threshold += (thr_final2 - network.lif2.threshold) * alpha_thr2

    return