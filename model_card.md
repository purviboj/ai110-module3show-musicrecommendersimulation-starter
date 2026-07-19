# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name

**HarmonyMatch**

---

## 2. Intended Use

This recommender is designed to suggest songs based on a user's favorite genre, mood, and preferred energy level. It is intended as a classroom project to demonstrate how a simple content-based recommendation system works rather than to provide production-quality music recommendations. The model assumes that users with similar preferences will enjoy songs with similar characteristics.

---

## 3. How the Model Works

The recommender compares each song in the dataset to the user's preferences. It checks whether the song's genre and mood match the user's favorites and awards points for those matches. It also compares the song's energy level to the user's preferred energy level and gives a higher score when they are closer together. After every song receives a score, the songs are sorted from highest to lowest, and the top recommendations are returned with a brief explanation.

---

## 4. Data

The dataset contains 18 songs covering a variety of genres including pop, rock, lofi, jazz, hip hop, folk, country, blues, electronic, and alternative music. I expanded the original starter dataset by adding additional songs to create more variety in the recommendations. The dataset is still relatively small and does not include factors such as lyrics, artists, listening history, or popularity.

---

## 5. Strengths

The recommender performs well when users have clear preferences for a specific genre and mood. During testing, the Happy Pop, Chill Lofi, and Intense Rock profiles consistently received recommendations that matched their expected musical style. The explanations also make it easy to understand why each song was recommended.

---

## 6. Limitations and Bias

The recommender only considers genre, mood, and energy when calculating scores. Because genre receives the highest weight, songs from different genres with similar characteristics may still rank lower. The small dataset also limits recommendation diversity, causing the same songs to appear frequently. Unlike real streaming services, this model does not learn from user behavior or listening history.

---

## 7. Evaluation

I tested the recommender using three user profiles: Happy Pop, Chill Lofi, and Intense Rock. Each profile produced a different recommendation list, showing that the scoring algorithm responds to changes in user preferences. I also experimented with increasing the importance of energy while reducing the importance of genre. This created more varied recommendations but made some results feel less accurate because genre is a strong indicator of musical taste.

---

## 8. Future Work

If I continued this project, I would:
- Include additional song features such as tempo, danceability, and acousticness.
- Use a much larger music catalog to improve recommendation diversity.
- Add collaborative filtering so recommendations could also be based on users with similar listening habits.
- Improve the explanation system by providing more detailed reasons for each recommendation.

---

## 9. Personal Reflection

This project helped me understand how recommendation systems transform user preferences into numerical scores that can be used to rank content. Even though the algorithm is simple, it still produced recommendations that felt personalized. One of the biggest lessons I learned was how changing a single scoring weight could noticeably change the recommendations. It also showed me why testing for bias and evaluating different user profiles is important when designing recommendation systems.