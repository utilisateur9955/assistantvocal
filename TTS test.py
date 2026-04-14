import asyncio
import edge_tts
import vlc

async def parler(texte, fichier="output.mp3"):
    voix = "fr-FR-HenriNeural"
    communicate = edge_tts.Communicate(texte, voix)
    await communicate.save(fichier)

    player = vlc.MediaPlayer(fichier)
    player.play()

    # attendre la fin de lecture
    import time
    duration = 0
    while duration == 0:  # attendre que VLC charge la durée
        duration = player.get_length() / 1000
        await asyncio.sleep(0.1)
    await asyncio.sleep(duration)

asyncio.run(parler("User@9955"))