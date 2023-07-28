from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

PATH = r"Path to the chrome driver"

# Create ChromeOptions
options = Options()
options.add_argument("--start-maximized")  # To start the browser maximized

driver = webdriver.ChromeDriver(options=options)
actions = ActionChains(driver)

def get_question():
    list_of_questions_class = driver.find_elements(By.CLASS_NAME, "M7eMe")
    list_of_questions = []
    for each_question in list_of_questions_class:
        question = []
        for word in each_question:
            question.append(each_question.text)
        list_of_questions.append(question)

def open_link(link):
    driver.get(link)

if __name__ == "__main__":
    link = r"https://forms.gle/ykLRZpfBRX9YVpLN9"