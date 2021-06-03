from rbaas.boss.actions import get_boss_health, decrement_boss_health

class TestActions:
    def test_get_health(self):
        assert get_boss_health() == 'Heres yo\' health'

    def test_decrement_boss_health(self):
        assert decrement_boss_health() == 'Health -1'