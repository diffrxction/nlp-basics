import re

def detect_noise(text):
    noise_pattern = r'[^a-zA-Z0-9\s]'
    noisy_characters = re.findall(noise_pattern, text)

    if noisy_characters:
        print(f"Detected noisy characters: {noisy_characters}")
    else:
        print("No noise detected!")

text = "I love NLP! #AI @2025 :)"
detect_noise(text)