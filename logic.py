# Задание №3
from translate import Translator
import requests
from collections import defaultdict

# Задание №5
qwestions = {"как тебя зовут" : "Я супер-крутой-бот и мое ппредназначение помогать тебе!",
             "сколько тебе лет" : "Это слишком философский вопрос",
             "какая твоя любимая еда" : "Конечно же пицца"}

class TextAnalysis():   
    
    # Задание №1
    memory = defaultdict(list)

    def __init__(self, text, owner):

        # Задание №2
        TextAnalysis.memory[owner].append(self)

        self.text = text
        self.translation = self.__translate(self.text, "ru", "en")

        # Задание №6
        if self.text.lower() in qwestions.keys():
            self.response = qwestions[text]
        else:
            self.response = self.get_answer() 

    
    def get_answer(self):
        res = self.__translate("I don't know how to help", "en", "ru")
        return res

    def __translate(self, text, from_lang, to_lang):
        try:
            # Задание №4
            translator = Translator(from_lang=from_lang, to_lang=to_lang)
            translation = translator.translate(text)
            return translation
        except:
            return "Перевод не удался"
