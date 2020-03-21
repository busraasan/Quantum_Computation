from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit, execute, Aer
from random import randrange
from math import cos, sin, pi

qreg = QuantumRegister(3)
creg = ClassicalRegister(2)

# qreg[2]: Asja's first qubit (qubit to be teleported)
# qreg[1]: Asja's second qubit
# qreg[0]: Balvis' qubit

mycircuit = QuantumCircuit(qreg, creg)

#creating entanglement between Asja's 2nd and Balvis' qubit.
mycircuit.h(qreg[1])
mycircuit.cx(qreg[1], qreg[0])

#we create a random quantum state in Asja's qubit which is being teleported.
d = randrange(360)
d_radian = d*pi/180

x = cos(d_radian)
y = sin(d_radian)
print("Picked angle is "+str(d)+" degrees, "+str(round(d_radian,2))+" radians.")
print("So to be teleported state is "+str(round(x,2))+"|0>+"+str(round(y,2))+"|1>.")

mycircuit.ry(2*d_radian, qreg[2])
mycircuit.barrier()

#Asja's first qubit is control and second qubit is target.
mycircuit.cx(qreg[1], qreg[2])

#Hadamard operator by Asja on her first qubit.
mycircuit.h(qreg[2])

#Alice measures her qubits. Now i know the state of Balvis' qubit.
mycircuit.measure(qreg[1],creg[0])
mycircuit.measure(qreg[2],creg[1])

job = execute(mycircuit,Aer.get_backend('qasm_simulator'), shots = 1)
counts = job.result().get_counts(mycircuit)
print(counts)
