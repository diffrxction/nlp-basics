import asyncio
from langdetect import detect
from googletrans import Translator

text = "Bonjour, tour de France"
language = detect(text)
print(language)

async def main():
    translator = Translator()
    translated = await translator.translate(text, src='fr', dest='en')
    print(translated.text)

asyncio.run(main=main())