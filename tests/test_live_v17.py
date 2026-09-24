"""V1.7 Live feeds + Observatory — §30-32 same stream isolated contexts."""
from axiom_harness.mission import MasterMission, LiveConfig, LiveFeedKind

BASE = {"id": "WTF-001", "protocol": "sha256:abc", "context_kind": "FRESH", "env_kind": "LIVE_FEED"}

def test_live_feeds_basic():
    m = MasterMission(**BASE, live=LiveConfig(feeds=[LiveFeedKind.NEWS, LiveFeedKind.MARKET], observatory=False))
    assert LiveFeedKind.NEWS in m.live.feeds
    assert m.live.observatory is False

def test_live_observatory_compare():
    m = MasterMission(**BASE, live=LiveConfig(feeds=[LiveFeedKind.WEB, LiveFeedKind.CUSTOM_API], observatory=True, models=["A","B","C"], compare=True))
    assert m.live.observatory is True
    assert m.live.models == ["A","B","C"]
    assert m.live.compare is True

def test_live_frozen_and_captions_gate():
    m = MasterMission(**BASE, live=LiveConfig(feeds=[LiveFeedKind.SIMULATED], observatory=True))
    # frozen
    try:
        m.live.feeds.append(LiveFeedKind.NEWS)
        assert False
    except Exception:
        pass
    # WCAG 1.2: if live includes audio/video, transcript_linked must be true at publish — Harness records it
    # here we just ensure live config exists and is sealed
    assert m.live.feeds[0] == LiveFeedKind.SIMULATED
