from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

import requests
import pyttsx3
import speech_recognition as sr

PATH = r"Path to the chrome driver"

# Create ChromeOptions
options = Options()
options.add_argument("--start-maximized")  # To start the browser maximized

driver = webdriver.ChromeDriver(options=options)
actions = ActionChains(driver)

def read_question(list_of_questions):
  engine = pyttsx3.init()
  for question in list_of_questions:
    question_text = question.text
    engine.setProperty('rate', 150)
    engine.say(question_text)
    engine.runAndWait()

    answer = get_input()
    print(f"You said: {answer}")

def get_input():
  recognizer = sr.Recognizer()
  with sr.Microphone() as source:
    recognizer.adjust_for_ambient_noise(source)
    print('Speak now:')
    audio = recognizer.listen(source)
  try:
    return recognizer.recognize_google(audio)
  except:
    return None
    
def get_question():
    list_of_questions_class = driver.find_elements(By.CLASS_NAME, "M7eMe")
    list_of_questions = []
    for each_question in list_of_questions_class:
        question = []
        for word in each_question:
            question.append(each_question.text)
        list_of_questions.append(question)
    return list_of_questions

if __name__ == "__main__":
    link = r"https://forms.gle/ykLRZpfBRX9YVpLN9"
    driver.get(link)

    # questions = get_question()
    list_of_questions = ["This is question 1", "This is question 2", "This is question 3", "This is question 4"]
    read_question(list_of_questions)

