import tkinter as tk
from tkinter import ttk, messagebox
import json

# --- Tournament Data ---
tournament_data = {
    'players': {
        # Group A
        'A1': {'group': 'A', 'scored_goals': 0, 'conceded_goals': 0, 'points': 0, 'display_name': 'A1'},
        'A2': {'group': 'A', 'scored_goals': 0, 'conceded_goals': 0, 'points': 0, 'display_name': 'A2'},
        'A3': {'group': 'A', 'scored_goals': 0, 'conceded_goals': 0, 'points': 0, 'display_name': 'A3'},
        # Group B
        'B1': {'group': 'B', 'scored_goals': 0, 'conceded_goals': 0, 'points': 0, 'display_name': 'B1'},
        'B2': {'group': 'B', 'scored_goals': 0, 'conceded_goals': 0, 'points': 0, 'display_name': 'B2'},
        'B3': {'group': 'B', 'scored_goals': 0, 'conceded_goals': 0, 'points': 0, 'display_name': 'B3'},
        # Group C
        'C1': {'group': 'C', 'scored_goals': 0, 'conceded_goals': 0, 'points': 0, 'display_name': 'C1'},
        'C2': {'group': 'C', 'scored_goals': 0, 'conceded_goals': 0, 'points': 0, 'display_name': 'C2'},
        'C3': {'group': 'C', 'scored_goals': 0, 'conceded_goals': 0, 'points': 0, 'display_name': 'C3'},
        'C4': {'group': 'C', 'scored_goals': 0, 'conceded_goals': 0, 'points': 0, 'display_name': 'C4'},
        # Group D
        'D1': {'group': 'D', 'scored_goals': 0, 'conceded_goals': 0, 'points': 0, 'display_name': 'D1'},
        'D2': {'group': 'D', 'scored_goals': 0, 'conceded_goals': 0, 'points': 0, 'display_name': 'D2'},
        'D3': {'group': 'D', 'scored_goals': 0, 'conceded_goals': 0, 'points': 0, 'display_name': 'D3'},
        'D4': {'group': 'D', 'scored_goals': 0, 'conceded_goals': 0, 'points': 0, 'display_name': 'D4'},
    },
    'matches': [
        {'id': 1, 'players': [('C4', 'B1'), ('C1', 'B2')], 'result': None},
        {'id': 2, 'players': [('D4', 'A1'), ('D1', 'A2')], 'result': None},
        {'id': 3, 'players': [('C2', 'B2'), ('C3', 'B3')], 'result': None},
        {'id': 4, 'players': [('A3', 'D3'), ('A1', 'D2')], 'result': None},
        {'id': 5, 'players': [('C4', 'B2'), ('C2', 'B3')], 'result': None},
        {'id': 6, 'players': [('A1', 'D1'), ('A2', 'D2')], 'result': None},
        {'id': 7, 'players': [('D4', 'B3'), ('D3', 'B1')], 'result': None},
        {'id': 8, 'players': [('C4', 'A1'), ('C1', 'A2')], 'result': None},
        {'id': 9, 'players': [('D4', 'B1'), ('D1', 'B2')], 'result': None},
        {'id': 10, 'players': [('C3', 'D3'), ('C1', 'D2')], 'result': None},
        {'id': 11, 'players': [('C4', 'B3'), ('C3', 'B1')], 'result': None},
        {'id': 12, 'players': [('A2', 'D3'), ('A3', 'D1')], 'result': None},
        {'id': 13, 'players': [('C4', 'A2'), ('C2', 'A3')], 'result': None},
        {'id': 14, 'players': [('D4', 'B2'), ('D2', 'B3')], 'result': None},
        {'id': 15, 'players': [('D4', 'A2'), ('D2', 'A3')], 'result': None},
        {'id': 16, 'players': [('C3', 'B2'), ('C1', 'B1')], 'result': None},
        {'id': 17, 'players': [('C1', 'B3'), ('C2', 'B1')], 'result': None},
        {'id': 18, 'players': [('C4', 'A3'), ('C3', 'A1')], 'result': None},
        {'id': 19, 'players': [('C1', 'D1'), ('C2', 'D2')], 'result': None},
        {'id': 20, 'players': [('D4', 'A3'), ('D3', 'A1')], 'result': None},
        {'id': 21, 'players': [('C2', 'D3'), ('C3', 'D1')], 'result': None},
    ]
}

# ---- Knockout Matches ----
knockout_matches = [
    {'id': 'AF1', 'round': 'Round of 16', 'teams': [None, None], 'result': None, 'description': '18:45 AF 1'},
    {'id': 'VF1', 'round': 'Quarterfinal', 'teams': [None, None], 'result': None, 'description': '18:45 VF 1'},
    {'id': 'VF2', 'round': 'Quarterfinal', 'teams': [None, None], 'result': None, 'description': '19:00 VF 2'},
    {'id': 'HF1', 'round': 'Semifinal', 'teams': [None, None], 'result': None, 'description': '19:15 HF 1'},
    {'id': 'HF2', 'round': 'Semifinal', 'teams': [None, None], 'result': None, 'description': '19:15 HF 2'},
    {'id': 'Final', 'round': 'Final', 'teams': [None, None], 'result': None, 'description': '19:30 Finale'},
    {'id': 'P34', 'round': '3rd/4th Place', 'teams': [None, None], 'result': None,
     'description': '19:30 Spiel um Platz 3'},
]


