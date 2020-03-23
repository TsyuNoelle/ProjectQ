from projectq.ops import H, Measure, CNOT, All, Rx, Ry, Deallocate
from projectq import MainEngine
from projectq.backends import Simulator
import math
import numpy as np

# first qureg
eng = MainEngine(backend=Simulator())
qureg = eng.allocate_qureg(5)
eng.flush()

H | qureg[0]
CNOT | (qureg[0], qureg[1])
CNOT | (qureg[1], qureg[2])
CNOT | (qureg[2], qureg[3])
Rx(0.6) | qureg[4]
eng.flush()

state_vec = eng.backend.cheat()[1]
print("cheat vec1:")
print(eng.backend.cheat())

# second qureg
eng.backend.set_wavefunction([1] + [0 for i in range(2**5 - 1)], qureg)

H | qureg[0]
CNOT | (qureg[0], qureg[1])
CNOT | (qureg[1], qureg[2])
Ry(0.5) | qureg[3]
Rx(0.6) | qureg[4]
eng.flush()

state_vec2 = eng.backend.cheat()[1]
print("cheat vec2:")
print(eng.backend.cheat())

print("Scalar product:")
print(np.vdot(state_vec, state_vec2))

All(Measure) | qureg
eng.flush()
