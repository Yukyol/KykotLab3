from modules.module2 import TransLate, LangDetect, CodeLang, LanguageList

text = "I wanna buy a new phone, can you recommend smth?"

translated_text = TransLate(text, 'en', 'uk')
print("Переклад:", translated_text)

detected_lang, confidence = LangDetect(text, 'all')
print("Визначення мови:", (detected_lang, confidence))

print("Список мов:", LanguageList("screen", text))
