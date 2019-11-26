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
            # не заываем что количество боченков изменилось
            self.barrel_count = len(self.set)
            return result
        # если боченки кончились
        raise Exception('Нечего вытаскивать из мешка :(')


class Player:
    '''
    в игре может быть несколько игроков. у каждого игрока может быть больше 1 карточки
    '''

    def __init__(self, name, cards_count=1):
        # имя игрока
        self.name = name
        # дадим ему столько карточек сколько надо
        self.cards = [Card() for i in range(cards_count)]
        # определим может ли игрок продолжать играть
        self.can_play = True
        # определим количество подебивши карточек у игрока
        self.winner_cards = 0

    def check_cards(self):
        # проверка может игрок продолжать играть или нет
        # предположим что у игрока уже закончились игровые карточки
        self.can_play = False
        # делаем проверку всех карточек игрока
        for card in self.cards:
            if card.can_play:
                # если хотя бы одна карточка может играть, то и игрок может играть
                self.can_play = True


class Card:
    '''
    класс игровых карточек
    '''

    def __init__(self, i):
        # у каждой карточки игрока свой номер
        self.id = i + 1
        # сразу определим может карточка играть дальше или нет
        self.can_play = True
        # изначально карточка не может быть победившей
        self.winner = False
        # на карточке должно быть 15 разных цифр от 1 до 90
        self.card_nums = sample(range(1, 91), 15)
        # TODO реализовать случайное положение цифр на карточке

    def check_card(self, num, answer):
        # проверяем карточку на наличие вытащенного боченка с цифрой
        # если карточка может играть
        if self.can_play:
            # если номер есть в карточке
            if num in self.card_nums:
                # заменяем его на '-'
                self.card_nums[self.card_nums.index(num)] = '-'


if __name__ == '__main__':
    abra = Bag()
    print(abra.set)
    abra.shuffle()
    print(abra.set)
    q = abra.choice()
    print(q)
    print(len(abra.set))
