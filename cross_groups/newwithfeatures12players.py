import tkinter as tk
from tkinter import ttk, messagebox
import json

# --- Tournament Data ---
tournament_data = {
    'players': {
        'A1': {'group': 'A', 'scored_goals': 0, 'conceded_goals': 0, 'points': 0, 'display_name': 'A1', 'wins': 0,
               'draws': 0, 'losses': 0},
        'A2': {'group': 'A', 'scored_goals': 0, 'conceded_goals': 0, 'points': 0, 'display_name': 'A2', 'wins': 0,
               'draws': 0, 'losses': 0},
        'A3': {'group': 'A', 'scored_goals': 0, 'conceded_goals': 0, 'points': 0, 'display_name': 'A3', 'wins': 0,
               'draws': 0, 'losses': 0},
        'B1': {'group': 'B', 'scored_goals': 0, 'conceded_goals': 0, 'points': 0, 'display_name': 'B1', 'wins': 0,
               'draws': 0, 'losses': 0},
        'B2': {'group': 'B', 'scored_goals': 0, 'conceded_goals': 0, 'points': 0, 'display_name': 'B2', 'wins': 0,
               'draws': 0, 'losses': 0},
        'B3': {'group': 'B', 'scored_goals': 0, 'conceded_goals': 0, 'points': 0, 'display_name': 'B3', 'wins': 0,
               'draws': 0, 'losses': 0},
        'C1': {'group': 'C', 'scored_goals': 0, 'conceded_goals': 0, 'points': 0, 'display_name': 'C1', 'wins': 0,
               'draws': 0, 'losses': 0},
        'C2': {'group': 'C', 'scored_goals': 0, 'conceded_goals': 0, 'points': 0, 'display_name': 'C2', 'wins': 0,
               'draws': 0, 'losses': 0},
        'C3': {'group': 'C', 'scored_goals': 0, 'conceded_goals': 0, 'points': 0, 'display_name': 'C3', 'wins': 0,
               'draws': 0, 'losses': 0},
        'D1': {'group': 'D', 'scored_goals': 0, 'conceded_goals': 0, 'points': 0, 'display_name': 'D1', 'wins': 0,
               'draws': 0, 'losses': 0},
        'D2': {'group': 'D', 'scored_goals': 0, 'conceded_goals': 0, 'points': 0, 'display_name': 'D2', 'wins': 0,
               'draws': 0, 'losses': 0},
        'D3': {'group': 'D', 'scored_goals': 0, 'conceded_goals': 0, 'points': 0, 'display_name': 'D3', 'wins': 0,
               'draws': 0, 'losses': 0},
    },
    'matches': [
    {'id': 1, 'players': [('A1', 'B1'), ('A2', 'B2')], 'result': None, 'description': '16:00'},
    {'id': 2, 'players': [('C1', 'D1'), ('C2', 'D2')], 'result': None, 'description': '16:00'},
    {'id': 3, 'players': [('A3', 'B3'), ('A1', 'B2')], 'result': None, 'description': '16:15'},
    {'id': 4, 'players': [('C3', 'D3'), ('C1', 'D2')], 'result': None, 'description': '16:15'},
    {'id': 5, 'players': [('A2', 'B3'), ('A3', 'B1')], 'result': None, 'description': '16:30'},
    {'id': 6, 'players': [('C2', 'D3'), ('C3', 'D1')], 'result': None, 'description': '16:30'},
    {'id': 7, 'players': [('A1', 'D1'), ('A2', 'D2')], 'result': None, 'description': '16:45'},
    {'id': 8, 'players': [('C1', 'B1'), ('C2', 'B2')], 'result': None, 'description': '16:45'},
    {'id': 9, 'players': [('A3', 'D3'), ('A1', 'D2')], 'result': None, 'description': '17:00'},
    {'id': 10, 'players': [('C3', 'B3'), ('C1', 'B2')], 'result': None, 'description': '17:00'},
    {'id': 11, 'players': [('A2', 'D3'), ('A3', 'D1')], 'result': None, 'description': '17:15'},
    {'id': 12, 'players': [('C2', 'B3'), ('C3', 'B1')], 'result': None, 'description': '17:15'},
    {'id': 13, 'players': [('A1', 'C1'), ('A2', 'C2')], 'result': None, 'description': '17:30'},
    {'id': 14, 'players': [('D1', 'B1'), ('D2', 'B2')], 'result': None, 'description': '17:30'},
    {'id': 15, 'players': [('A3', 'C3'), ('A1', 'C2')], 'result': None, 'description': '17:45'},
    {'id': 16, 'players': [('D3', 'B3'), ('D1', 'B2')], 'result': None, 'description': '17:45'},
    {'id': 17, 'players': [('A2', 'C3'), ('A3', 'C1')], 'result': None, 'description': '18:00'},
    {'id': 18, 'players': [('D2', 'B3'), ('D3', 'B1')], 'result': None, 'description': '18:00'},
]
}
knockout_matches = [
    {'id': 'VF1', 'round': 'Viertelfinale 1', 'teams': [None, None], 'result': None, 'description': '18:15'},
    {'id': 'VF2', 'round': 'Viertelfinale 2', 'teams': [None, None], 'result': None, 'description': '18:15'},
    {'id': 'HF1', 'round': 'Halbfinale 1', 'teams': [None, None], 'result': None, 'description': '18:30'},
    {'id': 'HF2', 'round': 'Halbfinale 2', 'teams': [None, None], 'result': None, 'description': '18:30'},
    {'id': 'P56', 'round': 'Spiel um Platz 5 + 6', 'teams': [None, None], 'result': None, 'description': '18:45'},
    {'id': 'P34', 'round': 'Spiel um Platz 5 + 6', 'teams': [None, None], 'result': None, 'description': '18:45'},
    {'id': 'Final', 'round': 'Finale', 'teams': [None, None], 'result': None, 'description': '19:00'},
]


