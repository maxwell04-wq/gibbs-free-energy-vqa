# Define SWAP test circuit used in Tr(rho^3) calcultion using mid-circuit measurment and reset
qubits = QuantumRegister(2)
clbits = ClassicalRegister(1,'clbit')

auxs = QuantumCircuit(qubits,clbits)

tr_rho3 = QuantumCircuit(2*num_sites+2)
tr_rho3 = tr_rho3.compose(auxs, [0,1])
tr_rho3.compose(ansatz, [i+2 for i in range(num_sites)], inplace=True)
tr_rho3.compose(ansatz, [i+2+num_sites for i in range(num_sites)], inplace=True)
tr_rho3.h(1)
tr_rho3.cswap(1,2,num_sites+2)
tr_rho3.barrier()
tr_rho3.reset([2+num_sites+i for i in range(num_sites)])
tr_rho3.compose(ansatz, [i+2+num_sites for i in range(num_sites)], inplace=True)
tr_rho3.cswap(1,2,num_sites+2)
tr_rho3.h(1)

tr_rho3.barrier()

N = 1
pauli_list = ['I','X','Y','Z']
for i in range(N):
    tr_rho3.cx(1,0)
    rand_pauli = random.choice(pauli_list)
    tr_rho3.pauli(rand_pauli,[0])
    if rand_pauli == 'X' or rand_pauli == 'Y':
        tr_rho3.x(0)
    tr_rho3.measure(0,0)
    tr_rho3.reset(0)
    with tr_rho3.if_test((0, 1)):
        tr_rho3.x(1)
    tr_rho3.barrier()

tr_rho3.measure(1,0)

display(tr_rho3.draw("mpl", style="iqp"))
