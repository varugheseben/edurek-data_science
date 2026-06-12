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

  ## Benefits of NLP
  - Ability to analyze both structured and unstructured data like speech, voices, social media posts
  - Improve customer satisfaction
  - Ability to understand target market
  - Reduce costs - Using NLP based systems to answer customer queries

  ## Limitations of NLP
  - Ambiguity in understanding the emotions, context, sarcasm, slang, errors exists human language

    **Types of Ambiguity in NLP**
    - **Lexical (Word level) Ambiguity**: Lexical ambiguity happens when a single word has more than one meaning. There are 2 types of this
      - Polysemy: A word has multiple meanings that are conceptually related.
         - Example: **"Run"** (To physically jog vs. to operate a piece of software).
      - **Homonymy**: A word has multiple meanings that are entirely unrelated.
         - Example: **"Bank"** (A financial institution vs. the side of a river).
    - **Syntactic(Structural) Ambiguity**: Syntactic ambiguity occurs when a whole sentence can be parsed into completely different grammatical structures, altering the meaning even if every individual word is perfectly understood.
       - **Prepositional Phrase Attachment**: A classic problem where it's unclear what a descriptive phrase modifies.
         - Example: "I saw the man with the telescope."
         - Interpretation A: I used a telescope to look at a man.
         - Interpretation B: I looked at a man who was holding a telescope.
       - **Coordination Scope**: Ambiguity introduced by conjunctions like "and" or "or".
         - Example: "Old men and women." (Does "old" apply to just the men, or both the men and the women?)
    - **Semantic Ambiguity**: Semantic ambiguity occurs when a sentence is grammatically clear and the words are well-defined, but the overall meaning of the sentence is still up for interpretation
      - Example: "Every girl loves a boy."
      - Interpretation A: For every individual girl in the world, there is a specific boy that she loves
      - Interpretation B: There is one specific, single boy that all girls collectively love.
    - **Anaphoric (Referential) Ambiguity**: This occurs when a pronoun (like he, she, it, they) or a referring phrase could point to multiple preceding nouns (entities) mentioned in the text.
      - Example: "The trophy didn't fit into the brown suitcase because it was too large."
      - The Problem: What does "it" refer to? Humans know a trophy doesn't fit into a suitcase if the trophy is too large. However, if you change the ending to "because it was too small", the word "it" suddenly flips to mean the suitcase.
    - **Pragmatic Ambiguity**: Pragmatic ambiguity happens when the literal meaning of a sentence is completely different from its intended meaning in a social or real-world context. It deals with intent, sarcasm, idioms, and subtext.
      - Example: "Can you pass the salt?"
      - Literal Meaning: A literal AI might look at your physical capability and answer: "Yes, I am physically capable of lifting and moving the salt shaker."
      - Pragmatic Meaning: The speaker is actually issuing a polite command/request to hand them the salt.
  - Failed to generate outcome of ambiguos statements

  ## Difference between Text Mining and NLP
  Both are of techniques used in AI to deal with human languages, but they have different different goals, approaches, and technical depths

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

 ## Setting up nltk
  - [NLTK Setup](https://github.com/varugheseben/edurek-data_science/blob/main/Artificial%20Intelligence/Natural%20Language%20Processing/Examples/nltk_setup.ipynb)
  - [NLTK Dataset Download](https://github.com/varugheseben/edurek-data_science/blob/main/Artificial%20Intelligence/Natural%20Language%20Processing/Examples/nltk_download.ipynb)

 ## Different concepts in NLP
  - ### **Corpus** (Plural corpora)

    In Natural Language Processing (NLP), a **corpus** (plural: corpora) is a large, structured collection of machine-readable texts or audio files compiled for linguistic analysis, model training, and statistical verification.

    Think of it as the ultimate textbook or dataset from which an AI or NLP algorithm learns how human language works.

    **Key Characteristics of Corpus**

    Not just any random pile of text qualifies as a corpus. To be useful for NLP, a corpus typically must be:
     - **Machine-Readable**: The text must be in a digital format (like .txt, .json, or .xml) that an NLP pipeline can tokenize, parse, and process automatically.
     - **Structured**: A good corpus is organized with metadata. For example, a corpus of book reviews might label each text with a star rating, a timestamp, and the category of the product.
     - **Representative**: It should accurately reflect the specific language, dialect, or domain it is meant to model. If you want to train a chatbot for a bank, your corpus should contain financial documents and customer service transcripts, not classical poetry.
   
    **Examples of Copora in NLP**
     - **Gutenberg**: Contains books, and is used for text analysis
        - [Example to view Gutenberg Corpora](https://github.com/varugheseben/edurek-data_science/blob/main/Artificial%20Intelligence/Natural%20Language%20Processing/Corpus/view_gutenberg_corpora.ipynb)
     - **Stopwords**: Contains common words, and is used for cleaning text
        - [Example to view Stopwords Corpora](https://github.com/varugheseben/edurek-data_science/blob/main/Artificial%20Intelligence/Natural%20Language%20Processing/Corpus/view_stopwords_corpora.ipynb)
     - **Wordnet**: Contains word meanings, and is used for semantics
        - [Example to view Wordnet Corpora](https://github.com/varugheseben/edurek-data_science/blob/main/Artificial%20Intelligence/Natural%20Language%20Processing/Corpus/view_wordnet_corpora.ipynb)
     - **Brown**: Contains text tagged with part of speech labels(nouns, verbs, adjectives, etc)
        - [Example to view Brown Corpora](https://github.com/varugheseben/edurek-data_science/blob/main/Artificial%20Intelligence/Natural%20Language%20Processing/Corpus/view_brown_corpora.ipynb)
     - **Movie Reviews**: Contains movie reviews, and is used for sentiment analysis
        - [Example to view Movie Review Corpora](https://github.com/varugheseben/edurek-data_science/blob/main/Artificial%20Intelligence/Natural%20Language%20Processing/Corpus/view_movie_review_corpora.ipynb)
      
    **Why Corpus is Necessary**
     - It is usefull for training NLP models
     - It is usefull for doing tokenization, stemming, Part of speech tagging
     - It is usefull for doing sentiment analysis
     - It is usefull for testing algorithms
     - It is usefull for studying language patterns
     - It is usefull for building chatbots

    **Lab**
     - [Example to list all Corpora]()

  - ### **Tokenization**

    It is the process of breaking text into individual words or phrases (tokens). A token can be a word or a sentence or a character or a sub word
      - Example: Lets say I have a sentence as "Let us learn Natural Language Processing". So tokens will be
         1. Let
         2. us
         3. learn
         4. Natural
         5. Language
         6. Processing

      **Why Tokenization is Necessary**
       - It helps to count words
       - It helps to identify sentiments
       - It helps to remove stopwords
       - It helps to do part of speech tagging
   
      **Examples**
       - [Tokenizing Words](https://github.com/varugheseben/edurek-data_science/blob/main/Artificial%20Intelligence/Natural%20Language%20Processing/Examples/Tokenization/nltk_word_tokenizing.ipynb)
       - [Tokenizing Sentences](https://github.com/varugheseben/edurek-data_science/blob/main/Artificial%20Intelligence/Natural%20Language%20Processing/Examples/Tokenization/nltk_sentence_tokenizing.ipynb)

  - ### **Frequency Distribution**

    Frequency distribution is used for determining how much time each token is repeated. This technique is used both in the case of work and sentence tokenization
    - [Example](https://github.com/varugheseben/edurek-data_science/blob/main/Artificial%20Intelligence/Natural%20Language%20Processing/Examples/Tokenization/frequency_distribution.ipynb)

  - ### **N-grams**

    In Natural Language Processing (NLP), an n-gram is a contiguous sequence of n items from a given sample of text or speech. Depending on the application, these items can be syllables, letters, words, or base pairs. Typically, in word-level NLP, they refer to sequences of co-occurring words.

    The "n" in n-gram stands for the number of elements in the sequence.

    **Types of N-grams**
     - **Unigram(n==1)**: A sequence of single word.
       - Example: 'Natural', 'Language', 'Processing'
     - **Bigram(n==2)**: A sequence of two consecutive words.
       - Example: 'Data Science', 'Learning NLP'
     - **Trigram(n==3)**: A sequence of three consecutive words.
       - Example: 'Natural Language Processing'
     - **N-gram(n>3)**: A sequence of N consecutive words.
       - Example: 'Learning Natural Language Processing', 'Python has many libraries which can be used for building systems with artificial intelligence'

    **Why do we use N-grams**
     - Preserving Context and Word Order
   
       Traditional NLP techniques like Bag-of-Words (BoW) treat a document as an unordered collection of words. This completely destroys context.
        - Consider the phrases: "Not good" vs. "Good, not bad".
        - A unigram model sees the same words, but a bigram model captures "not good" and "not bad", allowing a machine to correctly interpret sentiment.
     - Language Modeling and Next-Word Prediction

       N-grams are heavily used to calculate the probability of a word appearing next in a sentence based on the words that came before it. This powers:
        - Auto-correct algorithms
        - Search engine autocomplete suggestions
        - Speech recognition systems (deciding if a user said "there" or "their" based on context)

    **Lab**
     - [Example of Bigram](https://github.com/varugheseben/edurek-data_science/blob/main/Artificial%20Intelligence/Natural%20Language%20Processing/Examples/N-grams/bigram.ipynb)
     - [Example of Trigram](https://github.com/varugheseben/edurek-data_science/blob/main/Artificial%20Intelligence/Natural%20Language%20Processing/Examples/N-grams/trigram.ipynb)
     - [Example of N-gram](https://github.com/varugheseben/edurek-data_science/blob/main/Artificial%20Intelligence/Natural%20Language%20Processing/Examples/N-grams/n_gram.ipynb)

  - ### **Stemming**

    It is the text-preprocessing technique of reducing a word to its base or root form (known as the "stem").

    Example:
     - Stem for running, ran, runs is run
     - Stem for playing, played, plays is play

    Basically goal is to map related words to the same core token so a computer can treat them as the exact same concept. This way it will reduce the vocabulary size.

    **How Stemming Works**

    Stemmers do not understand vocabulary or grammar rules; they operate like a blunt pair of scissors. For example, a common rule in a stemmer might be: "If a word ends in 'ing', strip 'ing' off."

    **Why it is useful**
     - Used in **Information Retrieval System(eg: Search Engines)**: Lets say if user search for 'reading' then with help of stemming it will also search for word 'read'. This helps to generate accurate results for search engines
     - Used for sentiment analysis
     - Reduces vocabulary size
   
    **Errors in Stemming**
     - **Over Stemming(False Positive)**: This happens when two completely different words are chopped down to the exact same root, incorrectly linking their meanings.
       Example:
        - Words like 'Universal', 'University' and 'Universe' will be stemmed as 'Univers'. With this, a NLP model could predict that student attending a university is studying the 'universe'
     - **Under Stemming(False Negative)**: This happens when two words that should share the same root are cut differently, leaving them as distinct tokens.
       Example:
        - "alumnus" might stem to alumnu, while "alumni" stems to alumni. The system fails to see they are plural/singular variations of the same concept.
      
    **Different Stemming Algorithms**
     - **Porter Stemmer**: This is old stemmer algorithm. It is moderately aggressive but very reliable and computationally fast.
     - **Lancaster Stemmer**: Developed at Lancaster University, this is an incredibly aggressive stemmer. It is fast but causes a lot of over-stemming.
     - **Snowball Stemmer**: Also known as the "Porter2" stemmer, this is an improvement over the original Porter algorithm. It is slightly more precise, handles edge cases better, and supports multiple languages besides English(like Spanish, German, and French).

    **Lab**
     - [PorterStemmer](https://github.com/varugheseben/edurek-data_science/blob/main/Artificial%20Intelligence/Natural%20Language%20Processing/Examples/Stemming/porter_stemmer.ipynb)
     - [LancasterStemmer](https://github.com/varugheseben/edurek-data_science/blob/main/Artificial%20Intelligence/Natural%20Language%20Processing/Examples/Stemming/lancaster_stemmer.ipynb)
     - [SnowballStemmer](https://github.com/varugheseben/edurek-data_science/blob/main/Artificial%20Intelligence/Natural%20Language%20Processing/Examples/Stemming/snowball_stemmer.ipynb)
     - [Stemming](https://github.com/varugheseben/edurek-data_science/blob/main/Artificial%20Intelligence/Natural%20Language%20Processing/Examples/Stemming/stemming.ipynb)
             
  - ### **Lemmatization**

    This is a technique used in NLP to understand the conext of a word in a given sentence. Basically its the process of determining base form of the word known as **Lemma**.

    A Lemma is the canonical, dictionary form of a word

    Example:
      - Lemma for 'running', 'runs' and 'ran' is run when the part of speech is verb.

    Basically for lemmatization techniques uses part of speech of a word for determining the correct lemma.

    **How it Works**

    Unlike simpler methods that just chop off the ends of words, lemmatization relies on a deep understanding of a language's morphology. It utilizes vocabulary databases and morphological analysis to accurately return the base form of a word based on its context.

    To work correctly, a lemmatizer usually needs to know the Part of Speech (POS) of a word in a sentence. The same word can resolve to different lemmas depending on whether it is acting as a noun, verb, or adjective:
    Example:
      - "Meeting" as a verb (e.g., "We are meeting tomorrow") $\rightarrow$ Lemma: meet
      - "Meeting" as a noun (e.g., "The meeting was long") $\rightarrow$ Lemma: meeting

    **Why its important in NLP**

    Lemmatization is a crucial preprocessing step for various AI and data science applications because it reduces noise and condenses data dimensions
     - **Search Engines**: If you search for "traveling blocks," the engine can use lemmatization to match articles containing "travel block" or "traveled block."
     - **Sentiment Analysis**: It helps aggregate frequencies of words. "Happy," "happier," and "happiest" all point to the same core emotional concept.
     - **Topic Modeling**: It ensures that a model treats "develops," "developing," and "development" as the same underlying semantic concept, improving topic clarity.
  
    **Lemmatization vs Stemming**
    |Feature|Lemmatization|Stemming|
    |-------|-------------|--------|
    |Method|Uses vocabulary, grammar rules, and morphological analysis.|Uses crude, heuristic rules to chop off word endings (suffixes).|
    |Accuracy|High. Always returns a valid dictionary word.|Lower. Often results in non-words or incorrect groupings.|
    |Speed|Slower (requires lookups and linguistic context parsing).|Faster (simple string manipulation).|
    |Example('better')|Returns "good"|Returns "better"|
    |Example('studies')|Returns 'study'|Returns 'studi'|

    **Lab**
     - [Example-1 Lemmatization](https://github.com/varugheseben/edurek-data_science/blob/main/Artificial%20Intelligence/Natural%20Language%20Processing/Examples/Lemmatization/lemmatization_Example-1.ipynb)
     - [Example-2 Lemmatization](https://github.com/varugheseben/edurek-data_science/blob/main/Artificial%20Intelligence/Natural%20Language%20Processing/Examples/Lemmatization/lemmatization_Example_2.ipynb)
