from enum import Enum


class TokenType(Enum):
    MEASURE_DELIMITER = 0
    CHORD_REPETITION = 1
    CHORD_OVERLAP = 2
    PITCH = 3
    CHANGE_BY_SEMITONE = 4
    CHORD_ROOT_NODE_MODIFIER = 5
    SUBSCRIPT = 6
    SUPERSCRIPT = 7
    CHORD_QUALITY_MODIFIER = 8
    NUMBER = 9
    CHORD_COMPONENT_MODIFIER = 10
    METRIC_SIGNATURE = 11
    METER_DELIMITER = 12
    NO_CHORD = 13
    KEEP_WHITESPACE = 14
    UNKNOWN = 15


chord_notation_tokens = {
    TokenType.MEASURE_DELIMITER: ["|"],
    TokenType.CHORD_REPETITION: ["\\"],
    TokenType.CHORD_OVERLAP: ["-"],
    TokenType.PITCH: ["A", "B", "C", "D", "E", "F", "G"],
    TokenType.CHANGE_BY_SEMITONE: ["b", "#"],
    TokenType.CHORD_ROOT_NODE_MODIFIER: ["/"],
    TokenType.SUBSCRIPT: ["[", "]"],
    TokenType.SUPERSCRIPT: ["(", ")"],
    TokenType.CHORD_QUALITY_MODIFIER: ["dim", "aug", "m"],
    TokenType.NUMBER: ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"],
    TokenType.CHORD_COMPONENT_MODIFIER: ["add", "no", "sus"],
    TokenType.METRIC_SIGNATURE: ["<", ">"],
    TokenType.METER_DELIMITER: [":"],
    TokenType.NO_CHORD: ["N.C."],
    TokenType.KEEP_WHITESPACE: [" "],
}
