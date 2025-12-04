# utils/memory.py — EchoCare Ultra Memory System
# Stores last N user messages + persistent long-term JSON memory.

import json
import os

class EchoMemory:
    def __init__(self, user_id="default_user", max_items=20,
                 storage_path="data/user_profile.json"):
        self.user_id = user_id
        self.max_items = max_items
        self.storage_path = storage_path
        self.memories = []

        # ensure folder exists
        os.makedirs(os.path.dirname(self.storage_path), exist_ok=True)

        # load any existing memory
        self._load()

    # -----------------------------------------------------------
    # LOAD persistent memory
    # -----------------------------------------------------------
    def _load(self):
        if not os.path.exists(self.storage_path):
            self.memories = []
            return

        try:
            with open(self.storage_path, "r", encoding="utf-8") as f:
                data = json.load(f)

            self.memories = data.get(self.user_id, [])
        except Exception:
            self.memories = []

    # -----------------------------------------------------------
    # SAVE persistent memory
    # -----------------------------------------------------------
    def _save(self):
        try:
            # load existing file
            if os.path.exists(self.storage_path):
                with open(self.storage_path, "r", encoding="utf-8") as f:
                    all_data = json.load(f)
            else:
                all_data = {}

            all_data[self.user_id] = self.memories

            with open(self.storage_path, "w", encoding="utf-8") as f:
                json.dump(all_data, f, indent=2, ensure_ascii=False)

        except Exception as e:
            print("Memory save failed:", e)

    # -----------------------------------------------------------
    # Add new message
    # -----------------------------------------------------------
    def add(self, text: str):
        if not text or not text.strip():
            return

        self.memories.append(text.strip())

        # keep max_items only
        if len(self.memories) > self.max_items:
            self.memories = self.memories[-self.max_items:]

        self._save()

    # -----------------------------------------------------------
    # Return the last few messages as summary
    # -----------------------------------------------------------
    def get_summary(self) -> str:
        if not self.memories:
            return "No previous messages yet."

        # return last 5 messages joined
        return " | ".join(self.memories[-5:])

    # -----------------------------------------------------------
    # Clear all memory
    # -----------------------------------------------------------
    def clear(self):
        self.memories = []
        self._save()
