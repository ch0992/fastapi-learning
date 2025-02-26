from fastapi import FastAPI
from fastapi.testclient import TestClient

app = FastAPI()

@app.get("/")
async def read_root():
    return {"message": "Hello World"}

# TestClient 인스턴스 생성
client = TestClient(app)
# FastAPI 테스트를 위한 기본 설정 파일입니다.

# FastAPI: Python용 현대적이고 빠른 웹 프레임워크
# TestClient: FastAPI 애플리케이션을 테스트하기 위한 클라이언트

# client 객체를 통해 엔드포인트로 HTTP 요청을 보내고 응답을 검증할 수 있습니다.
# 이를 통해 API의 동작을 자동화된 방식으로 테스트할 수 있습니다.

def test_read_main():
    # "/" 경로에 GET 요청을 보냄
    response = client.get("/")
    print(response.status_code)
    print(response.json())

    # 응답 상태 코드가 200인지 확인
    assert response.status_code == 200        
    # 응답 JSON이 {"message": "Hello World"}인지 확인
    assert response.json() == {"message": "Hello World"}
