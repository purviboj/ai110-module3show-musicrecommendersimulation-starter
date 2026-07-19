from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass
import csv


@dataclass
class Song:
    """
    Represents a song and its attributes.
    Required by tests/test_recommender.py
    """
    id: int
    title: str
    artist: str
    genre: str
    mood: str
    energy: float
    tempo_bpm: float
    valence: float
    danceability: float
    acousticness: float

@dataclass
class UserProfile:
    """
    Represents a user's taste preferences.
    Required by tests/test_recommender.py
    """
    favorite_genre: str
    favorite_mood: str
    target_energy: float
    likes_acoustic: bool

class Recommender:
    """
    OOP implementation of the recommendation logic.
    Required by tests/test_recommender.py
    """
    def __init__(self, songs: List[Song]):
        self.songs = songs

    def recommend(self, user: UserProfile, k: int = 5) -> List[Song]:
        # TODO: Implement recommendation logic
        return self.songs[:k]

    def explain_recommendation(self, user: UserProfile, song: Song) -> str:
        # TODO: Implement explanation logic
        return "Explanation placeholder"

def load_songs(csv_path: str) -> List[Dict]:
    """
    Loads songs from a CSV file and converts numeric values
    into Python numbers.
    """
    songs = []

    with open(csv_path, newline="", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)

        for row in reader:
            row["id"] = int(row["id"])
            row["energy"] = float(row["energy"])
            row["tempo_bpm"] = float(row["tempo_bpm"])
            row["valence"] = float(row["valence"])
            row["danceability"] = float(row["danceability"])
            row["acousticness"] = float(row["acousticness"])

            songs.append(row)

    return songs

def score_song(user_prefs: Dict, song: Dict) -> Tuple[float, List[str]]:
    """
    Scores a song based on the user's preferences.
    Returns the numeric score and the reasons for that score.
    """
    score = 0.0
    reasons = []

    # Genre match
    if song["genre"].lower() == user_prefs["genre"].lower():
        score += 2.0
        reasons.append("Genre match (+2.0)")

    # Mood match
    if song["mood"].lower() == user_prefs["mood"].lower():
        score += 1.0
        reasons.append("Mood match (+1.0)")

    # Energy similarity
    energy_difference = abs(song["energy"] - user_prefs["energy"])
    energy_score = max(0, 1 - energy_difference)

    score += energy_score 

    if energy_score >= 0.75:
        reasons.append(f"Similar energy (+{energy_score:.2f})")
    return score, reasons

def recommend_songs(user_prefs: Dict, songs: List[Dict], k: int = 5) -> List[Tuple[Dict, float, str]]:
    """
    Scores every song, sorts them by score, and returns
    the top k recommendations.
    """
    recommendations = []

    for song in songs:
        score, reasons = score_song(user_prefs, song)
        explanation = ", ".join(reasons)
        recommendations.append((song, score, explanation))

    recommendations.sort(key=lambda x: x[1], reverse=True)

    return recommendations[:k]
