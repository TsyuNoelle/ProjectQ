from projectq.ops import H, Measure, CNOT, All
from projectq import MainEngine
from projectq.backends import Simulator
import math
import numpy as np

eng = MainEngine(backend=Simulator())
eng2 = MainEngine(backend=Simulator())

qureg = eng.allocate_qureg(2)
qureg2 = eng2.allocate_qureg(2)
eng2.flush()

# bell pair
H | qureg[0]
CNOT | (qureg[0], qureg[1])
eng.flush()
print("cheat:")
print(eng.backend.cheat())

eng2.backend.set_wavefunction([1/math.sqrt(2), 1/math.sqrt(2), 0, 0], qureg)
print("cheat:")
print(eng2.backend.cheat())

print("Scalar product:")
print(np.vdot(eng.backend.cheat()[1], eng2.backend.cheat()[1]).real)

All(Measure) | qureg
All(Measure) | qureg2
