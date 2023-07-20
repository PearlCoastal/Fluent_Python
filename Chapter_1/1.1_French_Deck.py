'''
Author: FEIFEI SUN
Description: 
Detail: 
Date: 2023-07-19 15:37:31

'''
import collections

Card = collections.namedtuple('Card', ['rank', 'suit'])


class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                       for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    # ___getitem__ 方法将切片扫做交给了self._cards 列表
    def __getitem__(self, position):
        return self._cards[position]
    
    # 添加字符串打印方法，将对象用字符串形式表示，而不是<xxx Object at 0x10e100070>
    def __repr__(self) -> str:
        return 'Card(%r, %r)' % (self._cards.rank, self._cards.suit)


if __name__ == '__main__':

    beer_card = Card['7', 'diamonds']
    print(beer_card)

    # French Deck 类可以正常使用 len() 函数返回长度
    deck = FrenchDeck()
    print(len(deck))

    # 抽取特定的一张牌, 由 __getitem__() 方法提供
    print(deck[0])
    print(deck[-1])

    # 随机抽取一张纸牌
    from random import choice
    print("return 1 random card")
    print(choice(deck))

    # 切片操作
    print("slicing list")
    print(deck[:3])

    print("输出全部是 A 的卡牌")
    # 抽出第一张 A（索引为12），然后每隔 13 张牌拿一张牌
    print(deck[12::13])

    # 可迭代
    print("-----------迭代测试repr函数-----------")
    for card in deck:
        print(card)

    print("__contains__ 方法 通常是隐式的")
    print(Card('Q', 'hearts') in deck)
    
    print("-----------实现排序-----------")
    suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)
    
    def spades_high(card):
        rank_value = FrenchDeck.ranks.index(card.rank)
        return rank_value * len(suit_values) + suit_values[card.suit]
    
    for card in sorted(deck, key=spades_high):
        print(card)
        