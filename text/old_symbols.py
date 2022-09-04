""" from https://github.com/keithito/tacotron """

"""
Defines the set of symbols used in text input to the model.

The default is a set of ASCII characters that works well for English or text that has been run through Unidecode. For other data, you can modify _characters. See TRAINING_DATA.md for details. """

from text import cmudict, pinyin

_pad = "_"
_punctuation = "\"!'(),.:;? "
_special = "-"
_weird = "“„…—՝«»։”–ʻʼ’`‘،۔؛"
_weird_hindi = "।"
_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
_silences = ["@sp", "@spn", "@sil"]

_letters_ru = 'ЭБюхшимКЖРейГЦШвткфЛДуЧчоПъХЗпыИбэЩаОнВрТжЕМгзНСФЮсяАьцщЯУдл'

_letters_bg = "ашцйЖСсбШНАЩГхфняеВЧРдкчувгЯТлБЛозюпИМщЙДЕмъПжиКЗрХОт"
_letters_hy_AM = "պմդԼՇՄԺՂջ՞ՓեկԵտթՉնԾԲղՌծխիոՔհբքչփւԴճցԽԿԸօշԷԹԻՊՀՆյԱզլվռևէըՈՍՁսգձրՕաֆՎժԳՏ"
_letters_ka = "ვშმკრღჯაჭიელგნწდჰსჩჟოფბხუტთცყქზპძ"
_letters_kk = "ашңУйЖӘСсұбҚіШыАөхняІдкуӨгүТлБозюпИМщрДЕмПжКәиеқғОт"
_letters_sw = "â"
_letters_ur = "ھرجنٓئلآپبض‘ںاےڈؤ؟ٰظغوعزدٹخَّہمٔشتطفڑیذيِکثگچُسقصح"

# Prepend "@" to ARPAbet symbols to ensure uniqueness (some are the same as uppercase letters):
# _arpabet = ["@" + s for s in cmudict.valid_symbols]
# _pinyin = ["@" + s for s in pinyin.valid_symbols]

# en_US
en_US_combined = ['a', 'aj', 'aw', 'aː', 'b', 'bʱ', 'bʲ', 'c', 'cʰ', 'd', 'dz', 'dʒ', 'dʲ', 'dː', 'd̪', 'd̪ʱ', 'd͡z', 'd͡ʒ', 'e', 'ej', 'eʱ', 'eː', 'f', 'fʲ', 'h', 'i', 'iː', 'j', 'k', 'kʰ', 'kʼ', 'l', 'lː', 'l̪', 'm', 'mʲ', 'm̩', 'n', 'nː', 'n̩', 'o', 'ow', 'oː', 'p', 'pʰ', 'pʲ', 'pʼ', 'pː', 'q', 'qʼ', 'r', 's', 'sʰ', 't', 'ts', 'tsʼ', 'tsː', 'tʃ', 'tʃʼ', 'tʰ', 'tʲ', 'tʼ', 'tː', 't̪', 't̪ʰ', 't̪ː', 't͡s', 't͡ʃ', 't͡ʃʰ', 'u', 'uː', 'v', 'vʲ', 'w', 'x', 'z', 'zː', 'æ', 'ç', 'ð', 'õː', 'ĩː', 'ŋ', 'ũː', 'ɐ', 'ɑ', 'ɑː', 'ɑ̃ː', 'ɒ', 'ɒː', 'ɓ', 'ɔ', 'ɔj', 'ɔː', 'ɕː', 'ɖ', 'ɖʱ', 'ɗ', 'ə', 'ə̃', 'ə̯', 'ɚ', 'ɛ', 'ɛː', 'ɛ̃ː', 'ɜ', 'ɟ', 'ɠ', 'ɡ', 'ɡʱ', 'ɣ', 'ɤ', 'ɦ', 'ɪ', 'ɫ', 'ɫː', 'ɫ̩', 'ɱ', 'ɲ', 'ɳ', 'ɸ', 'ɹ', 'ɽ', 'ɽʱ', 'ɾ', 'ɾʲ', 'ʁ', 'ʃ', 'ʃʰ', 'ʄ', 'ʈ', 'ʈʰ', 'ʉ', 'ʉː', 'ʊ', 'ʊ̃', 'ʋ', 'ʎ', 'ʏ', 'ʒ', 'ʔ', 'ʕ', 'θ', 'χ', 'ẽː']

_en_US_combined = ["@" + s for s in en_US_combined]