def save_tournament(filename):
    try:
        data = {
            "players": tournament_data["players"],
            "matches": tournament_data["matches"],
            "knockout_matches": knockout_matches
        }
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        messagebox.showinfo("Saved", f"Tournament saved to {filename}.")
    except Exception as e:
        messagebox.showerror("Error", f"Could not save: {e}")


def load_tournament(filename):
    try:
        with open(filename, "r", encoding="utf-8") as f:
            data = json.load(f)
        tournament_data["players"].clear()
        tournament_data["players"].update(data["players"])
        tournament_data["matches"].clear()
        tournament_data["matches"].extend(data["matches"])
        knockout_matches.clear()
        knockout_matches.extend(data["knockout_matches"])
        refresh_gui()
        messagebox.showinfo("Loaded", f"Tournament loaded from {filename}.")
    except Exception as e:
        messagebox.showerror("Error", f"Could not load: {e}")


def update_match_result(match_id, result):
    match = next((m for m in tournament_data['matches'] if m['id'] == match_id), None)
    if match and result:
        match['result'] = result
        reset_all_player_stats()
        calculate_statistics()
        refresh_gui()
        update_knockout_stage()
    else:
        kmatch = next((m for m in knockout_matches if m['id'] == match_id), None)
        if kmatch and result:
            kmatch['result'] = result
            refresh_gui()
            update_knockout_stage()


def reset_all_player_stats():
    for player in tournament_data['players'].values():
        player['scored_goals'] = 0
        player['conceded_goals'] = 0
        player['points'] = 0
        player['wins'] = 0
        player['draws'] = 0
        player['losses'] = 0


def calculate_statistics():
    for match in tournament_data['matches']:
        if match['result']:
            try:
                goals_team1, goals_team2 = map(int, match['result'].split('-'))
            except Exception:
                continue
            team1, team2 = match['players']
            # Update stats for team1 and team2
            update_player_stats(team1, goals_team1, goals_team2)
            update_player_stats(team2, goals_team2, goals_team1)
            # Now increment wins/draws/losses
            if goals_team1 > goals_team2:
                for player_name in team1:
                    tournament_data['players'][player_name]['wins'] += 1
                for player_name in team2:
                    tournament_data['players'][player_name]['losses'] += 1
            elif goals_team1 < goals_team2:
                for player_name in team2:
                    tournament_data['players'][player_name]['wins'] += 1
                for player_name in team1:
                    tournament_data['players'][player_name]['losses'] += 1
            else:
                for player_name in team1:
                    tournament_data['players'][player_name]['draws'] += 1
                for player_name in team2:
                    tournament_data['players'][player_name]['draws'] += 1


