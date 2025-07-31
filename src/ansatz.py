# Defien free energy calculation to be minimize based on ansatz parameters
def cost_func(params, ansatz, tr_rho2, tr_rho3, hamiltonian, beta, estimator, sampler):
    free_energy = 0

    # Expectation value of H
    e_pub = (ansatz, [hamiltonian], [params])
    energy = estimator.run(pubs=[e_pub]).result()[0].data.evs[0]
    free_energy += energy-3/(2*beta)

    n_shots = 1024

    # Calculation and post-processing of Tr(rho^2)
    s_pub = (tr_rho2,[params],n_shots)
    job2 = sampler.run(pubs=[s_pub]).result()[0].data.clbit.get_counts()
    try:
        R2 = job2['0']/n_shots - job2['1']/n_shots
    except:
        R2 = 1
    free_energy += (2/beta)*R2

    # Calculation and post-processing of Tr(rho^3)
    s_pub = (tr_rho3,[params],n_shots)
    job3 = sampler.run(pubs=[s_pub]).result()[0].data.clbit.get_counts()
    try:
        R3 = job3['0']/n_shots - job3['1']/n_shots
    except:
        R3 = 1
    free_energy += (-1/(2*beta))*R3

    return free_energy
