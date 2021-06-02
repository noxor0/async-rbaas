from rbaas.boss.actions import get_boss_health, decrement_boss_health

class TestActions:
    def test_get_health():
        assert 'Heres yo\' health' == get_boss_health()