# SimpleTM
Simple universal Turing Machine

This Python program is a simple implentation of an universal <a href="https://en.wikipedia.org/wiki/Turing_machine">Turing Machine</a> (TM). A Turing Machine is a model for general purpose computation.<br>

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
  -  write out onto the tape  
  - go to state qn  
  -  move the head one cell   Left (L) or Right (R)

Program file syntax (one transition per line):  

        qc inp qn out dir

Example line:  

    0 1 2 _ R

Interpretation:
- If in state '0'
- and read symbol '1':
  -  write blank '_'
  - go to state '2'
  - move head Right


## Intuition Behind the Turing Machine Emulator

This Python program simulates a simple Turing Machine by repeatedly performing the three fundamental TM actions:

1. Read the symbol under the tape head

2. Look up the matching transition rule

3. Write, move, and change state according to that rule



### The tape and head

The tape is represented as a long string containing:

- the input characters, followed by

- many blank symbols _

The head starts at the very first character of the input.

### States and the transition function

The machine keeps track of a current state (starting at "0").
All rules are loaded from the program file into a dictionary:

    (state, input_symbol) → (next_state, output_symbol, direction)


Intuitively:

    “If I am in state qc and I see symbol s, then I should write out, move my head left or right, and continue in state qn.”

### One iteration of the machine

Each loop of the emulator does the following:

1. Read the symbol under the head

2. Check whether there is a rule for (current_state, symbol)

3. If a rule exists:

   - Write the new symbol onto the tape

   - Move the head left or right by one cell

   - Switch to the next state

4. If no rule exists:

   - The machine halts and rejects the input

### Accepting and rejecting

- If the machine ever enters state "A", it halts and accepts.

- If it runs out of steps, or encounters a missing rule, it halts and rejects.

### Why this works

By following these simple operations: read, write, move, change state; the emulator reproduces exactly the behavior of a classical single-tape Turing Machine.
Every computation is just a sequence of local steps that gradually modify the tape and move the head across it.