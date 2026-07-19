# 🎵 Music Recommender Simulation

## Project Summary

In this project you will build and explain a small music recommender system.

Your goal is to:

- Represent songs and a user "taste profile" as data
- Design a scoring rule that turns that data into recommendations
- Evaluate what your system gets right and wrong
- Reflect on how this mirrors real world AI recommenders

Replace this paragraph with your own summary of what your version does.

---

## How The System Works

Explain your design in plain language.

Some prompts to answer:

- What features does each `Song` use in your system
  - For example: genre, mood, energy, tempo
- What information does your `UserProfile` store
- How does your `Recommender` compute a score for each song
- How do you choose which songs to recommend

You can include a simple diagram or bullet list if helpful.
Real-world music recommendation systems use information about users and songs to predict what someone may enjoy listening to next. Some platforms use collaborative filtering by comparing users with similar listening habits, while others use content-based filtering that compares song features such as genre, mood, and energy. This project implements a simple content-based recommender.

The recommender compares a user's preferred genre, mood, energy level, and valence with every song in the dataset. Each song receives points for matching these preferences, and the songs are ranked from the highest score to the lowest. The highest-ranked songs are returned as recommendations.

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

Paste a sample of your recommender's output here as a text block so a reader can see what it produces:

```
# e.g.:
# User profile: genre=indie, mood=chill, energy=low
# Recommendations:
#   1. ...
#   2. ...
#   3. ...
Top recommendations:

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

**Screenshot or video** *(optional)*: <!-- Insert a screenshot or demo video link here -->

---

## Experiments You Tried

Use this section to document the experiments you ran. For example:

- What happened when you changed the weight on genre from 2.0 to 0.5
- What happened when you added tempo or valence to the score
- How did your system behave for different types of users

---

## Limitations and Risks

Summarize some limitations of your recommender.

Examples:

- It only works on a tiny catalog
- It does not understand lyrics or language
- It might over favor one genre or mood

You will go deeper on this in your model card.

---

## Reflection

Read and complete `model_card.md`:

[**Model Card**](model_card.md)

Write 1 to 2 paragraphs here about what you learned:

- about how recommenders turn data into predictions
- about where bias or unfairness could show up in systems like this



