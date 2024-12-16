import pygame
import sys
from button import ImageButton
import random as rd

pygame.init()

WIDTH, HEIGHT = 360, 640

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My character film")
main_background = pygame.image.load("fon_film/start.jpg")


def main_menu():
    start_button = ImageButton(WIDTH / 2 - (252 / 2), 150, 252, 74, "Новая игра", "blue.jpg", "red.jpg")
    settings_button = ImageButton(WIDTH / 2 - (252 / 2), 250, 252, 74, "Настройки", "blue.jpg", "red.jpg")
    rules_button = ImageButton(WIDTH / 2 - (252 / 2), 350, 252, 74, "Правила", "blue.jpg", "red.jpg")
    exit_button = ImageButton(WIDTH / 2 - (252 / 2), 450, 252, 74, "Выход", "blue.jpg", "red.jpg")

    running = True
    while running:
        screen.fill((0, 0, 0))

        screen.blit(main_background, (0, -300))

        font = pygame.font.Font(None, 50)
        text_surface = font.render("Меню игры", True, (0, 0, 0))
        text_rect = text_surface.get_rect(center=(WIDTH/2, 100))
        screen.blit(text_surface, text_rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.USEREVENT and event.button == start_button:
                game_mode()

            if event.type == pygame.USEREVENT and event.button == settings_button:
                settings_menu()

            if event.type == pygame.USEREVENT and event.button == rules_button:
                rules()

            if event.type == pygame.USEREVENT and event.button == exit_button:
                pygame.quit()
                sys.exit()

            for btn in [start_button, settings_button, exit_button, rules_button]:
                btn.handle_event(event)

        for btn in [start_button, settings_button, exit_button, rules_button]:
            btn.check_hover(pygame.mouse.get_pos())
            btn.draw(screen)

        pygame.display.flip()


def settings_menu():
    audio_button = ImageButton(WIDTH / 2 - (252 / 2), 150, 252, 74, "Аудио", "blue.jpg", "red.jpg")
    video_button = ImageButton(WIDTH / 2 - (252 / 2), 250, 252, 74, "Видео", "blue.jpg", "red.jpg")
    back_button = ImageButton(0, 0, 50, 50, "", "buttons_image/back.jpg")

    running = True
    while running:
        screen.fill((0, 0, 0))

        screen.blit(main_background, (0, -300))

        font = pygame.font.Font(None, 72)
        text_surface = font.render("Настройки", True, (0, 0, 0))
        text_rect = text_surface.get_rect(center=(WIDTH / 2, 100))
        screen.blit(text_surface, text_rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.USEREVENT and event.button == back_button:
                running = False

            for btn in [audio_button, video_button, back_button]:
                btn.handle_event(event)

        for btn in [audio_button, video_button, back_button]:
            btn.check_hover(pygame.mouse.get_pos())
            btn.draw(screen)

        pygame.display.flip()


def game_mode():
    one_game_button = ImageButton(WIDTH / 2 - (252 / 2), 150, 252, 74, "Одиночная игра", "blue.jpg", "red.jpg")
    command_game_button = ImageButton(WIDTH / 2 - (252 / 2), 250, 252, 74, "Командная игра", "blue.jpg", "red.jpg")
    inter_game_button = ImageButton(WIDTH / 2 - (252 / 2), 350, 252, 74, "Игра по сети", "blue.jpg", "red.jpg")
    back_button = ImageButton(0, 0, 50, 50, "", "buttons_image/back.jpg")

    running = True
    while running:
        screen.fill((0, 0, 0))

        screen.blit(main_background, (0, -300))

        font = pygame.font.Font(None, 48)
        text_surface = font.render("Выбор режима игры", True, (0, 0, 0))
        text_rect = text_surface.get_rect(center=(WIDTH/2, 100))
        screen.blit(text_surface, text_rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.USEREVENT and event.button == one_game_button:
                one_game()

            if event.type == pygame.USEREVENT and event.button == command_game_button:
                pass

            if event.type == pygame.USEREVENT and event.button == inter_game_button:
                pass

            if event.type == pygame.USEREVENT and event.button == back_button:
                main_menu()

            for btn in [one_game_button, command_game_button, inter_game_button, back_button]:
                btn.handle_event(event)

        for btn in [one_game_button, command_game_button, inter_game_button, back_button]:
            btn.check_hover(pygame.mouse.get_pos())
            btn.draw(screen)

        pygame.display.flip()


def game():
    f = open('movie_characters.txt', 'r')
    contents = f.readlines()
    len_film = len(contents)
    num_film = rd.randint(0, len_film-1)
    film = contents[num_film]
    film = film.split()
    suget = film[0]
    character = film[rd.randint(1, len(film)-1)]
    return suget, character


def rules():
    back_button = ImageButton(0, 0, 50, 50, "", "buttons_image/back.jpg")

    running = True
    while running:
        screen.fill((0, 0, 0))

        screen.blit(main_background, (0, -300))

        font = pygame.font.Font(None, 55)
        text_surface = font.render("Объяснить фильм", True, (0, 0, 0))
        text_rect = text_surface.get_rect(center=(WIDTH / 2, HEIGHT / 2))
        screen.blit(text_surface, text_rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.USEREVENT and event.button == back_button:
                running = False

            for btn in [back_button]:
                btn.handle_event(event)

        for btn in [back_button]:
            btn.check_hover(pygame.mouse.get_pos())
            btn.draw(screen)

        pygame.display.flip()


def one_game():

    slovo = game()
    film = slovo[0]

    film_image = pygame.image.load('fon_film/' + film + '.jpg')
    film_image = pygame.transform.scale(film_image, (WIDTH, HEIGHT))

    change_button = ImageButton(WIDTH - 50, 0, 50, 50, "", "buttons_image/restart.jpg")
    back_button = ImageButton(0, 0, 50, 50, "", "buttons_image/back.jpg")

    running = True

    while running:
        screen.fill((0, 0, 0))

        screen.blit(film_image, (0, 0))

        font = pygame.font.Font(None, 20)
        text_surface = font.render('', True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=(WIDTH / 2, 100))
        screen.blit(text_surface, text_rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.USEREVENT and event.button == change_button:
                one_game()

            if event.type == pygame.USEREVENT and event.button == back_button:
                game_mode()

            for btn in [change_button, back_button]:
                btn.handle_event(event)

        for btn in [change_button, back_button]:
            btn.check_hover(pygame.mouse.get_pos())
            btn.draw(screen)

        pygame.display.flip()


if __name__ == "__main__":
    main_menu()
