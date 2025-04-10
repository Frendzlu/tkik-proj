class NToneTemperament:
	def __init__(self, n, freq, ratio=2):
		self.n = n
		self.ratio = ratio
		self.freq = freq

	def frequency(self, pitch):
		"""
			Returns the associated Hz values for single relative pitch ``pitch``.\n
		"""
		if type(pitch) in [int, float]:
			return (self.ratio**(1/self.n))**pitch*self.freq
		else:
			raise TypeError("The frequency should be a number")

	def frequencies(self, pitches):
		"""
			Returns the associated Hz values for multiple relative pitches ``pitches``.\n
			If the pitch is float, adds the decimal part as a cent scale
		"""
		if type(pitches) in [int, float]:
			return self.frequency(pitches)
		elif type(pitches) == list:
			return [self.frequency(pitch) for pitch in pitches]
		else:
			raise TypeError("The frequency should be a list of numbers or a number")