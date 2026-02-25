## Installation

```bash
pip install fastrtc
```

to use built-in pause detection (see [ReplyOnPause](https://fastrtc.org/userguide/audio/#reply-on-pause)), and text to speech (see [Text To Speech](https://fastrtc.org/userguide/audio/#text-to-speech)), install the `vad` and `tts` extras:

```bash
pip install "fastrtc[vad, stt, tts]"
```

## Quickstart
Import the Stream class and pass in a handler. The Stream has three main methods:

- .ui.launch(): Launch a built-in UI for easily testing and sharing your stream. Built with Gradio.
- .fastphone(): Get a free temporary phone number to call into your stream. Hugging Face token required.
- .mount(app): Mount the stream on a FastAPI app. Perfect for integrating with your already existing production system.