def update_player_stats(team, goals_for, goals_against):
    for player_name in team:
        player = tournament_data['players'][player_name]
        player['scored_goals'] += goals_for
        player['conceded_goals'] += goals_against
        if goals_for > goals_against:
            player['points'] += 3
        elif goals_for == goals_against:
            player['points'] += 1


def set_display_name(player_id, new_name):
    if player_id in tournament_data['players']:
        tournament_data['players'][player_id]['display_name'] = new_name
        refresh_gui()


def get_group_rankings():
    groups = sorted(set(player['group'] for player in tournament_data['players'].values()))
    group_rankings = {}
    for group in groups:
        players = [(name, info) for name, info in tournament_data['players'].items() if info['group'] == group]
        sorted_players = sorted(
            players,
            key=lambda x: (
                x[1]['points'],
                x[1]['scored_goals'] - x[1]['conceded_goals'],  # tordifferenz
                x[1]['scored_goals']
            ),
            reverse=True
        )
        group_rankings[group] = sorted_players
    return group_rankings


def update_knockout_stage():
    rankings = get_group_rankings()
    A = rankings['A']
    B = rankings['B']
    C = rankings['C']
    D = rankings['D']

    def g(group, n):
        if len(group) >= n: return group[n - 1][0]
        return None

    knockout_matches[0]['teams'] = [[g(A, 2), g(B, 2)], [g(C, 3), g(D, 3)]]  # VF1
    knockout_matches[1]['teams'] = [[g(C, 2), g(D, 2)], [g(A, 3), g(B, 3)]]  # VF2

    def get_winner(match):
        if match['result']:
            try:
                goals1, goals2 = map(int, match['result'].split('-'))
            except Exception:
                return None
            if goals1 > goals2:
                return match['teams'][0]
            elif goals2 > goals1:
                return match['teams'][1]
            else:
                return None
        return None

    knockout_matches[2]['teams'] = [[g(C, 1), g(D, 1)], get_winner(knockout_matches[0])]  # HF1
    knockout_matches[3]['teams'] = [[g(A, 1), g(B, 1)], get_winner(knockout_matches[1])]  # HF2

    def get_loser(match):
        if match['result']:
            try:
                goals1, goals2 = map(int, match['result'].split('-'))
            except Exception:
                return None
            if goals1 < goals2:
                return match['teams'][0]
            elif goals2 < goals1:
                return match['teams'][1]
            else:
                return None
        return None

    knockout_matches[4]['teams'] = [get_loser(knockout_matches[0]), get_loser(knockout_matches[1])]  # P56

    def get_semiloser(match):
        if match['result']:
            try:
                goals1, goals2 = map(int, match['result'].split('-'))
            except Exception:
                return None
            if goals1 < goals2:
                return match['teams'][0]
            elif goals2 < goals1:
                return match['teams'][1]
            else:
                return None
        return None

    knockout_matches[5]['teams'] = [get_semiloser(knockout_matches[2]), get_semiloser(knockout_matches[3])]  # P34
    knockout_matches[6]['teams'] = [get_winner(knockout_matches[2]), get_winner(knockout_matches[3])]  # Final


class VerticalScrolledFrame(tk.Frame):
    """A vertically scrollable frame for Tkinter."""

    def __init__(self, parent, *args, **kw):
        tk.Frame.__init__(self, parent, *args, **kw)
        vscrollbar = tk.Scrollbar(self, orient=tk.VERTICAL)
        vscrollbar.pack(fill=tk.Y, side=tk.RIGHT, expand=tk.FALSE)
        canvas = tk.Canvas(self, bd=0, highlightthickness=0, yscrollcommand=vscrollbar.set)
        canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=tk.TRUE)
        vscrollbar.config(command=canvas.yview)
        canvas.xview_moveto(0)
        canvas.yview_moveto(0)
        self.interior = interior = tk.Frame(canvas)
        interior_id = canvas.create_window(0, 0, window=interior, anchor=tk.NW)

        def _configure_interior(event):
            size = (interior.winfo_reqwidth(), interior.winfo_reqheight())
            canvas.config(scrollregion="0 0 %s %s" % size)
            if interior.winfo_reqwidth() != canvas.winfo_width():
                canvas.config(width=interior.winfo_reqwidth())

        interior.bind('<Configure>', _configure_interior)

        def _configure_canvas(event):
            if interior.winfo_reqwidth() != canvas.winfo_width():
                canvas.itemconfigure(interior_id, width=canvas.winfo_width())

        canvas.bind('<Configure>', _configure_canvas)

        def _on_mousewheel(event):
            canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

        canvas.bind_all("<MouseWheel>", _on_mousewheel)


