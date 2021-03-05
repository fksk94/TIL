# 표준 라이브러리
from typing import Optional
import time
import urllib.request as req
# 서드파티 라이브러리
from bs4 import BeautifulSoup
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
import pandas as pd
import uvicorn
# 로컬
from database import crud, database, models, schemas
from dependency import get_db


models.Base.metadata.create_all(bind=database.engine)
app = FastAPI()


# 타입 명시 필수!
# 주식 현재가 국가 및 주가 id별 크롤링 코드
@app.get("/crawling/{nation}/{stock_id}/")
def crawling_current_stock(stock_id: int, nation: str):
    # 야후는 robots.txt를 보고 크롤링해도 되는 것 확인.
    code = '0' * (6 - len(str(stock_id))) + str(stock_id)
    url = "https://finance.yahoo.com/quote/" + code + "." + nation + "?p=" + code + "." + nation + "&.tsrc=fin-srch"
    html = req.urlopen(url).read()
    soup = BeautifulSoup(html, 'html.parser')
    point = soup.find_all(class_ = 'Mend(20px)')
    data = point[1].find('span')
    list_data = str(data).split('>')[1].split('<')[0].split('.')[0].split(',')
    res_data = 0

    for i in range(len(list_data) - 1, -1, -1):
        res_data += int(list_data[len(list_data) -1 - i]) * 1000 ** i

    now = time.localtime()
    return {"code":code, "year": now.tm_year, "month": now.tm_mon, "day":now.tm_mday, "current_stock": res_data}


# 주식 데이터 입력
@app.post("/store/")
def get_stock_data(stocks_data: schemas.BaseStocks, db: Session = Depends(get_db)):
    # 데이터 예외 처리 필요.
    return create_stocks_data(db=db, stocks_data=stocks_data)


# 주식 초기 데이터 입력
@app.get("/initdata/")
def create_init_stock(db: Session = Depends(get_db)):
    # 초기 데이터 예외 처리 필요.
    data = pd.read_csv('assets/005930.csv', usecols=['날짜', '종가'])
    data_list = data.values
    for i in range(len(data_list)):
        code = "005930"
        DL = data_list[i][0].split()
        year = int(DL[0].rstrip('년'))
        month = int(DL[1].rstrip('월'))
        day = int(DL[2].rstrip('일'))
        current_stock = 0
        list_data = data_list[i][1].split(',')
        for i in range(len(list_data) - 1, -1, -1):
            current_stock += int(list_data[len(list_data) -1 - i]) * 1000 ** i
        db_stocks = models.Stocks(code=code, year=year, month=month, day=day, current_stock=current_stock)
        db.add(db_stocks)
        db.commit()
    return len(data_list)


# 주식 데이터 생성
def create_stocks_data(db: Session, stocks_data: schemas.BaseStocks):
    db_stocks = models.Stocks(code=stocks_data.code, year=stocks_data.year, month=stocks_data.month, day=stocks_data.day, current_stock=stocks_data.current_stock)
    db.add(db_stocks)
    db.commit()
    db.refresh(db_stocks)
    return db_stocks


# 유저 생성
@app.post("/users", response_model=schemas.User)
def create_user2(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db=db, user=user)


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)