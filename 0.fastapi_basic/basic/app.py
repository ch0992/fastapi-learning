# FastAPI와 테스트 클라이언트 임포트
from fastapi import FastAPI  # FastAPI: 현대적인 파이썬 웹 프레임워크
from fastapi.testclient import TestClient  # TestClient: API 테스트를 위한 클라이언트

# FastAPI 애플리케이션 인스턴스 생성
app = FastAPI()

# 루트 경로("/")에 대한 GET 요청 핸들러
# async def: 비동기 함수 정의
# @app.get("/"): 데코레이터를 사용하여 라우트 등록
@app.get("/")
async def read_root():
    # JSON 형식으로 응답 반환
    return {"message": "Hello World"}

# TestClient 인스턴스 생성
# 이를 통해 FastAPI 애플리케이션을 테스트할 수 있음
client = TestClient(app)

# API 엔드포인트 테스트 함수
def test_read_main():
    # 1. API 요청 보내기
    # "/" 경로로 GET 요청을 보내고 응답을 받음
    response = client.get("/")
    
    # 2. 상태 코드 검증
    # HTTP 200 OK는 요청이 성공적으로 처리되었음을 의미
    assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"
    
    # 3. 응답 데이터 검증
    # response.json()으로 JSON 응답을 파이썬 딕셔너리로 변환
    response_json = response.json()
    assert response_json == {"message": "Hello World"}, f"Expected JSON {{'message': 'Hello World'}}, but got {response_json}"
    
    # 4. 응답 헤더 검증
    # Content-Type이 application/json인지 확인
    assert response.headers["content-type"] == "application/json", f"Expected content-type 'application/json', but got {response.headers['content-type']}"
    
    # 5. 성능 검증
    # 응답 시간이 0.5초(500ms) 미만인지 확인
    assert response.elapsed.total_seconds() < 0.5, f"Response time exceeded 500ms: {response.elapsed.total_seconds()}s"
    
    # 6. 테스트 결과 출력
    # 상세한 응답 정보를 콘솔에 출력
    print(f"Status Code: {response.status_code}")
    print(f"Response JSON: {response_json}")
    print(f"Response Headers: {response.headers}")
    print(f"Response Time: {response.elapsed.total_seconds()}s")
