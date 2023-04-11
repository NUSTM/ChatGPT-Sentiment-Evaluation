# Is ChatGPT a Good Sentiment Analyzer?




## Introduction

Recently, ChatGPT has drawn great attention from both the research community and the public. However, despite its huge success, we still know little about the capability boundaries, i.e., where it does well and fails. we are particularly curious how ChatGPT performs on the sentiment analysis tasks, i.e., **Can it really understand the *opinions*, *sentiments*, and *emotions* contained in the text?**

To answer this question, we conduct a preliminary evaluation on **5** representative sentiment analysis tasks and **18** benchmark datasets, which involves four different settings including **standard evaluation**, **polarity shift evaluation**, **open-domain evaluation**, and **sentiment inference evaluation**. We compare ChatGPT with fine-tuned BERT-based models and corresponding SOTA models on each task for reference.


Through rigorous evaluation, our findings are as follows:

1. **ChatGPT exhibits impressive zero-shot performance in sentiment classification tasks** and can rival fine-tuned BERT, although it falls slightly behind the domain-specific fullysupervised SOTA models.
2. **ChatGPT appears to be less accurate on sentiment information extraction tasks such as E2E-ABSA.** Upon observation, we find that ChatGPT is often able to generate reasonable answers, even though they may not strictly match the textual expression. From this point of view, the exact matching evaluation in information extraction is not very fair for ChatGPT. **In our human evaluation, ChatGPT can still perform well in these tasks.**
3. **Few-shot prompting (i.e., equipping with a few demonstration examples in the input) can significantly improve performance across various tasks, datasets, and domains**, even surpassing fine-tuned BERT in some cases but still being inferior to SOTA models.
4. When coping with the **polarity shift phenomenon (e.g., negation and speculation)**, a challenging problem in sentiment analysis, **ChatGPT can make more accurate predictions than fine-tuned BERT**.
5. Compared to the conventional practice - training domain-specific models, which typically perform poorly when generalized to unseen domains, **ChatGPT demonstrates its powerful open-domain sentiment analysis ability in general**, yet it is still worth noting that its performance is quite limited in a few specific domains.
6. **ChatGPT exhibits impressive sentiment inference ability**, achieving comparable performance on the emotion cause extraction task or emotion-cause pair extraction task, in comparison with the fully-supervised SOTA models we set up.

In summary, compared to training a specialized sentiment analysis system for each domain or dataset, **ChatGPT can already serve as a universal and well-behaved sentiment analyzer**.

## Evaluation
### Standard Evaluation

<!-- <div align=center>![image]() -->
  
<div align=center><img src="[https://img-blog.csdnimg.cn/20200725104000982.png](https://user-images.githubusercontent.com/46218454/231040827-e6641bb9-af0a-459c-83f7-38544e298a23.png)" width="100%"></div>
