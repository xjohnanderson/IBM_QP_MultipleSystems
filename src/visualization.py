"""
Module for handling display outputs for quantum objects.
"""
from IPython.display import display

def show_state(state, label=""):
    """Displays a quantum state using LaTeX rendering."""
    if label:
        print(f"--- {label} ---")
    display(state.draw("latex"))

def show_operator(op, label=""):
    """Displays a quantum operator using LaTeX rendering."""
    if label:
        print(f"--- {label} ---")
    display(op.draw("latex"))