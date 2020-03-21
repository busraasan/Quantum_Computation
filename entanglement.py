# import all necessary objects and methods for quantum circuits
from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit, execute, Aer

qreg = QuantumRegister(2)
creg = ClassicalRegister(2)

mycircuit = QuantumCircuit(qreg, creg)

mycircuit.h(qreg[0])
mycircuit.cx(qreg[0], qreg[1])

mycircuit.x(qreg[0])

#balvis

mycircuit.cx(qreg[0], qreg[1])
mycircuit.h(qreg[0])

mycircuit.measure(qreg, creg)

job = execute(mycircuit,Aer.get_backend('qasm_simulator'), shots = 1)
counts = job.result().get_counts(mycircuit)
print(counts)
