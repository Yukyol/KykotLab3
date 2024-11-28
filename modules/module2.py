from deep_translator import GoogleTranslator
from langdetect import detect, DetectorFactory

DetectorFactory.seed = 0

LANGUAGES = {
    'en': 'English',
    'uk': 'Ukrainian',
    'fr': 'French',
    'de': 'German',
    'es': 'Spanish',
    'it': 'Italian',
    'pl': 'Polish',
}

def TransLate(text: str, scr: str, dest: str) -> str:
    try:
        translator = GoogleTranslator(source=scr, target=dest)
        translated = translator.translate(text)
        return translated
    except Exception as e:
        return f"Помилка при перекладі: {str(e)}"

def LangDetect(text: str, set: str) -> str:
    try:
        lang = detect(text)
        confidence = 1.0
        if set == "lang":
            return lang
        elif set == "confidence":
            return confidence
        elif set == "all":
            return lang, confidence
        else:
            return "Помилка: невірний параметр."
    except Exception as e:
        return f"Помилка: {str(e)}"

def CodeLang(lang: str) -> str:
    if lang in LANGUAGES:
        return lang
    elif lang in LANGUAGES.values():
        return [code for code, name in LANGUAGES.items() if name == lang][0]
    else:
        return "Помилка: невірний параметр."

def LanguageList(out: str = "screen", text: str = None) -> str:
    languages = [(i + 1, name, code) for i, (code, name) in enumerate(LANGUAGES.items())]

    if out == "screen":
        print(f"{'N':<2} {'Language':<20} {'ISO-639 code':<15} {'Text'}")
        print('-' * 60)
        for i, name, code in languages:
            translated_text = GoogleTranslator(source='auto', target=code).translate(text) if text else ""
            print(f"{i:<2} {name:<20} {code:<15} {translated_text}")
        return "Ok"
    elif out == "file":
        return "File output not implemented."
    else:
        return "Помилка: невірний тип виводу."
