from fastapi import FastAPI
import random

app = FastAPI()

@app.get("/signal")
def get_signal():
    return {
        "symbol": "BTCUSDT",
        "signal": random.choice(["long", "short"]),
        "confidence": round(random.uniform(0.6, 0.9), 2)
    }
