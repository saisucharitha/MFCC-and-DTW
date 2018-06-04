import librosa
import numpy
X, sample_rate = librosa.load('nikhil1.wav')
stft = numpy.abs(librosa.stft(X))
mfccs = numpy.mean(librosa.feature.mfcc(y=X, sr=sample_rate, n_mfcc=40).T,axis=0)
chroma = numpy.mean(librosa.feature.chroma_stft(S=stft, sr=sample_rate).T,axis=0)
mel = numpy.mean(librosa.feature.melspectrogram(X, sr=sample_rate).T,axis=0)
contrast = numpy.mean(librosa.feature.spectral_contrast(S=stft, sr=sample_rate).T,axis=0)
tonnetz = numpy.mean(librosa.feature.tonnetz(y=librosa.effects.harmonic(X), sr=sample_rate).T,axis=0)
feat = numpy.hstack([mfccs,chroma,mel,contrast,tonnetz])
print(feat[:12])
