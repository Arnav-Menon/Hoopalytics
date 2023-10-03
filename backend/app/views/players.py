# -*- coding: utf-8 -*-
import logging
from functools import partial

from rest_framework.response import Response
from rest_framework.views import APIView, exception_handler
from app.dbmodels import models
from django.http import Http404, HttpResponseNotFound
from rest_framework.decorators import api_view

LOGGER = logging.getLogger('django')

# http://127.0.0.1:8000/api/v1/playerSummary/{11}
class PlayerSummary(APIView):
    logger = LOGGER

    def get(self, request, playerID):
        """Return player data"""
        response = {}

        player_stats = models.Player_Stats.objects.filter(player_id=playerID)

        if not player_stats:

            raise Http404("Player ID doesn't exist. Please try a different one")

        else:

            response["name"] = player_stats[0].player.player_name

            games = []
            for ps in player_stats:
                game = {
                    "date": ps.game.game_date,
                    "isStarter": ps.is_starter,
                    "minutes": ps.minutes,
                    "points": ps.points,
                    "assists": ps.assists,
                    "offensiveRebounds": ps.offensive_rebounds,
                    "defensiveRebounds": ps.defensive_rebounds,
                    "steals": ps.steals,
                    "blocks": ps.blocks,
                    "turnovers": ps.turnovers,
                    "defensiveFouls": ps.defensive_fouls,
                    "offensiveFouls": ps.offensive_fouls,
                    "freeThrowsMade": ps.free_throws_made,
                    "freeThrowsAttempted": ps.free_throws_attempted,
                    "twoPointersMade": ps.two_pointers_made,
                    "twoPointersAttempted": ps.two_pointers_attempted,
                    "threePointersMade": ps.three_pointers_made,
                    "threePointersAttempted": ps.three_pointers_attempted
                }

                shots = []
                shots_for_player = models.Shot_Data.objects.filter(player_id=playerID, game_id=ps.game.game_id)
                for s in shots_for_player:
                    shot = {
                        "isMake": s.is_make,
                        "locationX": s.location_x,
                        "locationY": s.location_y,
                    }
                    shots.append(shot)

                game["shots"] = shots

                games.append(game)

            response["games"] = games

            return Response(response)
