import random


class Bag:
    '''
    по правилам игры есть мешок с боченками от 1 до 90
    из него вытягивают боченки случайным образом
    '''

    def __init__(self):
        # закидываем все боченки в мешок
        self.set = random.sample(range(1, 91), 90)
        # сразу определяем сколько в мешке боченков
        self.barrel_count = len(self.set)

    def shuffle(self):
        # перетосовываем мешок (трясем чтобы было более случайно)
        random.shuffle(self.set)

    def choice(self):
        # выбираем один боченок из имеющихся в мешке
        # проверим есть ли в мешке боченки
        if self.barrel_count:
            # сперва перемешиваем мешок
            self.shuffle()
            # теперь можем доставать послединй боченок
            # удаляет последний элемент и возвращает его
            result = self.set.pop()
            # не забываем что количество боченков изменилось
            self.barrel_count = len(self.set)
            return result
        # если боченки кончились
        raise Exception('Нечего вытаскивать из мешка :(')


class Player:
    '''
    в игре может быть несколько игроков. у каждого игрока может быть больше 1 карточки
    '''

    def __init__(self, name, id, cards_count=1):
        # имя игрока
        self.name = name
        # добавил id игрока, на случай если имена будут совпадать
        self.id = id + 1
        # дадим ему столько карточек сколько надо
        self.cards = [Card(i) for i in range(cards_count)]
        # определим может ли игрок продолжать играть
        self.can_play = True
        # определим количество подебивших карточек у игрока
        self.winner_cards = 0 # хотел определять победителя по количеству победивших карточек, но передумал

    def show(self):
        # показывает информацию о игроке
        print(f'Игрок номер {self.id}: {self.name}')

    def check_can_play(self):
        # проверка может игрок продолжать играть или нет
        # предположим что у игрока уже закончились игровые карточки
        self.can_play = False
        # делаем проверку всех карточек игрока
        for card in self.cards:
            if card.can_play:
                # если хотя бы одна карточка может играть, то и игрок может играть
                self.can_play = True

    # def check_cards(self):
    #     # тут проверяем все карточки, будем зачеркивать или нет
    # принято решение реализовать иначе, чтобы не было взаимодействие с консолью из класса



class Card:
    '''
    класс игровых карточек
    '''

    def __init__(self, i):
        # у каждой карточки игрока свой номер
        self.id = i + 1 # тут делаем +1 так как в списках индексы с 0 а в реальном мире с 1
        # сразу определим может карточка играть дальше или нет
        self.can_play = True
        # изначально карточка не может быть победившей
        self.winner = False
        # на карточке должно быть 15 разных цифр от 1 до 90
        self.card_nums = random.sample(range(1, 91), 15)

        # в карточке 27 позиций (3 строки по 9 полей), в каждой строке по 5 цифр
        # определеяем места для цифр на карточке, они должны быть не изменны
        self._box = random.sample(range(0, 9), 5) + random.sample(range(9, 18), 5) + random.sample(range(18, 27), 5)

        # мастам надо сопоставить числа, словарь подойдет
        # сперва по всем позициям делаем пропуски
        self._num_dict = {key: '•' for key in range(27)}
        # в позиции с цифрами записываем значения цифр
        for i in range(15):
            self._num_dict[self._box[i]] = self.card_nums[i]

    def show(self):
        print(f'карточка номер {self.id}')
        # print(self.card_nums)
        # вывод карточки с учетом расположения цифр в карточке
        for i in range(9):
            print(self._num_dict[i], end='\t')
        print()
        for i in range(9, 18):
            print(self._num_dict[i], end='\t')
        print()
        for i in range(18, 27):
            print(self._num_dict[i], end='\t')
        print()
        # if self.can_play:
        #     print('Карточка может играть')
        # else:
        #     print('Карточка НЕ может больше играть')

    def check_win(self):
        # проверка победила карточка или нет
        result = True
        for num in self.card_nums:
            if num != '-':
                result = False
        self.winner = result

    def check(self, num, answer):
        # проверяем карточку на наличие вытащенного боченка с цифрой
        # если карточка может играть
        if self.can_play:
            # если номер есть в карточке
            if num in self.card_nums:
                # проверим что нам ответил игрок
                if answer == 'y':
                    # заменяем его на '-'
                    index = self.card_nums.index(num)
                    self.card_nums[index] = '-'
                    # обновим и даныне в словаре
                    self._num_dict[self._box[index]] = self.card_nums[index]
                    # тут сразу можно проверить победила карточка или нет
                    self.check_win()
                    print('Номер зачеркнут, карточка выглядит так:')
                    self.show()
                else:
                    # номер есть в карточке но игрок его не зачеркивает
                    # карточка проигрывает
                    self.can_play = False
                    print('Вы ошиблись, карточка проигрывает..')
            else:
                # проверим что нам ответил игрок
                if answer == 'y':
                    # номера нет в карточке, но игрок чтото зачеркивает
                    # карточка проигрывает
                    self.can_play = False
                    print('Вы ошиблись, карточка проигрывает..')
                else:
                    print('Ничего не зачеркиваем, карточка выглядит так:')
                    self.show()

class ComputerPlayer(Player):
    '''
    класс игрока-компьютера
    '''
    def __init__(self, name, id, cards_count=1):
        # берем все то же самое что было у обычного игрока
        Player.__init__(self, name, id, cards_count)
        # только дадим компьютерные карточки вместо обычных
        self.cards = [ComputerCard(i) for i in range(cards_count)]

    def show(self):
        # показывает информацию о игроке-компьютере
        print(f'Компьютер номер {self.id}: {self.name}')


class ComputerCard(Card):
    '''
    класс карточек компьютера
    '''
    def check(self, num, answer=''):
        # хотел не вписывать параметр answer
        # но была ошибка сигнатуры родительского метода.
        # видимо количество папамтров нельзя менять.
        # переопределяем метод проверки, так как у компьютера мы не будем спрашивать, он не ощибается
        answer = 'y' if num in self.card_nums else 'n'
        # проверяем карточку на наличие вытащенного боченка с цифрой
        # если карточка может играть
        if self.can_play:
            # если номер есть в карточке
            if num in self.card_nums:
                # проверим что нам ответил игрок
                if answer == 'y':
                    # заменяем его на '-'
                    index = self.card_nums.index(num)
                    self.card_nums[index] = '-'
                    # обновим и даныне в словаре
                    self._num_dict[self._box[index]] = self.card_nums[index]
                    # тут сразу можно проверить победила карточка или нет
                    self.check_win()
                    print('Номер зачеркнут, карточка выглядит так:')
                    self.show()
                else:
                    # номер есть в карточке но игрок его не зачеркивает
                    # карточка проигрывает
                    self.can_play = False
                    print('Вы ошиблись, карточка проигрывает..')
            else:
                # проверим что нам ответил игрок
                if answer == 'y':
                    # номера нет в карточке, но игрок чтото зачеркивает
                    # карточка проигрывает
                    self.can_play = False
                    print('Вы ошиблись, карточка проигрывает..')
                else:
                    print('Ничего не зачеркиваем, карточка выглядит так:')
                    self.show()

# немного тестов
if __name__ == '__main__':
    abra = Bag()
    abra.shuffle()
    q = abra.choice()
    print()
    player = Player('Max', 0)
    player.show()
    player.cards[0].show()
    player.cards[0].check(player.cards[0].card_nums[1],'y')

    computer_player = ComputerPlayer('Umbrella', 0)
    computer_player.show()
    computer_player.cards[0].show()
    computer_player.cards[0].check(computer_player.cards[0].card_nums[1])

    print()

    print(computer_player.cards[0].winner)