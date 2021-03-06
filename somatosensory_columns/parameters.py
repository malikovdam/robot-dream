import nest
import numpy.random as random
from property import *

# E_L
L2_EL_mu = -79.3
L2_EL_sigma = 4.27 / 4

L3_EL_mu = -79.3
L3_EL_sigma = 4.27 / 4

L4_EL_mu = -71.8
L4_EL_sigma = 4.20 / 4

L5A_EL_mu = -69.9
L5A_EL_sigma = 4.18 / 4

L5B_EL_mu = -68.5
L5B_EL_sigma = 3.98 / 4

L6_EL_mu = -69.9
L6_EL_sigma = 4.18 / 4

# V_th
L2_Vth_mu = -49.5
L2_Vth_sigma = 3.81 / 4

L3_Vth_mu = -49.5
L3_Vth_sigma = 3.81 / 4

L4_Vth_mu = -48.7
L4_Vth_sigma = 3.53 / 4

L5A_Vth_mu = -49.7
L5A_Vth_sigma = 3.56 / 4

L5B_Vth_mu = -52.7
L5B_Vth_sigma = 3.59 / 4

L6_Vth_mu = -49.7
L6_Vth_sigma = 3.56 / 4

# C_m
L2_Cm_mu = 134.
L2_Cm_sigma = 32.8 / 4

L3_Cm_mu = 134.
L3_Cm_sigma = 32.8 / 4

L4_Cm_mu = 135.
L4_Cm_sigma = 36.7 / 4

L5A_Cm_mu = 133.
L5A_Cm_sigma = 31.9 / 4

L5B_Cm_mu = 284.
L5B_Cm_sigma = 78.5 / 4

L6_Cm_mu = 133.
L6_Cm_sigma = 31.9 / 4

# t_ref
L2_tref_mu = 1.3
L2_tref_sigma = 0.9 / 4

L3_tref_mu = 1.3
L3_tref_sigma = 0.9 / 4

L4_tref_mu = 1.8
L4_tref_sigma = 1.1 / 4

L5A_tref_mu = 2.7
L5A_tref_sigma = 1.7 / 4

L5B_tref_mu = 4.4
L5B_tref_sigma = 2.0 / 4

L6_tref_mu = 2.7
L6_tref_sigma = 1.7 / 4

# Connection probability
L2_to_L2    = 0.093
L2_to_L3    = 0.121
L2_to_L4    = 0.120
L2_to_L5A   = 0.043
L2_to_L5B   = 0.009

L3_to_L2    = 0.055
L3_to_L3    = 0.187
L3_to_L4    = 0.145
L3_to_L5A   = 0.022
L3_to_L5B   = 0.018

L4_to_L2    = 0.009
L4_to_L3    = 0.024
L4_to_L4    = 0.243
L4_to_L5A   = 0.007
L4_to_L5B   = 0.007

L5A_to_L2   = 0.095
L5A_to_L3   = 0.057
L5A_to_L4   = 0.116
L5A_to_L5A  = 0.191
L5A_to_L5B  = 0.017
L5A_to_L6   = 0.006

L5B_to_L2   = 0.083
L5B_to_L3   = 0.122
L5B_to_L4   = 0.081
L5B_to_L5A  = 0.080
L5B_to_L5B  = 0.072
L5B_to_L6   = 0.020

L6_to_L4    = 0.032
L6_to_L5A   = 0.032
L6_to_L5B   = 0.070
L6_to_L6    = 0.028

# Neuron parameters
"""
    [iaf_psc_exp]

    Parameter        Standard   Measure Description
    V_reset             -70.0   [mV]    Reset membrane potential after a spike
    V_th                -55.0   [mV]    Spike threshold
    tau_minus           20.0    [ms]
    tau_m               10.0    [ms]    Membrane time constant
    I_e                 0.0     [pA]    Constant input current
    V_m                 -70.0   [mV]    Membrane potential
    E_L                 -70.0   [mV]    Resting membrane potential
    tau_syn_ex          2.0     [ms]    Time constant of postsynaptic excitatory currents
    tau_minus_triplet   110.0   [  ]
    beta_Ca             0.001   [  ]
    t_ref               2.0     [ms]    Duration of refractory period (V_m = V_reset)
    Ca                  0.0     [  ]
    C_m                 250.0   [pF]    Capacity of the membrane
    tau_syn_in          2.0     [ms]    Time constant of postsynaptic inhibitory currents
    tau_Ca              10000.0 [  ]

    recordables:        input_currents_ex
    			        input_currents_in
    			        V_m
    			        weighted_spikes_ex
    			        weighted_spikes_in
"""

