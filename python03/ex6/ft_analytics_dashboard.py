players = [
    {"name": "alice", "score": 2300, "achievements": 5, "region": "north"},
    {"name": "bob", "score": 1800, "achievements": 3, "region": "east"},
    {"name": "charlie", "score": 2150, "achievements": 7, "region": "central"},
    {"name": "diana", "score": 2200, "achievements": 4, "region": "north"},
]

high_scorers = [p["name"] for p in players if p["score"] > 2000]
doubled_scores = [p["score"]*2 for p in players]
active_players = [p["name"] for p in players if p["achievements"] > 0]


def main() -> None:

    print("=== Game Analytics Dashboard ===\n")
    print("=== List Comprehension Examples ===")
    high_scorers = [p["name"] for p in players if p["score"] > 2000]
    print("High scorers (>2000):", high_scorers)

    # Transforme les scores
    doubled_scores = [p["score"]*2 for p in players]
    print("Scores doubled:", doubled_scores)

    # Joueurs actifs
    active_players = [p["name"] for p in players if p["achievements"] > 0]
    print("Active players:", active_players)

    print("\n=== Dict Comprehension Examples ===")
    player_scores = {p["name"]: p["score"] for p in players}
    print("Player scores:", player_scores)

    # Compter catégories
    score_categories = {
        "high": sum(1 for p in players if p["score"] > 2000),
        "medium": sum(1 for p in players if 1500 <= p["score"] <= 2000),
        "low": sum(1 for p in players if p["score"] < 1500)
    }
    print("Score categories:", score_categories)

    achievement_counts = {p["name"]: p["achievements"] for p in players}
    print("Achievement counts:", achievement_counts)

    print("\n=== Set Comprehension Examples ===")
    unique_players = {p["name"] for p in players}
    print("Unique players:", unique_players)

    unique_regions = {p["region"] for p in players}
    print("Active regions:", unique_regions)

    print("\n=== Combined Analysis ===")
    total_players = len(players)
    print("Total players:", total_players)

    # Average score
    average_score = sum(p["score"] for p in players) / len(players)
    print("Average score:", average_score)

    # Top performer
    top_score = max(p["score"] for p in players)
    for p in players:
        if p["score"] == top_score:
            top_player = p
            break
    print(
            "Top performer:",
            top_player["name"], "(",
            top_player["score"], "points,", top_player["achievements"],
            "achievements )"
            )


if __name__ == "__main__":
    main()
