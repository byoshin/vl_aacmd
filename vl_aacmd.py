import keyboard
import json
import time
import pyperclip
import sys
import speech_recognition as sr
import jaconv
import argparse


def on_key_event(event):
    if event.event_type == keyboard.KEY_DOWN:
        key = event.name
        print(f"[!]key:{key}")
        if key == trigger_key:
            input_buffer.clear()
            input_buffer.append(key)
        if key == send_key:
            results = ""
            for item in input_buffer:
                results += str(item)
            if results == stop_command:
                keyboard.unhook_all()
                print("終了します、お疲れ様でした！")
                sys.exit(0)
            for config_item in config:
                if config_item["command"] == results:
                    pyperclip.copy(config_item["output"])
                    time.sleep(0.1)
                    if not option:
                        keyboard.press("shift")
                    keyboard.press(send_key)
                    time.sleep(0.01)
                    keyboard.release(send_key)
                    if not option:
                        keyboard.release("shift")
                    keyboard.press_and_release('ctrl+v')
                    keyboard.press(send_key)
                    time.sleep(0.01)
                    keyboard.release(send_key)
                    break
            input_buffer.clear()

        if (
            len(input_buffer) > 0
            and not (key == trigger_key)
            and not (key == "enter")
            and not (key == "shift")
        ):
            if input_buffer[0] == trigger_key:
                if not key == "backspace":
                    input_buffer.append(key)
                else:
                    del input_buffer[-1]
            else:
                input_buffer.clear()
        if len(input_buffer) > 50:
            input_buffer.clear()
        print(f"[!]buffer:{input_buffer}")


def transcription():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("音声キャプチャ...")
        recognizer.adjust_for_ambient_noise(source)
        while True:
            try:
                print("開始")
                audio = recognizer.listen(source, phrase_time_limit=3)
                text = recognizer.recognize_google(audio, language='ja-JP')
                if all('ァ' <= char <= 'ン' for char in text):
                    hiragana_text = jaconv.kata2hira(text)
                else:
                    hiragana_text = text
                results = jaconv.kana2alphabet(hiragana_text)
                print(f"ローマ字変換: {results}")
                print(f"認識結果: {text}")
                for config_item in config:
                    if config_item["vc"] == results:
                        pyperclip.copy(config_item["output"])
                        time.sleep(0.1)
                        if not option:
                            keyboard.press("shift")
                        keyboard.press(send_key)
                        time.sleep(0.01)
                        keyboard.release(send_key)
                        if not option:
                            keyboard.release("shift")
                        keyboard.press_and_release('ctrl+v')
                        keyboard.press(send_key)
                        time.sleep(0.01)
                        keyboard.release(send_key)
            except sr.UnknownValueError:
                print("音声が認識できませんでした")
            except sr.RequestError as e:
                print(f"Google Speech Recognitionサービスに接続できません: {e}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--team', action='store_true')
    args = parser.parse_args()
    option = args.team
    json_config_path = "config.json"
    with open(json_config_path, "r", encoding="utf-8") as json_file:
        config = json.load(json_file)
    trigger_key = "/"
    send_key = "enter"
    input_buffer = []
    stop_command = "/stop"
    print(f"検知を開始します！ [ {stop_command} ]で終了します。")
    keyboard.hook(on_key_event)
    transcription()
    try:
        keyboard.wait()
    except Exception:
        pass
