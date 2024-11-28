import json
import os
from modules.module1 import TransLate, LangDetect, LanguageList


def read_config(config_file: str) -> dict:
    with open(config_file, 'r', encoding='utf-8') as file:
        return json.load(file)


def count_text_features(text: str) -> tuple:
    num_chars = len(text)
    num_words = len(text.split())
    num_sentences = text.count('.') + text.count('!') + text.count('?')
    return num_chars, num_words, num_sentences


def translate_text(input_file: str, config: dict):
    if not os.path.exists(input_file):
        print(f"Помилка: Файл {input_file} не знайдено.")
        return

    with open(input_file, 'r', encoding='utf-8') as file:
        text = file.read()

    num_chars, num_words, num_sentences = count_text_features(text)

    print(f"Назва файлу: {input_file}")
    print(f"Розмір файлу: {os.path.getsize(input_file)} байт")
    print(f"Кількість символів: {num_chars}")
    print(f"Кількість слів: {num_words}")
    print(f"Кількість речень: {num_sentences}")
    print(f"Мова тексту: {LangDetect(text, 'lang')}")

    if num_chars > config["max_characters"]:
        print("Кількість символів перевищує вказану в конфігураційному файлі.")
        return
    if num_words > config["max_words"]:
        print("Кількість слів перевищує вказану в конфігураційному файлі.")
        return
    if num_sentences > config["max_sentences"]:
        print("Кількість речень перевищує вказану в конфігураційному файлі.")
        return

    translated_text = TransLate(text, 'auto', config["language_code"])

    if config["output"] == "screen":
        print(f"Перекладена мова: {config['language_code']}")
        print("Перекладений текст:")
        print(translated_text)
    elif config["output"] == "file":
        output_file = f"{os.path.splitext(input_file)[0]}_{config['language_code']}.txt"
        with open(output_file, 'w', encoding='utf-8') as outfile:
            outfile.write(translated_text)
        print("Ok: Перекладений текст збережено в", output_file)
    else:
        print("Помилка: невірний параметр виводу.")

if __name__ == "__main__":
    config = read_config("config.json")
    translate_text(config["input_file"], config)
