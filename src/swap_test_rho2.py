# Define SWAP test circuit used in Tr(rho^2) calcultion

qubits = QuantumRegister(2)
clbits = ClassicalRegister(1,'clbit')

auxs = QuantumCircuit(qubits,clbits)

tr_rho2 = QuantumCircuit(2*num_sites+2)
tr_rho2 = tr_rho2.compose(auxs, [0,1])
tr_rho2.compose(ansatz, [i+2 for i in range(num_sites)], inplace=True)
tr_rho2.compose(ansatz, [i+2+num_sites for i in range(num_sites)], inplace=True)
tr_rho2.h(1)
tr_rho2.cswap(1,2,num_sites+2)
tr_rho2.h(1)

tr_rho2.barrier()

N = 1
pauli_list = ['I','X','Y','Z']
for i in range(N):
    tr_rho2.cx(1,0)
    rand_pauli = random.choice(pauli_list)
    tr_rho2.pauli(rand_pauli,[0])
    if rand_pauli == 'X' or rand_pauli == 'Y':
        tr_rho2.x(0)
    tr_rho2.measure(0,0)
    tr_rho2.reset(0)
    with tr_rho2.if_test((0, 1)):
        tr_rho2.x(1)
    tr_rho2.barrier()

tr_rho2.measure(1,0)

display(tr_rho2.draw("mpl", style="iqp"))
