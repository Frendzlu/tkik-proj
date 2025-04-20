from chord_notation_interpreter.Instruments import Instruments
from chord_notation_interpreter.Measure import Measure

class Sheet:
	melodic_lines = dict[Instruments, list[Measure]]

	def __init__(self, instruments=(Instruments.default,)):
		self.melodic_lines = {x: [] for x in instruments}

