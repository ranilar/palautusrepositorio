import unittest
from statistics_service import StatisticsService
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        # annetaan StatisticsService-luokan oliolle "stub"-luokan olio
        self.stats = StatisticsService(
            PlayerReaderStub()
        )

    def test_etsi_pelaaja(self):
        player = self.stats.search("Lemieux")
        self.assertIsNotNone(player)
        self.assertAlmostEqual(player.name, "Lemieux")

    def test_pelaaja_ei_loydy(self):
        player = self.stats.search("Nonexistent Player")
        self.assertIsNone(player)

    def test_palauta_oikea(self):
        team_players = self.stats.team("EDM")
        team_player_names = [player.name for player in team_players]
        self.assertAlmostEqual(len(team_players), 3)
        self.assertIn("Semenko", team_player_names)
        self.assertIn("Kurri", team_player_names)
        self.assertIn("Gretzky", team_player_names)

    def test_ei_pelaajia(self):
        team_players = self.stats.team("NYR")
        self.assertAlmostEqual(len(team_players), 0)

    def test_parhaat_pelaajat(self):
        top_players = self.stats.top(2)
        top_player_names = [player.name for player in top_players]
        self.assertAlmostEqual(len(top_players), 3)  
        self.assertAlmostEqual(top_player_names[0], "Gretzky")
        self.assertAlmostEqual(top_player_names[1], "Lemieux")
        self.assertAlmostEqual(top_player_names[2], "Yzerman")

    def test_palauta_gretzky(self):
        top_players = self.stats.top(0)
        self.assertAlmostEqual(len(top_players), 1)
        self.assertAlmostEqual(top_players[0].name, "Gretzky")
