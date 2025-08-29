from pathlib import Path
import sys

sys.path.append(str(Path(__file__).resolve().parents[1]))

from fastapi.testclient import TestClient
from sqlmodel import Session, select, delete

from app.main import app
from app.infra.database import engine, init_db
from app.models.db import CalcSnapshot


def get_client() -> TestClient:
    init_db()
    with Session(engine) as session:
        session.exec(delete(CalcSnapshot))
        session.commit()
    return TestClient(app)


def test_health() -> None:
    client = get_client()
    response = client.get("/api/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_calc_and_db_snapshot() -> None:
    client = get_client()
    response = client.get(
        "/api/calc",
        params={"date": "1984-02-02", "time": "00:00", "tz": "Asia/Seoul"},
    )
    assert response.status_code == 200
    assert response.json() == {
        "year": "癸亥",
        "month": "乙丑",
        "day": "丙寅",
        "time": "戊子",
    }
    with Session(engine) as session:
        rows = session.exec(select(CalcSnapshot)).all()
        assert len(rows) == 1
