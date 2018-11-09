from sklearn.base import BaseEstimator, TransformerMixin
import re
import unicodedata


class ReplaceTransformer(BaseEstimator, TransformerMixin):

    def __init__(self, src, dst):
        """
        Set source and destination.

        Args:
            src(str): Regular expression
            dst(str): destination character or word.
        """
        self.src = src
        self.dst = dst
        self.p = re.compile(self.src)

    def fit(self, x, y=None):
        return self

    def transform(self, X):
        return [self.p.sub(self.dst, x) for x in X]


def katakana_to_hiragana(text):
    """
    Replace Katakana[ァ-ヶ] to Hiragena.
    """
    d = {i: i - 0x60 for i in range(ord('ァ'), ord('ヶ') + 1)}
    return text.translate(d)


def hiragana_to_katakana(text):
    """
    Replace Hiragana[ぁ-ゖ] to Katakana.
    """
    d = {i: i + 0x60 for i in range(ord('ぁ'), ord('ゖ') + 1)}
    return text.translate(d)


def jpnum_to_num(text, kanji=True, zenkaku=True):
    """
    〇-九 -> 0-9 / ０−９ -> 0-9
    """
    d = {}
    if kanji:
        d.update({ord(s): ord(str(t))
                  for t, s in zip(range(0, 10), '〇一二三四五六七八九')})
    if zenkaku:
        d.update({ord(s): ord(str(t))
                  for t, s in zip(range(0, 10), '０１２３４５６７８９')})

    return text.translate(d)


def remove_emoji(text, dst=' '):
    """
    a🤗🤓🤔🤘🦁🤐b🤗🤖🤑c ->  a      b   c
    """
    return re.sub('[🌀-🧿]', dst, text)


def small_to_large(text):
    """
    ぁぃぅ -> あいう
    """
    d = {ord(s): ord(l) for s, l in
         zip('ぁぃぅぇぉゃゅょっァィゥェォャュョッ',
             'あいうえおやゆよつアイウエオヤユヨツ')}
    return text.translate(d)


def remove_yure(text):
    """
    思い切って揺れを削ぎ落とすやつ
    
    - [ー-]除去
    - [・]の除去
    """
    return re.sub(r'[-ー・]', '', text)


def num_to_zero(text):
    """
    数字を0揃え
    """
    return re.sub(r'[\d]', '0', text)


def basic_normalizer(text):
    """
    もとの意味を崩さない程度に正規化
    """
    # TODO 
    # text = unicodedata.normalize("NFKC", text)
    # text = re.sub(r'[\.,\r\n\t]', ' ', text)
    # text = remove_emoji(text)
    # 


def ml_normalizer():
    """
    tfidfやベクトル化するとき用にかなり表記をまとめる
    
    コメ正規化のあと分かち書きすると失敗するので、分かち書きしたあとにこの関数は実行する
    - 小文字:大文字化 ぁぃぅ -> あいう   
    """
    # TODO
