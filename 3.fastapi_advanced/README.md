# FastAPI 고급 도서 관리 시스템

이 프로젝트는 FastAPI를 사용한 고급 도서 관리 시스템으로, 사용자 인증, 권한 관리, 데이터베이스 연동 등 실제 프로덕션 환경에서 필요한 다양한 기능을 포함하고 있습니다.

## 1. 프로젝트 구조

```
3.fastapi_advanced/
├── app/                        # 메인 애플리케이션 패키지
│   ├── api/                    # API 관련 코드
│   │   ├── v1/                # API 버전 1
│   │   │   ├── endpoints/     # 각 기능별 엔드포인트
│   │   │   │   ├── book.py    # 도서 관리 API
│   │   │   │   ├── login.py   # 인증 API
│   │   │   │   └── users.py   # 사용자 관리 API
│   │   │   └── router.py      # API 라우터 설정
│   │   └── dependencies/      # API 의존성 (인증 등)
│   │       └── auth.py        # 인증 관련 의존성
│   ├── core/                  # 핵심 설정
│   │   ├── config.py         # 환경 설정
│   │   └── security.py       # 보안 관련 유틸리티
│   ├── crud/                  # 데이터베이스 CRUD 작업
│   │   ├── book.py           # 도서 CRUD
│   │   └── user.py           # 사용자 CRUD
│   ├── db/                    # 데이터베이스 관련
│   │   ├── base.py           # 데이터베이스 설정
│   │   └── models/           # SQLAlchemy 모델
│   │       ├── book.py       # 도서 모델
│   │       └── user.py       # 사용자 모델
│   ├── schemas/              # Pydantic 스키마
│   │   ├── book.py          # 도서 스키마
│   │   └── user.py          # 사용자 스키마
│   └── main.py              # FastAPI 애플리케이션
├── tests/                    # 테스트 코드
│   └── api_test.py          # API 테스트
├── .env                     # 환경 변수
└── requirements.txt         # 의존성 목록
```

## 2. 주요 기능

1. **사용자 관리**
   - JWT 기반 인증
   - 역할 기반 접근 제어 (일반 사용자/관리자)
   - 비밀번호 해싱

2. **도서 관리**
   - 도서 CRUD 작업
   - 사용자별 도서 관리
   - 권한 기반 접근 제어

3. **보안**
   - CORS 설정
   - 비밀번호 암호화
   - 토큰 기반 인증

## 3. 설치 및 설정

### 3.1 가상환경 설정
```bash
# 가상환경 생성
python -m venv .venv

# 가상환경 활성화
.venv\Scripts\activate  # Windows
source .venv/bin/activate  # macOS/Linux

# 의존성 설치
pip install -r requirements.txt
```

### 3.2 환경 변수 설정
`.env` 파일을 생성하고 다음 내용을 설정합니다:

```env
# 데이터베이스 설정
DATABASE_URL=sqlite:///./sql_app.db    # SQLite 데이터베이스 경로

# 보안 설정
SECRET_KEY=your-secret-key-here        # JWT 토큰 암호화 키
ALGORITHM=HS256                        # JWT 암호화 알고리즘
ACCESS_TOKEN_EXPIRE_MINUTES=30         # 토큰 만료 시간(분)

# API 설정
API_V1_STR=/api/v1                    # API 버전 prefix
PROJECT_NAME=Advanced Book Management System

# 관리자 계정 설정
FIRST_SUPERUSER=admin@example.com     # 초기 관리자 이메일
FIRST_SUPERUSER_PASSWORD=admin123     # 초기 관리자 비밀번호
```

### 3.3 데이터베이스 초기화
```bash
# PYTHONPATH 설정 (프로젝트 루트 디렉토리로 설정)
$env:PYTHONPATH = "C:\workspace\fastapi\3.fastapi_advanced"  # Windows
export PYTHONPATH="/workspace/fastapi/3.fastapi_advanced"   # macOS/Linux

# 데이터베이스 초기화 및 관리자 계정 생성
python app/initial_data.py
```

### 3.4 서버 실행
```bash
# 개발 서버 실행 (자동 리로드 활성화)
python -m uvicorn app.main:app --reload

# 서버가 http://127.0.0.1:8000 에서 실행됩니다
```

## 4. API 문서
서버 실행 후 다음 URL에서 API 문서를 확인할 수 있습니다:
- Swagger UI: http://127.0.0.1:8000/api/v1/docs
- ReDoc: http://127.0.0.1:8000/api/v1/redoc

