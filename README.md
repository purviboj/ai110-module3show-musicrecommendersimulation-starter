# 🎵 Music Recommender Simulation

## Project Summary

This project simulates a simple content-based music recommendation system. It compares a user's preferred genre, mood, and energy level with songs in a music catalog and assigns each song a weighted score. The highest-scoring songs are returned as personalized recommendations along with explanations describing why they were selected.



---

## How The System Works

Real-world music recommendation systems use information about users and songs to predict what someone may enjoy listening to next. Some platforms use collaborative filtering by comparing users with similar listening habits, while others use content-based filtering that compares song features such as genre, mood, and energy. This project implements a simple content-based recommender.

The recommender compares a user's preferred genre, mood, energy level, and valence with every song in the dataset. Each song receives points for matching these preferences, and the songs are ranked from the highest score to the lowest. The highest-ranked songs are returned as recommendations.
User Preferences
      │
      ▼
Load songs from songs.csv
      │
      ▼
Score each song
      │
      ▼
Rank songs
      │
      ▼
Return Top 5 Recommendations

### Features Used

- Genre
- Mood
- Energy
- Valence
Each song is compared against the user's preferences using a weighted scoring system.

- +2 points if the genre matches.
- +1 point if the mood matches.
- Up to +1 point based on how close the song's energy level is to the user's preferred energy.

After every song receives a score, the songs are sorted from highest to lowest score. The recommender returns the top five songs with the highest scores.

### Potential Biases

This recommender prioritizes genre more heavily than other features, so it may overlook songs from different genres that have a similar mood or energy. Since the dataset is relatively small, recommendations may also become repetitive and not represent the full diversity of music available.
---

## Getting Started

### Setup

1. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv .venv
   source .venv/bin/activate      # Mac or Linux
   .venv\Scripts\activate         # Windows

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Run the app:

```bash
python -m src.main
```

### Running Tests

Run the starter tests with:

```bash
pytest
```

You can add more tests in `tests/test_recommender.py`.

---

## Sample Recommendation Output


### Happy Pop

```text
Sunrise City - Score: 3.98
Because: Genre match (+2.0), Mood match (+1.0), Similar energy (+0.98)

Gym Hero - Score: 2.87
Because: Genre match (+2.0), Similar energy (+0.87)

Rooftop Lights - Score: 1.96
Because: Mood match (+1.0), Similar energy (+0.96)

Night Drive Loop - Score: 0.95
Because: Similar energy (+0.95)

Neon Basketball Court - Score: 0.92
Because: Similar energy (+0.92)
```

### Chill Lofi

```text
Midnight Coding - Score: 3.98
Because: Genre match (+2.0), Mood match (+1.0), Similar energy (+0.98)

Library Rain - Score: 3.95
Because: Genre match (+2.0), Mood match (+1.0), Similar energy (+0.95)

Focus Flow - Score: 3.00
Because: Genre match (+2.0), Similar energy (+1.00)

Spacewalk Thoughts - Score: 1.88
Because: Mood match (+1.0), Similar energy (+0.88)

Coffee Shop Stories - Score: 0.97
Because: Similar energy (+0.97)
```

### Intense Rock

```text
Storm Runner - Score: 3.99
Because: Genre match (+2.0), Mood match (+1.0), Similar energy (+0.99)

Run It Back Again - Score: 2.95
Because: Genre match (+2.0), Similar energy (+0.95)

Gym Hero - Score: 1.97
Because: Mood match (+1.0), Similar energy (+0.97)

Neon Basketball Court - Score: 0.98
Because: Similar energy (+0.98)

Sunrise City - Score: 0.92
Because: Similar energy (+0.92)
```

**Screenshot or video** *(optional)*: <!-- Insert a screenshot or demo video link here -->

---

## Experiments You Tried


I experimented by reducing the weight of the genre feature to 1.0 and not 2.0 while increasing the influence of energy similarity by multiplying by 2.0. This caused songs with similar energy levels to rank higher, even if they belonged to different genres.

Although the recommendations became more varied, some felt less accurate because genre is one of the strongest indicators of a user's musical preferences. I restored the original weights because they produced recommendations that better matched my expectations.

---

## Limitations and Risks



You will go deeper on this in your model card.
This recommender only considers genre, mood, and energy when making recommendations. It does not consider lyrics, artists, listening history, or user feedback. Since the dataset contains only 18 songs, recommendations can become repetitive. The algorithm also favors genre, which may cause songs from other genres with similar characteristics to be ranked lower.

---

## Reflection

Read and complete `model_card.md`:

[**Model Card**](model_card.md)


This project helped me understand how recommendation systems convert user preferences into numerical scores that can be used to rank content. I also learned that even a simple scoring algorithm can produce recommendations that feel personalized.

One interesting takeaway was how changing a single weight could noticeably affect the recommendations. It showed me that small design decisions can introduce bias or change the overall behavior of a recommendation system, which is why testing and evaluation are important.



