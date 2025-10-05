import whisper
from pydub import AudioSegment
import os

def convert_to_wav(input_file, output_file):
    """m4a を wav に変換"""
    try:
        audio = AudioSegment.from_file(input_file, format="m4a")
        audio.export(output_file, format="wav")
        print(f"✅ 変換完了: {output_file}")
    except Exception as e:
        print("❌ 変換失敗:", e)

def transcribe_audio(file_path):
    """Whisperで文字起こし"""
    model = whisper.load_model("base")  # small / medium にすると精度UP
    result = model.transcribe(file_path, language="ja")
    print("=== 音声認識結果 ===")
    print(result["text"])
    return result["text"]

if __name__ == "__main__":
    # 入力ファイル (録音したm4a)
    input_file = "data/3.m4a"
    # 出力ファイル (wav形式に変換)
    output_file = "data/sample.wav"

    # ステップ① m4a → wav に変換
    if os.path.exists(input_file):
        convert_to_wav(input_file, output_file)
    else:
        print(f"❌ 入力ファイルが見つかりません: {input_file}")
        exit()

    # ステップ② wav を文字起こし
    if os.path.exists(output_file):
        text = transcribe_audio(output_file)
        with open("data/transcription.txt", "w", encoding="utf-8") as f:
            f.write(text)
    else:
        print(f"❌ 出力ファイルが見つかりません: {output_file}")


