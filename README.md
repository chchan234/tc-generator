# TC Generator - 자동 테스트 케이스 생성기

기획서 문서(PDF, DOCX)를 분석하여 상세 테스트 케이스(TC)를 자동으로 생성하고, LangGraph 기반 Multi-Agent 시스템으로 검수 및 피드백을 제공하는 도구입니다.

## 주요 기능

- **기획서 문서 업로드**: PDF, DOCX 형식의 기획서 파일 업로드 지원
- **텍스트 추출 및 전처리**: 문서에서 텍스트 추출 및 불필요한 내용 필터링
- **Chunking 및 요약**: 긴 문서의 경우 적절한 크기로 나누고 요약
- **테스트 케이스 자동 생성**: Google Gemini를 활용한 상세 TC 자동 생성
- **테스트 케이스 자동 검수**: LangGraph Multi-Agent 기반 TC 품질 검수 및 피드백
- **결과 내보내기**: 생성된 TC를 CSV, Excel 형식으로 저장 지원
- **기능 영역별 생성**: 기능 영역을 분석하여 더 상세한 테스트 케이스 생성

## 설치 방법

1. 저장소 클론 또는 다운로드:

```bash
git clone https://github.com/chchan234/tc-generator.git
cd tc-generator
```

2. 필요한 패키지 설치:

```bash
pip install -r requirements.txt
```

3. Google Gemini API 키 준비:
   - [Google AI Studio](https://makersuite.google.com/app/apikey)에서 API 키 발급

## 사용 방법

1. 애플리케이션 실행:

```bash
python app.py
```

2. API 키 설정:
   - Google Gemini API 키 입력

3. 기획서 파일 업로드:
   - PDF 또는 DOCX 형식의 기획서 파일 선택

4. 설정 구성:
   - 테스트 케이스 템플릿 유형 선택 (기본, API, UI, 모바일)
   - 청크 크기 및 중복 설정
   - 테스트 케이스 자동 검수 옵션 선택
   - 생성 방식 선택 (일반 생성 또는 기능 영역별 생성)

5. 처리 시작:
   - "처리 시작" 버튼 클릭
   - 진행 상황 확인

6. 결과 확인 및 내보내기:
   - 탭을 통해 원본 텍스트, 처리된 텍스트, 생성된 TC, 피드백 확인
   - CSV 또는 Excel 형식으로 내보내기

## 시스템 요구사항

- Python 3.9 이상
- 인터넷 연결 (Google Gemini API 사용)
- 최소 4GB RAM 권장

## 실행 파일 빌드

실행 파일(.exe)을 빌드하려면 다음 명령을 실행하세요:

```bash
python create_exe.py
```

빌드된 실행 파일은 `dist` 폴더에 생성됩니다.

## 프로젝트 구조

```
tc-generator/
├── app.py                 # 메인 애플리케이션
├── create_exe.py          # 실행 파일 빌드 스크립트
├── src/
│   ├── document_processor.py  # 문서 처리
│   ├── text_extractor.py      # 텍스트 추출
│   ├── chunker.py             # 청킹 및 요약
│   ├── tc_generator.py        # TC 생성 (Gemini 연동)
│   ├── tc_reviewer.py         # LangGraph 활용 검수
│   └── file_manager.py        # 파일 저장 관리
├── output/                # 결과물 저장 디렉토리
├── templates/             # GUI 템플릿
├── static/                # 정적 파일
└── requirements.txt       # 의존성 패키지
```

## 주의사항

- API 키는 안전하게 관리해주세요. 애플리케이션 내에서는 일시적으로만 저장됩니다.
- 대용량 문서 처리 시 메모리 사용량이 높아질 수 있습니다.
- 인터넷 연결 상태에 따라 처리 속도가 달라질 수 있습니다.
- 실행 파일(.exe)은 처음 실행 시 압축 해제에 시간이 걸릴 수 있습니다.

## 라이선스

이 프로젝트는 MIT 라이선스 하에 배포됩니다.

## 문의 및 기여

문제 신고나 기능 제안은 GitHub 이슈를 통해 제출해주세요.