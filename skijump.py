import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import json
import os
import re


class SkiJumpApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Ski Jumping - 2 Jumps Scoreboard")
        self.geometry("900x520")
        self.resizable(True, True)

        # name -> {'j1': float|None, 'j2': float|None, 'sum': float}
        self.players = {}
        self.sort_mode = "sum"  # keep best on top by default

        # Tree row handling
        self.row_ids = {}  # name -> Treeview iid
        self.animating = False
        self.anim_after_id = None
        self.animation_queue = []  # names queued for animation

        self.create_widgets()

    def create_widgets(self):
        control = ttk.Frame(self, padding=8)
        control.pack(side=tk.TOP, fill=tk.X)

        ttk.Label(control, text="Name").grid(row=0, column=0, sticky='w')
        self.name_entry = ttk.Entry(control, width=20)
        self.name_entry.grid(row=1, column=0, padx=(0, 10))

        ttk.Label(control, text="Jump").grid(row=0, column=1, sticky='w')
        self.jump_var = tk.IntVar(value=1)
        jump_frame = ttk.Frame(control)
        jump_frame.grid(row=1, column=1)
        ttk.Radiobutton(jump_frame, text="1", variable=self.jump_var, value=1).pack(side=tk.LEFT)
        ttk.Radiobutton(jump_frame, text="2", variable=self.jump_var, value=2).pack(side=tk.LEFT)

        ttk.Label(control, text="Score").grid(row=0, column=2, sticky='w')
        self.score_entry = ttk.Entry(control, width=10)
        self.score_entry.grid(row=1, column=2, padx=(0, 10))
        self.score_entry.bind("<Return>", lambda e: self.set_score())
        # Validierung: nur Ziffern, optional Komma/Punkt mit max. 1 Dezimalstelle
        vcmd = (self.register(self.validate_score_input), '%P')
        self.score_entry.configure(validate='key', validatecommand=vcmd)

        ttk.Button(control, text="Set Score", command=self.set_score).grid(row=1, column=3, padx=(0, 10))
        ttk.Button(control, text="Add Player", command=self.add_player).grid(row=1, column=4, padx=(0, 10))
        ttk.Button(control, text="Reset All", command=self.reset_all).grid(row=1, column=5)

        # File controls
        file_ctrl = ttk.Frame(self, padding=(8, 0, 8, 8))
        file_ctrl.pack(side=tk.TOP, fill=tk.X)

        ttk.Label(file_ctrl, text="File").grid(row=0, column=0, sticky='w')
        self.file_entry = ttk.Entry(file_ctrl, width=40)
        self.file_entry.insert(0, "ski_scores.json")
        self.file_entry.grid(row=0, column=1, padx=(6, 10), sticky='we')
        file_ctrl.columnconfigure(1, weight=1)

        ttk.Button(file_ctrl, text="Save", command=self.save_to_file).grid(row=0, column=2, padx=(0, 6))
        ttk.Button(file_ctrl, text="Load", command=self.load_from_file).grid(row=0, column=3, padx=(0, 6))
        ttk.Button(file_ctrl, text="Browse…", command=self.browse_file).grid(row=0, column=4)

        table_frame = ttk.Frame(self, padding=8)
        table_frame.pack(fill=tk.BOTH, expand=True)

        # Neue Spalte "gap" (Abstand zum Führenden)
        self.tree = ttk.Treeview(
            table_frame,
            columns=("name", "j1", "j2", "sum", "gap"),
            show="headings",
            selectmode="browse"
        )
        self.tree.heading("name", text="Name", command=lambda: self.sort_by("name"))
        self.tree.heading("j1", text="Jump 1")
        self.tree.heading("j2", text="Jump 2")
        self.tree.heading("sum", text="Summe", command=lambda: self.sort_by("sum"))
        self.tree.heading("gap", text="Abstand zum Führenden", command=lambda: self.sort_by("sum"))

        self.tree.column("name", width=260, anchor=tk.W)
        self.tree.column("j1", width=120, anchor=tk.CENTER)
        self.tree.column("j2", width=120, anchor=tk.CENTER)
        self.tree.column("sum", width=120, anchor=tk.CENTER)
        self.tree.column("gap", width=180, anchor=tk.CENTER)

        # Tag used to highlight a moving row during animation
        self.tree.tag_configure("moving", background="#fff3bf")  # light yellow

        self.tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        scroll = ttk.Scrollbar(table_frame, orient=tk.VERTICAL, command=self.tree.yview)
        self.tree.configure(yscrollcommand=scroll.set)
        scroll.pack(side=tk.RIGHT, fill=tk.Y)

        self.tree.bind("<<TreeviewSelect>>", self.on_select_row)

    def add_player(self):
        name = self.name_entry.get().strip()
        if not name:
            messagebox.showwarning("Missing name", "Enter a player name.")
            return
        if name not in self.players:
            self.players[name] = {'j1': None, 'j2': None, 'sum': 0.0}
            self.ensure_row(name)
            self.queue_animation(name)
        else:
            messagebox.showinfo("Exists", f"{name} is already in the table.")

    def ensure_row(self, name):
        if name not in self.row_ids:
            data = self.players[name]
            j1 = "" if data['j1'] is None else self.format_score(data['j1'])
            j2 = "" if data['j2'] is None else self.format_score(data['j2'])
            total = "" if (data['j1'] is None and data['j2'] is None) else self.format_score(data['sum'])
            leader_sum = self.get_leader_sum()
            attempted = (data['j1'] is not None or data['j2'] is not None)
            gap = "" if (leader_sum is None or not attempted) else self.format_score(
                max(0.0, round(leader_sum - data['sum'], 1)))
            iid = self.tree.insert("", tk.END, values=(name, j1, j2, total, gap))
            self.row_ids[name] = iid

    def set_score(self):
        name = self.name_entry.get().strip()
        s = self.score_entry.get().strip()
        if not name:
            messagebox.showwarning("Missing name", "Enter a player name.")
            return
        if not s:
            messagebox.showwarning("Missing score", "Enter a jump score.")
            return
        try:
            # Komma zu Punkt normalisieren, eine Dezimalstelle runden
            score = float(s.replace(",", "."))
            score = round(score, 1)
        except ValueError:
            messagebox.showerror("Invalid score", "Score must be a number with at most one decimal.")
            return

        jnum = self.jump_var.get()
        if name not in self.players:
            self.players[name] = {'j1': None, 'j2': None, 'sum': 0.0}
        self.ensure_row(name)

        key = 'j1' if jnum == 1 else 'j2'
        self.players[name][key] = score
        # Summe immer mit einer Nachkommastelle runden
        self.players[name]['sum'] = round((self.players[name]['j1'] or 0) + (self.players[name]['j2'] or 0), 1)

        # Werte sofort aktualisieren + alle Abstände neu berechnen
        self.update_row_values(name)
        self.refresh_gaps()

        self.score_entry.delete(0, tk.END)
        self.sort_mode = "sum"
        self.queue_animation(name)
        self.select_name(name)
        self.score_entry.focus_set()

    def update_row_values(self, name):
        iid = self.row_ids.get(name)
        if not iid:
            return
        data = self.players[name]
        j1 = "" if data['j1'] is None else self.format_score(data['j1'])
        j2 = "" if data['j2'] is None else self.format_score(data['j2'])
        total = "" if (data['j1'] is None and data['j2'] is None) else self.format_score(data['sum'])
        leader_sum = self.get_leader_sum()
        attempted = (data['j1'] is not None or data['j2'] is not None)
        gap = "" if (leader_sum is None or not attempted) else self.format_score(
            max(0.0, round(leader_sum - data['sum'], 1)))
        self.tree.item(iid, values=(name, j1, j2, total, gap))

    def refresh_gaps(self):
        leader_sum = self.get_leader_sum()
        for name, iid in self.row_ids.items():
            d = self.players[name]
            attempted = (d['j1'] is not None or d['j2'] is not None)
            j1 = "" if d['j1'] is None else self.format_score(d['j1'])
            j2 = "" if d['j2'] is None else self.format_score(d['j2'])
            total = "" if (d['j1'] is None and d['j2'] is None) else self.format_score(d['sum'])
            if leader_sum is None or not attempted:
                gap = ""
            else:
                gap_val = max(0.0, round(leader_sum - d['sum'], 1))
                gap = self.format_score(gap_val)
            self.tree.item(iid, values=(name, j1, j2, total, gap))

    def select_name(self, name):
        iid = self.row_ids.get(name)
        if iid:
            self.tree.selection_set(iid)
            self.tree.see(iid)

    def format_score(self, val):
        if val is None:
            return ""
            # Anzeige immer mit einer Dezimalstelle und deutschem Komma
        return f"{val:.1f}".replace(".", ",")

    def sort_by(self, field):
        self.cancel_animation()
        self.sort_mode = "sum" if field in ("sum", "gap") else "name"
        self.refresh_table()

    def refresh_table(self):
        for iid in self.tree.get_children():
            self.tree.delete(iid)
        self.row_ids.clear()

        items = list(self.players.items())
        if self.sort_mode == "sum":
            items.sort(key=lambda kv: (-kv[1]['sum'], kv[0].lower()))
        else:
            items.sort(key=lambda kv: kv[0].lower())

        leader_sum = self.get_leader_sum()

        for name, data in items:
            j1 = "" if data['j1'] is None else self.format_score(data['j1'])
            j2 = "" if data['j2'] is None else self.format_score(data['j2'])
            total = "" if (data['j1'] is None and data['j2'] is None) else self.format_score(data['sum'])
            attempted = (data['j1'] is not None or data['j2'] is not None)
            gap = "" if (leader_sum is None or not attempted) else self.format_score(
                max(0.0, round(leader_sum - data['sum'], 1)))
            iid = self.tree.insert("", tk.END, values=(name, j1, j2, total, gap))
            self.row_ids[name] = iid

    def reset_all(self):
        if messagebox.askyesno("Reset", "Clear all players and scores?"):
            self.cancel_animation()
            self.players.clear()
            self.row_ids.clear()
            for iid in self.tree.get_children():
                self.tree.delete(iid)

    def on_select_row(self, event):
        sel = self.tree.selection()
        if sel:
            vals = self.tree.item(sel[0], "values")
            if vals:
                self.name_entry.delete(0, tk.END)
                self.name_entry.insert(0, vals[0])

                # Animation management

    def queue_animation(self, name):
        if name not in self.players:
            return
        if name not in self.animation_queue:
            self.animation_queue.append(name)
        if not self.animating:
            self.animate_next()

    def animate_next(self):
        if not self.animation_queue:
            return
        name = self.animation_queue.pop(0)
        self.animate_move(name)

    def cancel_animation(self):
        if self.anim_after_id:
            try:
                self.after_cancel(self.anim_after_id)
            except Exception:
                pass
        self.anim_after_id = None
        self.animating = False
        for iid in self.tree.get_children():
            tags = list(self.tree.item(iid, "tags"))
            if "moving" in tags:
                tags.remove("moving")
                self.tree.item(iid, tags=tuple(tags))
        self.animation_queue.clear()

    def get_sorted_names(self):
        names = list(self.players.keys())
        if self.sort_mode == "sum":
            names.sort(key=lambda n: (-self.players[n]['sum'], n.lower()))
        else:
            names.sort(key=lambda n: n.lower())
        return names

    def get_leader_sum(self):
        sums = [
            d['sum']
            for d in self.players.values()
            if (d['j1'] is not None or d['j2'] is not None)
        ]
        if not sums:
            return None
        return max(sums)

    def animate_move(self, name):
        iid = self.row_ids.get(name)
        if not iid:
            self.animating = False
            self.anim_after_id = None
            self.animate_next()
            return

        self.animating = True

        tags = set(self.tree.item(iid, "tags") or [])
        tags.add("moving")
        self.tree.item(iid, tags=tuple(tags))

        children = list(self.tree.get_children())
        current_idx = children.index(iid)

        sorted_names = self.get_sorted_names()
        target_idx = sorted_names.index(name)

        if target_idx == current_idx:
            tags.remove("moving")
            self.tree.item(iid, tags=tuple(tags))
            self.animating = False
            self.anim_after_id = None
            self.animate_next()
            return

        step = -1 if target_idx < current_idx else 1
        delay_ms = 800

        def do_step():
            nonlocal current_idx
            next_idx = current_idx + step
            try:
                self.tree.move(iid, "", next_idx)
            except tk.TclError:
                self.cancel_animation()
                return
            current_idx = next_idx
            self.tree.see(iid)
            if current_idx != target_idx:
                self.anim_after_id = self.after(delay_ms, do_step)
            else:
                current_tags = set(self.tree.item(iid, "tags") or [])
                if "moving" in current_tags:
                    current_tags.remove("moving")
                    self.tree.item(iid, tags=tuple(current_tags))
                self.animating = False
                self.anim_after_id = None
                self.animate_next()

        self.anim_after_id = self.after(delay_ms, do_step)

        # File operations

    def browse_file(self):
        path = filedialog.asksaveasfilename(
            defaultextension=".json",
            filetypes=[("JSON files", "*.json"), ("All files", "*.*")],
            initialfile=self.file_entry.get().strip() or "ski_scores.json",
            title="Choose file"
        )
        if path:
            self.file_entry.delete(0, tk.END)
            self.file_entry.insert(0, path)

    def save_to_file(self):
        path = self.file_entry.get().strip()
        if not path:
            messagebox.showwarning("No file", "Please enter a filename to save.")
            return
        try:
            data = {
                "sort_mode": self.sort_mode,
                "players": {
                    name: {"j1": self.players[name]['j1'], "j2": self.players[name]['j2']}
                    for name in self.players
                }
            }
            dirpart = os.path.dirname(path)
            if dirpart and not os.path.exists(dirpart):
                os.makedirs(dirpart, exist_ok=True)
            with open(path, "w", encoding="utf-8") as f:
                json.dump(data, f, indent=2)
            messagebox.showinfo("Saved", f"Scores saved to:\n{path}")
        except Exception as e:
            messagebox.showerror("Save failed", f"Could not save file:\n{e}")

    def load_from_file(self):
        path = self.file_entry.get().strip()
        if not path:
            messagebox.showwarning("No file", "Please enter a filename to load.")
            return
        if not os.path.exists(path):
            pick = filedialog.askopenfilename(
                filetypes=[("JSON files", "*.json"), ("All files", "*.*")],
                title="Select file to load"
            )
            if not pick:
                return
            path = pick
            self.file_entry.delete(0, tk.END)
            self.file_entry.insert(0, path)
        try:
            with open(path, "r", encoding="utf-8") as f:
                data = json.load(f)
            if not isinstance(data, dict) or "players" not in data:
                raise ValueError("Invalid file format.")
            loaded_players = {}
            players_obj = data.get("players", {})
            for name, pdata in players_obj.items():
                j1 = pdata.get("j1", None)
                j2 = pdata.get("j2", None)
                j1 = float(j1) if j1 is not None else None
                j2 = float(j2) if j2 is not None else None
                # Rundung auf eine Dezimalstelle sicherstellen
                j1 = None if j1 is None else round(j1, 1)
                j2 = None if j2 is None else round(j2, 1)
                ssum = round((j1 or 0) + (j2 or 0), 1)
                loaded_players[name] = {"j1": j1, "j2": j2, "sum": ssum}
            self.cancel_animation()
            self.players = loaded_players
            self.sort_mode = data.get("sort_mode", "sum")
            self.refresh_table()
            messagebox.showinfo("Loaded", f"Scores loaded from:\n{path}")
        except Exception as e:
            messagebox.showerror("Load failed", f"Could not load file:\n{e}")

            # Eingabevalidierung: maximal 1 Dezimalstelle, Komma oder Punkt erlaubt

    def validate_score_input(self, newval: str) -> bool:
        if newval == "":
            return True
        return bool(re.match(r'^\d+([.,]\d?)?$', newval))


if __name__ == "__main__":
    app = SkiJumpApp()
    app.mainloop()