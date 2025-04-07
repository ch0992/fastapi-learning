# HTTP 요청을 위한 requests 라이브러리
import requests
# JSON 데이터 처리를 위한 json 모듈
import json

def test_api():
    """모든 API 엔드포인트를 순차적으로 테스트합니다.
    
    테스트 순서:
    1. 로그인 및 JWT 토큰 발급
    2. 새로운 책 생성
    3. 책 목록 조회
    4. 특정 책 조회
    5. 책 정보 업데이트
    6. 책 삭제
    """
    
    # 1. 관리자 계정으로 로그인하여 JWT 토큰 발급 받기
    response = requests.post(
        # 로그인 API 엔드포인트
        'http://127.0.0.1:8000/api/v1/login/access-token',
        # 로그인 정보 (관리자 계정)
        data={
            'username': 'admin@example.com',  # 관리자 이메일
            'password': 'admin123'  # 관리자 비밀번호
        },
        # 폼 데이터 형식으로 전송
        headers={'Content-Type': 'application/x-www-form-urlencoded'}
    )
    # 응답 출력
    print('Login Response:')
    print(f'Status Code: {response.status_code}')
    print(f'Response: {response.text}')

    # 발급받은 JWT 토큰을 헤더에 설정
    token = response.json()['access_token']
    headers = {
        # Bearer 토큰 인증 방식 사용
        'Authorization': f'Bearer {token}',
        # JSON 데이터 형식 사용
        'Content-Type': 'application/json'
    }

    # 2. 새로운 책 생성
    # 생성할 책 정보
    book_data = {
        'title': 'FastAPI 완벽 가이드',  # 책 제목
        'author': '홍길동',  # 저자
        'published_year': 2024,  # 출판년도
        'isbn': '978-89-98-76543-2-1',  # ISBN
        'description': 'FastAPI를 이용한 웹 애플리케이션 개발 가이드'  # 설명
    }

    # POST 요청으로 새 책 생성
    response = requests.post(
        # 책 생성 API 엔드포인트
        'http://127.0.0.1:8000/api/v1/books/',
        # 인증 및 콘텐츠 타입 헤더
        headers=headers,
        # 책 데이터를 JSON으로 직렬화하여 전송
        json=book_data
    )
    # 응답 출력
    print('\nCreate Book Response:')
    print(f'Status Code: {response.status_code}')
    print(f'Response: {response.text}')

    # 3. 전체 책 목록 조회
    response = requests.get(
        # 책 목록 조회 API 엔드포인트
        'http://127.0.0.1:8000/api/v1/books/',
        # 인증 헤더 포함
        headers=headers
    )
    # 응답 출력
    print('\nList Books Response:')
    print(f'Status Code: {response.status_code}')
    print(f'Response: {response.text}')

    # 4. ID가 1인 책의 상세 정보 조회
    response = requests.get(
        # 책 상세 정보 조회 API 엔드포인트 (ID: 1)
        'http://127.0.0.1:8000/api/v1/books/1',
        # 인증 헤더 포함
        headers=headers
    )
    # 응답 출력
    print('\nGet Book Detail Response:')
    print(f'Status Code: {response.status_code}')
    print(f'Response: {response.text}')

    # 5. 책 정보 업데이트
    # 업데이트할 내용 (설명만 변경)
    update_data = {
        'description': '업데이트된 설명: FastAPI를 이용한 현대적인 웹 API 개발 가이드'
    }

    # PUT 요청으로 책 정보 업데이트
    response = requests.put(
        # 책 업데이트 API 엔드포인트 (ID: 1)
        'http://127.0.0.1:8000/api/v1/books/1',
        # 인증 및 콘텐츠 타입 헤더
        headers=headers,
        # 업데이트할 데이터를 JSON으로 직렬화하여 전송
        json=update_data
    )
    # 응답 출력
    print('\nUpdate Book Response:')
    print(f'Status Code: {response.status_code}')
    print(f'Response: {response.text}')

    # 6. 책 삭제
    response = requests.delete(
        # 책 삭제 API 엔드포인트 (ID: 1)
        'http://127.0.0.1:8000/api/v1/books/1',
        # 인증 헤더 포함
        headers=headers
    )
    # 응답 출력
    print('\nDelete Book Response:')
    print(f'Status Code: {response.status_code}')
    print(f'Response: {response.text}')

# 스크립트로 직접 실행하는 경우
# python api_test.py
if __name__ == '__main__':
    test_api()
