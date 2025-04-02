# Format description
**_This is a custom format defined by us_** 

Each measure is delimited by two `|` symbols
Each measure at it's beginning contains a number (a power of 2) that defines the smallest chord subdivision
The symbol `%` denotes the repetition of the chord, **OR**, if it's after a measure, the whole measure.
The measures can be grouped using `(` and `)`, and the groups can also be repeated using the `%` symbol
The following repetition notations are equivalent:
- `% 3`
- `%%%`

Note that the former may only be used outside the measure.

Segno's and codas can also be defined using numbered labels (`@`, a number and the delimiter `;`).

The _dal segno al coda_ can be simulated using the jump signature (`&`, a number and the delimiter `;`).
If no number is provided, the jump is considered to be to the beginning of the file.

**All jump commands only work once, and if in a repetition, _only_ at the last repetition**

Each measure has a number at its beginning that denotes the smallest division of measure. If the number is absent, a 4 is assumed.

Just after the denominator may appear the measure duration, with syntax of the form
- <
- `<number>` - the amount of `<subdivision>` in the measure
- :
- `<subdivision>`
- \>

# Grammar
### V
- b, \#
- m, maj, aug, dim
- add, no, sus
- 0-9
- A, B, C, D, E, F, G
- _, %, N.C.
- @, &
- (, ), <, >
- :, ;
- \-, /
### N
- `MeasureKrnl`
- `Preamble`
- `MeasureSuffix`
- `Subdiv`
- `MetricSgn`
- `Chords`
- `P2Number`
- `Number`
- `Number∅`
- `Digit+`
- `Digit∅`
- `JmpSgn`
- `GroupRepeat`
### S = `MeasureKrnl`
### P
- `MeasureKrnl` => `MeasureKrnl` `MeasureKrnl` | `MeasureKrnl` `Preamble`(`MeasureKrnl`)`MeasureSuffix` | `Preamble`(`MeasureKrnl`)`MeasureSuffix` 
- `MeasureKrnl` => |`Subdiv` `MetricSgn` `Chords`|
- `Subdiv` => `P2Number` | ∅
- `P2Number` => `Number` // limit to 1 | 2 | 4 | 8 | 16 | 32 | 64 | 128 | 256
- `Number` => `Digit+` `Number∅`
- `Number∅`=> `Digit∅` | `Digit∅` `Number∅`
- `Digit+` => 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9
- `Digit∅`=> 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | ∅
- `MetricSgn` => <`Number`:`P2Number`> | ∅
- `Preamble` => @`Number`; | ∅
- `MeasureSuffix` => `JmpSgn` `MeasureSuffix` | `GroupRepeat` `MeasureSuffix` | ∅
- `JmpSgn` => &`Number`;
- `GroupRepeat` => % | % `Number`

- `Chords` => `MultiChord` | `MultiChord` `ChordRepeat∅` `Chords` | `MultiChord` `JmpSgn` `Chords`
- `ChordRepeat∅` => % | % `ChordRepeat∅` | ∅
- `MultiChord` => `Chord` | `Chord`-`Chord` | `Chord`/`RootNote` | N.C. | _ 
- `Chord` => `RootNote` `Mode` `Modifiers` |
- `RootNote` => `BaseNote` `RootNoteModifier` | `BaseNote`
- `BaseNote` => A | B | C | D | E | F | G
- `RootNoteModifier` => b | #
- `Mode` => maj | m | dim | aug | ∅
- `Modifiers` => `ChordBaseSize` `ComponentModifiers` `Additions` `Suspensions` `Reductions`
- `ChordBaseSize` => `Number` // limit to 7 | 9 | 11 | 13
- `ComponentModifiers` => `Modifier` `ComponentNumber`
- `Modifier` => b | #
- `ComponentNumber` => `Number` // limit to 5 | 6 | 7 | 9 | 11
- `Additions` => add `Number` | add`Modifier` `Number`// limit to 5 | 8 | 9 | 10 | 11 | 12 | 13 | 14
- `Suspensions` => sus`Number` // limited to 2 and 4, with error if no 3
- `Reductions` => no`Number` //limit to 3 and 5