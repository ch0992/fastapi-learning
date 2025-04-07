# FastAPI 기본 CRUD

이 프로젝트는 FastAPI를 사용하여 기본적인 CRUD(Create, Read, Update, Delete) 작업을 구현하는 방법을 보여주는 예제입니다.

## 주요 학습 내용

1. RESTful API 구현
   - 표준 HTTP 메서드 활용 (GET, POST, PUT, DELETE)
   - 리소스 기반 URL 설계
   - 상태 코드 활용

2. 데이터 모델링과 검증
   - Pydantic 모델 정의
   - 입력 데이터 검증
   - 응답 모델 설계

3. 메모리 기반 데이터 저장소
   - 데이터 구조 설계
   - CRUD 작업 구현
   - 데이터 영속성 관리

## 프로젝트 구조

```
fastapi_basic_crud/
├── main.py           # 메인 애플리케이션 코드
└── requirements.txt  # 의존성 목록
```

## API 엔드포인트

### 도서 관리
- `GET /books`: 모든 도서 목록 조회
- `GET /books/{book_id}`: 특정 도서 조회
- `POST /books`: 새 도서 추가
- `PUT /books/{book_id}`: 도서 정보 수정
- `DELETE /books/{book_id}`: 도서 삭제

## 설치 및 실행

1. 의존성 설치
```bash
pip install -r requirements.txt
```

2. 서버 실행
```bash
uvicorn main:app --reload
```

3. API 문서 확인
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## 데이터 모델

```python
class Book(BaseModel):
    id: Optional[int] = None
    title: str
    author: str
    description: Optional[str] = None
    price: float
```

## 주요 기능

1. **데이터 검증**
   - Pydantic을 사용한 자동 데이터 검증
   - 필수 필드 확인
   - 데이터 타입 검증

2. **오류 처리**
   - 적절한 HTTP 상태 코드 반환
   - 상세한 오류 메시지 제공

3. **자동 문서화**
   - OpenAPI (Swagger) 문서 자동 생성
   - 대화형 API 테스트 인터페이스

## 학습 목표

이 프로젝트를 통해 다음을 학습할 수 있습니다:

1. FastAPI의 기본 구조와 작동 방식
2. RESTful API 설계 원칙
3. Pydantic을 사용한 데이터 모델링
4. HTTP 메서드와 상태 코드의 올바른 사용
5. API 문서화 자동화
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







