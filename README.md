# Format description
**_This is a custom format defined by us_** 

Each measure is delimited by two `|` symbols
Each measure at it's beginning contains a number (a power of 2) that defines the smallest chord subdivision
The symbol `\` denotes the repetition of the chord, **OR**, if it's after a measure, the whole measure.
The measures can be grouped using `{` and `}`, and the groups can also be repeated using the `\` symbol
The following repetition notations are equivalent:
- `\ 3`
- `\ \ \`

Note that the former may only be used outside the measure.

Segno's and codas can also be defined using numbered labels (`@`, a number and the delimiter `;`).

The _dal segno al coda_ can be simulated using the jump signature (`&`, a number and the delimiter `;`).
If no number is provided, the jump is considered to be to the beginning of the file.

**All jump commands only work once, and if in a repetition, _only_ at the last repetition**