## 5. API 테스트

### 5.1 테스트 스크립트 실행
`tests/api_test.py` 파일을 사용하여 모든 API를 테스트할 수 있습니다:

```bash
# requests 패키지 설치 (필요한 경우)
pip install requests

# 테스트 실행
python tests/api_test.py
```

### 5.2 테스트 항목
1. **인증**
   - 로그인 및 JWT 토큰 발급
   - 토큰 유효성 검사

2. **도서 관리**
   - 도서 생성
   - 도서 목록 조회
   - 특정 도서 조회
   - 도서 정보 수정
   - 도서 삭제

### 5.3 예상 출력
```
Login Response:
Status Code: 200
Response: {"access_token": "...", "token_type": "bearer"}

Create Book Response:
Status Code: 200
Response: {"title": "FastAPI 완벽 가이드", ...}

... [기타 API 테스트 결과]
```

## 설치 및 실행 가이드

### 1. 환경 설정

```bash
# 가상환경 생성 및 활성화
python -m venv .venv
.venv\Scripts\activate  # Windows
source .venv/bin/activate  # macOS/Linux

# 의존성 설치
pip install -r requirements.txt
```

### 2. 환경 변수 설정

`.env` 파일을 생성하고 다음 내용을 설정합니다:

```env
# Database configuration
DATABASE_URL=sqlite:///./sql_app.db

# Security
SECRET_KEY=your-secret-key-here
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30

# API configuration
API_V1_STR=/api/v1
PROJECT_NAME=Advanced Book Management System

# Admin user
FIRST_SUPERUSER=admin@example.com
FIRST_SUPERUSER_PASSWORD=admin123
```

### 3. 데이터베이스 초기화

```bash
# PYTHONPATH 설정
$env:PYTHONPATH = "현재_프로젝트_경로"  # Windows
export PYTHONPATH="현재_프로젝트_경로"  # macOS/Linux

# 초기 데이터 생성
python app/initial_data.py
```

이 과정에서 다음이 수행됩니다:
- 데이터베이스 테이블 생성
- 관리자 계정 생성 (email: admin@example.com, password: admin123)

### 4. 서버 실행

```bash
python -m uvicorn app.main:app --reload
```

서버가 http://127.0.0.1:8000 에서 실행됩니다.

### 5. API 테스트 가이드

#### 5.1 API 테스트 실행

1. `tests/api_test.py` 파일을 생성했습니다. 이 파일은 모든 API 테스트를 순차적으로 실행합니다:
- 로그인 및 토큰 발급
- 책 생성
- 책 목록 조회
- 특정 책 조회
- 책 정보 수정
- 책 삭제

2. 테스트 실행 방법:

```bash
# requests 패키지 설치 (필요한 경우)
pip install requests

# 테스트 실행
python tests/api_test.py
```

3. 출력 형식:
```
Login Response:
Status Code: 200
Response: {"access_token": "...", "token_type": "bearer"}

Create Book Response:
Status Code: 200
Response: {"title": "FastAPI 완벽 가이드", ...}

... [기타 API 테스트 결과]
```

### 6. API 문서

- Swagger UI: http://127.0.0.1:8000/api/v1/docs
- ReDoc: http://127.0.0.1:8000/api/v1/redoc

## 주요 기능

1. **사용자 관리**
   - 회원가입/로그인
   - JWT 기반 인증
   - 권한 관리 (일반 사용자/관리자)

2. **도서 관리**
   - CRUD 작업
   - 사용자별 도서 관리
   - 권한 기반 접근 제어

3. **데이터베이스**
   - SQLAlchemy ORM
   - SQLite 데이터베이스 (개발용)
   - 마이그레이션 지원

4. **보안**
   - 비밀번호 해싱
   - JWT 토큰 인증
   - CORS 설정

## 프로젝트 구조

```
3.fastapi_advanced/
├── app/
│   ├── api/
│   │   ├── v1/
│   │   │   ├── endpoints/
│   │   │   │   ├── book.py
│   │   │   │   ├── login.py
│   │   │   │   └── users.py
│   │   │   └── router.py
│   │   └── dependencies/
│   │       └── auth.py
│   ├── core/
│   │   ├── config.py
│   │   └── security.py
│   ├── crud/
│   │   ├── book.py
│   │   └── user.py
│   ├── db/
│   │   ├── base.py
│   │   └── models/
│   │       ├── book.py
│   │       └── user.py
│   ├── schemas/
│   │   ├── book.py
│   │   └── user.py
│   └── main.py
├── .env
└── requirements.txt
```

