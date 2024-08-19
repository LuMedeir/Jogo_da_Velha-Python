# interface.py
import pygame
import sys
import time

# Cores para a interface
BG_COLOR = (93, 147, 36)         # Cor de fundo
LINE_COLOR = (249, 228, 197)     # Cor das linhas do tabuleiro
CIRCLE_COLOR = (255, 172, 0)     # Cor dos círculos
CROSS_COLOR = (0, 125, 184)      # Cor dos X
BUTTON_COLOR = (238, 140, 182)   # Cor do botão
BUTTON_TEXT_COLOR = (255, 255, 255)  # Cor do texto do botão
INIT_TEXT_COLOR = (0, 0, 0)      # Cor do texto inicial

# Configurações da interface
WIDTH, HEIGHT = 600, 600         # Largura e altura da janela do jogo
BOARD_ROWS = 3                   # Número de linhas do tabuleiro
BOARD_COLS = 3                   # Número de colunas do tabuleiro
LINE_WIDTH = 15                  # Largura das linhas do tabuleiro
SQUARE_SIZE = WIDTH // BOARD_COLS # Tamanho de cada quadrado do tabuleiro
CIRCLE_RADIUS = SQUARE_SIZE // 3 # Raio do círculo
CIRCLE_WIDTH = 15                # Largura das linhas do círculo
CROSS_WIDTH = 25                 # Largura das linhas do X
SPACE = SQUARE_SIZE // 4         # Espaço entre as linhas do X e a borda do quadrado

# Inicializar a tela
screen = pygame.display.set_mode((WIDTH, 700))  # Cria a janela do jogo com altura extra para o botão
pygame.display.set_caption('Jogo da Velha')     # Define o título da janela
screen.fill(BG_COLOR)                           # Preenche a tela com a cor de fundo

def draw_lines():
    """Desenha as linhas horizontais e verticais do tabuleiro."""
    # Linhas horizontais
    for i in range(1, BOARD_ROWS):
        pygame.draw.line(screen, LINE_COLOR, (0, SQUARE_SIZE * i), (WIDTH, SQUARE_SIZE * i), LINE_WIDTH)
    
    # Linhas verticais
    for i in range(1, BOARD_COLS):
        pygame.draw.line(screen, LINE_COLOR, (SQUARE_SIZE * i, 0), (SQUARE_SIZE * i, HEIGHT), LINE_WIDTH)

