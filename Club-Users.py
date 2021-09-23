from chessdotcom import get_club_members 
import pprint


printer = pprint.PrettyPrinter()

class get_usernames_from_club():
    def __init__(self, club_name, save_text, ):
        #getting the names of the club_members
        self.club_members = get_club_members(club_name).json
        self.member_iter = self.club_members['members']['all_time']
        usernames = []
        for member in self.member_iter:
            usernames.append(member['username'])

        if save_text:
            with open("user_urls.txt", "w") as f:
                    for username in usernames:
                        f.write(f'{username}\n')
