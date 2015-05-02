__author__ = 'bob'

import unittest
from django.test import TestCase
from armory import models


class TestWinrate100Percent(TestCase):
    def setUp(self):
        for i in xrange(10):
            p = models.Participant(summonerId=i, champion=1, spell1Id=1, spell2Id=2, teamId=001, matchId=i)
            p.save()
            ps = models.ParticipantStats(winner=1)
            ps.save()
            ps.participant.add(p)
        self.champ = models.Champions(id=1, name="Testy")
        self.champ.save()

    def test_single_champ_win_rate_100_percent(self):
        self.assertEqual(self.champ.winrate, 100)

    def test_two_champ_win_rate_100_percent(self):
        for i in xrange(5):
            p = models.Participant(summonerId=i, champion=2, spell1Id=1, spell2Id=2, teamId=001, matchId=i)
            p.save()
        self.champ2 = models.Champions(id=2, name="Testy")
        self.champ2.save()
        self.assertEqual(self.champ.winrate, 100)
        self.assertEqual(self.champ2.winrate, 100)


class TestWinrate50Percent(TestCase):
    def setUp(self):
        for i in xrange(10):
            win = 1
            p = models.Participant(summonerId=i, champion=1, spell1Id=1, spell2Id=2, teamId=001, matchId=i)
            p.save()
            if i % 2:
                win = 0
            ps = models.ParticipantStats(winner=win)
            ps.save()
            ps.participant.add(p)
        self.champ = models.Champions(id=1, name="Testy")
        self.champ.save()

        for i in xrange(10, 20):
            win = 1
            p = models.Participant(summonerId=i, champion=2, spell1Id=1, spell2Id=2, teamId=001, matchId=i)
            p.save()
            if i % 2:
                win = 0
            ps = models.ParticipantStats(winner=win)
            ps.save()
            ps.participant.add(p)
        self.champ2 = models.Champions(id=2, name="Testy")
        self.champ2.save()

    def test_two_champ_win_rate_50_percent(self):
        self.assertEqual(self.champ.winrate, 50)
        self.assertEqual(self.champ2.winrate, 50)


class TestWinrate80Percent(TestCase):
    def setUp(self):
        for i in xrange(10):
            win = 1
            p = models.Participant(summonerId=i, champion=1, spell1Id=1, spell2Id=2, teamId=001, matchId=i)
            p.save()
            if i == 1 or i == 0:
                win = 0
            ps = models.ParticipantStats(winner=win)
            ps.save()
            ps.participant.add(p)
        self.champ = models.Champions(id=1, name="Testy")
        self.champ.save()

        for i in xrange(10, 20):
            win = 1
            p = models.Participant(summonerId=i, champion=2, spell1Id=1, spell2Id=2, teamId=001, matchId=i)
            p.save()
            if i == 10 or i == 11:
                win = 0
            ps = models.ParticipantStats(winner=win)
            ps.save()
            ps.participant.add(p)
        self.champ2 = models.Champions(id=2, name="Testy")
        self.champ2.save()

    def test_two_champ_win_rate_80_percent(self):

        self.assertEqual(self.champ.winrate, 80)
        self.assertEqual(self.champ2.winrate, 80)


if __name__ == '__main__':
    unittest.main()
