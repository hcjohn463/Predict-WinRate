# Predict-WinRate
# 英雄聯盟勝率預測

## Game Data

#### OPGG：https://op.gg/ranking/ladder/
#### Server : ['br', 'jp', 'euw', 'oce', 'lan', 'tr', 'www', 'na', 'eune','las', 'ru']

|Game version|Game type|Totally Games|Data Preprocessing|
| ------- | ------------| ---------- | --------------- |
|10.25|Ranked Solo|5008|Drop Remake Game|

## Game Prediction

### According to the team composition of both characters, the accuracy of predicting the winner (%)

|Game version|Game type|RandomForest|AdaBoost|XGBoost|SVM|Logistic Regression|
| ------ | ------------ | -------- | -------- | -------- | -------- | -------- |
|10.25|Ranked Solo| 84.3 | 85.0 | 83.0 | 81.1 | 80.0 |

## Reference
#### 1. How I created a League of Legends High-Elo database using scrapy :https://medium.com/@_marcusft/how-i-created-a-league-of-legends-high-elo-database-using-scrapy-3becdee8f385
