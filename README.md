# SimpleTM
Simple universal Turing Machine

This Python program is a simple implentation of an universal <a href="https://en.wikipedia.org/wiki/Turing_machine">Turing Machine</a> (TM). A Turing Machine is a model for general purpose computation.

Transfer function f(current-q-state, input-symbol) = (next-q-state, output-symbol, direction-head)<br>
Shorten f(qc, inp) = (qn, out, dir)<br>

1. We stand in state 'qc'
2. If the head reads 'inp' from the tape: then go to state 'qn'
3. Write 'out' and overwrite that 'inp' on the tape
4. Move the head to in 'dir' direction (R(ight) og L(eft)) 

This Python program emulate such TM and read in its "program" or congfiguration from a file and compute an input string.

The varables in the Python program: f(qc, inp) = (qn, out, dir)<br>
The syntax in the tmprogra.txt: qc inp qn out dir

Ex for tmprogram.txt:<br>
If we want qc=0 inp=1 qn=2 out=_ dir=R<br>

> 0 1  2 _ R<br>

We stand in state '0'.<br> 
If we read '1' then we replace it with '_' and goes to state '2'. <br>
And then move the head to the Right  <br>


