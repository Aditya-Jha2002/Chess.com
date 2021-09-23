from chessdotcom import get_player_game_archives
import csv
import requests
import os
from tqdm import tqdm


class User:
    def __init__(self, username, path_to_csv):
        self.username = username
        self.path_to_csv = path_to_csv

    def get_games_url(self):
        data = get_player_game_archives(self.username).json
        url = data["archives"]
        return url

    def create_csv(self):

        with open(os.path.join(self.path_to_csv, "games.csv"), "a") as csv_file:
            csv_writer = csv.writer(csv_file, delimiter=",")
            urls = self.get_games_url()
            for url in tqdm(
                urls, total=len(urls), desc="Month", position=1, leave=False
            ):
                games = requests.get(url).json()
                for game in games["games"][:]:
                    try:
                        white_username = game["white"]["username"]
                        black_username = game["black"]["username"]
                        white_id = game["white"]["@id"]
                        black_id = game["black"]["@id"]
                        white_rating = game["white"]["rating"]
                        black_rating = game["black"]["rating"]
                        white_result = game["white"]["result"]
                        black_result = game["black"]["result"]
                        time_class = game["time_class"]
                        time_control = game["time_control"]
                        rated = game["rated"]
                        rules = game["rules"]
                        fen = game["fen"]
                        pgn = game["pgn"]
                    except:
                        continue
                    csv_writer.writerow(
                        (
                            white_username,
                            black_username,
                            white_id,
                            black_id,
                            white_rating,
                            black_rating,
                            white_result,
                            black_result,
                            time_class,
                            time_control,
                            rules,
                            rated,
                            fen,
                            pgn,
                        )
                    )


def initialize_csv(path_to_csv):
    fieldnames = (
        "white_username",
        "black_username",
        "white_id",
        "black_id",
        "white_rating",
        "black_rating",
        "white_result",
        "black_result",
        "time_class",
        "time_control",
        "rules",
        "rated",
        "fen",
        "pgn",
    )
    with open(os.path.join(path_to_csv, "games.csv"), "a") as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=",")
        csv_writer.writerow(fieldnames)

