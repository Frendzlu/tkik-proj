import pprint

notes = {
	"C": -9,
	"D": -7,
	"E": -5,
	"F": -4,
	"G": -2,
	"A": -12,
	"B": -10,
}

mods = {
	"b": -1,
	"#": 1
}

class Chord:

	def __str__(self) -> str:
		return "wololo"

	def __init__(self, initial_string, root_note, mode="maj", modifiers=None, duration=(1, 1)):
		self.root_note = root_note
		self.mode = mode
		self.modifiers = modifiers
		self.duration = duration
		self.initial_string = initial_string
		self.pitches = []
		self.components = [1]

		if len(root_note) > 1:
			trt, mod = root_note[0], root_note[1]
			num = notes[trt] + mods[mod]
		else:
			num = notes[root_note]

		self.pitches.append(num)
		self.components += [3, 5]

		if modifiers and "base_size" in modifiers:
			print(modifiers["base_size"])
			print(list(range(7, modifiers["base_size"]+1, 2)))
			self.components += list(range(7, modifiers["base_size"]+1, 2))

		print(self.components)



