import unittest
import sys
import os
# Permite que game_logic seja importado, mesmo que esteja em um diretório acima
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from game.game_logic import check_win, available_square, is_board_full, reset_board, mark_square


# Classe de testes para a lógica do jogo da velha, usando unittest
class TestGameLogic(unittest.TestCase):

    # Testa se a função check_win detecta corretamente uma vitória horizontal
    def test_check_win_horizontal(self):
        board = reset_board()
        # Simulando uma vitória horizontal para o jogador 1
        board[0] = [1, 1, 1]
        result = check_win(1, board)
        self.assertEqual(result, ('horizontal', 0))

    # Testa se a função check_win detecta corretamente uma vitória vertical
    def test_check_win_vertical(self):
        board = reset_board()
        # Simulando uma vitória vertical para o jogador 2
        board[0][0] = board[1][0] = board[2][0] = 2
        result = check_win(2, board)
        self.assertEqual(result, ('vertical', 0))

    # Testa se a função check_win detecta corretamente uma vitória diagonal
    def test_check_win_desc_diagonal(self):
        board = reset_board()
        # Simulando uma vitória diagonal para o jogador 1
        board[0][0] = board[1][1] = board[2][2] = 1
        result = check_win(1, board)
        self.assertEqual(result, ('desc_diagonal', None))

    # Testa se a função check_win detecta corretamente uma vitória diagonal
    def test_check_win_asc_diagonal(self):
        board = reset_board()
        # Simulando uma vitória diagonal para o jogador 2
        board[2][0] = board[1][1] = board[0][2] = 2
        result = check_win(2, board)
        self.assertEqual(result, ('asc_diagonal', None))

    # Testa se a função is_board_full detecta corretamente quando o tabuleiro está cheio
    def test_is_board_full(self):
        board = reset_board()
        self.assertFalse(is_board_full(board))
        # Preencher o tabuleiro para que ele fique cheio
        for row in range(3):
            for col in range(3):
                board[row][col] = 1
        self.assertTrue(is_board_full(board))

    # Testa se a função available_square detecta corretamente se uma posição no tabuleiro está disponível
    def test_available_square(self):
        board = reset_board()
        # Verifica que a posição (0, 0) está disponível no tabuleiro vazio
        self.assertTrue(available_square(0, 0, board))
        # Marca a posição (0, 0) no tabuleiro para o jogador 1
        mark_square(0, 0, 1, board)
        # Verifica que a posição (0, 0) não está mais disponível
        self.assertFalse(available_square(0, 0, board))

if __name__ == '__main__':
    unittest.main()