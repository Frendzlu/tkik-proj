notes = {
	"C": -9,
	"D": -7,
	"E": -5,
	"F": -4,
	"G": -2,
	"A": 0,
	"B": 2,
}


class Chord:
	type: str
	notes: list[int]
	root_note: str
	root_pitch: int
	mode: str
	root_note_modifier: int
	modifiers: str
	duration: int
	base_note: str
	base_note_modifier: int
	other_chord = None

	def __str__(self) -> str:
		if self.type == "no_chord":
			return "N.C."
		if self.type == "chord":
			return f"{self.root_note}{['', '#', 'b'][self.root_note_modifier]}{self.mode}{self.modifiers}"
		if self.type == "slash_chord":
			return (f"{self.root_note}{['', '#', 'b'][self.root_note_modifier]}{self.mode}{self.modifiers}/" +
			        f"{self.base_note}{['', '#', 'b'][self.base_note_modifier]}")
		return (f"{self.root_note}{['', '#', 'b'][self.root_note_modifier]}{self.mode}{self.modifiers}-"
		        f"{self.other_chord.root_note}{['', '#', 'b'][self.other_chord.root_note_modifier]}{self.other_chord.mode}{self.other_chord.modifiers}")

	def __init__(self, chord_type, duration=1, root_note=None, base_note=None, secondary_chord=None):
		self.type = chord_type
		self.root_note = root_note
		if chord_type == "no_chord":
			self.notes = []
			self.duration = duration
			return
		if not root_note:
			raise ValueError("Root note cannot be None")
		if chord_type == "chord_over_chord":
			if not secondary_chord:
				raise ValueError("secondary_chord is required")

			pass
		elif chord_type == "slash_chord":
			if not base_note:
				raise ValueError("base_note is required")
			pass
		else:
			pass