import tkinter as tk
from tkinter import ttk

# 12 players, 4 groups, 3 per group
tournament_data = {
    'players': {
        'A1': {'group': 'A', 'scored_goals': 0, 'conceded_goals': 0, 'points': 0, 'display_name': 'A1'},
        'A2': {'group': 'A', 'scored_goals': 0, 'conceded_goals': 0, 'points': 0, 'display_name': 'A2'},
        'A3': {'group': 'A', 'scored_goals': 0, 'conceded_goals': 0, 'points': 0, 'display_name': 'A3'},
        'B1': {'group': 'B', 'scored_goals': 0, 'conceded_goals': 0, 'points': 0, 'display_name': 'B1'},
        'B2': {'group': 'B', 'scored_goals': 0, 'conceded_goals': 0, 'points': 0, 'display_name': 'B2'},
        'B3': {'group': 'B', 'scored_goals': 0, 'conceded_goals': 0, 'points': 0, 'display_name': 'B3'},
        'C1': {'group': 'C', 'scored_goals': 0, 'conceded_goals': 0, 'points': 0, 'display_name': 'C1'},
        'C2': {'group': 'C', 'scored_goals': 0, 'conceded_goals': 0, 'points': 0, 'display_name': 'C2'},
        'C3': {'group': 'C', 'scored_goals': 0, 'conceded_goals': 0, 'points': 0, 'display_name': 'C3'},
        'D1': {'group': 'D', 'scored_goals': 0, 'conceded_goals': 0, 'points': 0, 'display_name': 'D1'},
        'D2': {'group': 'D', 'scored_goals': 0, 'conceded_goals': 0, 'points': 0, 'display_name': 'D2'},
        'D3': {'group': 'D', 'scored_goals': 0, 'conceded_goals': 0, 'points': 0, 'display_name': 'D3'},
    },
    'matches': [
        # Group Stage (Spieltag 1–9)
        {'id': 1, 'players': [('A1', 'B1'), ('A2', 'B2')], 'result': None},
        {'id': 2, 'players': [('C1', 'D1'), ('C2', 'D2')], 'result': None},
        {'id': 3, 'players': [('A3', 'B3'), ('A1', 'B2')], 'result': None},
        {'id': 4, 'players': [('C3', 'D3'), ('C1', 'D2')], 'result': None},
        {'id': 5, 'players': [('A2', 'B3'), ('A3', 'B1')], 'result': None},
        {'id': 6, 'players': [('C2', 'D3'), ('C3', 'D1')], 'result': None},
        {'id': 7, 'players': [('A1', 'D1'), ('A2', 'D2')], 'result': None},
        {'id': 8, 'players': [('C1', 'B1'), ('C2', 'B2')], 'result': None},
        {'id': 9, 'players': [('A3', 'D3'), ('A1', 'D2')], 'result': None},
        {'id': 10, 'players': [('C3', 'B3'), ('C1', 'B2')], 'result': None},
        {'id': 11, 'players': [('A2', 'D3'), ('A3', 'D1')], 'result': None},
        {'id': 12, 'players': [('C2', 'B3'), ('C3', 'B1')], 'result': None},
        {'id': 13, 'players': [('A1', 'C1'), ('A2', 'C2')], 'result': None},
        {'id': 14, 'players': [('D1', 'B1'), ('D2', 'B2')], 'result': None},
        {'id': 15, 'players': [('A3', 'C3'), ('A1', 'C2')], 'result': None},
        {'id': 16, 'players': [('D3', 'B3'), ('D1', 'B2')], 'result': None},
        {'id': 17, 'players': [('A2', 'C3'), ('A3', 'C1')], 'result': None},
        {'id': 18, 'players': [('D2', 'B3'), ('D3', 'B1')], 'result': None},
        # Knockout Stage (customize as needed)
        {'id': 19, 'players': [('A2', 'B2'), ('A3', 'B3')], 'result': None},  # VF1
        {'id': 20, 'players': [('C2', 'D2'), ('C3', 'D3')], 'result': None},  # VF2
        {'id': 21, 'players': [('A1', 'B1'), ('C1', 'D1')], 'result': None},  # HF1
        {'id': 22, 'players': [('A2', 'B2'), ('C2', 'D2')], 'result': None},  # HF2
        {'id': 23, 'players': [('A3', 'B3'), ('C3', 'D3')], 'result': None},  # Platz 5+6
        {'id': 24, 'players': [('A1', 'B1'), ('C1', 'D1')], 'result': None},  # Platz 3+4
        {'id': 25, 'players': [('A2', 'B2'), ('C2', 'D2')], 'result': None},  # Finale
    ]
}


