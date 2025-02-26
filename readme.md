
# FastAPI 프로젝트

## 프로젝트 구조

```
fastapi/
├── app.py
├── test/
│   ├── __init__.py
│   ├── test.py
```




## 실행 방법

### 1. 가상환경 설정 및 의존성 설치

```
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```



### 2. 서버 실행

```
uvicorn app:app --reload
```







