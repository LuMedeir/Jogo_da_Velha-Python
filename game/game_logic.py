# game_logic.py

import pygame
import sys

# Importação de funções e constantes do arquivo interface.py
from interface import (
    draw_lines, draw_figures, draw_win_line, restart_interface, screen, 
    draw_button, button_clicked, screen_init, screen_empate, draw_button, 
    occupied_position, screen_win, BOARD_ROWS, BOARD_COLS
)

def mark_square(row, col, player, board):
    """
    Marca uma posição no tabuleiro com o jogador atual.

    Args:
        row (int): Linha do tabuleiro.
        col (int): Coluna do tabuleiro.
        player (int): Jogador atual (1 ou 2).
        board (list): Estado atual do tabuleiro.
    """
    board[row][col] = player

def available_square(row, col, board):
    """
    Verifica se uma posição no tabuleiro está disponível.

    Args:
        row (int): Linha do tabuleiro.
        col (int): Coluna do tabuleiro.
        board (list): Estado atual do tabuleiro.

    Returns:
        bool: Retorna True se a posição estiver disponível, caso contrário, False.
    """
    if (row > 600):
        return False
    return board[row][col] == 0

def is_board_full(board):
    """
    Verifica se o tabuleiro está completamente preenchido.

    Args:
        board (list): Estado atual do tabuleiro.

    Returns:
        bool: Retorna True se o tabuleiro estiver cheio, caso contrário, False.
    """
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] == 0:
                return False
    return True

def check_win(player, board):
    """
    Verifica se há um vencedor no jogo.

    Args:
        player (int): Jogador atual (1 ou 2).
        board (list): Estado atual do tabuleiro.

    Returns:
        tuple: Uma tupla contendo o tipo de vitória ('horizontal', 'vertical', 'asc_diagonal', 'desc_diagonal') e a linha/coluna ou None.
    """
    # Verificar linhas
    for row in range(BOARD_ROWS):
        if board[row][0] == board[row][1] == board[row][2] == player:
            return 'horizontal', row

    # Verificar colunas
    for col in range(BOARD_COLS):
        if board[0][col] == board[1][col] == board[2][col] == player:
            return 'vertical', col

    # Verificar diagonais
    if board[0][0] == board[1][1] == board[2][2] == player:
        return 'desc_diagonal', None

    if board[2][0] == board[1][1] == board[0][2] == player:
        return 'asc_diagonal', None

    return None

def reset_board():
    """
    Reseta o tabuleiro para o estado inicial.

    Returns:
        list: Um novo tabuleiro 3x3 com todas as posições zeradas.
    """
    return [[0 for _ in range(3)] for _ in range(3)]

def handle_quit_event(event):
    """
    Lida com o evento de saída do jogo.

    Args:
        event (pygame.event.Event): Evento de saída (QUIT).
    """
    if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()

def handle_mouse_click(event, board, player):
    """
    Lida com o clique do mouse, atualizando o tabuleiro e alternando o jogador.

    Args:
        event (pygame.event.Event): Evento de clique do mouse.
        board (list): Estado atual do tabuleiro.
        player (int): Jogador atual (1 ou 2).

    Returns:
        tuple: O estado atualizado do tabuleiro e o jogador atual.
    """
    mouseX, mouseY = event.pos

    if button_clicked(event.pos):
        return reset_board(), player

    if mouseY > 600:  # Evita cliques fora do tabuleiro
        return board, player

    clicked_row = mouseY // (600 // 3)
    clicked_col = mouseX // (600 // 3)

    if available_square(clicked_row, clicked_col, board):
        mark_square(clicked_row, clicked_col, player, board)
        win_result = check_win(player, board)
        if win_result:
            draw_figures(board)
            draw_win_line(win_result[0], win_result[1], board)
            screen_win(player)
            return reset_board(), player

        player = 2 if player == 1 else 1

    else:
        occupied_position(mouseX, mouseY)

    return board, player
