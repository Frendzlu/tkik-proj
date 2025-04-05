from utils import reader
from lark import Lark


if __name__ == "__main__":
    grammar = reader("./grammar.txt")
    chord_code = reader("./test.txt")

    # chord code parser
    ccp = Lark(rf"{grammar}", start="start")

    # abstract syntax tree
    ast = ccp.parse(chord_code)
    print(ast.pretty())


# MeasureKrnl:      MeasureKrnl MeasureKrnl
#                 | MeasureKrnl Preamble "(" MeasureKrnl ")" MeasureSuffix
#                 | Preamble "(" MeasureKrnl ")" MeasureSuffix
#                 | "|" Subdiv TimeSgn Chords "|"

# Subdiv:                 P2Number | ∅
# P2Number:               Number
# Number:                 Digit+ Number∅
# Number∅:                Digit∅ | Digit∅ Number∅
# Digit+:                 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9
# Digit∅:                 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | ∅
# TimeSgn:                "<" Number ":" P2Number ">" | ∅
# Preamble:               "@" Number ";" | ∅
# MeasureSuffix:          JmpSgn MeasureSuffix | GroupRepeat MeasureSuffix | ∅
# JmpSgn:                 "&" Number ";"
# GroupRepeat:            "%" | "%" Number
# Chords:                 MultiChord TimeExtension | MultiChord TimeExtension ChordRepeat∅ Chords | TimeExtension MultiChord JmpSgn Chords
# ChordRepeat∅:           "%" | "%" ChordRepeat∅ | ∅
# MultiChord:             Chord |  Chord "-" Chord | Chord "/" RootNote | "N.C." | "_"
# TimeExtension:          "*" Number | ∅
# Chord:                  RootNote Mode Modifiers "|"
# RootNote:               BaseNote RootNoteModifier | BaseNote
# BaseNote:               "A" | "B" | "C" | "D" | "E" | "F" | "G"
# RootNoteModifier:       "b" | "#"
# Mode:                   "maj" | "m" | "dim" | "aug" | ∅
# Modifiers:              ChordBaseSize ComponentModifiers Additions Suspensions Reductions
# ChordBaseSize:          Number
# ComponentModifiers:     Modifier ComponentNumber ComponentModifiers | ∅
# Modifier:               "b" | "#" | ∅
# ComponentNumber:        Number
# Additions:              "add" Modifier Number Additions | ∅
# Suspensions:            "sus" Number
# Reductions:             "no" Number Reductions | ∅


# start: measure_krnl

# measure_krnl:     measure_krnl measure_krnl
#                 | measure_krnl preamble LPAR measure_krnl RPAR measure_suffix
#                 | preamble LPAR measure_krnl RPAR measure_suffix
#                 | PIPE subdiv time_sgn chords PIPE

# subdiv:                 p2number?
# p2number:               NUMBER
# time_sgn:               LT NUMBER COLON p2number GT
#         |
# preamble:               AT NUMBER SEMI
#         |
# measure_suffix:         jmp_sgn measure_suffix | group_repeat measure_suffix
#         |
# jmp_sgn:                AMP NUMBER SEMI
# group_repeat:           PERCENT | PERCENT NUMBER
# chords:                 multichord time_extension | multichord time_extension chord_repeat_eps chords | time_extension multichord jmp_sgn chords
# chord_repeat_eps:       PERCENT | PERCENT chord_repeat_eps
#         |
# multichord:             chord (SLASH root_note)? |  chord DASH chord | NC | UNDERSCORE
# time_extension:         STAR NUMBER
#         |
# chord:                  root_note mode modifiers PIPE
# root_note:              base_note root_note_modifier | base_note
# base_note:              NOTES
# root_note_modifier:     FLAT | HASH
# mode:                   MODE?
# modifiers:              chord_base_size component_modifiers additions suspensions reductions
# chord_base_size:        NUMBER
# component_modifiers:    modifier component_number component_modifiers
#         |
# modifier:               FLAT | HASH
#         |
# component_number:       NUMBER
# additions:              ADD modifier NUMBER additions
#         |
# suspensions:            SUS NUMBER
# reductions:             NO NUMBER reductions
#         |


# //terminals
# SLASH: "/"
# DASH: "-"
# STAR: "*"
# AMP: "&"
# PERCENT: "%"
# HASH: "#"
# FLAT: "b"
# LT: "<"
# GT: ">"
# LPAR: "("
# RPAR: ")"
# PIPE: "|"
# SEMI: ";"
# AT: "@"
# COLON: ":"
# UNDERSCORE: "_"
# NC: "N.C."
# MODE: "maj" | "m" | "dim" | "aug"
# ADD: "add"
# NO: "no"
# SUS: "sus"
# NOTES: "A" | "B" | "C" | "D" | "E" | "F" | "G"

# %import common.SIGNED_NUMBER    -> NUMBER
# %import common.WS
# %ignore WS