neuron_parameters = {   #'E_L': -70.,
                        #'V_th': -50.,
                        'V_reset': -67.,
                        #'C_m': 250.,
                        #'t_ref': 2.,
                        'V_m': -60.,
                        #'tau_syn_ex': 5.,
                        #'tau_syn_in': 5.
                        'tau_m': 5.
}

# L2P     L2 pyramidal cell
# L3P     L3 pyramidal cell
# L4SN    L4 spiny neuron -> pyramidal
# stL5P   slender-tufted L5A pyramidal cell
# ttL5BP  thick-tufted L5B pyramidal cell
# ctL6AP  corticothalamic L6A pyramidal cell
L2_param = dict(dict(E_L=L2_EL_mu,
                     V_th=L2_Vth_mu,
                     C_m=L2_Cm_mu,
                     t_ref=L2_tref_mu, **neuron_parameters))
L3_param = dict(dict(E_L=L3_EL_mu,
                     V_th=L3_Vth_mu,
                     C_m=L3_Cm_mu,
                     t_ref=L3_tref_mu, **neuron_parameters))
L4_param = dict(dict(E_L=L4_EL_mu,
                     V_th=L4_Vth_mu,
                     C_m=L4_Cm_mu,
                     t_ref=L4_tref_mu, **neuron_parameters))
L5A_param = dict(dict(E_L=L5A_EL_mu,
                     V_th=L5A_Vth_mu,
                     C_m=L5A_Cm_mu,
                     t_ref=L5A_tref_mu, **neuron_parameters))
L5B_param = dict(dict(E_L=L5B_EL_mu,
                     V_th=L5B_Vth_mu,
                     C_m=L5B_Cm_mu,
                     t_ref=L5B_tref_mu, **neuron_parameters))
L6_param = dict(dict(E_L=L6_EL_mu,
                     V_th=L6_Vth_mu,
                     C_m=L6_Cm_mu,
                     t_ref=L6_tref_mu, **neuron_parameters))
# Synapse common parameters
"""
    [stdp_synapse]

    lambda     [ms] - Step size
    alpha      [ms] - Asymmetry parameter (scales depressing increments as alpha*lambda)
    tau_plus   [ms] - Time constant of STDP window, potentiation (tau_minus defined in post-synaptic neuron)
    mu_plus    [pA] - Weight dependence exponent, potentiation
    mu_minus   [pA] - Weight dependence exponent, depression
    Wmax       [pA] - Maximum allowed weight
    weight     [nS] - Weight (power) of synapse
    delay      [ms] - Distribution of delay values for connections
"""

STDP_synapseparams = {
    'model':     'stdp_synapse',
    #'alpha':    {'distribution': 'normal_clipped', 'low': 0.5, 'mu': 5.0, 'sigma': 1.0},
    #'lambda':    50.,
    #'alpha':     10.,
    #'tau_plus':  20.
}

# Glutamate synapse
STDP_params_Glu = dict(dict(delay=1.5, weight=w_Glu), **STDP_synapseparams)
# GABA synapse
STDP_params_GABA = dict(dict(delay=1.5, weight=w_GABA), **STDP_synapseparams)

# Dictionary of synapses with keys and their parameters
neurotransmitters = {Glu:   (STDP_params_Glu,  w_Glu),
                     GABA:  (STDP_params_GABA, w_GABA)}

# Device parameters
multimeter_param = {'to_memory': True,
                    'to_file': False,
                    'withtime': True,
                    'interval': 0.1,
                    'record_from': ['V_m', "input_currents_ex"],
                    'withgid': True}

detector_param = {'withtime': True,
                  'withgid': True,
                  'to_file': False,
                  'to_memory': True,
                  'scientific': True}