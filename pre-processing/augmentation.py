import nlpaug.augmenter.word as naw

text = "The horse is galloping on the field."
aug = naw.SynonymAug(aug_src='wordnet')
augmented_text = aug.augment(text)

print(augmented_text)