## 시작하기

1. **환경 설정**
```bash
python -m venv .venv
.venv\Scripts\activate  # Windows
source .venv/bin/activate  # macOS/Linux
```

2. **의존성 설치**
```bash
pip install -r requirements.txt
```

3. **환경 변수 설정**
`.env` 파일을 수정하여 필요한 설정을 변경합니다.

4. **초기 데이터 생성**
```bash
python -m app.initial_data
```

5. **서버 실행**
```bash
uvicorn app.main:app --reload
```

## API 엔드포인트 상세

### 인증
- `POST /api/v1/login/access-token`
  - 로그인 및 토큰 발급
  - 요청 본문: `username`, `password`
  - 응답: `access_token`, `token_type`

- `POST /api/v1/login/test-token`
  - 토큰 유효성 테스트
  - 필요 헤더: `Authorization: Bearer {token}`
  - 응답: 현재 사용자 정보

### 사용자
- `GET /api/v1/users/`
  - 사용자 목록 조회 (관리자 전용)
  - 필요 헤더: `Authorization: Bearer {token}`
  - 응답: 사용자 목록

- `GET /api/v1/users/me`
  - 현재 사용자 정보 조회
  - 필요 헤더: `Authorization: Bearer {token}`
  - 응답: 현재 사용자 정보

### 도서
- `GET /api/v1/books/`
  - 도서 목록 조회
  - 필요 헤더: `Authorization: Bearer {token}`
  - 옵션 파라미터: `skip`, `limit`
  - 응답: 도서 목록

- `POST /api/v1/books/`
  - 새 도서 등록
  - 필요 헤더: `Authorization: Bearer {token}`
  - 요청 본문: `title`, `author`, `published_year`, `isbn`, `description`
  - 응답: 생성된 도서 정보

- `GET /api/v1/books/{book_id}`
  - 특정 도서 조회
  - 필요 헤더: `Authorization: Bearer {token}`
  - 응답: 도서 상세 정보

- `PUT /api/v1/books/{book_id}`
  - 도서 정보 수정
  - 필요 헤더: `Authorization: Bearer {token}`
  - 요청 본문: 수정할 필드들
  - 응답: 수정된 도서 정보

- `DELETE /api/v1/books/{book_id}`
  - 도서 삭제
  - 필요 헤더: `Authorization: Bearer {token}`
  - 응답: 삭제된 도서 정보

## API 문서
서버 실행 후 다음 URL에서 API 문서를 확인할 수 있습니다:
- Swagger UI: http://127.0.0.1:8000/docs
- ReDoc: http://127.0.0.1:8000/redoc

## 테스트

### 1. 관리자 로그인
```bash
curl -X POST "http://localhost:8000/api/v1/login/access-token" \
     -H "Content-Type: application/x-www-form-urlencoded" \
     -d "username=admin@example.com&password=admin123"
```

### 2. 도서 생성 (인증 필요)
```bash
curl -X POST "http://localhost:8000/api/v1/books/" \
     -H "Authorization: Bearer {your_token}" \
     -H "Content-Type: application/json" \
     -d '{
           "title": "FastAPI Advanced",
           "author": "FastAPI Team",
           "published_year": 2023,
           "isbn": "978-1234567890",
           "description": "Advanced FastAPI Guide"
         }'
```

## 보안 고려사항

1. **환경 변수**
   - 프로덕션 환경에서는 반드시 안전한 비밀키 사용
   - 데이터베이스 자격증명 보호

2. **인증**
   - JWT 토큰 만료 시간 적절히 설정
   - HTTPS 사용 권장

3. **데이터베이스**
   - 프로덕션 환경에서는 SQLite 대신 PostgreSQL 등 사용
   - 적절한 인덱싱 설정

## 다음 단계

1. **기능 개선**
   - 이메일 인증 추가
   - 비밀번호 재설정
   - 파일 업로드 (책 표지 등)

2. **성능 최적화**
   - 캐싱 구현
   - 데이터베이스 쿼리 최적화
   - 비동기 작업 처리

3. **배포**
   - Docker 컨테이너화
   - CI/CD 파이프라인 구축
   - 모니터링 시스템 구축
