from pytube import YouTube
import whisper
import os

def download_audio_from_youtube(url, output_path):
    yt = YouTube(url)
    audio_stream = yt.streams.get_audio_only()
    audio_file_path = audio_stream.download(output_path=output_path)
    return audio_file_path


def transcribe_audio_with_whisper(audio_path):
    model = whisper.load_model("base") # tiny, base, small, medium, large
    result = model.transcribe(audio_path)
    return result['text']

def save_text_to_file(text, file_path):
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(text)


def main():
    # 사용자로부터 YouTube 링크 입력 받기
    youtube_url = input("Enter the YouTube video URL: ")


    # 오디오 파일 다운로드
    print("Downloading audio...")
    audio_path = download_audio_from_youtube(youtube_url, './output')

    # Whisper를 사용하여 오디오에서 텍스트 추출
    print("Transcribing audio...")
    transcript = transcribe_audio_with_whisper(audio_path)

    # 추출된 텍스트를 파일로 저장
    output_text_file = os.path.splitext(os.path.basename(audio_path))[0] + '.txt'
    save_text_to_file(transcript, f'./output/{output_text_file}')

    print(f"Transcription completed and saved as {output_text_file}")


if __name__ == '__main__':
    main()