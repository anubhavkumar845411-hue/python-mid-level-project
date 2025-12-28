import asyncio
import edge_tts
import pygame
import os

VOICE = "en-GB-SoniaNeural"
OUTPUT_FILE = "data.mp3"

async def _speak_async(text):
    communicate = edge_tts.Communicate(text=text, voice=VOICE)
    await communicate.save(OUTPUT_FILE)

def speak(text):
    try:
        asyncio.run(_speak_async(text))

        pygame.mixer.init()
        pygame.mixer.music.load(OUTPUT_FILE)
        pygame.mixer.music.play()

        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)

    except Exception as e:
        print("TTS Error:", e)

    finally:
        pygame.mixer.music.stop()
        pygame.mixer.quit()
        if os.path.exists(OUTPUT_FILE):
            os.remove(OUTPUT_FILE)
