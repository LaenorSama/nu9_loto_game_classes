from my_classes import Player, ComputerPlayer
def hello_func():
    print('Добро пожаловать!')
    print('Это всеми любимая игра лото!')

def bye_func():
    print('Хорошего дня!')

def wanna_play():
    result = input('Хотите играть? (y/n)')
    if result == 'y':
        result = True
    else:
        result = False
    return result

def create_players(num_players):
    players = []
    # создаем игроков людей
    for i in range(num_players):
        name = input(f'Введите имя игрока {i + 1}:')
        id = i
        cards = input(f'Введите количество карточек игрока (если ничего не ввести будет 1 карточка)')
        if cards == '':
            cards = 1
        else:
            try:
                cards = int(cards)
            except Exception:
                print('Что-то пошло не так..')

        player = Player(name, id, cards)
        players.append(player)
    return players

def create_players_pc(num_players):
    players = []
    # создаем игроков людей
    for i in range(num_players):
        name = input(f'Введите имя компьютера {i + 1}:')
        id = i
        cards = input(f'Введите количество карточек компьютера (если ничего не ввести будет 1 карточка)')
        if cards == '':
            cards = 1
        else:
            try:
                cards = int(cards)
            except Exception:
                print('Что-то пошло не так..')

        player = ComputerPlayer(name, id, cards)
        players.append(player)
    return players

def continue_game(players, players_pc, winners):
    # для проверки есть ли игроки способные продолжать, или определены победители
    # думаем что все уже проиграли
    players_can = False
    if players != None:
        for player in players:
            # ищем игрока который еще может сражаться
            if player.can_play:
                players_can = True
    players_pc_can = False
    if players_pc != None:
        for player_pc in players_pc:
            # ищем игрока который еще может сражаться
            if player_pc.can_play:
                players_pc_can = True
    # if not(players_can and players_pc_can):
    #     print('Нет игроком способных продолжать бой..')
    return (players_can or players_pc_can) and not winners
