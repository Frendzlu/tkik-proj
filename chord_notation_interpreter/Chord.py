import pprint
import warnings

notes = {
	"C": -9,
	"D": -7,
	"E": -5,
	"F": -4,
	"G": -2,
	"A": -12,
	"B": -10,
}

nts = list("ABCDEFGABCDEFGABCDEFGABCDEFGABCDEFG")

mods = {
	"b": -1,
	"#": 1
}

class Chord:

	def __str__(self) -> str:
		return "<Chord>: " + self.initial_string

	def __init__(self, initial_string, root_note=None, mode="maj", modifiers=None, duration=(1, 1), nc=False, chord_pos=None):
		self.root_note = root_note
		self.mode = mode
		self.modifiers = modifiers
		self.duration = duration
		self.initial_string = initial_string
		self.pitches = []
		self.components = [1]
		self.bass_note = None
		self.nc = nc
		self.error_stack = []

		if nc is True:
			self.chord_code = []
			return

		if self.mode is None:
			self.mode = "maj"

		if len(root_note) > 1:
			trt, mod = root_note[0], root_note[1]
			num = notes[trt] + mods[mod]
		else:
			num = notes[root_note]

		self.pitches.append(num)
		self.components += [3, 5]
		self.changes = {}

		if modifiers and "base_size" in modifiers:
			self.components += list(range(7, modifiers["base_size"]+1, 2))

		if modifiers and "additions" in modifiers:
			for a in modifiers["additions"]:
				self.components += [a["component"]]
				if "modifier" in a:
					self.changes[a["component"]] = a["modifier"]

		if modifiers and "suspend" in modifiers:
			if 3 not in self.components:
				warnings.warn("Third not in chord!")
			else:
				self.components.remove(3)
				self.components.append(modifiers["suspend"])

		if modifiers and "reductions" in modifiers:
			for red in modifiers["reductions"]:
				if red in self.components:
					self.components.remove(red)
				else:
					if chord_pos:
						for p in chord_pos["reductions"]:
							if p.value != "no" and int(p) == int(red):
								self.error_stack.append(f"Line {p.line}, column {p.column}: no {red} to be removed!")
				if red in self.changes:
					del self.changes[red]


		if modifiers and "modifiers" in modifiers:
			for m in modifiers["modifiers"]:
				if m["component"] not in self.components:
					self.components.append(m["component"])
				self.changes[m["component"]] = m["modifier"]

		if 3 in self.components:
			if mode == "m":
				self.changes[3] = "b"
			if mode == "dim":
				self.changes[3] = "b"

		if 5 in self.components:
			if mode == "dim":
				self.changes[5] = "b"
			if mode == "aug":
				self.changes[5] = "#"


		self.components.sort()

		i = nts.index(self.root_note[0])
		cnames = []
		ccode = []

		for comp in self.components:
			cnames.append(nts[i + comp - 1])

		for n in cnames:
			ccode.append(notes[n])

		pcode = ccode[0]
		for i, (comp, code) in enumerate(zip(self.components, ccode)):
			while code < pcode:
				code += 12
			pcode = code
			ccode[i] = code
			if comp in self.changes:
				ccode[i] += -1 if self.changes[comp] == "b" else 1

		if len(self.root_note) > 1:
			for i in range(len(ccode)):
				ccode[i] += -1 if self.root_note[1] == "b" else 1

		self.chord_code = ccode
		self.change_bass_note(root_note)

	def change_bass_note(self, nbs):
		self.bass_note = notes[nbs[0]] - 12
		if len(nbs) > 1:
			self.bass_note += -1 if nbs[1] == "b" else 1

	def tpose(self, num):
		if self.nc:
			return
		self.chord_code = [x+num for x in self.chord_code]
		self.bass_note += num

	def merge(self, new_chrd):
		self.initial_string += "-" + new_chrd.initial_string
		if new_chrd.nc:
			return
		self.chord_code += new_chrd.chord_code
		self.bass_note = new_chrd.bass_note




