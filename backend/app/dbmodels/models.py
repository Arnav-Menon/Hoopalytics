# -*- coding: utf-8 -*-
"""Contains models related to stats"""
from django.db import models

class Games(models.Model):
    game_id = models.IntegerField(primary_key=True)
    game_date = models.DateField()

class Teams(models.Model):
    team_id = models.IntegerField(primary_key=True)
    team_name = models.CharField(max_length=50)

class Players(models.Model):
    player_id = models.IntegerField(primary_key=True)
    player_name = models.CharField(max_length=100)

class Player_Stats(models.Model):
    team = models.ForeignKey("Teams", on_delete=models.CASCADE)
    game = models.ForeignKey("Games", on_delete=models.CASCADE)
    player = models.ForeignKey("Players", on_delete=models.CASCADE)
    is_starter = models.BooleanField(default=True)
    minutes = models.IntegerField(default=0)
    points = models.IntegerField(default=0)
    assists = models.IntegerField(default=0)
    offensive_rebounds = models.IntegerField(default=0)
    defensive_rebounds = models.IntegerField(default=0)
    steals = models.IntegerField(default=0)
    blocks = models.IntegerField(default=0)
    turnovers = models.IntegerField(default=0)
    defensive_fouls = models.IntegerField(default=0)
    offensive_fouls = models.IntegerField(default=0)
    free_throws_made = models.IntegerField(default=0)
    free_throws_attempted = models.IntegerField(default=0)
    two_pointers_made = models.IntegerField(default=0)
    two_pointers_attempted = models.IntegerField(default=0)
    three_pointers_made = models.IntegerField(default=0)
    three_pointers_attempted = models.IntegerField(default=0)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["game", "player"], name="unique_migration_host_combination"
            )
        ]

class Shot_Data(models.Model):
    shot_data_id = models.IntegerField(primary_key=True)
    game = models.ForeignKey("Games", on_delete=models.CASCADE)
    player = models.ForeignKey("Players", on_delete=models.CASCADE)
    is_make = models.BooleanField()
    location_x = models.FloatField()
    location_y = models.FloatField()