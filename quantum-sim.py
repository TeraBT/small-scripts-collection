from qiskit import QuantumCircuit

from qiskit_aer import Aer

import matplotlib.pyplot as plt

import numpy as np

backend = Aer.get_backend('qasm_simulator')

qc = QuantumCircuit(2)

qc.h(0)
qc.cx(0, 1)
qc.measure_all()

qc.draw('mpl')
plt.figure()

job = backend.run(qc, shots=1000)

result = job.result()

counts = result.get_counts(qc)
print(counts)
plt.bar(counts.keys(), counts.values())
plt.show()

########################################

qc = QuantumCircuit(1, 1)

qc.ry(np.pi/3, 0)

qc.measure(0, 0)

qc.draw('mpl')
plt.figure()

job = backend.run(qc, shots=1000)

result = job.result()
counts = result.get_counts(qc)
print(counts)
plt.bar(counts.keys(), counts.values())
plt.show()

########################################

qc = QuantumCircuit(1, 1)

qc.ry(np.pi/3, 0)
qc.x(0)

qc.measure(0, 0)

qc.draw('mpl')
plt.figure()

job = backend.run(qc, shots=1000)

result = job.result()
counts = result.get_counts(qc)

print(counts)
plt.bar(counts.keys(), counts.values())
plt.show()