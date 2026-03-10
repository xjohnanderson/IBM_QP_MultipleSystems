
# Main execution entry point for quantum state manipulations.

import qiskit
from src.quantum_ops import get_basic_states, get_operators, get_superposition_state
from src.visualization import show_state, show_operator

def run_demonstration():
    print(f"Qiskit version: {qiskit.__version__}")
    
    zero, one, plus, minus_i = get_basic_states()
    h, i_op, x, cx = get_operators()

    # Demonstrations
    show_state(zero.tensor(one), "psi")
    show_state(plus.tensor(minus_i), "phi")
    show_state(plus ^ minus_i, "plus ^ minus_i")
    
    show_operator(h.tensor(i_op), "H tensor I")
    show_operator(h.tensor(i_op).tensor(x), "H tensor I tensor X")
    show_operator(h ^ i_op ^ x, "H ^ I ^ X")

    # Evolution
    psi = plus.tensor(zero)
    show_state(psi.evolve(cx), "Evolved State")

    # Measurement
    w = get_superposition_state()
    show_state(w, "Initial W")

    res1, state1 = w.measure([0])
    print(f"Measured: {res1}")
    show_state(state1, "State after measurement [0]")

    res2, state2 = w.measure([0, 1])
    print(f"Measured: {res2}")
    show_state(state2, "State after measurement [0, 1]")

if __name__ == "__main__":
    run_demonstration()