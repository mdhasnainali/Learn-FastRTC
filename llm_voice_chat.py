import os

from fastrtc import (ReplyOnPause, Stream, get_stt_model, get_tts_model)
from openai import OpenAI

sambanova_client = OpenAI(
    api_key="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", base_url="https://api.sambanova.ai/v1"
)
stt_model = get_stt_model()
tts_model = get_tts_model()

def echo(audio):
    prompt = stt_model.stt(audio)
    response = sambanova_client.chat.completions.create(
        model="Meta-Llama-3.2-3B-Instruct",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=200,
    )
    prompt = response.choices[0].message.content
    for audio_chunk in tts_model.stream_tts_sync(prompt):
        yield audio_chunk

stream = Stream(ReplyOnPause(echo), modality="audio", mode="send-receive")

stream.ui.launch()