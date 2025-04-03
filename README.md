# Format description
**_This is a custom format defined by us_**, heavily based on the commonly used [chord notation format](https://en.wikipedia.org/wiki/Chord_notation)

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

Triplets, and other non-measure groups can be defined using a `Chord`*`Number` notation. The multiplication extends or shortens the relative time the chord sounds.

# Grammar = {Σ, N, S, P}
### Terminal symbols Σ
- b, \#
- m, maj, aug, dim
- add, no, sus
- 0-9
- A, B, C, D, E, F, G
- _, %, N.C., *
- @, &
- (, ), <, >
- :, ;
- \-, /
### Non-terminal symbols N
- `MeasureKrnl`
- `Preamble`
- `MeasureSuffix`
- `Subdiv`
- `TimeSgn`
- `Chords`
- `P2Number`
- `Number`
- `Number∅`
- `Digit+`
- `Digit∅`
- `JmpSgn`
- `GroupRepeat`
- `Chords`
- `MultiChord`
- `Chord`
- `RootNote`
- `BaseNote`
- `RootNoteModifier`
- `Mode`
- `Modifiers`
- `ChordBaseSize`
- `ComponentModifiers`
- `Modifier`
- `ComponentNumber`
- `Additions`
- `Suspensions`
- `Reductions`
- `TimeExtension`
### Starting symbol S = `MeasureKrnl`
### Productions P
- `MeasureKrnl` => `MeasureKrnl` `MeasureKrnl` | `MeasureKrnl` `Preamble`(`MeasureKrnl`)`MeasureSuffix` | `Preamble`(`MeasureKrnl`)`MeasureSuffix` 
- `MeasureKrnl` => |`Subdiv` `TimeSgn` `Chords`|
- `Subdiv` => `P2Number` | ∅
- `P2Number` => `Number`
  - limit `Number` to 1 | 2 | 4 | 8 | 16 | 32 | 64 | 128 | 256
- `Number` => `Digit+` `Number∅`
- `Number∅`=> `Digit∅` | `Digit∅` `Number∅`
- `Digit+` => 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9
- `Digit∅`=> 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | ∅
- `TimeSgn` => <`Number`:`P2Number`> | ∅
- `Preamble` => @`Number`; | ∅
- `MeasureSuffix` => `JmpSgn` `MeasureSuffix` | `GroupRepeat` `MeasureSuffix` | ∅
- `JmpSgn` => &`Number`;
- `GroupRepeat` => % | % `Number`
- `Chords` => `MultiChord` `TimeExtension` | `MultiChord` `TimeExtension` `ChordRepeat∅` `Chords` | `TimeExtension` `MultiChord`  `JmpSgn` `Chords`
  - All the `Chords` (with the value of 1), multiplied by their `TimeExtension` (let's name it T) must sum to the time specified in the `TimeSgn` \<N:D>
  - The formula is: T/`Subdiv` == N/D
- `ChordRepeat∅` => % | % `ChordRepeat∅` | ∅
- `MultiChord` => `Chord` | `Chord`-`Chord` | `Chord`/`RootNote` | N.C. | _ 
- `TimeExtension` => *`Number` | ∅
- `Chord` => `RootNote` `Mode` `Modifiers` |
- `RootNote` => `BaseNote` `RootNoteModifier` | `BaseNote`
- `BaseNote` => A | B | C | D | E | F | G
- `RootNoteModifier` => b | #
- `Mode` => maj | m | dim | aug | ∅
  - error if preceding `RootNote` has a `RootNoteModifier`, the "maj" `Mode` specifier is absent and `Modifiers` has a `ChordBaseSize` or `ComponentModifiers` specifier present
- `Modifiers` => `ChordBaseSize` `ComponentModifiers` `Additions` `Suspensions` `Reductions`
- `ChordBaseSize` => `Number` 
  - limit `Number` to 7 | 9 | 11 | 13
- `ComponentModifiers` => `Modifier` `ComponentNumber` `ComponentModifiers` | ∅
- `Modifier` => b | # | ∅
- `ComponentNumber` => `Number`
  - limit `Number` to 5 | 6 | 7 | 9 | 11
- `Additions` => add`Modifier``Number` `Additions` | ∅ 
  - limit `Number` to 5 | 8 | 9 | 10 | 11 | 12 | 13 | 14
- `Suspensions` => sus`Number`
  - limit `Number` to 2 and 4
- `Reductions` => no`Number` `Reductions` | ∅
  - limit `Number` to 3 and 5
  - error if `Suspensions` is not ∅