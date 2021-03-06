import pandas as pd
from tqdm import tqdm
from util.scraper_utils import User, initialize_csv
from util.Extract_features_frm_pgn import Extract_features
from util.config import scrapper_cfg

if __name__ == "__main__":

    # usernames = scrapper_cfg.usernames
    with open('data/user_urls.txt', 'r') as f:
        usernames = []
        for line in f:
            username = line.split('/')[5]
            usernames.append(username)

    output_path = scrapper_cfg.output_path

    # initialize_csv(output_path)

    progress_bar = tqdm(usernames[50:], total=len(usernames), desc="Users left", position=0)

    for username in progress_bar:
        User(username, output_path).create_csv()

    Extract_features(output_path).get_features()
