import yfinance as yf
import json
import math

def fetch_and_calculate():
    # 1. 株価と為替の取得
    nvda_ticker = yf.Ticker("NVDA")
    usdjpy_ticker = yf.Ticker("JPY=X")

    # 最新の終値を取得
    nvda_price = nvda_ticker.history(period="1d")['Close'].iloc[0]
    usdjpy_price = usdjpy_ticker.history(period="1d")['Close'].iloc[0]

    # 2. 定数の設定
    SHARES = 241
    COST_BASIS = 7590421

    # 3. 計算（円単位で切り捨て）
    market_value = math.floor(nvda_price * usdjpy_price * SHARES)
    profit_loss = market_value - COST_BASIS

    # 4. JSONとして保存
    data = {
        "nvda_price": round(nvda_price, 2),
        "usd_jpy": round(usdjpy_price, 2),
        "market_value": market_value,
        "profit_loss": profit_loss
    }

    with open('data.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    fetch_and_calculate()
