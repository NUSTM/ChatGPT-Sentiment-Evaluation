# ChatGPT-Evaluation


## ABSA

#### Simple Prompts

    *Given a sentence or text, extract the aspect term(s) and determine their corresponding sentiment polarity. Text: {sentence}*

    Identify the aspect term(s) and sentiment polarity in a product review or feedback. Review: {sentence}

    Analyze the aspect term(s) and sentiment polarity in a social media post or tweet related to a topic or subject. Post: {sentence}
    
#### Complex Instructions (ICL)

##### 14Res

**3-shot**

`I want you to act as an annotator for the Aspect-Based Sentiment Analysis task. I will provide you with a customer review, and you will understand it, extract the aspect terms and predict the corresponding sentiment polarity in this review. Make sure that the aspect terms are present in the review. I want you to only predict the results without giving extra text or explanations. Here are some examples: Review: But the staff was so horrible to us. Label: [('staff', 'negative')] Review: Best of all is the warm vibe , the owner is super friendly and service is fast . Label: [['vibe', 'positive'], ['owner', 'positive'], ['service', 'positive']] Review: Nevertheless the food itself is pretty good . Label: [('food', 'positive')] My first review is '{sent}'`

**5-shot**

`I want you to act as an annotator for the Aspect-Based Sentiment Analysis task. I will provide you with a customer review, and you will understand it, extract the aspect terms and predict the corresponding sentiment polarity in this review. Make sure that the aspect terms are present in the review. I want you to only predict the results without giving extra text or explanations. Here are some examples: Review: But the staff was so horrible to us. Label: [('staff', 'negative')] Review: Best of all is the warm vibe , the owner is super friendly and service is fast . Label: [['vibe', 'positive'], ['owner', 'positive'], ['service', 'positive']] Review: Nevertheless the food itself is pretty good . Label: [('food', 'positive')] Review: Faan 's got a great concept but a little rough on the delivery .Label: [['delivery', 'negative']] Review: The fried rice is amazing here . Label: [['fried rice', 'positive']] My first review is '{sent}'`
    
## SST

#### Simple Prompts

    Can you analyze the sentiment of this statement and classify it as positive or negative? Statement: {sentence}
    
    Using sentiment analysis, determine whether the overall tone of this text is positive or negative. Text: {sentence}
    
    *Given this text, what is the sentiment conveyed? Is it positive or negative? Text: {sentence}*
