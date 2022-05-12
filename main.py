import pygame
import pygame.freetype
import sys
import random


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((0, 0))
        self.image.fill((0, 0, 0))
        self.rect = self.image.get_rect(center=(400, 750))
        self.current_health = 50
        self.maximum_health = 100
        self.health_bar_length = 400
        self.health_ratio = self.maximum_health / self.health_bar_length

        self.current_work = 50
        self.maximum_work = 100
        self.work_bar_length = 400
        self.work_ratio = self.maximum_work / self.work_bar_length

        self.current_school = 50
        self.maximum_school = 100
        self.school_bar_length = 400
        self.school_ratio = self.maximum_school / self.school_bar_length

        self.current_family = 50
        self.maximum_family = 100
        self.family_bar_length = 400
        self.family_ratio = self.maximum_family / self.family_bar_length

        self.score = 0
        self.game_over = False

    def update(self) -> None:
        self.basic_health()
        self.work()
        self.school()
        self.family()
        self.fail_state()

        # Basic ticks.
        self.current_health -= random.uniform(0.05, 0.25)
        self.current_family -= random.uniform(0.05, 0.25)
        self.current_school -= random.uniform(0.05, 0.25)
        self.current_work -= random.uniform(0.05, 0.25)

        self.score += 1

    def get_damage(self, amount):
        if self.current_health > 0:
            self.current_health -= amount
        if self.current_health <= 0:
            self.current_health = 0

    def add_health(self, amount):
        if self.current_health < self.maximum_health:
            self.current_health += amount
        if self.current_health >= self.maximum_health:
            self.current_health = self.maximum_health

    def add_work(self, amount):
        if self.current_work < self.maximum_work:
            self.current_work += amount
        if self.current_work >= self.maximum_work:
            self.current_work = self.maximum_work

    def add_school(self, amount):
        if self.current_school < self.maximum_school:
            self.current_school += amount
        if self.current_school >= self.maximum_school:
            self.current_school = self.maximum_school

    def add_family(self, amount):
        if self.current_family < self.maximum_family:
            self.current_family += amount
        if self.current_family >= self.maximum_family:
            self.current_family = self.maximum_family

    def basic_health(self):
        pygame.draw.rect(screen, (255, 0, 0), (10, 100, self.current_health / self.health_ratio, 25))
        pygame.draw.rect(screen, (255, 0, 0), (10, 100, self.health_bar_length, 25), 4)

    def work(self):
        pygame.draw.rect(screen, (0, 255, 0), (10, 200, self.current_work / self.work_ratio, 25))
        pygame.draw.rect(screen, (0, 255, 0), (10, 200, self.work_bar_length, 25), 4)

    def school(self):
        pygame.draw.rect(screen, (0, 0, 255), (10, 300, self.current_school / self.school_ratio, 25))
        pygame.draw.rect(screen, (0, 0, 255), (10, 300, self.school_bar_length, 25), 4)

    def family(self):
        pygame.draw.rect(screen, (255, 0, 255), (10, 400, self.current_family / self.family_ratio, 25))
        pygame.draw.rect(screen, (255, 0, 255), (10, 400, self.family_bar_length, 25), 4)

    def random_event(self):
        events = [0, 1, 2, 3]
        current_event = random.choice(events)
        # if current_event == 0:

    def fail_state(self):
        if self.current_health <= 0:
            self.write_score(self.score)
            self.restart()
        if self.current_family <= 0:
            self.write_score(self.score)
            self.restart()
        if self.current_work <= 0:
            self.write_score(self.score)
            self.restart()
        if self.current_school <= 0:
            self.write_score(self.score)
            self.restart()

    def restart(self):
        self.__init__()

    def write_score(self, score):
        with open('highscore.txt', 'w') as file:
            file.write(str(score))


pygame.init()
pygame.freetype.init()
screen = pygame.display.set_mode((800, 800))
clock = pygame.time.Clock()
user = pygame.sprite.GroupSingle(Player())
font = pygame.font.Font('freesansbold.ttf', 32)


# click = False


def main_menu():
    while True:

        screen.fill((0, 0, 0))
        title = font.render('LIFE SIMULATOR 2022', True, (random.randint(100, 255), 0, random.randint(100, 255)))
        play_text = font.render('PLAY', True, (random.randint(100, 255), 0, random.randint(100, 255)))
        quit_text = font.render('QUIT', True, (random.randint(100, 255), 0, random.randint(100, 255)))
        pygame.draw.rect(screen, (255, 255, 255), (200, 5, 400, 40), 4)
        screen.blit(title, (225, 10))

        mx, my = pygame.mouse.get_pos()

        play_button = pygame.Rect(300, 300, 200, 50)
        quit_button = pygame.Rect(300, 400, 200, 50)

        pygame.draw.rect(screen, (255, 255, 255), play_button)
        pygame.draw.rect(screen, (255, 255, 255), quit_button)
        screen.blit(play_text, (360, 310))
        screen.blit(quit_text, (360, 410))

        click = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        if play_button.collidepoint((mx, my)):
            if click:
                game_loop()
        if quit_button.collidepoint((mx, my)):
            if click:
                pygame.quit()
                sys.exit()

        pygame.display.update()
        pygame.display.set_caption('Life Simulator 2022')
        clock.tick(60)


def game_loop():
    while True:
        click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    user.sprite.add_health(10)
                if event.key == pygame.K_LEFT:
                    user.sprite.add_work(10)
                if event.key == pygame.K_RIGHT:
                    user.sprite.add_school(10)
                if event.key == pygame.K_DOWN:
                    user.sprite.add_family(10)

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        def read_score():
            with open('highscore.txt', 'r') as file:
                return int(file.read())

        screen.fill((30, 30, 30))
        user.draw(screen)
        user.update()
        title = font.render('LIFE SIMULATOR 2022', True, (255, 255, 255))
        score = font.render(f'Score = {user.sprite.score}', True, (255, 255, 255))
        high_score = font.render(f'High score = {read_score()}', True, (255, 255, 255))
        quit_text = font.render('QUIT', True, (random.randint(100, 255), 0, random.randint(100, 255)))
        quit_button = pygame.Rect(300, 700, 200, 50)
        screen.blit(high_score, (10, 500))
        screen.blit(score, (10, 10))
        screen.blit(title, (225, 10))
        pygame.draw.rect(screen, (255, 255, 255), (200, 5, 400, 40), 4)
        pygame.draw.rect(screen, (255, 255, 255), quit_button)
        screen.blit(quit_text, (360, 710))
        pygame.display.update()
        pygame.display.set_caption('Life Simulator 2022')
        clock.tick(60)
        mx, my = pygame.mouse.get_pos()
        if quit_button.collidepoint((mx, my)):
            if click:
                pygame.quit()
                sys.exit()


# game_loop()
main_menu()
