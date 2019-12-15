import pytest, random

from my_classes import Bag, Player, ComputerPlayer, Card, ComputerCard


class TestBag:

    def test_eq(self):
        bag1 = Bag()
        bag2 = Bag()
        assert bag1 == bag2
        assert not (bag1 != bag2)
        assert bag1[0] == bag1.set[0]
        assert f'В мешке остались следующие боченки: {bag1.set}' == str(bag1)

class TestPlayer:

    def setup(self):
        self.player1 = Player('user', 2, 2)
        self.player2 = Player('user2', 2, 2)

    def teardown(self):
        pass

    def test_eq_player(self):
        self.player1.cards[0].can_play = False
        assert not(self.player1 == self.player2)

    def test_ne_player(self):
        self.player1.cards[0].can_play = False
        assert self.player1 != self.player2

    def test_str_player(self):
        ok_str = f'Игрок: {self.player1.name}, id: {self.player1.id}, кол-во карточек: {len(self.player1.cards)}'
        assert ok_str == str(self.player1)

    # сделаем тест с параметрами
    @pytest.mark.parametrize('x', [0, 1])
    def test_getitem(self, x):
        assert self.player1[x] == self.player1.cards[x].card_nums

class TestComputerPlayer:
    # для игрока-компьютера только один магический метод работает подругому, так что и проверим только его
    def test_str_pc_player(self):
        pc_player = ComputerPlayer('AI', 2, 2)
        ok_str = f'Игрок-компьютер: {pc_player.name}, id: {pc_player.id}, кол-во карточек: {len(pc_player.cards)}'
        assert ok_str == str(pc_player)

class TestCard:

    def setup(self):
        self.card1 = Card(3)
        self.card2 = Card(4)

    def teardown(self):
        pass

    def test_str_card(self):
        ok_str_card = f'Карточка: {self.card1.id}, содержимое: {self.card1.card_nums}'
        assert ok_str_card == str(self.card1)

    def test_eq_card(self):
        ok_num_1 = self.card1.card_nums.count('-')
        ok_num_2 = self.card2.card_nums.count('-')
        assert ok_num_1 == ok_num_2

    def test_ne_card(self):
        ok_num_1 = self.card1.card_nums.count('-')
        ok_num_2 = self.card2.card_nums.count('-')
        assert not (ok_num_1 != ok_num_2)

    # сделаем тест с параметрами
    @pytest.mark.parametrize('x', [i for i in range(15)])
    def test_getitem(self, x):
        assert self.card1[x] == self.card1.card_nums[x]
