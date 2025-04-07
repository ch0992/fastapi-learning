# FastAPI로 만드는 도서 관리 API

안녕하세요! 이 프로젝트는 FastAPI를 사용하여 간단한 도서 관리 시스템을 만드는 방법을 배우는 예제입니다. CRUD(Create, Read, Update, Delete) 작업을 통해 RESTful API 개발의 기초를 배워봅시다.

## 이 프로젝트로 배우는 내용

1. FastAPI로 REST API 만들기
2. Pydantic을 사용한 데이터 검증
3. HTTP 메서드 사용하기 (GET, POST, PUT, DELETE)
4. 경로 매개변수와 요청 본문 다루기
5. API 문서 자동 생성 활용하기

## 시작하기 전에

### 필요한 도구
- Python 3.7 이상
- 코드 편집기 (VS Code 추천)
- 터미널 또는 명령 프롬프트

### 알아야 할 개념
1. **REST API란?**
   - 웹에서 데이터를 주고받는 방식의 표준
   - 리소스(예: 책)에 대한 CRUD 작업을 HTTP 메서드로 처리

2. **CRUD란?**
   - Create (생성) - POST 메서드
   - Read (읽기) - GET 메서드
   - Update (수정) - PUT 메서드
   - Delete (삭제) - DELETE 메서드

## 프로젝트 구조
```
fastapi_basic_crud/
├── main.py           # API 구현 코드
└── requirements.txt  # 필요한 패키지 목록
```

## 시작하기

### 1. 가상환경 만들기
```bash
# 가상환경 생성
python -m venv .venv

# 가상환경 활성화
.venv\Scripts\activate  # Windows
source .venv/bin/activate  # macOS/Linux
```

### 2. 패키지 설치하기
```bash
pip install -r requirements.txt
```

### 3. 서버 실행하기
```bash
uvicorn main:app --reload
```

## API 사용해보기

### 1. API 문서 확인
서버를 실행한 후 브라우저에서 다음 주소로 접속:
- http://127.0.0.1:8000/docs (Swagger UI)
- http://127.0.0.1:8000/redoc (ReDoc)

### 2. 기본 API 테스트

#### 책 생성하기 (Create)
```bash
curl -X POST "http://127.0.0.1:8000/books/" -H "Content-Type: application/json" -d "{\"id\": 3, \"title\": \"새로운 책\", \"author\": \"작가 이름\", \"published_year\": 2024, \"isbn\": \"123-456-789\", \"description\": \"책 설명\"}"
```

#### 모든 책 조회하기 (Read)
```bash
curl "http://127.0.0.1:8000/books/"
```

#### 특정 책 조회하기 (Read)
```bash
curl "http://127.0.0.1:8000/books/1"
```

#### 책 정보 수정하기 (Update)
```bash
curl -X PUT "http://127.0.0.1:8000/books/1" -H "Content-Type: application/json" -d "{\"id\": 1, \"title\": \"수정된 제목\", \"author\": \"작가\", \"published_year\": 2024, \"isbn\": \"123-456-789\", \"description\": \"수정된 설명\"}"
```

#### 책 삭제하기 (Delete)
```bash
curl -X DELETE "http://127.0.0.1:8000/books/1"
```

## 데이터 모델 이해하기

### Book 모델
```python
class Book(BaseModel):
    id: int                         # 책 고유 ID
    title: str                      # 책 제목
    author: str                     # 저자
    published_year: int             # 출판년도
    isbn: str                       # ISBN 번호
    description: Optional[str]      # 책 설명 (선택사항)
```

## 에러 처리

이 API는 다음과 같은 에러 상황을 처리합니다:
- 400 Bad Request: 책 ID가 이미 존재할 때
- 404 Not Found: 요청한 책을 찾을 수 없을 때

## 다음 단계로 배울 내용

1. 데이터베이스 연동하기 (SQLAlchemy)
2. 사용자 인증 추가하기
3. 더 많은 검증 규칙 추가하기
4. API 테스트 작성하기

## 도움이 되는 자료

- [FastAPI 공식 문서](https://fastapi.tiangolo.com/)
- [Pydantic 문서](https://pydantic-docs.helpmanual.io/)
- [HTTP 상태 코드](https://developer.mozilla.org/ko/docs/Web/HTTP/Status)
- [REST API 설계 가이드](https://docs.microsoft.com/ko-kr/azure/architecture/best-practices/api-design)

## 문제 해결

### 자주 발생하는 오류

1. "ModuleNotFoundError: No module named 'fastapi'"
   - 해결: `pip install fastapi uvicorn`

2. "Address already in use"
   - 해결: 이미 실행 중인 서버를 종료하거나 다른 포트 사용

3. "Validation error"
   - 해결: 요청 데이터가 Book 모델의 형식과 일치하는지 확인

도움이 필요하시다면 언제든 이슈를 등록해주세요!







