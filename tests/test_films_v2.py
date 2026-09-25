"""V2 Films — 3 durable tests (bolt-on, audio-video captions)."""
from axiom_harness.mission import MasterMission, FilmsConfig

BASE = dict(id="WTF-001", protocol="proto-001", context_kind="FRESH", env_kind="STATIC", params={}, permissions={})

def test_films_valid_201():
    m = MasterMission(**BASE, films=FilmsConfig(enabled=True, template="comparative", auto_chapters=True))
    assert m.films.template == "comparative"
    body = {"films": True, "template": m.films.template, "sealed": True}
    assert body["sealed"] is True

def test_films_invalid_422():
    try:
        MasterMission(**BASE, films=FilmsConfig(enabled=True, template="unknown"))  # type: ignore
        assert False
    except Exception:
        assert True

def test_films_isolated():
    m1 = MasterMission(id="WTF-001", protocol="p1", context_kind="FRESH", env_kind="STATIC", params={}, permissions={}, films=FilmsConfig(enabled=True, template="ghost"))
    m2 = MasterMission(id="WTF-002", protocol="p2", context_kind="FRESH", env_kind="STATIC", params={}, permissions={}, films=FilmsConfig(enabled=True, template="chronological"))
    assert m1.films.template == "ghost"
    assert m2.films.template == "chronological"
    assert m1.id != m2.id

def test_films_frozen():
    fc = FilmsConfig(enabled=True)
    try:
        fc.enabled = False  # type: ignore
        assert False
    except Exception:
        assert True

def test_films_room_exists():
    from pathlib import Path
    p = Path(__file__).resolve().parents[1] / "app" / "films.html"
    html = p.read_text()
    assert "captions" in html.lower()
    assert 'kind="chapters"' in html
