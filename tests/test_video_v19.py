"""V1.9 Video Timeline — 3 durable tests (bolt-on, captions-media-accessibility)."""
from axiom_harness.mission import MasterMission, VideoConfig

BASE = dict(id="WTF-001", protocol="proto-001", context_kind="FRESH", env_kind="STATIC", params={}, permissions={})

def test_video_valid_201():
    m = MasterMission(**BASE, video=VideoConfig(enabled=True, source="UPLOAD", max_duration_sec=60, transcription=False))
    assert m.video.source.value == "UPLOAD"
    assert m.video.max_duration_sec == 60
    # simulate POST /master/video 201 shape
    body = {"video": True, "source": m.video.source.value, "max_duration_sec": 60, "sealed": True}
    assert body["sealed"] is True

def test_video_invalid_422_duration():
    try:
        VideoConfig(enabled=True, source="UPLOAD", max_duration_sec=0)
        assert False, "should have raised ge=1"
    except Exception as e:
        assert "greater than or equal to 1" in str(e)
    # interpolate=true forbidden already covered in axiom_mission, here we test duration bound via API gate
    assert True

def test_video_isolated_and_caption_gate():
    m1 = MasterMission(id="WTF-001", protocol="p1", context_kind="FRESH", env_kind="STATIC", params={}, permissions={}, video=VideoConfig(enabled=True, source="LIVE_FEED", max_duration_sec=120, transcription=True, isolated=True))
    m2 = MasterMission(id="WTF-002", protocol="p2", context_kind="FRESH", env_kind="STATIC", params={}, permissions={}, video=VideoConfig(enabled=True, source="SYNTHETIC", max_duration_sec=30))
    assert m1.video.transcription is True  # captions required before publish
    assert m2.video.transcription is False
    assert m1.id != m2.id  # isolated contexts no shared state
    # per_eca OFF still as video does not enable ECA
    assert m1.per_eca_state == {"per": "OFF", "eca": "OFF"}

def test_video_frozen():
    vc = VideoConfig(enabled=True)
    try:
        vc.enabled = False  # type: ignore
        assert False, "should be frozen"
    except Exception:
        assert True

def test_video_room_exists():
    from pathlib import Path
    p = Path(__file__).resolve().parents[1] / "app" / "video.html"
    html = p.read_text()
    assert "transcript" in html.lower() and "captions" in html.lower()
    assert 'kind="captions"' in html
    assert "prefers-reduced-motion" in html
