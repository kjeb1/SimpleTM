
# Simple Turing Machine

# Transfer function f(current-q-state, input-symbol) = (next-q-state, output-symbol, direction)
# f(qc, inp) = (qn, out, dir)
# qc inp qn out dir
#
# 1. We stand in state 'qc'
# 2. If the head reads 'inp' from the tape: then go to state 'qn'
# 3. Write 'out' and overwrite that 'inp' on the tape
# 4. Move the head to in 'dir' direction (R(ight) og L(eft)) 

input = '01+01' # Binary addition, it should then accept "10"
program = open('tmprogram.txt').read()

max=500 # max tape len and max loops

transition = {}
state = "0"
headpos = 0 
tape = input + "_" * max

print("Input: " + input)

# Read in the program file into transition data-set
for line in program.splitlines():
   if not line.startswith('#') and len(line) >= 9:
      qc, inp, qn, out, dir = line.split()
      transition[qc,inp] = (qn, out, dir)

i = 0
while state != "A" and i < max:

   # Head reads from the tape
   inp = tape[headpos]

   # Get the transition function from the data-set for this state and this input symbol
   curretntTransition = transition.get((state, inp))

   if curretntTransition:
      qn, out, dir = curretntTransition

      # Write back on the the tape
      tape = tape[:headpos] + out + tape[headpos+1:]

      # Move the head to Right or Lefts
      if dir.lower() == 'r':
         headpos = headpos + 1
      elif dir.lower() == 'l':
         headpos = headpos -1

      # Go to next state 
      if state != qn:
         state = qn
         print()
      
      print("q" + state, tape.replace('_', ''),  dir)

   i += 1
if state == "A":
  print("\nq_Accept: output:", tape.replace('_', ''), "for input", input)
else:
  print("\nq_Reject for input", input)
