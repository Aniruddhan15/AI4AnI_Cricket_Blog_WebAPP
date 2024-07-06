# Given with steps:
## Make changes accordingly

"""
Install the Google AI Python SDK

$ pip install google-generativeai

See the getting started guide for more information:
https://ai.google.dev/gemini-api/docs/get-started/python
"""

import os

import google.generativeai as genai

genai.configure(api_key=os.environ["GEMINI_API_KEY"])

# Create the model
# See https://ai.google.dev/api/python/google/generativeai/GenerativeModel
generation_config = {
  "temperature": 0.6,
  "top_p": 1,
  "top_k": 0,
  "max_output_tokens": 2048,
  "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
  model_name="gemini-1.0-pro",
  generation_config=generation_config,
  # safety_settings = Adjust safety settings
  # See https://ai.google.dev/gemini-api/docs/safety-settings
)

chat_session = model.start_chat(
  history=[
    {
      "role": "user",
      "parts": [
        "Generate a comprehensive, engaging blog post relevent to \"cricket and the global leagues, ICC tournaments, player stats and players strength and role they play.\" Make sure to incorporate these keywords in the blog post. The blog content should have 500 words in length.Ensure the content is informative, and maintains a consistent tone throughout , and harmless to anyone\n",
      ],
    },
    {
      "role": "model",
      "parts": [
        "**Cricket: Global Leagues, ICC Tournaments, and the Powerhouse Players**\n\nCricket, a captivating sport that enjoys widespread popularity across the globe, has witnessed a significant surge in its global reach in recent years. The emergence of vibrant cricket leagues, prestigious ICC tournaments, and an array of exceptional players have all contributed to this growth.\n\n**Global Leagues: A Thriving Hub of Talent**\n\nOver the past decade, a plethora of cricket leagues have sprung up around the world, providing a platform for players to showcase their skills and connect with a diverse audience. These leagues have also played a crucial role in unearthing and nurturing young talent.\n\nSome of the most prominent global cricket leagues include the Indian Premier League (IPL), Big Bash League (BBL), and Caribbean Premier League (CPL). These leagues feature a star-studded lineup of players from various countries, giving fans an opportunity to witness their favorite cricketers in action.\n\n**ICC Tournaments: The Pinnacle of Cricket**\n\nThe International Cricket Council (ICC) organizes a series of prestigious tournaments that bring together the best cricket nations to compete for global supremacy. These tournaments include the Cricket World Cup, ICC Champions Trophy, and ICC T20 World Cup.\n\nICC tournaments are highly competitive and present a stage for players to etch their names into cricketing history. The performances of players in these tournaments often have a lasting impact on their careers and legacies.\n\n**Player Stats and Roles**\n\nCricket is a team sport that requires a diverse range of skills and roles. Each player has a specific role within the team, contributing to the overall success or failure. Key player statistics include batting average, bowling strike rate, and fielding efficiency.\n\nSome of the most iconic players in cricket history have excelled in specific roles. For example, Sachin Tendulkar is renowned as one of the greatest batsmen of all time, while Shane Warne is revered for his exceptional leg-spin bowling.\n\n**Strengths and Roles of Key Players**\n\n**Batsmen:** Batsmen are responsible for scoring runs for their team. Key strengths include a high batting average, consistent run-scoring, and the ability to adapt to different match situations.\n\n**Bowlers:** Bowlers aim to restrict the opposition from scoring runs. Key strengths include a high strike rate, economical bowling, and the ability to take wickets at crucial moments.\n\n**Fielders:** Fielders play a vital role in preventing the opposition from scoring runs and taking wickets. Key strengths include agility, quick reflexes, and accurate throwing.\n\n**Conclusion**\n\nCricket continues to captivate audiences around the world with its exciting global leagues, prestigious ICC tournaments, and exceptional players. The emergence of these leagues and tournaments has provided a platform for players to showcase their skills, while also highlighting the diverse strengths and roles that contribute to a successful cricket team. As cricket continues to evolve, the global reach and popularity of the sport are bound to soar to even greater heights.",
      ],
    },
  ]
)

response = chat_session.send_message("INSERT_INPUT_HERE")

print(response.text)