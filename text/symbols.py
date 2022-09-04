""" from https://github.com/keithito/tacotron """

"""
Defines the set of symbols used in text input to the model.

The default is a set of ASCII characters that works well for English or text that has been run through Unidecode. For other data, you can modify _characters. See TRAINING_DATA.md for details. """

from text import cmudict, pinyin

_pad = "_"
# _punctuation = "!'(),.:;? "
# _special = "-"
_nonalpha = " !\"',-.:;?؟َُِّٰٓٔ"
# _letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
_letters = "ABCDEFGHIJKLMNOPQRSTUVWYZabcdefghijklmnopqrstuvwxyzÄÖâäéöāăƙɓɗабвгдежзийклмнопрстуфхцчшщъыьэюяіғқңүұәөآؤئابتثجحخدذرزسشصضطظعغفقلمنويٹپچڈڑکگںھہیےაბგდევზთიკლმნოპჟრსტუფქღყშჩცძწჭხჯჰ"
_silences = ["@sp", "@spn", "@sil"]

# Prepend "@" to ARPAbet symbols to ensure uniqueness (some are the same as uppercase letters):
# _arpabet = ["@" + s for s in cmudict.valid_symbols]
# _pinyin = ["@" + s for s in pinyin.valid_symbols]

combined_phoneset = ['a', 'aj', 'aw', 'aː', 'ã', 'ãː', 'b', 'bʱ', 'bʲ', 'b̤', 'c', 'cʰ', 'ç', 'd', 'dz', 'dʒ', 'dʲ', 'dː', 'd̤', 'd̤ʒ̤', 'd̪', 'd̪ʱ', 'e', 'ej', 'eʰ', 'eː', 'ẽ', 'ẽː', 'f', 'fʲ', 'h', 'i', 'iː', 'ĩː', 'j', 'k', 'kʰ', 'kʲ', 'kʼ', 'l', 'lʲ', 'lː', 'l̪', 'm', 'mʲ', 'm̩', 'n', 'nʲ', 'nː', 'n̩', 'o', 'ow', 'oː', 'õː', 'p', 'pʰ', 'pʲ', 'pʼ', 'pː', 'q', 'qʼ', 'r', 'rʲ', 'r̩', 's', 'sʲ', 't', 'ts', 'tsʲ', 'tsʼ', 'tsː', 'tɕ', 'tʃ', 'tʃʰ', 'tʃʼ', 'tʰ', 'tʲ', 'tʼ', 'tː', 't̪', 't̪ʰ', 't̪ː', 'u', 'uː', 'ũ', 'ũː', 'v', 'vʲ', 'w', 'x', 'xʲ', 'y', 'yː', 'z', 'zʲ', 'zː', 'æ', 'æː', 'ð', 'ø', 'øː', 'ŋ', 'ɐ', 'ɑ', 'ɑː', 'ɑ̃ː', 'ɒ', 'ɒː', 'ɓ', 'ɔ', 'ɔ j', 'ɔː', 'ɕː', 'ɖ', 'ɖʱ', 'ɖ̤', 'ɗ', 'ə', 'ə̃', 'ə̯', 'ɛ', 'ɛː', 'ɛ̃ː', 'ɜ', 'ɜ˞', 'ɟ', 'ɠ', 'ɡ', 'ɡʱ', 'ɡ̤', 'ɣ', 'ɤ', 'ɦ', 'ɨ', 'ɪ', 'ɫ', 'ɫ ɫ', 'ɱ', 'ɲ', 'ɳ', 'ɸ', 'ɹ', 'ɹ̩', 'ɽ', 'ɽʱ', 'ɾ', 'ɾʲ', 'ʁ', 'ʂ', 'ʂ ʂ', 'ʃ', 'ʄ', 'ʈ', 'ʈʰ', 'ʉ', 'ʉː', 'ʊ', 'ʊ̃', 'ʋ', 'ʌ', 'ʎ', 'ʏ', 'ʒ', 'ʔ', 'ʕ', 'θ', 'χ']

_combined_phoneset = ["@" + s for s in combined_phoneset]

# Export all symbols:
symbols = (
    [_pad]
    # + list(_special)
    # + list(_punctuation)
    + list(_nonalpha)
    + list(_letters)
    # + _arpabet
    # + _pinyin

    + _combined_phoneset

    + _silences
)