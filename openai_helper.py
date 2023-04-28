import openai

from settings import OPENAI_API_KEY

openai.api_key = OPENAI_API_KEY

async def transcriptor(audio_file):
    # TODO: provide a language option
    # transcription = openai.Audio.transcribe("whisper-1", f, language=lang)
    transcription = openai.Audio.transcribe("whisper-1", audio_file)

    if transcription:
        return transcription
    else:
        return "Error transcribing..."

async def image_generator(prompt):
    response = openai.Image.create(
      prompt=prompt,
      n=1,
      size="1024x1024"
    )

    if response:
        return response['data'][0]['url']
    else:
        return "Error generating image..."
