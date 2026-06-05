# Natural Language Processing
  Natural language processing is a branch of AI which gives computers the ability to understand, interpret, and generate human language.

  Basically it bridges the gap between human communication(which is messy, nuanced, and unstructured) and computer code(which relies on strict, structured syntax).

  ## How NLP Works
  Human language is incredibly complex. It is full of idioms, sarcasm, accents, and homonyms (words that sound the same but have different meanings). To make sense of this, NLP breaks language down into smaller pieces through several core steps:
   - **Tokenization**: Breaking text into individual words or phrases (tokens).
   - **Stop Word Removal**: Filtering out common filler words (like "and," "the," or "is") that don't add core meaning.
   - **Stemming and Lemmatization**: Reducing words to their base or root form (e.g., "running" and "ran" become "run").
   - **Part-of-Speech (POS) Tagging**: Identifying nouns, verbs, adjectives, etc., to understand the grammatical structure.
   - **Named Entity Recognition (NER)**: Spotting and categorizing specific entities like names, places, dates, or organizations.

  ## Two Halves of NLP
  NLP generally splits into two main functional areas:
  - **Natural Language Understanding(NLU)**: This focuses on reading comprehension and intent. It determines what a human means, even if they use slang, make typos, or phrase things awkwardly.
  - **Natural Language Generation (NLG)**: This is the creative side. It takes structured computer data and translates it into natural-sounding human language.

  ## Examples of application using NLP
  - **Search Engines**: Autocomplete features and understanding the intent behind a vague search query.
  - **Smart Assistants**: Siri, Alexa, and Google Assistant processing your voice commands.
  - **Translation Tools**: Services like Google Translate converting one language to another in real-time.
  - **Spam Filters**: Email clients detecting phishing patterns or unwanted promotional mail.
  - **Sentiment Analysis**: Businesses analyzing social media comments or product reviews to see if customer feedback is generally positive, negative, or neutral.

  ## Difference between Text Mining and NLP
  Both are of techniques used in AI to dela with human languages, but they have different different goals, approaches, and technical depths

  **Text Mining** looks for patterns and statistics across vast amount of text.

  **Natural Language Processing** tries to understand the meaning and structure of the language.


  |Feature|Text Mining|Natural Language Processing|
  |-------|-----------|---------------------------|
  |Primary Goal|Discover hidden patterns, trends, and statistics across large datasets.|Understand, interpret, and generate human language like a human would.|
  |Focus|Quantity & Aggregation: What are the major themes or trends in these 10,000 documents?|Quality & Context: What is the specific meaning, intent, or emotion behind this sentence?|
  |Output|Graphs, charts, frequency tables, clusters, and structured data.|Sentences, translated text, precise answers, or contextual actions.|
  |Type of Analysis|Quantitative (counting, sorting, clustering).|Qualitative (syntax, semantics, pragmatics).|

 ## Case Study of Usage of Text Mining and NLP
 In modern data science, these two fields heavily overlap. Text mining frequently uses NLP techniques as a preprocessing step to clean and understand text before running statistical analyses.

 Let's say you run Sentiment Analysis on social media data.
  - **NLP** is used to analyze individual tweets to understand if a phrase like "That's sick!" means something is cool (positive) or gross (negative).
  - **Text Mining** then takes those millions of NLP-processed scores and aggregates them into a dashboard showing that overall public sentiment toward a brand dropped by 15% this week.
