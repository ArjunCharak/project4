import pygame
import keyboard
import time

def play_audio(file_path):
    pygame.mixer.init()
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

def main():
    audio_file_path = r'C:\Users\Aniket\Desktop\defence project\attack2t22wav-14511.mp3'

    while True:
        if keyboard.is_pressed('1'):
            print("Playing audio...")
            play_audio(audio_file_path)
            print("Audio finished playing.")

        time.sleep(0.1)

if __name__ == "__main__":
    main()
