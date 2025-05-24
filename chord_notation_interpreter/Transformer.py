from lark import Transformer, Tree, Token

from chord_notation_interpreter.Chord import Chord


class EvalExpressions(Transformer):
	def no_chord(self, args):
		return {"type": "no_chord"}

	# def modifiers_add_plus(self, args):
	# 	pass

	def reductions(self, args):
		initstr = "no".join([x[0] for x in args[1::2]])
		return "no" + initstr, {"reductions": [int(x[0]) for x in args[1::2]]}

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
				return {"duration": (len(args)*2, 1)}
			temp = args[0][0]
			if len(args) > 1:
				temp *= (len(args)-1)*2
			return {"duration": (temp, args[0][1])}
		return {"duration": (1, 1)}

	def base_note(self, args):
		return args[0]

	def root_note_modifier(self, args):
		return args[0]

	def root_note(self, args):
		if len(args) > 1:
			return args[0] + args[1], {"root_note": args[0] + args[1]}
		return args[0][0], {"root_note": args[0][0]}

	def component_modifiers(self, args):
		modifiers = []
		initstr = ""
		for i in range(len(args)//2):
			initstr += args[2*i]+args[2*i+1]
			modifiers.append({
				"modifier": args[2*i][0],
				"component": int(args[2*i+1])
			})
		return initstr, {"modifiers": modifiers}

	def modifier(self, args):
		return args[0]

	def component_number(self, args):
		return args[0]

	def additions(self, args):
		adds = []
		i = 1
		initstr = ""
		while i < len(args):
			initstr += "add"
			if args[i] in ["b", "#"]:
				initstr += args[i]+args[i+1]
				adds.append({
					"modifier": args[i][0],
					"component": int(args[i+1])
				})
				i += 3
			else:
				initstr += args[i]
				adds.append({
					"component": int(args[i]),
				})
				i += 2
		return initstr, {"additions": adds}

	def chord_base_size(self, args):
		return str(args[0]), {"base_size": int(args[0])}

	def mode(self, args):
		return str(args[0]), {"mode": str(args[0])}

	def suspensions(self, args):
		return f"sus{args[1][0]}", {"suspend": int(args[1][0])}

	def modifiers_add_plus(self, args):
		initstr = ""
		nd = {}
		for d in args:
			initstr += d[0]
			nd.update(d[1])
		return initstr, {"modifiers": nd}

	def modifiers_no_base_size_comp(self, args):
		nd = {}
		initstr = ""
		for d in args:
			initstr += d[0]
			nd.update(d[1])
		return initstr, {"modifiers": nd}

	def modifiers_base_size(self, args):
		nd = {}
		initstr = ""
		for d in args:
			initstr += d[0]
			nd.update(d[1])
		return initstr, {"modifiers": nd}

	def subdiv(self, args):
		return {"subdiv": int(args[0])}

	def chord(self, args):
		initstr = ""
		nd = {}
		for d in args:
			initstr += d[0]
			nd.update(d[1])

		if nd.get("modifiers") is not None:
			if len(nd.get("modifiers")) == 0:
				nd.pop("modifiers")

		return initstr, nd

	# def slash_chord(self, args):
	# 	nd = args[0]
	# 	nd["bass_note"] = args[2].get("root_note")
	# 	nd["type"] = "slash"
	# 	return nd
	#
	# def chord_over_chord(self, args):
	# 	return {
	# 		"type": "overchord",
	# 		"primary": args[0],
	# 		"secondary": args[2]
	# 	}