# --- Tournament Functions ---
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
                x[1]['scored_goals'] - x[1]['conceded_goals'],
                x[1]['scored_goals']
            ),
            reverse=True
        )
        group_rankings[group] = sorted_players
    return group_rankings


def get_looser_tabelle():
    """Return sorted list of last-placed players from each group."""
    group_rankings = get_group_rankings()
    groups = sorted(group_rankings.keys())
    loosers = []
    for group in groups:
        players = group_rankings[group]
        if players:
            last_player_name, last_info = players[-1]
            loosers.append((group, last_player_name, last_info))
    sorted_loosers = sorted(
        loosers,
        key=lambda x: (
            x[2]['points'],
            x[2]['scored_goals'] - x[2]['conceded_goals'],
            x[2]['scored_goals']
        ),
        reverse=True
    )
    return sorted_loosers  # List of (group, player_name, info)


# ---- Runners Up Table additions ----
def get_runners_up_table():
    """Return sorted list of second-placed players from each group."""
    group_rankings = get_group_rankings()
    groups = sorted(group_rankings.keys())
    runners = []
    for group in groups:
        players = group_rankings[group]
        if len(players) >= 2:
            player_name, info = players[1]
            runners.append((group, player_name, info))
    sorted_runners = sorted(
        runners,
        key=lambda x: (
            x[2]['points'],
            x[2]['scored_goals'] - x[2]['conceded_goals'],
            x[2]['scored_goals']
        ),
        reverse=True
    )
    return sorted_runners  # List of (group, player_name, info)


# ---- end Runners Up Table additions ----

def update_knockout_stage():
    rankings = get_group_rankings()
    groups = sorted(rankings.keys())
    A = rankings.get('A', [])
    B = rankings.get('B', [])
    C = rankings.get('C', [])
    D = rankings.get('D', [])

    def g(group, n):
        if len(group) >= n:
            return group[n - 1][0]
        return None

        # AF1: Just look at looser tabelle (best 4 last-placed)

    loosers = get_looser_tabelle()  # Each entry is (group, player_name, info)
    if len(loosers) >= 4:
        team1 = [loosers[0][1], loosers[1][1]]  # 1st + 2nd best looser
        team2 = [loosers[2][1], loosers[3][1]]  # 3rd + 4th best looser
        knockout_matches[0]['teams'] = [team1, team2]
    else:
        knockout_matches[0]['teams'] = [None, None]

        # --- ADJUSTED VF1: Use runners up tabelle ---
    runners = get_runners_up_table()
    if len(runners) >= 4:
        team1 = [runners[0][1], runners[1][1]]  # 1st + 2nd best runner up
        team2 = [runners[2][1], runners[3][1]]  # 3rd + 4th best runner up
        knockout_matches[1]['teams'] = [team1, [g(C, 3), g(D, 3)]]
    else:
        knockout_matches[1]['teams'] = [None, None]

        # VF2: 3rd place C/D vs winner AF1  <--- CORRECTED HERE

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

    knockout_matches[2]['teams'] = [team2, get_winner(knockout_matches[0])]


    knockout_matches[3]['teams'] = [[g(A, 1), g(B, 1)], get_winner(knockout_matches[1])]


    knockout_matches[4]['teams'] = [[g(C, 1), g(D, 1)], get_winner(knockout_matches[2])]

    # Spiel um Platz 3: loser HF1 vs loser HF2
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

    knockout_matches[6]['teams'] = [get_loser(knockout_matches[3]), get_loser(knockout_matches[4])]
    # Finale: winner HF1 vs winner HF2
    knockout_matches[5]['teams'] = [get_winner(knockout_matches[3]), get_winner(knockout_matches[4])]


# --- Tkinter GUI ---
root = tk.Tk()
root.title("Tournament Schedule")
root.geometry("1200x1000")
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

# --- Rankings Row Frame (for groups + looser tabelle) ---
rankings_row_frame = ttk.Frame(root)
rankings_row_frame.pack(fill="x", padx=10, pady=5)

rankings_frames = {}
groups = sorted(set(player['group'] for player in tournament_data['players'].values()))
for i, group in enumerate(groups):
    frame = ttk.LabelFrame(rankings_row_frame, text=f"Group {group} Player Rankings")
    frame.pack(side='left', padx=10, pady=10, fill='y')
    rankings_frames[group] = frame

# --- Looser Tabelle Frame (now shows all last-placed, sorted) ---
looser_frame = ttk.LabelFrame(rankings_row_frame, text="Looser Tabelle (Last Place Players, Sorted)")
looser_frame.pack(side='left', padx=10, pady=10, fill='y')
# ---- Runners Up Table additions ----
runners_up_frame = ttk.LabelFrame(rankings_row_frame, text="Runners Up Table (2nd Place Players, Sorted)")
runners_up_frame.pack(side='left', padx=10, pady=10, fill='y')


