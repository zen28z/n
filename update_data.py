import yfinance as yf
import json
import math

def fetch_and_calculate():
    # 1. 株価と為替の取得
    nvda_ticker = yf.Ticker("NVDA")
    usdjpy_ticker = yf.Ticker("JPY=X")

    # 休場日（土日や祝日）を考慮し、余裕を持って過去5日分のデータを取得します
    nvda_hist = nvda_ticker.history(period="5d")['Close']
    usdjpy_hist = usdjpy_ticker.history(period="5d")['Close']

    # 最新の終値（後ろから1番目）と前日の終値（後ろから2番目）を取得
    nvda_price = nvda_hist.iloc[-1]
    nvda_prev = nvda_hist.iloc[-2]
    
    usdjpy_price = usdjpy_hist.iloc[-1]
    usdjpy_prev = usdjpy_hist.iloc[-2]

    # 2. 定数の設定
    SHARES = 241
    COST_BASIS = 7590421

    # 3. 計算（円単位で切り捨て）
    # 最新の評価額と損益
    market_value = math.floor(nvda_price * usdjpy_price * SHARES)
    profit_loss = market_value - COST_BASIS
    
    # 前日の評価額（前日比計算用）
    prev_market_value = math.floor(nvda_prev * usdjpy_prev * SHARES)
    
    # 評価額の前日比（円）
    day_over_day_change = market_value - prev_market_value

    # 4. JSONとして保存
    data = {
        "nvda_price": round(nvda_price, 2),
        "nvda_price_prev": round(nvda_prev, 2),         # 追加: 前日の株価
        "usd_jpy": round(usdjpy_price, 2),
        "usd_jpy_prev": round(usdjpy_prev, 2),          # 追加: 前日の為替
        "market_value": market_value,
        "profit_loss": profit_loss,
        "day_over_day_change": day_over_day_change      # 追加: 評価額の前日比（増減額）
    }

    with open('data.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    fetch_and_calculate()
