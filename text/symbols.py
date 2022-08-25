""" from https://github.com/keithito/tacotron """

"""
Defines the set of symbols used in text input to the model.

The default is a set of ASCII characters that works well for English or text that has been run through Unidecode. For other data, you can modify _characters. See TRAINING_DATA.md for details. """

from text import cmudict, pinyin

_pad = "_"
_punctuation = "\"!'(),.:;? "
_special = "-"
_weird = "“„…—՝«»։”–ʻʼ’`‘،۔؛"
_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
_silences = ["@sp", "@spn", "@sil"]

_letters_bg = "ашцйЖСсбШНАЩГхфняеВЧРдкчувгЯТлБЛозюпИМщЙДЕмъПжиКЗрХОт"
_letters_hy_AM = "պմդԼՇՄԺՂջ՞ՓեկԵտթՉնԾԲղՌծխիոՔհբքչփւԴճցԽԿԸօշԷԹԻՊՀՆյԱզլվռևէըՈՍՁսգձրՕաֆՎժԳՏ"
_letters_ka = "ვშმკრღჯაჭიელგნწდჰსჩჟოფბხუტთცყქზპძ"
_letters_kk = "ашңУйЖӘСсұбҚіШыАөхняІдкуӨгүТлБозюпИМщрДЕмПжКәиеқғОт"
_letters_sw = "â"
_letters_ur = "ھرجنٓئلآپبض‘ںاےڈؤ؟ٰظغوعزدٹخَّہمٔشتطفڑیذيِکثگچُسقصح"

# Prepend "@" to ARPAbet symbols to ensure uniqueness (some are the same as uppercase letters):
# _arpabet = ["@" + s for s in cmudict.valid_symbols]
# _pinyin = ["@" + s for s in pinyin.valid_symbols]

en_US_combined = ['a', 'aj', 'aw', 'aː', 'b', 'bʱ', 'bʲ', 'c', 'cʰ', 'd', 'dz', 'dʒ', 'dʲ', 'dː', 'd̪', 'd̪ʱ', 'd͡z', 'd͡ʒ', 'e', 'ej', 'eʱ', 'eː', 'f', 'fʲ', 'h', 'i', 'iː', 'j', 'k', 'kʰ', 'kʼ', 'l', 'lː', 'l̪', 'm', 'mʲ', 'm̩', 'n', 'nː', 'n̩', 'o', 'ow', 'oː', 'p', 'pʰ', 'pʲ', 'pʼ', 'pː', 'q', 'qʼ', 'r', 's', 'sʰ', 't', 'ts', 'tsʼ', 'tsː', 'tʃ', 'tʃʼ', 'tʰ', 'tʲ', 'tʼ', 'tː', 't̪', 't̪ʰ', 't̪ː', 't͡s', 't͡ʃ', 't͡ʃʰ', 'u', 'uː', 'v', 'vʲ', 'w', 'x', 'z', 'zː', 'æ', 'ç', 'ð', 'õː', 'ĩː', 'ŋ', 'ũː', 'ɐ', 'ɑ', 'ɑː', 'ɑ̃ː', 'ɒ', 'ɒː', 'ɓ', 'ɔ', 'ɔj', 'ɔː', 'ɕː', 'ɖ', 'ɖʱ', 'ɗ', 'ə', 'ə̃', 'ə̯', 'ɚ', 'ɛ', 'ɛː', 'ɛ̃ː', 'ɜ', 'ɟ', 'ɠ', 'ɡ', 'ɡʱ', 'ɣ', 'ɤ', 'ɦ', 'ɪ', 'ɫ', 'ɫː', 'ɫ̩', 'ɱ', 'ɲ', 'ɳ', 'ɸ', 'ɹ', 'ɽ', 'ɽʱ', 'ɾ', 'ɾʲ', 'ʁ', 'ʃ', 'ʃʰ', 'ʄ', 'ʈ', 'ʈʰ', 'ʉ', 'ʉː', 'ʊ', 'ʊ̃', 'ʋ', 'ʎ', 'ʏ', 'ʒ', 'ʔ', 'ʕ', 'θ', 'χ', 'ẽː']

_en_US_combined = ["@" + s for s in en_US_combined]

# Export all symbols:
symbols = (
    [_pad]
    + list(_special)
    + list(_punctuation)
    + list(_letters)

    + list (_weird)
    + list(_letters_bg)
    + list(_letters_hy_AM)
    + list(_letters_ka)
    + list(_letters_kk)
    + list(_letters_sw)
    + list(_letters_ur)

    + _en_US_combined

    # + _arpabet
    # + _pinyin
    + _silences
)
