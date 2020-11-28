def match_fixture(teams):
    for team_a in teams:
        for team_b in teams:
            if team_a != team_b:
                print(team_a + " vs " + team_b)
        print()

match_fixture(["Bangladesh", "West Indies", "Australia", "South Africa"])