# ru
ru_combined = ['b', 'ɛː', 'zː', 'ɓ', 'ɨ', 'χ', 'e', 'xʲ', 'z', 'i', 'sʰ', 'pʼ', 'x', 'iː', 'm', 'ɾ', 't', 'bʱ', 'dʒ', 'ɛ', 'ʂ', 'v', 'ʊ̃', 'ɪ', 'θ', 'k', 'dː', 'tʃʰ', 'zʲ', 'ɱ', 'ʒ', 'tsʼ', 'kʲ', 'pː', 'ɤ', 'eʰ', 'ɔ', 'õː', 'ɛ̃ː', 'tʼ', 'fʲ', 'ɑ̃ː', 'ɠ', 'ʁ', 'ʂ ʂ', 'd', 'j', 'ts', 'uː', 'ʈʰ', 'h', 'd̪', 'nʲ', 'ə̯', 'u', 'ʄ', 'tsː', 'd̪ʱ', 'pʲ', 'l̪', 'ʔ', 'ɸ', 'tʰ', 'nː', 'ẽː', 'oː', 'ɦ', 'ɑː', 'ɖ', 'ð', 'ũː', 'ʋ', 'ʃʰ', 'ɑ', 's', 'ʏ', 'rʲ', 'ʊ', 'n', 'ɔː', 'ʈ', 'eː', 'vʲ', 'ɽ', 'tʲ', 'ə', 'ɣ', 'ɲ', 'lː', 't̪ː', 'ɫ', 'r', 'kʼ', 'bʲ', 'ĩː', 'ɕː', 'ɳ', 'c', 'p', 'ɡʱ', 'pʰ', 'ɗ', 't̪ʰ', 'ɽʱ', 'tː', 'ʃ', 'dʲ', 'aː', 'w', 'tʃ', 'tʃʼ', 'æ', 'kʰ', 'ɖʱ', 'a', 'tɕ', 'lʲ', 'ŋ', 'ə̃', 'q', 'ɡ', 't̪', 'ʕ', 'dz', 'sʲ', 'l', 'qʼ', 'dʒʱ', 'o', 'f', 'mʲ', 'ɒ', 'tsʲ']

_ru_combined = ["@" + s for s in ru_combined]

# hi
hi_combined = ['ɗ', 'dː', 'ɑ', 'd̤', 'dz', 'j', 'ɖʱ', 'kʰ', 'ũː', 'ɛː', 'dʒ', 'nː', 'ʂ', 'ɖ', 'm', 'd̪', 'pʰ', 's', 'ɱ', 'w', 'b̤', 'ɓ', 'aː', 'ɪ', 'b', 'ɤ', 'tʼ', 'ɽʱ', 'p', 'iː', 'ə̃', 'k', 'ɦ', 'u', 'ɑː', 'ɒ', 'ẽː', 'ɫ', 'ĩː', 'eʰ', 'tsː', 'ts', 'n', 'tː', 'i', 'c', 'qʼ', 'ũ', 'bʱ', 'ɖ̤', 'ɡ̤', 't', 'θ', 'ɔː', 'ʕ', 'ɾ', 'tʃʰ', 'v', 't̪ʰ', 'ʊ̃', 'pː', 'ɠ', 'pʼ', 'q', 'tsʼ', 't̪', 'æ', 'ɡ', 'ð', 'ɛ̃ː', 'uː', 'χ', 'ʃ', 'ẽ', 'a', 'l̪', 'tʃ', 'tʰ', 'ʈʰ', 'ə̯', 'z', 'd̤ʒ̤', 'l', 'ʄ', 'ɸ', 'ɛ', 'd̪ʱ', 'æː', 'tʃʼ', 'ɹ', 'ʈ', 'ɑ̃ː', 'h', 'ŋ', 'd', 't̪ː', 'ʊ', 'x', 'ɹ̩', 'ãː', 'ʁ', 'ʏ', 'ə', 'kʼ', 'ʃʰ', 'o', 'ɲ', 'f', 'e', 'ʔ', 'ɳ', 'dʒ', 'eː', 'ʌ', 'õː', 'r̩', 'sʰ', 'zː', 'ʒ', 'oː', 'ɕː', 'ã', 'ɔ', 'r', 'ɽ', 'ɡʱ', 'lː', 'ʋ', 'ɣ']

_hi_combined = ["@" + s for s in hi_combined]

# Export all symbols:
symbols = (
    [_pad]
    + list(_special)
    + list(_punctuation)
    + list(_letters)

    + list (_weird)
    + list (_weird_hindi)

    + list(_letters_bg)
    + list(_letters_hy_AM)
    + list(_letters_ka)
    + list(_letters_kk)
    + list(_letters_sw)
    + list(_letters_ur)

    + list(_letters_ru) # ru

    # + _en_US_combined # en_US
    # + _ru_combined # ru
    + _hi_combined # hi

    # + _arpabet
    # + _pinyin
    + _silences
)
