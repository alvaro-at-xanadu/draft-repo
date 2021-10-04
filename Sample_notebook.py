r"""

Photonic Quantum Computers
===========================

The purpose of this section is to introduce how quantum computers may use photons to work.
Photons are good because they do not interact with each other (longer decoherence times)
and can be easily transported using optical fibres. Also, we do not have the problem of
storing at low temperatures. 

"""

##############################################################################
#
# Coherent states
# ----------------
# Hello world
# A coherent state is a superposition of Fock states. It looks like this:
# :math:`e^{-|\alpha|^2/2}\sum_{n=0}\frac{\alpha^n}{\sqrt{n!}}\left\lvert n \right\rangle`

import pennylane as qml
from pennylane import numpy as np

dev = qml.device('default.mixed', wires=2)

@qml.qnode(dev)
def circuit():
    qml.Hadamard(wires=0)
    qml.CNOT(wires=[0, 1])
    return qml.expval(qml.PauliZ(0) @ qml.PauliZ(1))


print(f"QNode output = {circuit():.4f}")