def draw_figures(board):
    """
    Desenha as figuras (círculos e X) no tabuleiro.

    Args:
        board (list): Matriz representando o estado do tabuleiro.
    """
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] == 1:
                pygame.draw.circle(screen, CIRCLE_COLOR, (int(col * SQUARE_SIZE + SQUARE_SIZE//2), int(row * SQUARE_SIZE + SQUARE_SIZE//2)), CIRCLE_RADIUS, CIRCLE_WIDTH)
            elif board[row][col] == 2:
                pygame.draw.line(screen, CROSS_COLOR, 
                                (col * SQUARE_SIZE + SPACE, row * SQUARE_SIZE + SQUARE_SIZE - SPACE), 
                                (col * SQUARE_SIZE + SQUARE_SIZE - SPACE, row * SQUARE_SIZE + SPACE), CROSS_WIDTH)
                pygame.draw.line(screen, CROSS_COLOR, 
                                (col * SQUARE_SIZE + SPACE, row * SQUARE_SIZE + SPACE), 
                                (col * SQUARE_SIZE + SQUARE_SIZE - SPACE, row * SQUARE_SIZE + SQUARE_SIZE - SPACE), CROSS_WIDTH)

def draw_win_line(win_type, index, board):
    """
    Desenha a linha indicativa de vitória.

    Args:
        win_type (str): Tipo de vitória ('vertical', 'horizontal', 'asc_diagonal', 'desc_diagonal').
        index (int): Índice da linha ou coluna da vitória.
        board (list): Matriz representando o estado do tabuleiro.
    """
    if win_type == 'vertical':
        posX = index * SQUARE_SIZE + SQUARE_SIZE // 2
        pygame.draw.line(screen, CIRCLE_COLOR if board[0][index] == 1 else CROSS_COLOR, (posX, 15), (posX, HEIGHT - 15), LINE_WIDTH)
    elif win_type == 'horizontal':
        posY = index * SQUARE_SIZE + SQUARE_SIZE // 2
        pygame.draw.line(screen, CIRCLE_COLOR if board[index][0] == 1 else CROSS_COLOR, (15, posY), (WIDTH - 15, posY), LINE_WIDTH)
    elif win_type == 'asc_diagonal':
        pygame.draw.line(screen, CIRCLE_COLOR if board[2][0] == 1 else CROSS_COLOR, (15, HEIGHT - 15), (WIDTH - 15, 15), LINE_WIDTH)
    elif win_type == 'desc_diagonal':
        pygame.draw.line(screen, CIRCLE_COLOR if board[0][0] == 1 else CROSS_COLOR, (15, 15), (WIDTH - 15, HEIGHT - 15), LINE_WIDTH)

def restart_interface():
    """Reinicia a interface do jogo, desenhando o tabuleiro e o botão de reinício."""
    start_image = pygame.image.load('./game/image/details_interface3.png')
    screen.fill(BG_COLOR)
    screen.blit(start_image, (0, 0))
    draw_lines()
    draw_button()

def draw_button():
    """Desenha o botão de reinício na tela."""
    button_rect = pygame.Rect(230, 625, 140, 50)
    pygame.draw.rect(screen, BUTTON_COLOR, button_rect)

    font = pygame.font.Font(None, 36)
    text = font.render("Restart", True, BUTTON_TEXT_COLOR)
    text_rect = text.get_rect(center=button_rect.center)
    screen.blit(text, text_rect)

def button_clicked(pos):
    """
    Verifica se o botão de reinício foi clicado.

    Args:
        pos (tuple): Posição (x, y) do clique do mouse.

    Returns:
        bool: True se o botão foi clicado, False caso contrário.
    """
    button_rect = pygame.Rect(225, 625, 140, 50)
    return button_rect.collidepoint(pos)

def screen_init():
    """Exibe a tela inicial com uma mensagem piscante até o jogador pressionar uma tecla."""
    start_image = pygame.image.load('./game/image/init_screen.png')
    
    waiting = True
    while waiting:
        screen.blit(start_image, (0, 0))
        draw_blinking_text()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                waiting = False  # Sai do loop quando qualquer tecla é pressionada
        pygame.display.update()
        pygame.time.Clock().tick(60)

def screen_empate():
    """Exibe a tela de empate até o jogador pressionar uma tecla."""
    empate_image = pygame.image.load('./game/image/tie.png')
    bg = pygame.image.load('./game/image/background.png')
    screen.blit(bg, (0, 0))
    screen.blit(empate_image, (0, 0))
    pygame.display.update()

    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                waiting = False  # Sai do loop quando qualquer tecla é pressionada
            
def screen_win(player):
    """
    Exibe a tela de vitória do jogador até que uma tecla seja pressionada.

    Args:
        player (int): O jogador que venceu (1 para O, 2 para X).
    """
    X_win_image = pygame.image.load('./game/image/X_win.png')
    O_win_image = pygame.image.load('./game/image/O_win.png')
    bg = pygame.image.load('./game/image/background.png')
    screen.blit(bg, (0, 0))

    if player == 1:
        screen.blit(O_win_image, (0, 0))
    elif player == 2:
        screen.blit(X_win_image, (0, 0))
    pygame.display.update()

    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                waiting = False  # Sai do loop quando qualquer tecla é pressionada
    
def draw_blinking_text():
    """Desenha um texto piscante na tela inicial."""
    blink_interval = 700  # Intervalo de tempo para a imagem aparecer e desaparecer
    current_time = pygame.time.get_ticks()
    show_text = (current_time // blink_interval) % 2 == 0

    if show_text:
        render_text = pygame.font.Font(None, 38).render("Press any button to play", True, INIT_TEXT_COLOR)
        text_rect = render_text.get_rect(center=(WIDTH//2, 460))
        screen.blit(render_text, text_rect)
        
def occupied_position(mouseX, mouseY):
    """
    Exibe uma imagem indicando que a posição no tabuleiro já está ocupada.

    Args:
        mouseX (int): Posição X do mouse.
        mouseY (int): Posição Y do mouse.
    """
    occupied = pygame.image.load('./game/image/occupied.png')
    screen.blit(occupied, (mouseX - 25, mouseY - 25))
    pygame.display.update()
    time.sleep(0.35)  # Pausa