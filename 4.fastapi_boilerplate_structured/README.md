# FastAPI Boilerplate with Structured Project Layout

이 프로젝트는 FastAPI를 사용한 구조화된 보일러플레이트입니다.

## 프로젝트 구조

```
.
├── app/
│   ├── main.py          # FastAPI 애플리케이션 및 설정
│   ├── models/          # Pydantic 모델
│   ├── routers/         # API 라우터
│   └── services/        # 비즈니스 로직
└── requirements.txt     # 프로젝트 의존성
```

## 설치 방법

1. 가상환경 생성 및 활성화:
```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

2. 의존성 설치:
```bash
pip install -r requirements.txt
```

## 실행 방법

```bash
uvicorn app.main:app --reload
```

서버가 시작되면 다음 URL에서 API를 확인할 수 있습니다:
- API 문서: http://localhost:8000/docs
- ReDoc 문서: http://localhost:8000/redoc

## API 엔드포인트

- GET /items - 모든 아이템 조회
- GET /items/{item_id} - 특정 아이템 조회
- POST /items - 새 아이템 생성
- PUT /items/{item_id} - 아이템 수정
- DELETE /items/{item_id} - 아이템 삭제
