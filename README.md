# SimpleTM
Simple universal Turing Machine
 
> Usage: SimpleTM.py [program file]  [input]
>  Ex: SimpleTM.py addition.txt 01+01

This Python program is a simple implentation of an universal <a href="https://en.wikipedia.org/wiki/Turing_machine">Turing Machine</a> (TM). A Turing Machine is a model for general purpose computation.<br>
It can have these outcomes:
- It accept the input string (enters qA)
- It reject the input string (in this progam, it just stops)
- It loops - same as rejects (it will stop after 500 iterations)
A Turing Machine operates based on instructions (or program, or configuration). Each instruction is described with a transfer function.

Transfer function, f(current-q-state, input-symbol) = (next-q-state, output-symbol, direction-head)<br>
Shorten f(qc, inp) = (qn, out, dir)<br>

1. We stand in state 'qc'
2. If the head reads 'inp' from the tape: then go to state 'qn'
3. Write 'out' and overwrite that 'inp' on the tape
4. Move the head to in 'dir' direction (R(ight) og L(eft)) 

This Python program emulate such TM and read in its "program" from a file and compute an input string. Since it can write back on the input string, an outcome could also be that string.

The varables in the Python program: f(qc, inp) = (qn, out, dir)<br>
The syntax for the program files: qc inp qn out dir

Ex for testprogram.txt:<br>
If we want qc=0 inp=1 qn=2 out=_ dir=R<br>

> 0 1  2 _ R<br>

We stand in state '0'.<br> 
If we read '1' then we replace it with '_' and goes to state '2'. <br>
And then move the head to the Right  <br>