def update_match_result(match_id, result):
    match = next((m for m in tournament_data['matches'] if m['id'] == match_id), None)
    if match and result:
        match['result'] = result
        reset_all_player_stats()
        calculate_statistics()
        refresh_gui()


def reset_all_player_stats():
    for player in tournament_data['players'].values():
        player['scored_goals'] = 0
        player['conceded_goals'] = 0
        player['points'] = 0


def calculate_statistics():
    for match in tournament_data['matches']:
        if match['result']:
            try:
                goals_team1, goals_team2 = map(int, match['result'].split('-'))
            except Exception:
                continue
            team1, team2 = match['players']
            update_player_stats(team1, goals_team1, goals_team2)
            update_player_stats(team2, goals_team2, goals_team1)


def update_player_stats(team, goals_for, goals_against):
    for player_name in team:
        player = tournament_data['players'][player_name]
        player['scored_goals'] += goals_for
        player['conceded_goals'] += goals_against
        if goals_for > goals_against:
            player['points'] += 3
        elif goals_for == goals_against:
            player['points'] += 1


def display_rankings():
    groups = sorted(rankings_frames.keys())
    for i, group in enumerate(groups):
        frame = rankings_frames[group]
        frame.grid(row=1, column=i % len(groups), padx=10, pady=10, sticky="nsew")
        for widget in frame.winfo_children():
            widget.destroy()
        players = [(name, info) for name, info in tournament_data['players'].items() if info['group'] == group]
        sorted_players = sorted(players, key=lambda x: (x[1]['points'], x[1]['scored_goals']), reverse=True)
        for player, info in sorted_players:
            tk.Label(frame,
                     text=f"{info['display_name']}: {info['points']} pts, {info['scored_goals']} scored, {info['conceded_goals']} conceded").pack()


def set_display_name(player_id, new_name):
    if player_id in tournament_data['players']:
        tournament_data['players'][player_id]['display_name'] = new_name
        refresh_gui()


def refresh_gui():
    display_rankings()
    num_columns = 2
    for i, match_frame in enumerate(match_frames):
        row = (i // num_columns) + len(rankings_frames)
        column = i % num_columns
        match = next((m for m in tournament_data['matches'] if m['id'] == match_frame['match_id']), None)
        if match:
            team1_players = ", ".join(tournament_data['players'][p]['display_name'] for p in match['players'][0])
            team2_players = ", ".join(tournament_data['players'][p]['display_name'] for p in match['players'][1])
            match_frame['label'].config(text=f"Match {match['id']} - {team1_players} vs {team2_players}")
            match_frame['frame'].grid(row=row, column=column, padx=10, pady=5, sticky="ew")


root = tk.Tk()
root.title("Tournament Schedule")

name_frame = ttk.LabelFrame(root, text="Set Player Display Name")
name_frame.grid(row=0, column=0, columnspan=2, padx=10, pady=5, sticky="ew")
player_id_entry = tk.Entry(name_frame, width=20)
player_id_entry.pack(side='left', padx=(10, 5))
new_name_entry = tk.Entry(name_frame, width=20)
new_name_entry.pack(side='left', padx=(5, 10))
set_name_button = tk.Button(name_frame, text="Set Name",
                            command=lambda: set_display_name(player_id_entry.get(), new_name_entry.get()))
set_name_button.pack(side='left', padx=10)

rankings_frames = {}
groups = set(player['group'] for player in tournament_data['players'].values())
for group in groups:
    frame = ttk.LabelFrame(root, text=f"Group {group} Player Rankings")
    rankings_frames[group] = frame

match_frames = []
for match in tournament_data['matches']:
    team1_players = ", ".join(tournament_data['players'][p]['display_name'] for p in match['players'][0])
    team2_players = ", ".join(tournament_data['players'][p]['display_name'] for p in match['players'][1])
    frame = ttk.LabelFrame(root, text=f"Match {match['id']} - {team1_players} vs {team2_players}")
    match_label = ttk.Label(frame, text=f"Match {match['id']} - {team1_players} vs {team2_players}")
    match_label.pack()
    result_entry = tk.Entry(frame)
    result_entry.pack()
    submit_button = tk.Button(frame, text="Enter Result",
                              command=lambda m_id=match['id'], entry=result_entry: update_match_result(m_id,
                                                                                                       entry.get()))
    submit_button.pack()
    match_frames.append({'match_id': match['id'], 'label': match_label, 'frame': frame})

refresh_gui()
root.mainloop()