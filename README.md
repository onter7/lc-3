# LC-3
LC-3 Implementation in Logisim

**Version 1** implements the core functionality, excluding I/O and interrupts.

Supported instructions: **ADD**, **AND**, **BR**, **JMP**, **LD**, **LDI**, **LDR**, **LEA**, **NOT**, **ST**, **STI**, **STR**

`lc3_states.xlsx` defines control signals per LC-3 state. Some states are not yet populated in the version 1 draft.

`rom.py` script reads `lc3_states.xlsx`, generating a hex file used to load microinstructions into the LC-3 ROM. Currently, the input and output file names are hardcoded.

`microcode.hex` contains the compiled microcode and must be regenerated after any changes to `lc3_states.xlsx`.

![LC-3 v1 schematic](/v1_schema.png)
