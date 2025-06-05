import copy

from lark import Transformer, Tree, Token

from chord_notation_interpreter.Chord import Chord
from chord_notation_interpreter.Measure import Measure


class EvalExpressions(Transformer):
    used_segno_numbers = {}
    used_jump_numbers = []
    error_stack = []
    last_used_sgn = (4, 4)

    def no_chord(self, args):
        return {"type": "no_chord"}

    def reductions(self, args):
        initstr = "no".join([x[0] for x in args[1::2]])
        return "no" + initstr, {"reductions": [int(x[0]) for x in args[1::2]]}, {"reductions": args}

    def number(self, args):
        return args[0]

    def p2_number(self, args):
        return args[0]

    def time_sgn(self, args):
        return {"time_sgn": (int(args[1]), int(args[3]))}

    def time_extension(self, args):
        if len(args) == 4:
            return int(args[1]), int(args[3])
        return int(args[1]), 1

    def duration(self, args):
        if len(args) > 0:
            if isinstance(args[0], Token):
                return {"duration": (len(args) * 2, 1)}
            temp = args[0][0]
            if len(args) > 1:
                temp *= (len(args) - 1) * 2
            return {"duration": (temp, args[0][1])}
        return {"duration": (1, 1)}

    def base_note(self, args):
        return args[0]

    def root_note_modifier(self, args):
        return args[0]

    def modified_root_note(self, args):
        return args[0] + args[1], {"root_note": args[0] + args[1]}

    def root_note(self, args):
        return args[0][0], {"root_note": args[0][0]}

    def component_modifiers(self, args):
        if int(args[-1]) in [1, 3]:
            self.error_stack.append(
                f"Line {args[-1].line}, column {args[-1].column}: Modification of 1 or 3 is not supported."
            )

        modifiers = []
        initstr = ""
        for i in range(len(args) // 2):
            initstr += args[2 * i] + args[2 * i + 1]
            modifiers.append({"modifier": args[2 * i][0], "component": int(args[2 * i + 1])})
        return initstr, {"modifiers": modifiers}

    def modifier(self, args):
        return args[0]

    def component_number(self, args):
        return args[0]

    def additions(self, args):
        if int(args[-1]) not in [2, 4, 6, 8, 9, 10, 11, 12, 13, 14]:
            self.error_stack.append(
                f"Line {args[-1].line}, column {args[-1].column}: Addition of {args[-1]} is not supported. Allowed values are from 2 to 14, except 3, 5 and 7"
            )
        adds = []
        i = 1
        initstr = ""
        while i < len(args):
            initstr += "add"
            if args[i] in ["b", "#"]:
                initstr += args[i] + args[i + 1]
                adds.append({"modifier": args[i][0], "component": int(args[i + 1])})
                i += 3
            else:
                initstr += args[i]
                adds.append(
                    {
                        "component": int(args[i]),
                    }
                )
                i += 2
        return initstr, {"additions": adds}

    def chord_base_size(self, args):
        if int(args[0]) not in [7, 9, 11, 13]:
            self.error_stack.append(
                f"Line {args[0].line}, column {args[0].column}: Chord size of {args[0]} is not supported. Allowed values are 7, 9, 11, 13."
            )
        return str(args[0]), {"base_size": int(args[0])}

    def mode(self, args):
        return str(args[0]), {"mode": str(args[0])}

    def suspensions(self, args):
        return f"sus{args[1][0]}", {"suspend": int(args[1][0])}, {"suspensions": args}

    def modifiers_add_plus(self, args):
        initstr = ""
        nd = {}
        line_pos = {}
        for d in args:
            initstr += d[0]
            nd.update(d[1])
            if len(d) > 2:
                line_pos.update(d[2])

        return initstr, {"modifiers": nd}, line_pos

    def modifiers_no_base_size_comp(self, args):
        nd = {}
        initstr = ""
        line_pos = {}
        for d in args:
            initstr += d[0]
            nd.update(d[1])
            if len(d) > 2:
                line_pos.update(d[2])
        return initstr, {"modifiers": nd}, line_pos

    def modifiers_base_size(self, args):
        nd = {}
        initstr = ""
        line_pos = {}
        for d in args:
            initstr += d[0]
            nd.update(d[1])
            if len(d) > 2:
                line_pos.update(d[2])
        return initstr, {"modifiers": nd}, line_pos

    def subdiv(self, args):
        return {"subdiv": int(args[0])}

    def chord(self, args):
        initstr = ""
        nd = {}
        chord_pos = {}
        for d in args:
            initstr += d[0]
            nd.update(d[1])
            if len(d) > 2:
                chord_pos.update(d[2])

        if nd.get("modifiers") is not None:
            if len(nd.get("modifiers")) == 0:
                nd.pop("modifiers")

        chrd = Chord(initstr, nd.get("root_note"), mode=nd.get("mode"), modifiers=nd.get("modifiers"), chord_pos=chord_pos)

        self.error_stack += chrd.error_stack
        return initstr, chrd

    def slash_chord(self, args):
        init_str = args[0][0] + "/" + args[2][0]
        chrd = args[0][1]
        chrd.change_bass_note(args[2][1].get("root_note"))
        return init_str, chrd

    def chord_over_chord(self, args):
        init_str = args[0][0] + "-" + args[2][0]
        chrd1 = args[0][1]
        chrd2 = args[2][1]
        chrd2.tpose(-12)
        chrd1.merge(chrd2)
        return init_str, chrd1

    def multi_chord(self, args):
        if args[0] == "%":
            return "%", args[1].get("duration")
        if "type" in args[0]:
            return Chord("N.C", nc=True)
        init_str, chrd = args[0]
        dur = args[1].get("duration")
        chrd.duration = dur
        return chrd

    def chords(self, args):
        sch = args[0]
        narg = []
        for i in range(len(args)):
            nc = args[i]
            if isinstance(nc, tuple):
                dur = args[i][1]
                nc = copy.deepcopy(sch)
                nc.duration = dur
            narg.append(nc)
            sch = nc
        return {"chords": narg}

    def preamble(self, args):
        if int(args[1]) in self.used_segno_numbers.keys():
            self.error_stack.append(
                f"Line {args[1].line}, column {args[1].column}: segno numbers conflict - "
                f"previously defined in line {self.used_segno_numbers[int(args[1])][0]}, column "
                f"{self.used_segno_numbers[int(args[1])][1]}"
            )
        else:
            self.used_segno_numbers[int(args[1])] = args[1].line, args[1].column
        return {"segno_number": int(args[1])}

    def group_repeat(self, args):
        return {"repeat": int(args[1])}

    def jmp_sgn(self, args):
        x = int(args[1])
        if x not in self.used_jump_numbers:
            self.used_jump_numbers.append(x)
        return {"jump_to": x}

    def measure_suffix(self, args):
        return {"suffix": args}

    def measure(self, args):
        segno_number = None
        time_signature = self.last_used_sgn
        subdiv = 4
        chords = []
        suffix = []

        for a in args:
            if isinstance(a, dict):
                if "segno_number" in a:
                    segno_number = a["segno_number"]
                    continue
                if "subdiv" in a:
                    subdiv = a["subdiv"]
                    continue
                if "time_sgn" in a:
                    time_signature = a["time_sgn"]
                    self.last_used_sgn = a["time_sgn"]
                    continue
                if "chords" in a:
                    chords = a["chords"]
                    continue
                if "suffix" in a:
                    suffix = a["suffix"]
                    continue

        m = Measure(chords, subdiv, time_signature, segno_number, suffix)

        self.error_stack += m.error_stack

        return m

    def measure_group(self, args):
        sgn = None
        suffix = []

        measures = []

        for arg in args:
            if isinstance(arg, dict):
                if "segno_number" in arg:
                    sgn = arg["segno_number"]
                    continue
                if "suffix" in arg:
                    suffix = arg["suffix"]
                    continue

            if isinstance(arg, Measure):
                measures.append(arg)
                continue

            if isinstance(arg, list):
                return arg

        return measures

    def start(self, args):
        measures = []

        for arg in args:
            if isinstance(arg, list):
                measures += arg
                continue
            measures.append(arg)

        return measures
