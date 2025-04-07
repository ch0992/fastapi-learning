# FastAPI 시작하기

이 프로젝트는 FastAPI를 처음 시작하는 분들을 위한 가장 기본적인 예제입니다. 간단한 "Hello World" API를 만들고 테스트하는 방법을 배워봅시다.

## 프로젝트 설명

이 프로젝트는 다음과 같은 내용을 포함하고 있습니다:

1. 간단한 FastAPI 서버 생성
2. API 엔드포인트 구현
3. API 테스트 코드 작성
4. 자동화된 테스트 실행

## 시작하기 전에 알아야 할 것들

### FastAPI란?
FastAPI는 현대적이고 빠른 웹 API를 만들기 위한 파이썬 프레임워크입니다. 다음과 같은 장점이 있습니다:
- 빠른 성능
- 자동 API 문서 생성
- 파이썬 타입 힌트 사용
- 비동기 프로그래밍 지원

### 비동기 프로그래밍이란?
`async`/`await` 키워드를 사용하는 비동기 프로그래밍은 동시에 여러 작업을 처리할 수 있게 해줍니다. 
예를 들어, 우리의 코드에서 `async def read_root()`는 비동기 함수입니다.

## 프로젝트 구조
```
0.fastapi_basic/
├── basic/
│   └── app.py      # 메인 애플리케이션 코드
└── README.md       # 프로젝트 설명서
```

## 코드 설명

### 1. FastAPI 애플리케이션 생성
```python
from fastapi import FastAPI
app = FastAPI()
```
- `FastAPI()`: FastAPI 애플리케이션 인스턴스를 생성합니다.

### 2. API 엔드포인트 정의
```python
@app.get("/")
async def read_root():
    return {"message": "Hello World"}
```
- `@app.get("/")`: 루트 경로("/")에 대한 GET 요청을 처리하는 데코레이터
- `async def`: 비동기 함수 선언
- `return {"message": "Hello World"}`: JSON 형식으로 응답 반환

### 3. API 테스트
```python
from fastapi.testclient import TestClient
client = TestClient(app)

def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
```
- `TestClient`: FastAPI 애플리케이션을 테스트하기 위한 클라이언트
- `client.get("/")`: GET 요청 보내기
- `assert`: 테스트 조건 확인

## 실행 방법

### 1. 필요한 패키지 설치
```bash
pip install fastapi uvicorn pytest httpx
```

### 2. 서버 실행
```bash
uvicorn basic.app:app --reload
```
- `--reload`: 코드 변경 시 자동으로 서버 재시작

### 3. API 테스트
```bash
python -m pytest basic/app.py -v
```

## API 사용해보기

서버가 실행되면 다음 URL에서 API를 확인할 수 있습니다:

1. API 접속: http://127.0.0.1:8000
   - 응답: `{"message": "Hello World"}`

2. API 문서 보기:
   - Swagger UI: http://127.0.0.1:8000/docs
   - ReDoc: http://127.0.0.1:8000/redoc

## 배운 내용

이 예제를 통해 다음 내용을 배웠습니다:
1. FastAPI로 간단한 API 서버 만들기
2. 비동기 함수 사용하기
3. JSON 형식으로 응답 반환하기
4. API 테스트 코드 작성하기
5. 자동화된 테스트 실행하기

## 다음 단계

이제 기본적인 FastAPI 사용법을 배웠으니, 다음과 같은 것들을 시도해보세요:
1. 새로운 엔드포인트 추가하기
2. 경로 매개변수 사용하기
3. 요청 본문(Request Body) 처리하기
4. 더 많은 테스트 케이스 작성하기

## 도움이 되는 자료
- [FastAPI 공식 문서](https://fastapi.tiangolo.com/)
- [FastAPI 튜토리얼](https://fastapi.tiangolo.com/tutorial/)
- [Python 비동기 프로그래밍](https://docs.python.org/ko/3/library/asyncio.html)
