# FastAPI 구조화된 도서 관리 API

이 프로젝트는 FastAPI를 사용하여 도서 관리 API를 MVC 패턴으로 구현한 예제입니다. 코드의 구조화와 관심사의 분리를 통해 더 유지보수하기 쉽고 확장 가능한 API를 만드는 방법을 보여줍니다.

## 프로젝트 구조

```
2.fastapi_structured/
├── app/
│   ├── models/          # 데이터 모델 정의
│   │   └── book.py
│   ├── services/        # 비즈니스 로직 처리
│   │   └── book_service.py
│   ├── routers/         # 라우트 처리 (컨트롤러)
│   │   └── book_router.py
│   └── main.py         # 애플리케이션 시작점
└── requirements.txt    # 프로젝트 의존성
```

## MVC 패턴 구현

### 1. Model (app/models/book.py)
- 데이터 구조 정의
- Pydantic을 사용한 데이터 검증
- 타입 힌트를 통한 명확한 인터페이스

### 2. Service (app/services/book_service.py)
- 비즈니스 로직 처리
- 데이터 조작 및 저장
- 예외 처리

### 3. Controller (app/routers/book_router.py)
- HTTP 요청 처리
- 라우팅 설정
- 의존성 주입
- 요청/응답 형식 정의

## 시작하기

### 1. 가상환경 설정
```bash
python -m venv .venv
.venv\\Scripts\\activate  # Windows
source .venv/bin/activate  # macOS/Linux
```

### 2. 의존성 설치
```bash
pip install -r requirements.txt
```

### 3. 서버 실행
```bash
# app 디렉토리의 main.py를 시작점으로 실행
uvicorn app.main:app --reload
```

## API 엔드포인트

### 책 관리 API
- `GET /books/`: 모든 책 목록 조회
- `GET /books/{book_id}`: 특정 책 조회
- `POST /books/`: 새 책 생성
- `PUT /books/{book_id}`: 책 정보 수정
- `DELETE /books/{book_id}`: 책 삭제

## API 문서
서버 실행 후 다음 URL에서 자동 생성된 API 문서를 확인할 수 있습니다:
- Swagger UI: http://127.0.0.1:8000/docs
- ReDoc: http://127.0.0.1:8000/redoc

## 프로젝트 특징

### 1. 관심사의 분리
- 모델: 데이터 구조 정의
- 서비스: 비즈니스 로직
- 라우터: HTTP 요청 처리

### 2. 의존성 주입
- `Depends`를 사용한 서비스 주입
- 테스트 용이성 향상
- 결합도 감소

### 3. 타입 안정성
- Pydantic 모델
- 타입 힌트
- 자동 검증

### 4. 확장성
- 모듈화된 구조
- 새로운 기능 추가 용이
- 테스트 작성 편리

## 다음 개선 사항
1. 데이터베이스 연동
2. 사용자 인증
3. 캐싱 구현
4. 로깅 추가
5. 테스트 코드 작성

## API 테스트 예제

### PowerShell을 사용한 API 테스트

#### 1. 모든 책 조회
```powershell
Invoke-RestMethod -Uri 'http://localhost:8000/books/' -Method Get
```

#### 2. 새 책 생성
```powershell
$body = @{
    id = 3
    title = 'FastAPI Testing'
    author = 'Test Author'
    published_year = 2025
    isbn = '978-1111111111'
    description = 'A guide to testing FastAPI applications'
} | ConvertTo-Json

Invoke-RestMethod -Uri 'http://localhost:8000/books/' -Method Post -Body $body -ContentType 'application/json'
```

#### 3. 특정 책 조회
```powershell
Invoke-RestMethod -Uri 'http://localhost:8000/books/1' -Method Get
```

#### 4. 책 정보 업데이트
```powershell
$body = @{
    id = 1
    title = 'Updated Python Programming'
    author = 'John Doe'
    published_year = 2024
    isbn = '978-1234567890'
    description = 'An updated comprehensive guide to Python'
} | ConvertTo-Json

Invoke-RestMethod -Uri 'http://localhost:8000/books/1' -Method Put -Body $body -ContentType 'application/json'
```

#### 5. 책 삭제
```powershell
Invoke-RestMethod -Uri 'http://localhost:8000/books/2' -Method Delete
```

### 예상 응답

#### 책 목록 조회 응답
```json
[
  {
    "id": 1,
    "title": "Python Programming",
    "author": "John Doe",
    "published_year": 2023,
    "isbn": "978-1234567890",
    "description": "A comprehensive guide to Python"
  },
  {
    "id": 2,
    "title": "FastAPI Master",
    "author": "Jane Smith",
    "published_year": 2024,
    "isbn": "978-0987654321",
    "description": "Learn FastAPI development"
  }
]
```

#### 삭제 응답
```json
{
  "message": "Book deleted successfully"
}
```

## 참고 자료
- [FastAPI 공식 문서](https://fastapi.tiangolo.com/)
- [Pydantic 문서](https://pydantic-docs.helpmanual.io/)
- [의존성 주입 가이드](https://fastapi.tiangolo.com/tutorial/dependencies/)
