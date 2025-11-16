#!/usr/bin/env python3
"""
TinyASM2TM.py

Compiler from a simple Tiny Assembly language to your Turing Machine
transition table format:

    qc inp qn out dir

Tiny Assembly syntax:

    # Comments start with '#'

    state <name>:
        on <symbol>: write <out_symbol>, move <L|R>, goto <next_state>

Special:
    - 'ACCEPT' as next_state is compiled to the TM accept state "A".
    - Symbols are single characters (e.g. 0, 1, _, +, -).

Example input (TinyASM):

    # Flip bits until blank, then accept
    state 0:
        on 0: write 1, move R, goto 0
        on 1: write 0, move R, goto 0
        on _: write _, move R, goto ACCEPT

Example output (TM):

    0 0 0 1 R
    0 1 0 0 R
    0 _ A _ R
"""

import sys


def parse_tinyasm(lines):
    """
    Parse Tiny Assembly lines into a list of transitions.

    Returns:
        transitions: list of (qc, inp, qn, out, dir)
    """
    transitions = []
    current_state = None
    line_no = 0

    for raw_line in lines:
        line_no += 1
        line = raw_line.strip()

        # Skip empty lines and comments
        if not line or line.startswith("#"):
            continue

        # State definition: state <name>:
        if line.startswith("state "):
            # Expected: state NAME:
            if not line.endswith(":"):
                raise ValueError(f"Syntax error at line {line_no}: missing ':' in state definition")
            header = line[len("state "):-1].strip()
            if not header:
                raise ValueError(f"Syntax error at line {line_no}: empty state name")
            current_state = header
            continue

        # Inside a state we expect "on ..." lines
        if current_state is None:
            raise ValueError(f"Syntax error at line {line_no}: 'on' outside of any state")

        if not line.startswith("on "):
            raise ValueError(f"Syntax error at line {line_no}: expected 'on', got: {line}")

        # Example: "on 0: write 1, move R, goto loop"
        # Split at ":", left is "on 0", right is " write 1, move R, goto loop"
        try:
            left, right = line.split(":", 1)
        except ValueError:
            raise ValueError(f"Syntax error at line {line_no}: missing ':' in 'on' line")

        left = left.strip()   # "on 0"
        right = right.strip() # "write 1, move R, goto loop"

        # Parse left: "on <symbol>"
        parts = left.split()
        if len(parts) != 2 or parts[0] != "on":
            raise ValueError(f"Syntax error at line {line_no}: expected 'on <symbol>'")

        inp_symbol = parts[1]
        if len(inp_symbol) != 1:
            raise ValueError(f"Syntax error at line {line_no}: input symbol must be a single character")

        # Now parse right part: "write X, move D, goto S"
        # We can split by commas
        commands = [c.strip() for c in right.split(",")]
        if len(commands) != 3:
            raise ValueError(
                f"Syntax error at line {line_no}: expected 'write..., move..., goto...', got: {right}"
            )

        # Defaults
        out_symbol = None
        direction = None
        next_state = None

        for cmd in commands:
            # Write
            if cmd.startswith("write "):
                out_symbol = cmd[len("write "):].strip()
                if len(out_symbol) != 1:
                    raise ValueError(
                        f"Syntax error at line {line_no}: output symbol must be a single character"
                    )
            # Move
            elif cmd.startswith("move "):
                direction = cmd[len("move "):].strip().upper()
                if direction not in ("L", "R"):
                    raise ValueError(
                        f"Syntax error at line {line_no}: move direction must be 'L' or 'R'"
                    )
            # Goto
            elif cmd.startswith("goto "):
                next_state = cmd[len("goto "):].strip()
                if not next_state:
                    raise ValueError(f"Syntax error at line {line_no}: empty goto state")
            else:
                raise ValueError(f"Syntax error at line {line_no}: unknown command '{cmd}'")

        if out_symbol is None or direction is None or next_state is None:
            raise ValueError(
                f"Syntax error at line {line_no}: missing write/move/goto in 'on' line"
            )

        # Map special state name ACCEPT → "A"
        if next_state == "ACCEPT":
            qn = "A"
        else:
            qn = next_state

        qc = current_state
        inp = inp_symbol
        out = out_symbol
        dir_ = direction

        transitions.append((qc, inp, qn, out, dir_))

    return transitions


def main():
    if len(sys.argv) < 2:
        print("Usage: TinyASM2TM.py [tinyasm file] > TM-program.txt")
        sys.exit(1)

    tinyasm_path = sys.argv[1]

    with open(tinyasm_path) as f:
        lines = f.readlines()

    transitions = parse_tinyasm(lines)

    # Output in TM format: qc inp qn out dir
    for qc, inp, qn, out, dir_ in transitions:
        print(qc, inp, qn, out, dir_)


if __name__ == "__main__":
    main()
