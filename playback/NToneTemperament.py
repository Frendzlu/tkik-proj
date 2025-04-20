import numpy as np


class NTTFrequencyGroup:
	def __init__(self, ntt, chord_code, frequencies, rootN):
		self.ntt = ntt
		self.chord_code = chord_code
		self.frequencies = frequencies
		self.rootN = rootN

	def to_ntt(self, ntt):
		new_chord_code = []
		for interval in self.chord_code:
			ti = interval
			if self.rootN is not None:
				ti -= self.rootN
			ti = np.round((ti/self.ntt.n) * ntt.n).astype(dtype=np.int8)
			new_chord_code.append(ti)
		n_root_n = np.round((self.rootN/self.ntt.n) * ntt.n).astype(dtype=np.int8) if self.rootN is not None else None
		if n_root_n:
			new_chord_code = [c + n_root_n for c in new_chord_code]
		new_ntt_fgroup = NTTFrequencyGroup(ntt, new_chord_code, ntt.frequencies(new_chord_code).frequencies, n_root_n)
		return new_ntt_fgroup

class NToneTemperament:
	def __init__(self, n, freq, ratio=2):
		self.n = n
		self.ratio = ratio
		self.freq = freq

	def frequency(self, pitch):
		"""
			Returns the associated Hz values for single relative pitch ``pitch``.\n
		"""
		if type(pitch) in [int, float, np.int8]:
			return (self.ratio**(1/self.n))**pitch*self.freq
		else:
			raise TypeError("The frequency should be a number")

	def frequencies(self, pitches, rootN=None):
		"""
			Returns the associated Hz values for multiple relative pitches ``pitches``.\n
			If the pitch is float, adds the decimal part as a cent scale
		"""
		if type(pitches) in [int, float, np.int8]:
			return NTTFrequencyGroup(self, pitches, self.frequency(pitches), rootN)
		elif type(pitches) == list:
			return NTTFrequencyGroup(self, pitches, [self.frequency(pitch) for pitch in pitches], rootN)
		else:
			raise TypeError("The frequency should be a list of numbers or a number")

	def batch_convert(self, chords):
		nc = []
		for c in chords:
			nc.append(c.to_ntt(self))
		return nc