root = tk.Tk()
root.title("Tournament Schedule")
root.geometry("1100x950")
top_frame = ttk.Frame(root)
top_frame.pack(fill="x", padx=10, pady=5)
# --- Filename entry for save/load ---
filename_var = tk.StringVar(value="tournament_save.json")
filename_entry = tk.Entry(top_frame, textvariable=filename_var, width=30)
filename_entry.pack(side="left", padx=10)
save_btn = tk.Button(top_frame, text="Save Tournament", command=lambda: save_tournament(filename_var.get()))
save_btn.pack(side="left", padx=10)
load_btn = tk.Button(top_frame, text="Load Tournament", command=lambda: load_tournament(filename_var.get()))
load_btn.pack(side="left", padx=10)
name_frame = ttk.LabelFrame(top_frame, text="Set Player Display Name")
name_frame.pack(fill="x", padx=10, pady=5)
player_id_entry = tk.Entry(name_frame, width=20)
player_id_entry.pack(side='left', padx=(10, 5))
new_name_entry = tk.Entry(name_frame, width=20)
new_name_entry.pack(side='left', padx=(5, 10))
set_name_button = tk.Button(
    name_frame, text="Set Name",
    command=lambda: set_display_name(player_id_entry.get(), new_name_entry.get()))
set_name_button.pack(side='left', padx=10)
rankings_row_frame = ttk.Frame(root)
rankings_row_frame.pack(fill="x", padx=10, pady=5)
rankings_frames = {}
groups = sorted(set(player['group'] for player in tournament_data['players'].values()))
for i, group in enumerate(groups):
    frame = ttk.LabelFrame(rankings_row_frame, text=f"Group {group} Player Rankings")
    frame.pack(side='left', padx=10, pady=10, fill='y')
    rankings_frames[group] = frame

scrolled_frame = VerticalScrolledFrame(root)
scrolled_frame.pack(fill=tk.BOTH, expand=True)
main_frame = scrolled_frame.interior
num_columns = 2
for col in range(num_columns):
    main_frame.grid_columnconfigure(col, minsize=350, weight=1)

match_frames = []
for i, match in enumerate(tournament_data['matches']):
    team1_players = ", ".join(tournament_data['players'][p]['display_name'] for p in match['players'][0])
    team2_players = ", ".join(tournament_data['players'][p]['display_name'] for p in match['players'][1])
    # --- Show result in match label ---
    result_str = match['result'] if match['result'] else "-"
    label_text = f"Match {match['id']} - {team1_players} vs {team2_players}   Results: {result_str}"
    frame = ttk.LabelFrame(main_frame, text=label_text)
    match_label = ttk.Label(frame, text=label_text)
    match_label.pack()
    result_entry = tk.Entry(frame)
    result_entry.pack()
    submit_button = tk.Button(frame, text="Ergebnis speichern",
                              command=lambda m_id=match['id'], entry=result_entry: update_match_result(m_id,
                                                                                                       entry.get()))
    submit_button.pack()
    match_frames.append({'match_id': match['id'], 'label': match_label, 'frame': frame, 'result_entry': result_entry})

# ==== Knockout Stage NON-Scrollable GUI ====
knockout_main_frame = ttk.Frame(root)
knockout_main_frame.pack(fill="both", expand=False, padx=10, pady=10)
knockout_match_frames = []


