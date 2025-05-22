# import required module
from playsound import playsound, PlaysoundException

# for playing laugh mp4 file
# Note: playsound is primarily for audio files (e.g., MP3, WAV). 
# MP4 support might be limited or require additional codecs.
# Consider converting HamilJokerLaugh.mp4 to an audio format for reliable playback.
try:
    playsound('./HamilJokerLaugh.mp4')
except PlaysoundException as e:
    print(f"Error playing sound: {e}")
    print("Please ensure './HamilJokerLaugh.mp4' is a valid audio file and VLC is installed if on Linux.")
except FileNotFoundError:
    print("Error: './HamilJokerLaugh.mp4' not found. Make sure the file exists in the current directory.")

if __name__ == "__main__":
    # This part is just an example of how you might call it if this script were more complex.
    # For now, it will just run the playsound command above when the script is executed.
    print("Attempting to play sound...")

