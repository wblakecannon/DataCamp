## Calculating the envelope of sound

# Plot the raw data first
audio.plot(figsize=(10, 5))
plt.show()
_________________________________________________

# Rectify the audio signal
audio_rectified = audio.apply(np.abs)

# Plot the result
audio_rectified.plot(figsize=(10, 5))
plt.show()
__________________________________________________

# Smooth by applying a rolling mean
audio_rectified_smooth = audio_rectified.rolling(50).mean()

# Plot the result
audio_rectified_smooth.plot(figsize=(10, 5))
plt.show()