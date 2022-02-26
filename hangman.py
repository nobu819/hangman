def hangman(word):
    wrong = 0
    stages = ["",
              "________    ",
              "|           ",
              "|      |    ",
              "|      0    ",
              "|     /|\   ",
              "|     / \   ",
              "|||         "
             ]
    rletters = list(word)
    board  = ["_"] * len(word)
    win = False
    print("ハンガーゲームへようこそ!")
    while wrong < len(stages) - 1:
        print("\n")
        msg = "1文字、予想文字を入力 (有名な洋画)"
        char = input(msg)
        if char in rletters:
            cind = rletters.index(char)
            board[cind] = char
            rletters[cind] = '$'
        else:
            wrong += 1
        print(" ".join(board))
        e = wrong + 1
        print("\n".join(stages[0:e]))
        if "_" not in board:
            print("あなたの勝ち! victory!!!")
            print(" ".join(board))
            win = True
            break
    
    if not win:
        print("\n".join(stages[0:wrong+1]))
        print("ハッハッハ、あなたの負け!正解は {}".format(word))


movie = ["starwars", "missioninpossible", "matrix", "007", "spiderman", "harrypotter", "homealone", "backtothefuture",
         "terminator", "jurassicpark", "badman", "beautyandthebeast", "ironman", "aladdin", "avengers", "monstersinc"
        ]

import random
c = random.randint(0,15)
hangman(movie[0])