# ---- end Runners Up Table additions ----
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
                x[1]['scored_goals'] - x[1]['conceded_goals'],
                x[1]['scored_goals']
            ),
            reverse=True
        )
        for idx, (player, info) in enumerate(sorted_players, 1):
            tordiff = info['scored_goals'] - info['conceded_goals']
            tk.Label(frame,
                     text=f"{idx}. {info['display_name']}  {info['scored_goals']}:{info['conceded_goals']}  "
                          f"Points: {info['points']}  Tordiff: {tordiff}").pack(anchor="w")


def display_group_loosers():
    for widget in looser_frame.winfo_children():
        widget.destroy()
    tk.Label(looser_frame, text="Group   Player   Points   Tordiff   Goals").pack(anchor="w")
    sorted_loosers = get_looser_tabelle()
    for entry in sorted_loosers:
        group, player_name, info = entry
        tordiff = info['scored_goals'] - info['conceded_goals']
        txt = f"{group}   {info['display_name']}   {info['points']}   {tordiff}   {info['scored_goals']}"
        tk.Label(looser_frame, text=txt).pack(anchor="w")
        # ---- Runners Up Table additions ----


def display_runners_up():
    for widget in runners_up_frame.winfo_children():
        widget.destroy()
    tk.Label(runners_up_frame, text="Group   Player   Points   Tordiff   Goals").pack(anchor="w")
    sorted_runners = get_runners_up_table()
    for entry in sorted_runners:
        group, player_name, info = entry
        tordiff = info['scored_goals'] - info['conceded_goals']
        txt = f"{group}   {info['display_name']}   {info['points']}   {tordiff}   {info['scored_goals']}"
        tk.Label(runners_up_frame, text=txt).pack(anchor="w")
        # ---- end Runners Up Table additions ----


# --- Match Frames ---
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
    result_str = match['result'] if match['result'] else "-"
    label_text = f"Match {match['id']} - {team1_players} vs {team2_players}   Result: {result_str}"
    frame = ttk.LabelFrame(main_frame, text=label_text)
    match_label = ttk.Label(frame, text=label_text)
    match_label.pack()
    result_entry = tk.Entry(frame)
    result_entry.pack()
    submit_button = tk.Button(frame, text="Enter Result",
                              command=lambda m_id=match['id'], entry=result_entry: update_match_result(m_id,
                                                                                                       entry.get()))
    submit_button.pack()
    match_frames.append({'match_id': match['id'], 'label': match_label, 'frame': frame, 'result_entry': result_entry})

# ==== Knockout Stage NON-Scrollable GUI ====
knockout_main_frame = ttk.Frame(root)
knockout_main_frame.pack(fill="both", expand=False, padx=10, pady=10)
knockout_match_frames = []


def display_knockout_stage():
    for widget in knockout_main_frame.winfo_children():
        widget.destroy()
    knockout_match_frames.clear()
    # First row: AF, VF1, VF2, HF1, HF2
    first_row_matches = [knockout_matches[0], knockout_matches[1], knockout_matches[2], knockout_matches[3],
                         knockout_matches[4]]
    # Second row: Final, Platz 3
    second_row_matches = [knockout_matches[5], knockout_matches[6]]
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
            frame = ttk.LabelFrame(knockout_main_frame, text=f"{match['description']} ({match['round']})")
            label = ttk.Label(frame, text=label_text)
            label.pack()
            result_entry = tk.Entry(frame)
            result_entry.pack()
            submit_button = tk.Button(frame, text="Enter Result",
                                      command=lambda m_id=match['id'], entry=result_entry: update_match_result(m_id,
                                                                                                               entry.get()))
            submit_button.pack()
            frame.grid(row=row_index, column=col_index, padx=5, pady=2, sticky="ew")
            knockout_match_frames.append(
                {'match_id': match['id'], 'label': label, 'frame': frame, 'result_entry': result_entry})


def refresh_gui():
    display_rankings()
    display_group_loosers()
    display_runners_up()  # ---- Runners Up Table additions ----
    for i, match_frame in enumerate(match_frames):
        row = (i // num_columns)
        column = i % num_columns
        match = next((m for m in tournament_data['matches'] if m['id'] == match_frame['match_id']), None)
        if match:
            team1_players = ", ".join(tournament_data['players'][p]['display_name'] for p in match['players'][0])
            team2_players = ", ".join(tournament_data['players'][p]['display_name'] for p in match['players'][1])
            result_str = match['result'] if match['result'] else "-"
            label_text = f"Match {match['id']} - {team1_players} vs {team2_players}   Result: {result_str}"
            match_frame['label'].config(text=label_text)
            match_frame['frame'].configure(text=label_text)
            match_frame['frame'].grid(row=row, column=column, padx=10, pady=5, sticky="ew")
    update_knockout_stage()
    display_knockout_stage()


refresh_gui()
root.mainloop()