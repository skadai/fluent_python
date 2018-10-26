import collections
from math import hypot

# 使用魔法方法至少两个好处
#  1. 用户简单调用
#  2. 和系统函数如 random 的无缝衔接
Card = collections.namedtuple('Card', ['rank', 'suit'])
suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)


def spades_high(card):
    rank_value = FrenchDeck.ranks.index(card.rank)
    return rank_value * len(suit_values) + suit_values[card.suit]


class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        # in reversed关键字可用, 但是有contains会更好
        return self._cards[position]


class Vector:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __repr__(self):
        # 此处r字符限制了只能传入数字不能是字符串
        return 'Vector(%r, %r)' % (self.x, self.y)

    def __abs__(self):
        return hypot(self.x, self.y)

    def __bool__(self):
        # __bool 和 __len__会是的自定义布尔生效
        return bool(abs(self))

    def __add__(self, other):
        # infix 操作符号只能新建对象不能修改已有对象
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)


if __name__ == '__main__':
    s = FrenchDeck()
    for card in sorted(s, key=spades_high):
        print(card)