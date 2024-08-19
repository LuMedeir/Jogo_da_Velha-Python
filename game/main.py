import pygame
import sys
from game_logic import (
    is_board_full, reset_board,
    handle_quit_event, handle_mouse_click
)
from interface import (
    draw_figures, restart_interface,
    screen_init, screen_empate, 
)

def main():
    """
    Função principal que inicializa e executa o jogo da velha.
    
    O jogo alterna entre os jogadores 1 e 2, verifica as condições de vitória ou empate, 
    e atualiza a interface gráfica com base nas interações do usuário.
    """
    pygame.init()
    player = 1  # Define o jogador inicial como 1
    board = reset_board()  # Inicializa o tabuleiro vazio

    screen_init()  # Exibe a tela de início do jogo
    restart_interface()  # Desenha a interface inicial do jogo

    while True:
        restart_interface()  # Redesenha a interface a cada iteração do loop
        draw_figures(board)  # Desenha as figuras no tabuleiro

        if is_board_full(board):
            screen_empate()  # Exibe a tela de empate se o tabuleiro estiver cheio
            board = reset_board()  # Reinicia o tabuleiro
            continue

        for event in pygame.event.get():
            handle_quit_event(event)  # Lida com o evento de saída do jogo
            if event.type == pygame.MOUSEBUTTONDOWN:
                board, player = handle_mouse_click(event, board, player)  # Lida com o clique do mouse

        pygame.display.update()  # Atualiza a tela

if __name__ == "__main__":
    main()
