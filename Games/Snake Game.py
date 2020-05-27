import sys
import random
import pygame
import time

class Launcher:

    # Initialise global variables for display properties
    def __init__(self):
        self.window = pygame.display.set_mode((500, 500))
        pygame.display.set_caption("Snake Game")
        self.fps = pygame.time.Clock()

        self.score = 0
        self.snake = Snake()
        self.food = Food();

    def start(self):

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameOver()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        self.snake.changeDirectionOfSnake('RIGHT') 
                    if event.key == pygame.K_UP:
                        self.snake.changeDirectionOfSnake('UP') 
                    if event.key == pygame.K_DOWN:
                        self.snake.changeDirectionOfSnake('DOWN') 
                    if event.key == pygame.K_LEFT:
                        self.snake.changeDirectionOfSnake('LEFT') 

            foodPos = self.food.spawnFood()
            if (self.snake.move(foodPos)):
                self.score += 1
                self.food.setFoodOnScreen(False)

            self.window.fill(pygame.Color('black'))
            for pos in self.snake.getBody():
                pygame.draw.rect(self.window, pygame.Color('green'), pygame.Rect(pos[0], pos[1], 10, 10))
                pygame.draw.rect(self.window, pygame.Color('red'), pygame.Rect(foodPos[0], foodPos[1], 10, 10))

            if (self.snake.checkCollision() == True):
                self.snake.gameOver()

            pygame.display.set_caption("Snake Game | Score: " + str(self.score))
            pygame.display.flip()
            self.fps.tick(24)


class Snake():
    def __init__(self):
        self.position = [100, 50]
        self.body = [[100, 50], [90, 50], [80, 50]]
        self.direction = "RIGHT"
        self.changeDirectionTo = self.direction

    def changeDirectionOfSnake(self, dir):
        if dir == "RIGHT" and not self.direction == "LEFT":
            self.direction = "RIGHT"
        if dir == "LEFT" and not self.direction == "RIGHT":
            self.direction = "LEFT"
        if dir == "UP" and not self.direction == "DOWN":
            self.direction = "UP"
        if dir == "DOWN" and not self.direction == "UP":
            self.direction = "DOWN"

    def move(self, foodPos):
        if self.direction == "RIGHT":
            self.position[0] += 10
        if self.direction == "LEFT":
            self.position[0] -= 10
        if self.direction == "UP":
            self.position[1] -= 10
        if self.direction == "DOWN":
            self.position[1] += 10

        self.body.insert(0, list(self.position))
        if self.position == foodPos:
            return True
        else:
            self.body.pop()
            return False

    def checkCollision(self):
        if self.position[0] > 490 or self.position[0] < 0:
            return True
        elif self.position[1] > 490 or self.position[1] < 0:
            return True

        # For body part in tail
        for bodyPart in self.body[1:]:
            if self.position == bodyPart:
                return True
        return False    
    
    def getHeadPos(self):
        return self.position
    
    def getBody(self):
        return self.body

    def gameOver(self):
        print("Game Over!")
        pygame.quit()
        sys.exit()


class Food():
    def __init__(self):
        self.position = [random.randrange(1, 50)*10,
             random.randrange(1, 50)*10]
        self.isFoodOnScreen = True

    def spawnFood(self):
        if (self.isFoodOnScreen == False):
            self.position = [random.randrange(1, 50)*10,
             random.randrange(1, 50)*10]
            self.isFoodOnScreen = True
        return self.position

    def setFoodOnScreen(self, boolean):
        self.isFoodOnScreen = boolean;
        

def main():
    launcher = Launcher()
    launcher.start()
    
if __name__ == "__main__":
    main()
