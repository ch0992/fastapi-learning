# FastAPI Learning Path

이 저장소는 FastAPI를 사용한 웹 API 개발의 단계별 학습 경로를 제공합니다. 기초부터 고급 기능까지 체계적으로 구성되어 있습니다.

## 프로젝트 구조

```
fastapi/
├── 0.fastapi_basic/        # FastAPI 기초
├── 1.fastapi_basic_crud/   # 기본적인 CRUD 구현
├── 2.fastapi_structured/   # 구조화된 프로젝트
└── 3.fastapi_advanced/     # 고급 기능 구현
```

## 단계별 설명

### 0. FastAPI 기초 (0.fastapi_basic)
- FastAPI의 기본 개념과 사용법 학습
- 간단한 엔드포인트 생성
- 요청/응답 모델 이해
- 경로 매개변수와 쿼리 매개변수 사용

### 1. 기본 CRUD (1.fastapi_basic_crud)
- 기본적인 CRUD(Create, Read, Update, Delete) 작업 구현
- Pydantic 모델을 사용한 데이터 검증
- 메모리 기반의 간단한 데이터 저장소 사용
- HTTP 메서드 활용 (GET, POST, PUT, DELETE)

### 2. 구조화된 프로젝트 (2.fastapi_structured)
- 모듈화된 프로젝트 구조 설계
- 라우터를 사용한 엔드포인트 그룹화
- 서비스 레이어 패턴 적용
- 의존성 주입 기초

### 3. 고급 기능 구현 (3.fastapi_advanced)
- SQLAlchemy를 사용한 데이터베이스 통합
- JWT 기반 사용자 인증
- CORS 미들웨어 설정
- 환경 변수 관리
- 사용자 권한 관리
- 테스트 코드 작성
- API 문서화 (Swagger/ReDoc)

## 실행 방법

각 프로젝트 폴더에는 자체 `requirements.txt` 파일이 있습니다. 다음 단계를 따라 실행하세요:

1. 가상 환경 생성 및 활성화
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\\Scripts\\activate   # Windows
```

2. 의존성 설치
```bash
pip install -r requirements.txt
```

3. 애플리케이션 실행
```bash
uvicorn app.main:app --reload
```

## API 문서

각 프로젝트를 실행한 후, 다음 URL에서 API 문서를 확인할 수 있습니다:
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## 라이선스

이 프로젝트는 MIT 라이선스 하에 배포됩니다. 자세한 내용은 LICENSE 파일을 참조하세요.
