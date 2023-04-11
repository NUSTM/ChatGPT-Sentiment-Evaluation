# Is ChatGPT a Good Sentiment Analyzer?




## Introduction

Recently, ChatGPT has drawn great attention from both the research community and the public. However, despite its huge success, we still know little about the capability boundaries, i.e., where it does well and fails. we are particularly curious how ChatGPT performs on the sentiment analysis tasks, i.e., **Can it really understand the *opinions*, *sentiments*, and *emotions* contained in the text?**

To answer this question, we conduct a preliminary evaluation on **5** representative sentiment analysis tasks and **18** benchmark datasets, which involves four different settings including **standard evaluation**, **polarity shift evaluation**, **open-domain evaluation**, and **sentiment inference evaluation**. We compare ChatGPT with fine-tuned BERT-based models and corresponding SOTA models on each task for reference.

## Standard Evaluation

*100 instances per dataset per task*

**Sentence-level Sentiment Classification**: SST-2

**Aspect-Based Sentiment Classification**: 14-Lap, 14-Res

**E2E ABSA**: 14-Lap, 14-Res

## Polarity Shifting Evaluation

*100 instances per dataset per task*

**Sentence-level Sentiment Classification**: TODO

**ABSC**: [14-Res-Spec, 14Lap-Spec, 14-Res-Neg, 14Lap-Neg](https://github.com/jerbarnes/multitask_negation_for_targeted_sentiment)

## Open Domain Evalation

*ABSC: 50 instances per dataset*

*E2E-ABSA: 30 instances per dataset*

**ABSC** & **E2E-ABSA**: 14-Res, 14-Lap, Twitter14, Book-ACOS, Clothing-ACOS, Hotel-ACOS, [Financial-News-Headline](https://www.kaggle.com/datasets/ankurzing/aspect-based-sentiment-analysis-for-financial-news), Service, Device, [METS-CoV](https://github.com/YLab-Open/METS-CoV)

## Emotion Cognition Evalution

*100 instances per dataset*

**ECE** & **ECPE**: [Ding et al. 2021](https://github.com/NUSTM/ECPE)
