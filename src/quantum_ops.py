"""
Module for quantum state and operator definitions.
"""
from qiskit.quantum_info import Statevector, Operator
from numpy import sqrt

def get_basic_states():
    """Returns initialized Statevectors."""
    zero = Statevector.from_label("0")
    one = Statevector.from_label("1")
    plus = Statevector.from_label("+")
    minus_i = Statevector.from_label("l")
    return zero, one, plus, minus_i

def get_operators():
    """Returns initialized Operators."""
    h = Operator.from_label("H")
    i_op = Operator.from_label("I")
    x = Operator.from_label("X")
    cx = Operator([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0]])
    return h, i_op, x, cx

def get_superposition_state():
    """Returns a predefined quantum state."""
    return Statevector([0, 1, 1, 0, 1, 0, 0, 0] / sqrt(3))