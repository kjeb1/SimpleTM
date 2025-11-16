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