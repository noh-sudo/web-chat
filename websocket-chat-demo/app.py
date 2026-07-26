# fast api 테스트용 진입점
''' 
uvicorn app:app --reload 로 실행,
app:app는 app.py 파일의 app 객체를 의미
디폴트 포트 8000, 주소값 로컬로 접속하면 메시지 확인 가능
'''
from fastapi import FastAPI

app = FastAPI()

@app.get("/")   # 홈 엔드포인트 (시작 페이지)
def home():
    return {"message": "FastAPI WebSocket 채팅 테스트"}