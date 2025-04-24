# 🎼 Custom Chord Format Interpreter

## 👤 Authors  
- **Name**: Krzysztof Piątek  
- **Email**: piatek@student.agh.edu.pl  
- **Name**: Mateusz Francik  
- **Email**: kiedys_tu_bedzie@mail.mateusza.oby 

## 📌 Project Topic  
**Interpreter for a Custom Music Notation Format** — a parser and playback engine for a domain-specific language representing chord progressions, built to facilitate music experimentation, composition, and live performance.

## 🎯 Project Assumptions

### General Goals  
The project aims to build a tool that can interpret a custom-designed music notation language and **play back** the described chord progressions using generated audio. The notation allows detailed timing, chord structure, and repetition schemes that go beyond traditional lead sheet formats.

### Type of Translator  
**Interpreter** — the program reads and immediately acts on the custom music format, producing sound as output.

### Expected Output  
- Live or rendered **audio playback** of the input chord progression.

### Language of Implementation  
**Python**

### Scanner/Parser Implementation  
- Built using **Lark**, a modern parsing library for Python that supports context-free grammars.
- Grammar is defined in Lark's EBNF-style format.

---

## 🔠 Tokens

The following tokens are defined in the lexer portion of the Lark grammar:

| Token Name    | Description                                  |
|---------------|----------------------------------------------|
| `NUMBER`      | Numeric value (used in time, chords, etc.)   |
| `SLASH (/)`   | Slash chords notation (e.g., C/E)            |
| `DASH (-)`    | Chord over chord (e.g., C-E)                 |
| `STAR (*)`    | Duration modifier                            |
| `AMP (&)`     | Jump signal                                  |
| `PERCENT (%)` | Repeats indicator                            |
| `HASH (#)`    | Sharp                                        |
| `FLAT (b)`    | Flat                                         |
| `LT (<)`      | Time signature open                          |
| `GT (>)`      | Time signature close                         |
| `LPAR, RPAR`  | Parentheses for grouping (they are both different tokens)|
| `PIPE (\|)`    | Measure boundary                             |
| `SEMI (;)`    | End of label or jump                         |
| `AT (@)`      | Measure label                                |
| `COLON (:)`   | Used in time signature                       |
| `UNDERSCORE`  | Chord hold                                   |
| `NC`          | No chord                                     |
| `MODE`        | Chord mode: `maj`, `m`, `dim`, `aug`         |
| `ADD`         | Addition to chords                           |
| `NO`          | Reduction/removal from chords                |
| `SUS`         | Suspension notation                          |
| `NOTES`       | Musical notes: A–G                           |


# WARNING
GRAMMAR IS NOT YET LALR COMPATIBLE - WORK IN PROGRESS

## 📚 Grammar (Lark EBNF)

```lark
start: measure* measure_group* measure*

measure_group: preamble? LPAR measure* measure_group* measure* RPAR measure_suffix?

measure: preamble? PIPE subdiv? time_sgn? chords PIPE measure_suffix?

subdiv: p2_number
time_sgn: LT number COLON p2_number GT
preamble: AT number SEMI
measure_suffix: (jmp_sgn | group_repeat)+

jmp_sgn: AMP number SEMI
group_repeat: PERCENT number?

chords: (multi_chord)+

hold_chord: UNDERSCORE | UNDERSCORE hold_chord

multi_chord: (chord | chord_over_chord | slash_chord | no_chord) time_extension? hold_chord? | PERCENT hold_chord?

chord_over_chord: chord DASH chord
no_chord: NC
slash_chord: chord SLASH root_note

time_extension: STAR number
chord: root_note mode? modifiers*

root_note: base_note root_note_modifier?
base_note: NOTES
root_note_modifier: FLAT | HASH

mode: MODE
modifiers: chord_base_size? component_modifiers? additions? suspensions? reductions?

chord_base_size: number
component_modifiers: (modifier? component_number)+
modifier: FLAT | HASH
component_number: number

additions: ADD modifier? number+
suspensions: SUS ("2" | "4")
reductions: NO ("3" | "5")

p2_number: number
number: NUMBER

NUMBER: /[0-9]//[1-9]/*
SLASH: "/"
DASH: "-"
STAR: "*"
AMP: "&"
PERCENT: "%"
HASH: "#"
FLAT: "b"
LT: "<"
GT: ">"
LPAR: "("
RPAR: ")"
PIPE: "|"
SEMI: ";"
AT: "@"
COLON: ":"
UNDERSCORE: "_"
NC: "N.C."
MODE: "maj" | "m" | "dim" | "aug"
ADD: "add"
NO: "no"
SUS: "sus"
NOTES: "A" | "B" | "C" | "D" | "E" | "F" | "G"
