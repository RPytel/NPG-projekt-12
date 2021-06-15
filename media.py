import simpleaudio as sa

def play_sound() -> None:
    filename = 'windsound.wav'
    wave_obj = sa.WaveObject.from_wave_file(filename)
    play_obj = wave_obj.play()
    play_obj.wait_done()