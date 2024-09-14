import gym
from gym import spaces
import numpy as np
import pyautogui as pag
import random
import keyboard
import time
from stable_baselines3 import PPO
import logging
import cv2

# Environment Definition
class NoAFKEnv(gym.Env):
    def __init__(self):
        super(NoAFKEnv, self).__init__()
        self.action_space = spaces.Discrete(5)  # 4 directions + no action
        self.observation_space = spaces.Box(low=0, high=1000, shape=(4,), dtype=np.float32)
        self.state = np.array([0, 0, 0, 0], dtype=np.float32)
        self.step_count = 0

    def step(self, action):
        # Move mouse based on action
        if action != 4:
            x1 = int(input("Write the first random position of the x"))
            x2 = int(input("Write the second random position for the x"))
            y1= int(input("Write the first random position for the y"))
            y2 = int(input("Write the second random position for the y"))
            x = random.randint(x1, x2)
            y = random.randint(y1, y2)
            pag.moveTo(x, y, 0.5)
            keys = ['w', 'a', 's', 'd']
            keyboard.press_and_release(keys[action])

        # Update state with additional features
        mouse_pos = np.array([pag.position().x, pag.position().y], dtype=np.float32)
        time_since_last_action = self.step_count % 100
        self.state = np.concatenate([mouse_pos, [time_since_last_action]])

        # Reward and done logic
        reward = self.calculate_reward(action)
        done = self.step_count >= 100
        self.step_count += 1
        return self.state, reward, done, {}

    def calculate_reward(self, action):
        reward = 0
        if action != 4:
            reward += 1
        if self.step_count % 20 == 0:
            reward += 0.5
        if self.state[0] > 600 and self.state[1] < 500:
            reward += 2
        return reward

    def reset(self):
        self.state = np.array([0, 0, 0, 0], dtype=np.float32)
        self.step_count = 0
        return self.state

# RL Model Training
def train_model():
    env = NoAFKEnv()
    model = PPO('MlpPolicy', env, verbose=1)
    model.learn(total_timesteps=10000)
    model.save("no_afk_model")

# Evaluation
def evaluate_model(model, env, num_episodes=10):
    for episode in range(num_episodes):
        state = env.reset()
        done = False
        total_reward = 0
        while not done:
            action, _ = model.predict(state)
            state, reward, done, _ = env.step(action)
            total_reward += reward
        print(f"Episode {episode}: Total Reward: {total_reward}")

# Capture and Process Screen (Computer Vision)
def capture_screen():
    screen = np.array(cv2.cvtColor(np.array(pag.screenshot()), cv2.COLOR_RGB2BGR))
    return screen

def preprocess_screen(screen):
    gray = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)
    return gray

# Logging
logging.basicConfig(filename='training.log', level=logging.INFO)

def log_metrics(step_count, reward):
    logging.info(f"Step: {step_count}, Reward: {reward}")

# User Feedback Integration
def get_user_feedback():
    feedback = input("Provide feedback on the agent's performance: ")
    # Use feedback to adjust training

# Example Run
if __name__ == "__main__":
    train_model()
    model = PPO.load("no_afk_model")
    env = NoAFKEnv()
    evaluate_model(model, env)
    print("Made by Mythereus")
