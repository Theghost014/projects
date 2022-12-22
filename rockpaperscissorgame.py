from getpass import getpass as input
def script():
    print()
    print("EPIC BATTLE!")
    print("Rock ✊ X Paper ✋ X Scissor ✌")
    print()
    print("To choose, please use: R (rock), P (paper) or S (scissor)")
    print()
    print()
    jogador1 = input("Player 1 name: ")
    print()
    jogador2 = input("Player 2 name: ")

    def function():
        print()
        print(jogador1, "turn: ")
        escolha1 = input("Your move: ")
        print()
        print(jogador2, "turn:")
        escolha2 = input("Your move: ")
        if escolha1 == "R" and escolha2 == "R":
            print()
            print("✊ x ✊")
            print("Rock against rock is a tie!!")
            print()
        elif escolha1 == "R" and escolha2 == "P":
            print()
            print("✊ X ✋")
            print("Paper embraced and ended with the rock!!!")
            print(jogador2, "won!")
            print()
        elif escolha1 == "R" and escolha2 == "S":
            print()
            print("✊ X ✌")
            print("Oh! The rock breaks the scissor!")
            print(jogador1, "won!")
            print()
        elif escolha1 == "P" and escolha2 == "R":
            print()
            print("✋ X ✊")
            print("Paper embraced and ended with the rock!!!")
            print(jogador1, "won!")
            print()
        elif escolha1 == "P" and escolha2 == "P":
            print()
            print("✋ X ✋")
            print("Paper against Paper is a tie!")
            print()
        elif escolha1 == "P" and escolha2 == "S":
            print()
            print("✋ X ✌")
            print("CUT CUT CUT! Scissor cuts the paper!")
            print(jogador2, "won!!")
            print()
        elif escolha1 == "S" and escolha2 == "R":
            print()
            print("✌ X ✊")
            print("Oh! The rock breaks the scissor!")
            print(jogador2, "won!")
            print()
        elif escolha1 == "S" and escolha2 == "S":
            print()
            print("✌ X ✌")
            print("Scissor against scissor is a tie!")
            print()
        elif escolha1 == "S" and escolha2 == "P":
            print()
            print("✌ X ✋")
            print("CUT CUT CUT! Scissor cuts the paper!")
            print(jogador1, "won!")
            print()
        else:
            print()
            print("Please, use only R, P or S to choose your move.")
            print()
        again = input("Do you want to play again? (use yes or no): ")
        #
        if again == "no":
            print()
            print("Thanks for playing!")
            r = input("Press [ENTER] to exit")
        elif again == "yes":
            print()
            jogadores = input(
                "Do you want to play again with the same players? (use yes or no): ")

            if jogadores == "no":
                script()
            elif jogadores == "yes":
                function()
            else:
                print()
                print("Please, use yes or no!")
                r = input("Press [ENTER] to restart the game")
                script()
        else:
            print()
            print("Please, use only yes or no!")
            r = input("Press [ENTER] to restart the game")
            script()
    function()


script()
