import nlpaug.augmenter.word as naw

text = "The horse is galloping on the field."
aug = naw.SynonymAug(aug_src='wordnet')
augmented_text = aug.augment(text)

print(augmented_text)

# OR

from googletrans import Translator
import asyncio

async def main():
    translator = Translator()
    text = "The horse is galloping across the vast field."

    translated_text = await translator.translate(text, src='en', dest='fr')
    translated_text = translated_text.text
    back_translated_text = await translator.translate(translated_text, src='fr', dest='en')
    back_translated_text = back_translated_text.text
    print(back_translated_text)

asyncio.run(main())