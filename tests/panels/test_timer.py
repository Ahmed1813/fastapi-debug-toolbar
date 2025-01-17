from ..mark import override_panels
from ..testclient import TestClient

try:
    import resource
except ImportError:
    resource = None


@override_panels(["debug_toolbar.panels.timer.TimerPanel"])
def test_timer(client: TestClient) -> None:
    store_id = client.get_store_id("/async")
    stats = client.get_stats(store_id, "TimerPanel")

    if resource is not None:
        assert "total" in stats
