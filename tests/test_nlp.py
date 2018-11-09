from ml_collection import nlp


def test_ReplaceTransformer():
    obj = nlp.ReplaceTransformer('[\d]', '0')
    src = ['123１２３']
    target = obj.transform(src)
    expected = ['000000']
    assert target == expected


def test_katakana_to_hiragana():
    src = 'あいうアイウｱｲｳ'
    target = nlp.katakana_to_hiragana(src)
    expected = 'あいうあいうｱｲｳ'
    assert target == expected


def test_hiragana_to_katakana():
    src = 'あいうアイウｱｲｳ'
    target = nlp.hiragana_to_katakana(src)
    expected = 'アイウアイウｱｲｳ'
    assert target == expected


def test_jpnum_to_num():
    src = '09０９〇九'
    target = nlp.jpnum_to_num(src)
    expected = '090909'
    assert target == expected


def test_small_to_large():
    src = 'ぁぃぅぇぉゃゅょァィゥェォャュョ'
    target = nlp.small_to_large(src)
    expected = 'あいうえおやゆよアイウエオヤユヨ'
    assert target == expected


def test_remove_yure():
    src = 'プール　・　シャンプー'
    target = nlp.remove_yure(src)
    expected = 'プル　　シャンプ'
    assert target == expected


def test_num_to_zero():
    src = '１２３123'
    target = nlp.num_to_zero(src)
    expected = '000000'
    assert target == expected


def test_remove_emoji():
    src = 'a🤗🤓🤔🤘🦁🤐b🤗🤖🤑c'
    target = nlp.remove_emoji(src)
    expected = 'a      b   c'
    assert target == expected
