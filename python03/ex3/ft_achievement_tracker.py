def ft_achievement_tracker() -> None:
    print("=== Achievement Tracker System ===")

    alice = {'first_kill', 'level_10', 'treasure_hunter', 'speed_demon'}
    bob = {'first_kill', 'level_10', 'boss_slayer', 'collector'}
    charlie = {
        'level_10',
        'treasure_hunter',
        'boss_slayer',
        'speed_demon',
        'perfectionist'
    }
    # Affichage des achievements par joueur
    print(f"Player alice achievements: {alice}")
    print(f"Player bob achievements: {bob}")
    print(f"Player charlie achievements: {charlie}")

    print("=== Achievement Analytics ===")

    # Toutes les achievements uniques
    all_achievements = alice.union(bob).union(charlie)
    print(f"All unique achievements: {all_achievements}")
    print(f"Total unique achievements: {len(all_achievements)}")

    # Achievements communs à tous
    common_all = alice.intersection(bob).intersection(charlie)
    print(f"Common to all players: {common_all}")

    # Rare achievements (présents dans exactement 1 set)
    rare_achievements = set()
    for ach in all_achievements:
        count = 0
        if ach in alice:
            count += 1
        if ach in bob:
            count += 1
        if ach in charlie:
            count += 1
        if count == 1:
            rare_achievements.add(ach)
    print(f"Rare achievements (1 player): {rare_achievements}")

    # Comparaisons Alice vs Bob
    print(f"Alice vs Bob common: {alice.intersection(bob)}")
    print(f"Alice unique: {alice.difference(bob)}")
    print(f"Bob unique: {bob.difference(alice)}")


if __name__ == "__main__":
    ft_achievement_tracker()
