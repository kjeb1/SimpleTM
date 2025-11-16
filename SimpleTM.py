#!/usr/bin/env python3
"""
Simple Universal Turing Machine (TM) Emulator.

Usage:
    SimpleTM.py [program file] [input]
Example:
    SimpleTM.py addition.txt 01+01

A Turing Machine is an abstract model of computation operating over:
    - an infinite tape of symbols,
    - a read/write head,
    - and a finite set of states.

A TM program is described by a transition function:

    f(current_state, input_symbol) = (next_state, output_symbol, head_direction)

Short form:
    f(qc, inp) = (qn, out, dir)

Meaning:
    - If the machine is in state qc
    - and the head reads the symbol inp,
      then:
        * write out onto the tape
        * go to state qn
        * move the head one cell Left (L) or Right (R)

Program file syntax (one transition per line):
        qc inp qn out dir

Example line:
    0 1 2 _ R

Interpretation:
    - If in state '0'
    - and read symbol '1':
        * write blank '_'
        * go to state '2'
        * move head Right
"""

import sys

# Maximum number of TM steps allowed (prevents infinite loops)
MAX_STEPS = 500

# Tape blank symbol
BLANK = "_"

# Accepting state name
ACCEPT_STATE = "A"


def load_program(path):
    """
    Load the TM transition table from a text file.

    Expected line format:
        qc inp qn out dir

    Rules:
        - Empty lines are ignored.
        - Lines starting with '#' are comments.
        - Any line not containing exactly 5 tokens is skipped.

    Returns:
        A dictionary mapping (qc, inp) → (qn, out, dir)
    """
    transitions = {}

    with open(path) as f:
        for line in f:
            line = line.strip()

            # Skip comments and empty lines
            if not line or line.startswith("#"):
                continue

            parts = line.split()

            if len(parts) != 5:
                print("Warning: ignoring invalid line in program file:", line)
                continue

            qc, inp, qn, out, direction = parts
            transitions[(qc, inp)] = (qn, out, direction)

    return transitions


def run_tm(transitions, tm_input):
    """
    Execute the Turing Machine on the given input string.

    - Initial state is always "0".
    - Tape is initialized as: input_string + BLANK * MAX_STEPS
    - Head starts at position 0.
    - Machine halts on:
        • reaching ACCEPT_STATE,
        • missing transition,
        • out-of-bounds left movement,
        • exceeding MAX_STEPS.

    During execution:
        - Tape updates are applied directly.
        - State changes are printed.
        - BLANK symbols are hidden in printed tape output.
    """
    state = "0"
    headpos = 0

    # Use a list for the tape so individual cells can be edited efficiently
    tape = list(tm_input + BLANK * MAX_STEPS)

    print("Input:", tm_input)

    for step in range(MAX_STEPS):
        # Check for acceptance
        if state == ACCEPT_STATE:
            break

        # Read symbol under head
        symbol = tape[headpos]

        # Lookup transition: f(state, symbol)
        current_transition = transitions.get((state, symbol))

        if current_transition is None:
            print(
                f"\nNo transition defined for state {state} "
                f"with symbol '{symbol}' — halting."
            )
            break

        qn, out, direction = current_transition

        # Write to tape
        tape[headpos] = out

        # Move head
        if direction.lower() == "r":
            headpos += 1
        elif direction.lower() == "l":
            # Prevent moving left of the tape start
            if headpos == 0:
                print("\nHead attempted to move left of tape start — halting.")
                break
            headpos -= 1
        else:
            print("\nUnknown direction in program:", direction)
            break

        # Update state
        if state != qn:
            state = qn
            print()  # extra newline for readability

        # Print tape without BLANKs
        tape_str = "".join(tape).replace(BLANK, "")
        print("q" + state, tape_str, direction)

    # Final output (BLANKs removed)
    output = "".join(tape).replace(BLANK, "")

    if state == ACCEPT_STATE:
        print("\nq_Accept: output:", output, "for input", tm_input)
    else:
        print("\nq_Reject for input", tm_input)


def main():
    # Check arguments
    if len(sys.argv) < 3:
        print(f"Usage: {sys.argv[0]} [program file]  [input]")
        print(f"  Example: {sys.argv[0]} addition.txt 01+01")
        return

    program_file = sys.argv[1]
    tm_input = sys.argv[2]

    transitions = load_program(program_file)
    run_tm(transitions, tm_input)


if __name__ == "__main__":
    main()
