from my_classes import Bag
from functions_for_loto import hello_func, bye_func, wanna_play, create_players, create_players_pc, continue_game

# собственно сам процесс игры
hello_func()

choice = wanna_play()

while choice:
    try:
        num_players = int(input('Введите количество игроков-людей:'))
    except ValueError:
        print('Введите положительное число')

    try:
        num_players_pc = int(input('Введите количество игроков-компьютеров:'))
    except ValueError:
        print('Введите положительное число')

    players = create_players(num_players)
    players_pc = create_players_pc(num_players_pc)

    # создаем мешок с боченками
    bag = Bag()

    # создадим список победителей. когда в нем ктонить появится то игра закончится
    winners = []

    # смотрим есть ли победитель и есть ли игроки с карточками которые могут играть
    while continue_game(players, players_pc, winners):
        print(f' В мешке {bag.barrel_count} боченков!')
        print('Трясем мешок!!')
        bag.shuffle()
        barrel = bag.choice()
        print(f'Вытаскиваем из мешка боченок с номером {barrel}')

        # ходят живые игроки поочереди, если они есть
        if players != None:
            for player in players:
                if player.can_play:
                    player.show()
                    print(len(player.cards))
                    for card in player.cards:
                        if card.can_play:
                            card.show()
                            answer = input(f'Из мешка был вытащен боченок номер {barrel}, хотите зачеркнуть в нарточке?(y/n)')
                            card.check(barrel, answer)
                            card.check_win()
                            if card.winner:
                                winners.append(f'Победил игрок номер {player.id}: {player.name}, c карточкой номер {card.id}')
                            print()

        # ходят игроки-компьютеры поочереди, если они есть
        if players_pc != None:
            for player in players_pc:
                if player.can_play:
                    player.show()
                    for card in player.cards:
                        if card.can_play:
                            card.show()
                            print(f'Из мешка был вытащен боченок номер {barrel}')
                            card.check(barrel)
                            card.check_win()
                            if card.winner:
                                winners.append(
                                    f'Победил игрок-компьютер номер {player.id}: {player.name}, c карточкой номер {card.id}')
                            print()
    # выводим победителей
    for winner in winners:
        print(winner)
    # спрашиваем будет ли еще одна игра
    choice = wanna_play()

bye_func()