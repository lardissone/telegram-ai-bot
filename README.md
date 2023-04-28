# Telegram AI Bot

A Telegram bot that uses AI to transcribe audio messages to text and generate images using OpenAI API.

## Installation

1. Clone the repository
2. Copy `settings.example.py` to `settings.py`
3. Fill in the required values in `settings.py`. See  [Settings](#settings) for more information.
4. Run `docker compose up -d`

## Settings

| Name | Description |
| --- | --- |
| `OPENAI_API_KEY` | OpenAI API key. You can get it from [here](https://platform.openai.com/account/api-keys). |
| `TELEGRAM_BOT_TOKEN` | Telegram bot token. You can get it from [BotFather](https://t.me/BotFather). |
| `TELEGRAM_CHAT_IDS` | A list of all users allowed to talk with the bot. You can get the chat id using [IDBot](https://t.me/myidbot). |

## Usage

### Audio transcription

1. Send an audio message to the bot (you can also forward an audio message from another chat)
2. Wait for the bot to transcribe the audio message

### Image generation

1. Send a message to the bot with the text `/image {prompt}`, where `{prompt}` is the prompt for the image generation
2. Wait for the bot to generate the image

## License

This project is licensed under the MIT License.

```
MIT License

Copyright (c) 2023 Leandro Ardissone

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```
