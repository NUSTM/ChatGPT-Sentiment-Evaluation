# Is ChatGPT a Good Sentiment Analyzer?


**Is ChatGPT a Good Sentiment Analyzer? A Preliminary Study** [[arXiv:2304.04339]](https://arxiv.org/pdf/2304.04339.pdf)

In this repo, we release the test sets we used for evaluation in our paper.


## Introduction (TL;DR)

Recently, ChatGPT has drawn great attention from both the research community and the public. However, despite its huge success, we still know little about the capability boundaries, i.e., where it does well and fails. We are particularly curious how ChatGPT performs on the sentiment analysis tasks, i.e., **Can it really understand the *opinions*, *sentiments*, and *emotions* contained in the text?**

To answer this question, we conduct a preliminary evaluation on **5** representative sentiment analysis tasks and **18** benchmark datasets, which involves four different settings including **standard evaluation**, **polarity shift evaluation**, **open-domain evaluation**, and **sentiment inference evaluation**. We compare ChatGPT with fine-tuned BERT-based models and corresponding SOTA models on each task for reference.


Through rigorous evaluation, our findings are as follows:

1. **ChatGPT exhibits impressive zero-shot performance in sentiment classification tasks** and can rival fine-tuned BERT, although it falls slightly behind the domain-specific fullysupervised SOTA models.
2. **ChatGPT appears to be less accurate on sentiment information extraction tasks such as E2E-ABSA.** Upon observation, we find that ChatGPT is often able to generate reasonable answers, even though they may not strictly match the textual expression. From this point of view, the exact matching evaluation in information extraction is not very fair for ChatGPT. **In our human evaluation, ChatGPT can still perform well in these tasks.**
3. **Few-shot prompting (i.e., equipping with a few demonstration examples in the input) can significantly improve performance across various tasks, datasets, and domains**, even surpassing fine-tuned BERT in some cases but still being inferior to SOTA models.
4. When coping with the **polarity shift phenomenon (e.g., negation and speculation)**, a challenging problem in sentiment analysis, **ChatGPT can make more accurate predictions than fine-tuned BERT**.
5. Compared to the conventional practice - training domain-specific models, which typically perform poorly when generalized to unseen domains, **ChatGPT demonstrates its powerful open-domain sentiment analysis ability in general**, yet it is still worth noting that its performance is quite limited in a few specific domains.
6. **ChatGPT exhibits impressive sentiment inference ability**, achieving comparable performance on the emotion cause extraction task or emotion-cause pair extraction task, in comparison with the fully-supervised SOTA models we set up.

In summary, compared to training a specialized sentiment analysis system for each domain or dataset, **ChatGPT can already serve as a universal and well-behaved sentiment analyzer**.


## Citation

If you find this work helpful, please cite our paper as follows:

```
@article{wang2023chatgpt-sentiment,
  title={Is ChatGPT a Good Sentiment Analyzer? A Preliminary Study},
  author={Zengzhi Wang and Qiming Xie and Zixiang Ding and Yi Feng and Rui Xia},
  journal={arXiv preprint},
  year={2023}
}
```

If you have any questions related to this work, you can open an issue with details or feel free to email Zengzhi(`zzwang@njust.edu.cn`), Qiming(`qmxie@njust.edu.cn`).

## Evaluation
### Standard Evaluation

#### Zero-shot Results

<div align=center><img src="https://user-images.githubusercontent.com/46218454/231040827-e6641bb9-af0a-459c-83f7-38544e298a23.png" width="80%"></div>

Human Evaluation (still in zero-shot)

<div align=center><img src="https://user-images.githubusercontent.com/46218454/231041803-e3b24e97-b25d-41e8-8149-7c8cfab370a6.png" width="40%"></div>




#### Few-shot Prompting

<div align=center><img src="https://user-images.githubusercontent.com/46218454/231041595-ad6b95e7-fdb0-47a8-bf9d-d439dd2988d5.png" width="80%"></div>


### Polarity Shift Evaluation


<div align=center><img src="https://user-images.githubusercontent.com/46218454/231042068-4ceda66a-af79-45d2-ba2d-b3a9ffb7c832.png" width="40%"></div>


### Open-Domain Evaluation


<div align=center><img src="https://user-images.githubusercontent.com/46218454/231042280-300e61cf-e88d-4ea8-b113-adab121891c5.png" width="80%"></div>




<div align=center><img src="https://user-images.githubusercontent.com/46218454/231042325-b029279d-e1d8-4421-9abc-f6f21856cbe9.png" width="80%"></div>



###  Sentiment Inference Evaluation

We choose the ECE and ECPE tasks as the testbed.

<div align=center><img src="https://user-images.githubusercontent.com/46218454/231042755-b8340dcb-9dc6-45f0-81fd-77dbe82f8e15.png" width="40%"></div>


## Case Study

### Standard Evaluation

<div align=center><img src="https://user-images.githubusercontent.com/46218454/231044048-88222746-f2bd-453a-a388-b5ae1140721f.png" width="70%"></div>

### Polarity Shift Evaluation

<div align=center><img src="https://user-images.githubusercontent.com/46218454/231044246-78c7c06c-03fd-4209-9274-2143ca053eee.png" width="70%"></div>


### Open-Domain Evaluation

<div align=center><img src="https://user-images.githubusercontent.com/46218454/231044402-a30959ed-5518-40ad-aca1-81cf31721cd6.png" width="70%"></div>


### Sentiment Inference Evaluation

#### Emotion Cause Extraction (ECE)


<div align=center><img src="https://user-images.githubusercontent.com/46218454/231044708-e23c9391-0fc6-4ade-a454-a434fd2d1fe7.png" width="70%"></div>

#### Emotion-Cause Pair Extraction (ECPE)



<div align=center><img src="https://user-images.githubusercontent.com/46218454/231045221-77f68a48-670b-45e1-b32d-272ec9b18f87.png" width="70%"></div>


> Note that the right part is the English version translation of the left part for both ECE and ECPE.


