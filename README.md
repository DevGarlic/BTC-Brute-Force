# Bitcoin Brute-Force
비트코인의 니모닉 경우의 수는 2^256으로 이를 전부 확인하려면 우주의 나이보다 더 많은 시간이 걸립니다
![image](https://github.com/DevGarlic/BTC-Brute-Force/assets/155062121/cb4397ca-ae87-4806-b320-760573de927f)

# How to use
```python
pip install -r requirements.txt
```
```python
python main.py
```

# How to work
랜덤으로 프라이빗키를 생성해 지갑을 만든 후 잔액을 확인합니다
잔액이 확인된 지갑을 찾으면 FoundWallet.txt에 지갑의 정보와 프라이빗키를 저장합니다

# 주의사항
해당 프로젝트는 비트코인의 보안검증을 위해 개발되었으며 프로그램을 사용하여 생기는 법적 책임은 사용자에게 있습니다
