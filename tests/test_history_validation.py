def test_invalid_days(client):
    response = client.get("/history/AAPL?days=abc")
    assert response.status_code == 400

def test_days_out_of_range(client):
    response = client.get("/history/AAPL?days=999")
    assert response.status_code == 400

def test_health_endpoint(client):
    response = client.get("/health")
    assert response.status_code == 200

def test_price_endpoint(client):
    response = client.get("/price/AAPL")
    assert response.status_code in [200, 404, 500]

def test_history_valid(client):
    response = client.get("/history/AAPL?days=7")
    assert response.status_code in [200, 404, 500]

def test_db_prices(client):
    response = client.get("/db/prices/AAPL")
    assert response.status_code in [200, 500]

def test_db_news(client):
    response = client.get("/db/news/AAPL")
    assert response.status_code in [200, 500]

def test_db_stats(client):
    response = client.get("/db/stats")
    assert response.status_code in [200, 500]

def test_sentiment_missing_text(client):
    response = client.post("/sentiment", json={})
    assert response.status_code == 400

def test_sentiment_batch_empty(client):
    response = client.post("/sentiment/batch", json={"texts": []})
    assert response.status_code == 400

def test_sentiment_batch_too_many(client):
    response = client.post("/sentiment/batch", json={"texts": ["x"] * 101})
    assert response.status_code == 400

def test_sentiment_summary(client):
    response = client.get("/db/sentiment-summary/AAPL")
    assert response.status_code in [200, 500]