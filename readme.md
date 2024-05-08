## YouTube Link로 텍스트 파일 형식의 대본 생성

### 개요
이 스크립트는 YouTube Link의 오디오를 다운로드하고, Whisper 라이브러리를 사용하여 텍스트로 변환하는 기능을 제공합니다.

### 요구 사항
- Python 3.x
- Pytube 라이브러리
- Whisper 라이브러리

### 설치
1. [여기](https://www.python.org/downloads/)에서 Python 3.x를 설치하세요.
2. pip를 사용하여 필요한 라이브러리를 설치하세요:
    ```
    pip install pytube whisper
    ```

### 사용법
1. `main.py` 스크립트를 실행하세요
2. youtube 영상 주소 또는 공유를 눌러 얻을 수 있는 Link를 입력하세요
3. `./output` 디렉터리에 오디오(mp4)와 대본 스크립트(txt)를 저장합니다.

### 스크립트 상세 정보
- `download_audio_from_youtube(url, output_path)`: 지정된 YouTube URL에서 오디오를 다운로드하고 지정된 출력 디렉토리에 저장합니다.
- `transcribe_audio_with_whisper(audio_path)`: Whisper 라이브러리를 사용하여 지정된 오디오 파일에서 오디오를 전사합니다.
- `save_text_to_file(text, file_path)`: 제공된 텍스트를 지정된 파일 경로에 저장합니다.