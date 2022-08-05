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

en_US_combined = ['ʉː', 'ʊ', 'ɑː', 'pʰ', 'ɚ', 'ʈʰ', 'ɑ̃ː', 'æ', 'ɛː', 't͡ʃ', 'nː', 'o', 'ɛ', 'ʒ', 'ʏ', 'z', 'b', 'ɡ', 'õː', 'tʃʼ', 'ɣ', 'dʲ', 't̪ː', 'p', 'ð', 'ɐ', 'ɫː', 'ɳ', 'ɝ', 'mʲ', 'd̪ᵊ', 'ũː', 'ɒ', 'm', 'v', 'ɒː', 'aw', 'pː', 'tː', 'l̪', 'ɽ', 'ĩː', 'c', 'ʔ', 'n', 'e', 't͡s', 'ɑ', 'cʰ', 'u', 'aj', 'k', 'kʰ', 'bʲ', 'pʲ', 'χ', 'ɛ̃ː', 'ɤ', 'dː', 'ɾ', 'q', 'd͡ʒʱ', 'ɦ', 'ɓ', 'ʉ', 'r', 'uː', 'd͡z', 'ç', 't̪', 'ɡʱ', 'ɔː', 'ej', 'kʼ', 'tʰ', 'tsː', 'ɖ', 'lː', 'tʃ', 'ʃ', 'ʕ', 'dz', 'ɪ', 'bʱ', 'd͡ʒ', 'eː', 'l', 'ɫ̩', 'ow', 'iː', 'tsʼ', 'aː', 'ɲ', 'ʃʰ', 'ts', 'ɟ', 'a', 'vʲ', 's', 'ʄ', 'm̩', 'eʱ', 'h', 'ɕː', 'ʋ', 't͡ʃʰ', 'oː', 'ʁ', 'ẽː', 'ʊ̃', 'ɱ', 'ə̯', 'd̪', 'qʼ', 'dʒ', 'ŋ', 'ə̃', 'ˈɾ', 'ɾʲ', 't̪ʰ', 'fʲ', 'ɠ', 'tʼ', 'd', 'ɽʱ', 'j', 'ɖʱ', 'pʼ', 'ʎ', 'ʈ', 'ə', 'ɔ', 'sʰ', 'n̩', 'f', 'ɹ', 'ɔj', 't', 'θ', 'x', 'tʲ', 'i', 'ɗ', 'ɸ', 'ɫ', 'zː', 'd̪ʱ', 'w']

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
