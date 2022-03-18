
# Simple Turing Machine

import sys

if len(sys.argv) < 3:
   print("Usage: " + sys.argv[0] + " [program file]  [input]\n  Ex: " + sys.argv[0] + " addition.txt 01+01\n" )
   exit(0)

program = open(sys.argv[1]).read()
input = sys.argv[2]

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
