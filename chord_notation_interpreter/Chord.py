import pprint

notes = {
	"C": -21,
	"D": -19,
	"E": -17,
	"F": -16,
	"G": -14,
	"A": -12,
	"B": -10,
}


class Chord:


	def __str__(self) -> str:
		return "wololo"

	def __init__(self, initial_string, root_note, mode="maj", modifiers=None, duration=(1, 1)):
		self.root_note = root_note
		self.duration = duration
		self.initial_string = initial_string