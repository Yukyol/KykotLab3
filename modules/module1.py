from googletrans import Translator, LANGUAGES

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
        translator = Translator()
        translated = translator.translate(text, src=scr, dest=dest)
        return translated.text
    except Exception as e:
        return f"Помилка: {e}"

def LangDetect(text: str, set: str = "all") -> str:
    try:
        translator = Translator()
        lang_info = translator.detect(text)
        if set == "lang":
            return lang_info.lang
        elif set == "confidence":
            return lang_info.confidence
        return lang_info.lang, lang_info.confidence
    except Exception as e:
        return f"Помилка: {e}"

def CodeLang(lang: str) -> str:
    if lang in LANGUAGES:
        return lang
    for code, name in LANGUAGES.items():
        if name.lower() == lang.lower():
            return code
    return "Помилка: мова не знайдена."

def LanguageList(out: str = "screen", text: str = "") -> str:
    languages = [(i + 1, name, code) for i, (code, name) in enumerate(LANGUAGES.items())]
    if out == "screen":
        print("N  Language   ISO-639 code   Text")
        print("-" * 50)
        for idx, name, code in languages:
            translated_text = TransLate(text, 'auto', code) if text else ""
            print(f"{idx:<3} {name:<10} {code:<15} {translated_text}")
        return "Ok"
    return "Помилка: невірний параметр."
