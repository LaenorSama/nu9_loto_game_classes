import pytest, random

from my_classes import Bag, Player, ComputerPlayer, Card, ComputerCard

# тестируем класс мешка Bag()
class TestBag:

    def setup(self):
        self.bag = Bag()

    def teardown(self):
        pass

    def test_set(self):
        # проверяем создается ли мешок
        # ассерт пройдет если будет не пустой список
        assert self.bag.set
        # проверяем количество боченков, должно совпадать с длиной списка
        assert self.bag.barrel_count == len(self.bag.set)
        # все боченки так же должны быть в диапазоне от 1 до 90
        set_result = True
        for item in self.bag.set:
            if not (item >= 1 and item <= 90):
                set_result = False
        assert set_result

    def test_shyffle(self):
        # проверим перемешивание
        bag_old = self.bag.set
        barrel_count_old = self.bag.barrel_count
        self.bag.shuffle()
        # количество боченков после перемешивания не должно измениться
        assert barrel_count_old == self.bag.barrel_count
        # боченки должны остаться те же самые, и количество тоже не изменится
        shuffle_result = list(set(bag_old) & set(self.bag.set))
        assert barrel_count_old == len(shuffle_result)
        assert barrel_count_old == self.bag.barrel_count

    def test_choice(self):
        # запомним сколько было боченков в мешке
        barrel_count_old = self.bag.barrel_count
        # проверяем что возвращается один боченок из диапазона от 1 до 90
        choise_result = self.bag.choice()
        assert choise_result >= 1 and choise_result <= 90
        # проверим уменьшилось ли количество боченков на 1
        assert barrel_count_old == self.bag.barrel_count + 1
        # смоделируем ситуацию когда в мешке нет боченков
        self.bag.set= []
        self.bag.barrel_count = 0
        with pytest.raises(Exception):
            # если сейчас попробуем вытащить из мешка что-нибудь, то должна быть ошибка
            self.bag.choice()

# тестируем класс игрока Player()
class TestPlayer:

    def setup(self):
        self.player = Player('name', 3, 3)

    def teardown(self):
        pass

    def test_init(self):
        # првоеряем все ли определилось при инициализации игрока
        assert self.player.name == 'name'
        assert self.player.id == 3 + 1
        assert len(self.player.cards) == 3
        # проверим тип карточек
        assert type(self.player.cards[0]) == Card
        assert self.player.can_play == True
        assert self.player.winner_cards == 0

# тестируем класс игрока-компьютера ComputerPlayer()
class TestComputerPlayer:

    def setup(self):
        self.pc_player = ComputerPlayer('AI', 3, 3)

    def teardown(self):
        pass

    def test_init(self):
        # првоеряем все ли определилось при инициализации
        # так как класс наследовался от уже протестированного класса, то закоментил то, что уже проверено
        # assert self.pc_player.name == 'AI'
        # assert self.pc_player.id == 3 + 1
        assert len(self.pc_player.cards) == 3
        # проверим тип карточек
        assert type(self.pc_player.cards[0]) == ComputerCard
        # assert self.pc_player.can_play == True
        # assert self.pc_player.winner_cards == 0

# тестируем класс карточек
class TestCard:

    def setup(self):
        self.card = Card(3)

    def teardown(self):
        pass

    def test_init(self):
        # првоеряем все ли определилось при инициализации карточки
        assert self.card.id == 3 + 1
        assert self.card.can_play == True
        assert self.card.winner == False
        # количество цифр в карточке
        assert len(self.card.card_nums) == 15
        # првоерим нет ли одинаковых цифр в карточке
        assert len(list(set(self.card.card_nums))) == 15
        # количество мест под номера на карточке
        assert len(self.card._box) == 15
        # проверим нет ли одинаковых мест под цифры
        assert len(list(set(self.card._box))) == 15
        # проверим помещается ли цифра на свое место в карточке
        assert self.card.card_nums[0] == self.card._num_dict[self.card._box[0]]
        # проверим сколько всего мест на карточке
        assert len(self.card._num_dict.keys()) == 27

    def test_check_win(self):
        # проверим выиграла карточка или нет
        self.card.card_nums = ['-' for i in range(15)]
        self.card.check_win()
        assert self.card.winner

    def test_check(self):
        # проверяем верно ли срабатывает когда игроки ошибаются

        num = 0
        answer = 'y'
        self.card.check(num, answer)
        # 0 в карточке быть не может, но игрок зачеркивает, поэтому карточка должна проиграть
        assert self.card.can_play == False

        # для следующего теста вернем как было
        self.card.can_play = True

        num = self.card.card_nums[0]
        answer = 'n'
        self.card.check(num, answer)
        # берем номер из карточки под номером 0, но игрок не зачеркивает, значит карточка проигрывает
        assert self.card.can_play == False

        # для следующего теста вернем как было
        self.card.can_play = True

        # проверим верно ли срабатывает когда игроки не ошибаются

        num = 0
        answer = 'n'
        self.card.check(num, answer)
        # 0 в карточке быть не может, но игрок ничего не зачеркивает, поэтому карточка не проигрывает
        assert self.card.can_play == True

        # для следующего теста вернем как было
        self.card.can_play = True

        num = self.card.card_nums[0]
        answer = 'y'
        self.card.check(num, answer)
        # берем номер из карточки под номером 0, но игрок зачеркивает, значит карточка не проигрывает
        assert self.card.can_play == True
        # так же у карточке должен зачеркнуться номер [0]
        assert self.card.card_nums[0] == '-'
        # ну и проверим на том ли месте его зачеркнули
        assert self.card._num_dict[self.card._box[0]] == '-'


class TestComputerCard(TestCard):
    # сделаем тесты для карточки-компьютера наследованием
    # соответственно переделаем сетап
    def setup(self):
        self.card = ComputerCard(3)

    def teardown(self):
        pass

    # переопределяем тест
    def test_check(self):
        # проверяем верно ли срабатывает когда номера нет в карточке
        num = 0
        self.card.check(num)
        # 0 в карточке быть не может, но пк-игрок не ошибается
        assert self.card.can_play == True

        # для следующего теста вернем как было
        self.card.can_play = True

        num = self.card.card_nums[0]
        self.card.check(num)
        # берем номер из карточки под номером 0, пк-игрок зачеркивает
        assert self.card.can_play == True
        # так же у карточке должен зачеркнуться номер [0]
        assert self.card.card_nums[0] == '-'
        # ну и проверим на том ли месте его зачеркнули
        assert self.card._num_dict[self.card._box[0]] == '-'