def display_rankings():
    for group in groups:
        frame = rankings_frames[group]
        for widget in frame.winfo_children():
            widget.destroy()
        players = [(name, info) for name, info in tournament_data['players'].items() if info['group'] == group]
        sorted_players = sorted(
            players,
            key=lambda x: (
                x[1]['points'],
                x[1]['scored_goals'] - x[1]['conceded_goals'],  # tordifferenz
                x[1]['scored_goals']
            ),
            reverse=True
        )
        header = ['#', 'Name', 'S U N', 'Tore', 'Diff', 'Punkte']
        for col, text in enumerate(header):
            tk.Label(frame, text=text, font=('Arial', 10, 'bold')).grid(row=0, column=col, sticky='w')

        for idx, (player, info) in enumerate(sorted_players, 1):
            tordiff = info['scored_goals'] - info['conceded_goals']
            tordiff_str = f"{tordiff:+d}"
            tk.Label(frame, text=str(idx)).grid(row=idx, column=0, sticky='w')
            tk.Label(frame, text=info['display_name']).grid(row=idx, column=1, sticky='w')
            tk.Label(frame, text=f"{info['wins']} {info['draws']} {info['losses']}").grid(row=idx, column=2, sticky='w')
            tk.Label(frame, text=f"{info['scored_goals']}:{info['conceded_goals']}").grid(row=idx, column=3, sticky='w')
            tk.Label(frame, text=tordiff_str).grid(row=idx, column=4, sticky='w')
            tk.Label(frame, text=str(info['points'])).grid(row=idx, column=5, sticky='w')  # Points aligned left


def display_knockout_stage():
    for widget in knockout_main_frame.winfo_children():
        widget.destroy()
    knockout_match_frames.clear()
    # First row: Quarterfinals (VF1, VF2) and Semifinals (HF1, HF2)
    first_row_matches = [knockout_matches[0], knockout_matches[1], knockout_matches[2], knockout_matches[3]]
    # Second row: Platz 5+6, Platz 3+4, Finale
    second_row_matches = [knockout_matches[4], knockout_matches[5], knockout_matches[6]]

    rows = [first_row_matches, second_row_matches]
    for row_index, matches_in_row in enumerate(rows):
        for col_index, match in enumerate(matches_in_row):
            team1 = match['teams'][0]
            team2 = match['teams'][1]

            def fmt(team):
                if not team:
                    return "?"
                if isinstance(team, list):
                    return ", ".join(tournament_data['players'][p]['display_name'] if p else "?" for p in team)
                else:
                    return ", ".join(
                        tournament_data['players'][p]['display_name'] if p else "?" for p in team) if team else "?"

            team1_str = fmt(team1)
            team2_str = fmt(team2)
            result_str = match['result'] if match['result'] else "-"
            label_text = f"{team1_str} vs {team2_str}   Result: {result_str}"
            frame = ttk.LabelFrame(knockout_main_frame, text=f"{match['description']} {match['round']}")
            label = ttk.Label(frame, text=label_text)
            label.pack()
            result_entry = tk.Entry(frame)
            result_entry.pack()
            submit_button = tk.Button(frame, text="Ergebnis speichern",
                                      command=lambda m_id=match['id'], entry=result_entry: update_match_result(m_id,
                                                                                                               entry.get()))
            submit_button.pack()
            frame.grid(row=row_index, column=col_index, padx=5, pady=2, sticky="ew")
            knockout_match_frames.append(
                {'match_id': match['id'], 'label': label, 'frame': frame, 'result_entry': result_entry})


def refresh_gui():
    display_rankings()
    for i, match_frame in enumerate(match_frames):
        row = (i // num_columns)
        column = i % num_columns
        match = next((m for m in tournament_data['matches'] if m['id'] == match_frame['match_id']), None)
        if match:
            team1_players = ", ".join(tournament_data['players'][p]['display_name'] for p in match['players'][0])
            team2_players = ", ".join(tournament_data['players'][p]['display_name'] for p in match['players'][1])
            result_str = match['result'] if match['result'] else "-"
            box_text = f"Spiel {match['id']} {match['description']} Uhr"
            label_text = f"Spiel {match['id']} - {team1_players} vs {team2_players}   Ergebnis: {result_str}"
            match_frame['label'].config(text=label_text)
            match_frame['frame'].configure(text=box_text)
            match_frame['frame'].grid(row=row, column=column, padx=10, pady=5, sticky="ew")
    update_knockout_stage()
    display_knockout_stage()


refresh_gui()
root.mainloop()