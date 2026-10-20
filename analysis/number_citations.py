#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Convert {{tag}} citations in 04_manuscript.md to sequential [n] numbers,
emit the numbered References section, and write references.bib (keys ref1..refN,
in citation order). One-to-one: in-text [n] == bib entry refN == list item [n]."""
import re, sys, io

MS = "/Users/mark/随笔/_workspace-p3/04_manuscript.md"
BIB = "/Users/mark/随笔/_workspace-p3/references.bib"

# tag -> (display reference string, bibtex entry)
R = {}

def add(tag, disp, bib):
    R[tag] = (disp, bib)

add("epoch24",
    "Epoch AI. Can AI scaling continue through 2030? Epoch AI Publication, 2024. https://epoch.ai/publications/can-ai-scaling-continue-through-2030",
    """@misc{REF,
  author       = {{Epoch AI}},
  title        = {Can {AI} scaling continue through 2030?},
  howpublished = {Epoch AI Publication},
  year         = {2024},
  url          = {https://epoch.ai/publications/can-ai-scaling-continue-through-2030}
}""")
add("aschenbrenner24",
    "L. Aschenbrenner. Situational Awareness: The Decade Ahead. Self-published, 2024. https://situational-awareness.ai/from-gpt-4-to-agi",
    """@misc{REF,
  author       = {Aschenbrenner, Leopold},
  title        = {Situational Awareness: The Decade Ahead},
  howpublished = {Self-published},
  year         = {2024},
  url          = {https://situational-awareness.ai/from-gpt-4-to-agi}
}""")
add("silversutton25",
    "D. Silver and R. S. Sutton. Welcome to the Era of Experience. In G. Konidaris (ed.), Designing an Intelligence. MIT Press, 2025. Preprint, April 2025. https://storage.googleapis.com/deepmind-media/Era-of-Experience%20/The%20Era%20of%20Experience%20Paper.pdf",
    """@incollection{REF,
  author    = {Silver, David and Sutton, Richard S.},
  title     = {Welcome to the Era of Experience},
  booktitle = {Designing an Intelligence},
  editor    = {Konidaris, George},
  publisher = {MIT Press},
  year      = {2025},
  note      = {Preprint, April 2025},
  url       = {https://storage.googleapis.com/deepmind-media/Era-of-Experience%20/The%20Era%20of%20Experience%20Paper.pdf}
}""")
add("shumailov24",
    "I. Shumailov, Z. Shumaylov, Y. Zhao, N. Papernot, R. Anderson, and Y. Gal. AI models collapse when trained on recursively generated data. Nature, 631:742–746, 2024. doi:10.1038/s41586-024-07566-y",
    """@article{REF,
  author  = {Shumailov, Ilia and Shumaylov, Zakhar and Zhao, Yiren and Papernot, Nicolas and Anderson, Rob and Gal, Yarin},
  title   = {{AI} models collapse when trained on recursively generated data},
  journal = {Nature},
  volume  = {631},
  pages   = {742--746},
  year    = {2024},
  doi     = {10.1038/s41586-024-07566-y}
}""")
add("yu-theory",
    "Y. Yu. Fitting the Practice, Not the Works: A Human-Referential Theory of AGI. Zenodo, 2026. doi:10.5281/zenodo.23391808",
    """@misc{REF,
  author = {Yu, Yugui},
  title  = {Fitting the Practice, Not the Works: A Human-Referential Theory of {AGI}},
  year   = {2026},
  doi    = {10.5281/zenodo.23391808}
}""")
add("yu-audit",
    "Y. Yu. Success Provides Direction, Failure Provides Precision: A Structured Audit of Failure Data in LLM Training. Zenodo, 2026. doi:10.5281/zenodo.23355929",
    """@misc{REF,
  author = {Yu, Yugui},
  title  = {Success Provides Direction, Failure Provides Precision: A Structured Audit of Failure Data in {LLM} Training},
  year   = {2026},
  doi    = {10.5281/zenodo.23355929}
}""")
add("sorensen25",
    "T. Sorensen et al. Spectrum Tuning: Post-Training for Distributional Coverage and In-Context Steerability. In Proc. ICLR, 2026. arXiv:2510.06084",
    """@inproceedings{REF,
  author    = {Sorensen, Trevor and others},
  title     = {Spectrum Tuning: Post-Training for Distributional Coverage and In-Context Steerability},
  booktitle = {Proceedings of the International Conference on Learning Representations (ICLR)},
  year      = {2026},
  eprint    = {2510.06084},
  archivePrefix = {arXiv}
}""")
add("datadog26",
    "Datadog. Teaching a 9B model to investigate production alerts. Datadog blog, September 23, 2026. https://www.datadoghq.com/blog/ai/investigate-production-alerts (accessed 2026-10-16)",
    """@misc{REF,
  author       = {{Datadog}},
  title        = {Teaching a 9{B} model to investigate production alerts},
  howpublished = {Datadog blog},
  year         = {2026},
  url          = {https://www.datadoghq.com/blog/ai/investigate-production-alerts},
  note         = {September 23, 2026; accessed 2026-10-16}
}""")
add("longpre-essay24",
    "S. Longpre et al. Data Authenticity, Consent, and Provenance for AI Are All Broken. MIT Generative AI Impact Initiative, 2024. https://mit-genai.pubpub.org/pub/uk7op8zs",
    """@misc{REF,
  author       = {Longpre, Shayne and others},
  title        = {Data Authenticity, Consent, and Provenance for {AI} Are All Broken},
  howpublished = {MIT Generative AI Impact Initiative},
  year         = {2024},
  url          = {https://mit-genai.pubpub.org/pub/uk7op8zs}
}""")
add("longpre24",
    "S. Longpre, R. Mahari, A. Lee, C. Lund, et al. Consent in Crisis: The Rapid Decline of the AI Data Commons. In NeurIPS Datasets and Benchmarks Track, 2024. arXiv:2407.14933",
    """@inproceedings{REF,
  author    = {Longpre, Shayne and Mahari, Robert and Lee, Ariel and Lund, Campbell and others},
  title     = {Consent in Crisis: The Rapid Decline of the {AI} Data Commons},
  booktitle = {NeurIPS Datasets and Benchmarks Track},
  year      = {2024},
  eprint    = {2407.14933},
  archivePrefix = {arXiv}
}""")
add("daliberti26",
    "L. G. d'Aliberti, M. Abdulhai, S. Druchyna, et al. Measuring and Mitigating Solution Mode Collapse in RLVR. arXiv:2610.11064, 2026",
    """@misc{REF,
  author       = {d'Aliberti, Liv G. and Abdulhai, Marwa and Druchyna, Sofiia and others},
  title        = {Measuring and Mitigating Solution Mode Collapse in {RLVR}},
  year         = {2026},
  eprint       = {2610.11064},
  archivePrefix = {arXiv}
}""")
add("liu26",
    "S. Liu et al. The Path to Recursive Self-Improving Agents: Foundation, Framework, and Future Directions. Preprints.org, 2026. Preprint 202608.0051 (not peer reviewed)",
    """@techreport{REF,
  author      = {Liu, Sitong and others},
  title       = {The Path to Recursive Self-Improving Agents: Foundation, Framework, and Future Directions},
  institution = {Preprints.org},
  year        = {2026},
  type        = {Preprint},
  number      = {202608.0051},
  note        = {Not peer reviewed}
}""")
add("zhou25",
    "K. Zhou et al. Should LLMs be WEIRD? Exploring Representativeness Bias and Discrimination in LLMs. arXiv:2508.19269, 2025",
    """@misc{REF,
  author       = {Zhou, Kevin and others},
  title        = {Should {LLMs} be {WEIRD}? Exploring Representativeness Bias and Discrimination in {LLMs}},
  year         = {2025},
  eprint       = {2508.19269},
  archivePrefix = {arXiv}
}""")
add("yang25",
    "Y. Yang, Y. Nan, et al. Measuring Data Diversity for Instruction Tuning: A Systematic Analysis and A Reliable Metric. In Proc. ACL, 2025. arXiv:2502.17184",
    """@inproceedings{REF,
  author    = {Yang, Yuming and Nan, Yang and others},
  title     = {Measuring Data Diversity for Instruction Tuning: A Systematic Analysis and A Reliable Metric},
  booktitle = {Proceedings of the Annual Meeting of the Association for Computational Linguistics (ACL)},
  year      = {2025},
  eprint    = {2502.17184},
  archivePrefix = {arXiv}
}""")
add("phutane25",
    "M. Phutane et al. ABLEIST: Intersectional Disability Bias in LLM-Generated Hiring Scenarios. arXiv:2510.10998, 2025",
    """@misc{REF,
  author       = {Phutane, Mitisha and others},
  title        = {{ABLEIST}: Intersectional Disability Bias in {LLM}-Generated Hiring Scenarios},
  year         = {2025},
  eprint       = {2510.10998},
  archivePrefix = {arXiv}
}""")
add("baek26",
    "D. D. Baek. D-FUSEr: Diverse Failure, Unified Success via Error-Distribution Shaping in LLM Reasoning. In Proc. ICML, PMLR v306, 2026",
    """@inproceedings{REF,
  author    = {Baek, Dongryeol D.},
  title     = {{D-FUSEr}: Diverse Failure, Unified Success via Error-Distribution Shaping in {LLM} Reasoning},
  booktitle = {Proceedings of the International Conference on Machine Learning (ICML)},
  series    = {PMLR},
  volume    = {306},
  year      = {2026}
}""")
add("ec-template",
    "European Commission, AI Office. Template for general-purpose AI model providers to summarise their training content. Official FAQ, 2025 (updated 2026). https://digital-strategy.ec.europa.eu/en/faqs/template-general-purpose-ai-model-providers-summarise-their-training-content (accessed 2026-10-16)",
    """@misc{REF,
  author       = {{European Commission, AI Office}},
  title        = {Template for general-purpose {AI} model providers to summarise their training content},
  howpublished = {Official FAQ},
  year         = {2025},
  url          = {https://digital-strategy.ec.europa.eu/en/faqs/template-general-purpose-ai-model-providers-summarise-their-training-content},
  note         = {Updated 2026; accessed 2026-10-16}
}""")
add("han25",
    "E. Han et al. Reinforcement Learning from User Feedback. arXiv:2505.14946, 2025",
    """@misc{REF,
  author       = {Han, Eric and others},
  title        = {Reinforcement Learning from User Feedback},
  year         = {2025},
  eprint       = {2505.14946},
  archivePrefix = {arXiv}
}""")
add("openai-sycophancy",
    "OpenAI. Sycophancy in GPT-4o: What happened and what we're doing about it. OpenAI, 2025. https://openai.com/index/sycophancy-in-gpt-4o",
    """@misc{REF,
  author       = {{OpenAI}},
  title        = {Sycophancy in {GPT-4o}: What happened and what we're doing about it},
  howpublished = {OpenAI},
  year         = {2025},
  url          = {https://openai.com/index/sycophancy-in-gpt-4o}
}""")
add("deepseek41",
    "A. Xu et al. (DeepSeek). DeepSeek-V4.1-Flash: Pushing the Limits of KV Cache. Technical report, arXiv:2609.19969, 2026",
    """@techreport{REF,
  author      = {Xu, Ang and others},
  title       = {{DeepSeek-V4.1-Flash}: Pushing the Limits of {KV} Cache},
  institution = {DeepSeek},
  year        = {2026},
  eprint      = {2609.19969},
  archivePrefix = {arXiv}
}""")
add("musk26",
    "E. Musk. Posts on X, May 25, 2026 and June 28, 2026. https://x.com/elonmusk/status/2058787384364265734 and https://x.com/elonmusk/status/2071184354756477041 (accessed 2026-10-16)",
    """@misc{REF,
  author       = {Musk, Elon},
  title        = {Posts on {X} regarding {Grok} {V9-Medium} and {Grok} 4.5 training data},
  howpublished = {X},
  year         = {2026},
  url          = {https://x.com/elonmusk/status/2058787384364265734},
  note         = {Second post: https://x.com/elonmusk/status/2071184354756477041; accessed 2026-10-16}
}""")
add("gpt6oct",
    "OpenAI. GPT-6 Sol and GPT-6 Luna: October 2026 update. System card, 2026-10-07. https://deploymentsafety.openai.com/gpt-6-october (accessed 2026-10-16)",
    """@techreport{REF,
  author      = {{OpenAI}},
  title       = {{GPT-6} Sol and {GPT-6} Luna: October 2026 update},
  institution = {OpenAI},
  type        = {System card},
  year        = {2026},
  url         = {https://deploymentsafety.openai.com/gpt-6-october},
  note        = {October 7, 2026; accessed 2026-10-16}
}""")
add("google-vrp",
    "Google. Announcing Google's new AI Vulnerability Reward Program. Bug Hunters blog, 2025. https://bughunters.google.com/blog/announcing-googles-new-ai-vulnerability-reward-program",
    """@misc{REF,
  author       = {{Google}},
  title        = {Announcing {Google}'s new {AI} Vulnerability Reward Program},
  howpublished = {Bug Hunters blog},
  year         = {2025},
  url          = {https://bughunters.google.com/blog/announcing-googles-new-ai-vulnerability-reward-program}
}""")
add("an23",
    "S. An et al. Learning From Mistakes Makes LLM Better Reasoner. arXiv:2310.20689, 2023",
    """@misc{REF,
  author       = {An, Shuang and others},
  title        = {Learning From Mistakes Makes {LLM} Better Reasoner},
  year         = {2023},
  eprint       = {2310.20689},
  archivePrefix = {arXiv}
}""")
add("hao26",
    "Hao et al. Why Multi-Step Tool-Use Reinforcement Learning Collapses and How Supervisory Signals Fix It. arXiv:2606.26027, 2026",
    """@misc{REF,
  author       = {Hao and others},
  title        = {Why Multi-Step Tool-Use Reinforcement Learning Collapses and How Supervisory Signals Fix It},
  year         = {2026},
  eprint       = {2606.26027},
  archivePrefix = {arXiv}
}""")
add("qiao26",
    "Z. Qiao et al. (Xiaomi). MiMo-V2.6: Scaling Reinforcement Learning Towards Self-Improvement. Technical report, arXiv:2610.11959, 2026",
    """@techreport{REF,
  author      = {Qiao, Zheng and others},
  title       = {{MiMo-V2.6}: Scaling Reinforcement Learning Towards Self-Improvement},
  institution = {Xiaomi},
  year        = {2026},
  eprint      = {2610.11959},
  archivePrefix = {arXiv}
}""")
add("zeng26",
    "A. Zeng et al. GLM-5: from Vibe Coding to Agentic Engineering. Technical report, arXiv:2602.15763, 2026",
    """@techreport{REF,
  author      = {Zeng, Aohan and others},
  title       = {{GLM-5}: from Vibe Coding to Agentic Engineering},
  institution = {Z.ai},
  year        = {2026},
  eprint      = {2602.15763},
  archivePrefix = {arXiv}
}""")
add("cao26",
    "R. Cao et al. (Qwen Team). Qwen3-Coder-Next Technical Report. arXiv:2603.00729, 2026",
    """@techreport{REF,
  author      = {Cao, Rui and others},
  title       = {{Qwen3-Coder-Next} Technical Report},
  institution = {Alibaba (Qwen Team)},
  year        = {2026},
  eprint      = {2603.00729},
  archivePrefix = {arXiv}
}""")
add("vals26",
    "Vals.ai. Two-thirds of MiMo v2.6's coding tasks leak the answer. Blog, October 7, 2026. https://www.vals.ai/blogs/mimo-reward-hacking (accessed 2026-10-16)",
    """@misc{REF,
  author       = {{Vals.ai}},
  title        = {Two-thirds of {MiMo} v2.6's coding tasks leak the answer},
  howpublished = {Blog},
  year         = {2026},
  url          = {https://www.vals.ai/blogs/mimo-reward-hacking},
  note         = {October 7, 2026; accessed 2026-10-16}
}""")
add("swebench-issue",
    "SWE-bench maintainers. Issue #465: repository future-state leakage. GitHub, 2025. https://github.com/SWE-bench/SWE-bench/issues/465 (accessed 2026-10-16)",
    """@misc{REF,
  author       = {{SWE-bench maintainers}},
  title        = {Issue \#465: repository future-state leakage},
  howpublished = {GitHub},
  year         = {2025},
  url          = {https://github.com/SWE-bench/SWE-bench/issues/465},
  note         = {Accessed 2026-10-16}
}""")
add("kteam26",
    "K Team (Moonshot AI). Kimi K3: Open Frontier Intelligence. Technical report, arXiv:2607.24653, 2026",
    """@techreport{REF,
  author      = {{K Team (Moonshot AI)}},
  title       = {Kimi {K3}: Open Frontier Intelligence},
  institution = {Moonshot AI},
  year        = {2026},
  eprint      = {2607.24653},
  archivePrefix = {arXiv}
}""")
add("kazdan25",
    "J. Kazdan, R. Schaeffer, et al. Collapse or Thrive? Perils and Promises of Synthetic Data in a Self-Generating World. In Proc. ICML, 2025. arXiv:2410.16713",
    """@inproceedings{REF,
  author    = {Kazdan, Joshua and Schaeffer, Rylan and others},
  title     = {Collapse or Thrive? Perils and Promises of Synthetic Data in a Self-Generating World},
  booktitle = {Proceedings of the International Conference on Machine Learning (ICML)},
  year      = {2025},
  eprint    = {2410.16713},
  archivePrefix = {arXiv}
}""")
add("barzilai25",
    "D. Barzilai and O. Shamir. When Models Don't Collapse: On the Consistency of Iterative MLE. In Proc. NeurIPS, 2025. arXiv:2505.19046",
    """@inproceedings{REF,
  author    = {Barzilai, Daniel and Shamir, Ohad},
  title     = {When Models Don't Collapse: On the Consistency of Iterative {MLE}},
  booktitle = {Advances in Neural Information Processing Systems (NeurIPS)},
  year      = {2025},
  eprint    = {2505.19046},
  archivePrefix = {arXiv}
}""")
add("luo26",
    "X. Luo et al. Learning from Synthetic Data without Model Collapse. arXiv:2607.17043, 2026",
    """@misc{REF,
  author       = {Luo, Xiao and others},
  title        = {Learning from Synthetic Data without Model Collapse},
  year         = {2026},
  eprint       = {2607.17043},
  archivePrefix = {arXiv}
}""")
add("techxplore-collapse",
    "TechXplore. Real-world AI collapse analysis: single real data point may avert collapse in simple models. News report, May 2026. https://techxplore.com/news/2026-05-real-world-ai-collapse-analysis.html (accessed 2026-10-16)",
    """@misc{REF,
  author       = {{TechXplore}},
  title        = {Real-world {AI} collapse analysis: single real data point may avert collapse in simple models},
  howpublished = {News report},
  year         = {2026},
  url          = {https://techxplore.com/news/2026-05-real-world-ai-collapse-analysis.html},
  note         = {May 2026; accessed 2026-10-16}
}""")
add("qin25",
    "Z. Qin, Q. Dong, et al. Scaling Laws of Synthetic Data for Language Models. arXiv:2503.19551, 2025",
    """@misc{REF,
  author       = {Qin, Zeyu and Dong, Qingxiu and others},
  title        = {Scaling Laws of Synthetic Data for Language Models},
  year         = {2025},
  eprint       = {2503.19551},
  archivePrefix = {arXiv}
}""")
add("zhao25",
    "A. Zhao et al. Absolute Zero: Reinforced Self-play Reasoning with Zero Data. In Proc. NeurIPS, 2025. arXiv:2505.03335",
    """@inproceedings{REF,
  author    = {Zhao, Andrew and others},
  title     = {Absolute Zero: Reinforced Self-play Reasoning with Zero Data},
  booktitle = {Advances in Neural Information Processing Systems (NeurIPS)},
  year      = {2025},
  eprint    = {2505.03335},
  archivePrefix = {arXiv}
}""")
add("tang26",
    "X. Tang et al. Ring-Zero: Scaling Zero RL to a Trillion Parameters for Emergent Reasoning. arXiv:2607.12395, 2026",
    """@misc{REF,
  author       = {Tang, Xinyu and others},
  title        = {Ring-Zero: Scaling Zero {RL} to a Trillion Parameters for Emergent Reasoning},
  year         = {2026},
  eprint       = {2607.12395},
  archivePrefix = {arXiv}
}""")
add("kang25",
    "F. Kang et al. Demystifying Synthetic Data in LLM Pre-training: A Systematic Study of Scaling Laws, Benefits, and Pitfalls. In Proc. EMNLP (main), 2025. arXiv:2510.01631",
    """@inproceedings{REF,
  author    = {Kang, Feiyang and others},
  title     = {Demystifying Synthetic Data in {LLM} Pre-training: A Systematic Study of Scaling Laws, Benefits, and Pitfalls},
  booktitle = {Proceedings of the Conference on Empirical Methods in Natural Language Processing (EMNLP), main},
  year      = {2025},
  eprint    = {2510.01631},
  archivePrefix = {arXiv}
}""")
add("fortifai",
    "S. Z. Shabgahi, P. Aghazadeh, A. Mirhoseini, et al. ForTIFAI: Fending off recursive training induced failure for AI model collapse. npj Artificial Intelligence, 2026. doi:10.1038/s44387-026-00127-w",
    """@article{REF,
  author  = {Shabgahi, Soheil Zibakhsh and Aghazadeh, Pedram and Mirhoseini, Azalia and others},
  title   = {{ForTIFAI}: Fending off recursive training induced failure for {AI} model collapse},
  journal = {npj Artificial Intelligence},
  year    = {2026},
  doi     = {10.1038/s44387-026-00127-w}
}""")
add("tongyi25",
    "Tongyi DeepResearch Team (Alibaba). Tongyi DeepResearch Technical Report. arXiv:2510.24701, 2025",
    """@techreport{REF,
  author      = {{Tongyi DeepResearch Team (Alibaba)}},
  title       = {Tongyi {DeepResearch} Technical Report},
  institution = {Alibaba},
  year        = {2025},
  eprint      = {2510.24701},
  archivePrefix = {arXiv}
}""")
add("openai-textgrain",
    "OpenAI. Our approach to EU text provenance rules. OpenAI, October 5, 2026. https://openai.com/index/eu-text-provenance",
    """@misc{REF,
  author       = {{OpenAI}},
  title        = {Our approach to {EU} text provenance rules},
  howpublished = {OpenAI},
  year         = {2026},
  url          = {https://openai.com/index/eu-text-provenance},
  note         = {October 5, 2026}
}""")
add("vcu-watermark",
    "VCU College of Engineering. Watermarking AI-generated text for transparency, provenance and safety. September 17, 2026. https://blogs.vcu.edu/engineering/2026/09/17/watermarking-ai-generated-text-for-transparency-provenance-and-safety (accessed 2026-10-16)",
    """@misc{REF,
  author       = {{VCU College of Engineering}},
  title        = {Watermarking {AI}-generated text for transparency, provenance and safety},
  howpublished = {Engineering blog},
  year         = {2026},
  url          = {https://blogs.vcu.edu/engineering/2026/09/17/watermarking-ai-generated-text-for-transparency-provenance-and-safety},
  note         = {September 17, 2026; accessed 2026-10-16}
}""")
add("techxplore-watermark",
    "TechXplore. AI image watermarks survive model training. News report, October 2026. https://techxplore.com/news/2026-10-ai-image-watermarks-survive-durability.html (accessed 2026-10-16)",
    """@misc{REF,
  author       = {{TechXplore}},
  title        = {{AI} image watermarks survive model training},
  howpublished = {News report},
  year         = {2026},
  url          = {https://techxplore.com/news/2026-10-ai-image-watermarks-survive-durability.html},
  note         = {October 2026; accessed 2026-10-16}
}""")
add("parmar24",
    "J. Parmar, A. Suri, N. Sohoni, et al. Reuse, Don't Retrain: A Recipe for Continued Pretraining of Large Language Models. arXiv:2407.07263, 2024",
    """@misc{REF,
  author       = {Parmar, Jirayu and Suri, Anshuman and Sohoni, Nimit and others},
  title        = {Reuse, Don't Retrain: A Recipe for Continued Pretraining of Large Language Models},
  year         = {2024},
  eprint       = {2407.07263},
  archivePrefix = {arXiv}
}""")
add("ibrahim24",
    "A. Ibrahim et al. Simple and Scalable Strategies to Continually Pre-train Large Language Models. arXiv:2403.08763, 2024",
    """@misc{REF,
  author       = {Ibrahim, Adam and others},
  title        = {Simple and Scalable Strategies to Continually Pre-train Large Language Models},
  year         = {2024},
  eprint       = {2403.08763},
  archivePrefix = {arXiv}
}""")
add("oncel26",
    "F. Öncel, S. H. Ali, et al. Time-Incremental Continued Pretraining of LLMs: Knowledge Updates Without Catastrophic Forgetting. arXiv:2609.23916, 2026",
    """@misc{REF,
  author       = {Öncel, Fırat and Ali, Salman Hussain and others},
  title        = {Time-Incremental Continued Pretraining of {LLMs}: Knowledge Updates Without Catastrophic Forgetting},
  year         = {2026},
  eprint       = {2609.23916},
  archivePrefix = {arXiv}
}""")
add("arnal26",
    "C. Arnal et al. Efficient RL Training for LLMs with Experience Replay. arXiv:2604.08706, 2026",
    """@misc{REF,
  author       = {Arnal, Corentin and others},
  title        = {Efficient {RL} Training for {LLMs} with Experience Replay},
  year         = {2026},
  eprint       = {2604.08706},
  archivePrefix = {arXiv}
}""")
add("fu25",
    "W. Fu et al. AReaL: A Large-Scale Asynchronous Reinforcement Learning System for Language Reasoning. In Proc. NeurIPS, 2025. arXiv:2505.24298",
    """@inproceedings{REF,
  author    = {Fu, Wei and others},
  title     = {{AReaL}: A Large-Scale Asynchronous Reinforcement Learning System for Language Reasoning},
  booktitle = {Advances in Neural Information Processing Systems (NeurIPS)},
  year      = {2025},
  eprint    = {2505.24298},
  archivePrefix = {arXiv}
}""")
add("mem026",
    "Mem0. State of AI Agent Memory 2026. Industry report, 2026. https://mem0.ai/blog/state-of-ai-agent-memory-2026 (accessed 2026-10-16)",
    """@techreport{REF,
  author      = {{Mem0}},
  title       = {State of {AI} Agent Memory 2026},
  institution = {Mem0},
  type        = {Industry report},
  year        = {2026},
  url         = {https://mem0.ai/blog/state-of-ai-agent-memory-2026},
  note        = {Accessed 2026-10-16}
}""")
add("a16z26",
    "Andreessen Horowitz. Why We Need Continual Learning. April 2026. https://a16z.com/why-we-need-continual-learning (accessed 2026-10-16)",
    """@misc{REF,
  author       = {{Andreessen Horowitz}},
  title        = {Why We Need Continual Learning},
  howpublished = {a16z},
  year         = {2026},
  url          = {https://a16z.com/why-we-need-continual-learning},
  note         = {April 2026; accessed 2026-10-16}
}""")
add("park24",
    "C. Park, P. Rohrbach, and Y. Choi. RLHF from Heterogeneous Feedback via Personalization. arXiv:2405.00254, 2024",
    """@misc{REF,
  author       = {Park, Chansoo and Rohrbach, Percy and Choi, Yejin},
  title        = {{RLHF} from Heterogeneous Feedback via Personalization},
  year         = {2024},
  eprint       = {2405.00254},
  archivePrefix = {arXiv}
}""")
add("huang24",
    "S. Huang et al. Collective Constitutional AI: Aligning a Language Model with Public Input. In Proc. ACM FAccT, 2024. arXiv:2406.07814. doi:10.1145/3630106.3658979",
    """@inproceedings{REF,
  author    = {Huang, Shauna and others},
  title     = {Collective Constitutional {AI}: Aligning a Language Model with Public Input},
  booktitle = {Proceedings of the ACM Conference on Fairness, Accountability, and Transparency (FAccT)},
  year      = {2024},
  doi       = {10.1145/3630106.3658979},
  eprint    = {2406.07814},
  archivePrefix = {arXiv}
}""")
add("anthropic-constitution",
    "Anthropic. Claude's Constitution. 2026. https://www.anthropic.com/constitution (accessed 2026-10-16)",
    """@misc{REF,
  author       = {{Anthropic}},
  title        = {Claude's Constitution},
  howpublished = {Anthropic},
  year         = {2026},
  url          = {https://www.anthropic.com/constitution},
  note         = {Accessed 2026-10-16}
}""")
add("openai-personality",
    "OpenAI. Customizing your ChatGPT personality. Help Center, 2026. https://help.openai.com/en/articles/11899719 (accessed 2026-10-16)",
    """@misc{REF,
  author       = {{OpenAI}},
  title        = {Customizing your {ChatGPT} personality},
  howpublished = {Help Center},
  year         = {2026},
  url          = {https://help.openai.com/en/articles/11899719},
  note         = {Accessed 2026-10-16}
}""")
add("qi26",
    "T. Qi et al. Auditing unauthorized training data from AI generated content using information isotopes. Nature Communications, 17:3007, 2026. doi:10.1038/s41467-026-68862-x",
    """@article{REF,
  author  = {Qi, Tao and others},
  title   = {Auditing unauthorized training data from {AI} generated content using information isotopes},
  journal = {Nature Communications},
  volume  = {17},
  pages   = {3007},
  year    = {2026},
  doi     = {10.1038/s41467-026-68862-x}
}""")
add("openai-misalignment",
    "OpenAI. Our framework for reporting model misalignment. September 16, 2026. https://openai.com/index/model-misalignment-reporting-framework; portal: https://alignment.openai.com/misalignment-reports (accessed 2026-10-16)",
    """@misc{REF,
  author       = {{OpenAI}},
  title        = {Our framework for reporting model misalignment},
  howpublished = {OpenAI},
  year         = {2026},
  url          = {https://openai.com/index/model-misalignment-reporting-framework},
  note         = {September 16, 2026; portal at alignment.openai.com/misalignment-reports accessed 2026-10-16}
}""")
add("reuters-astra",
    "Reuters. OpenAI shelves new AI model after internal safety tests. September 28, 2026. https://www.reuters.com/business/openai-shelves-new-ai-model-after-internal-safety-tests-wsj-reports-2026-09-28",
    """@misc{REF,
  author       = {{Reuters}},
  title        = {OpenAI shelves new {AI} model after internal safety tests},
  howpublished = {Reuters},
  year         = {2026},
  url          = {https://www.reuters.com/business/openai-shelves-new-ai-model-after-internal-safety-tests-wsj-reports-2026-09-28},
  note         = {September 28, 2026}
}""")
add("chowdhury26",
    "R. Chowdhury. terms.txt: A Consent and Compensation Protocol for Agentic Web Access. arXiv:2609.11152, 2026",
    """@misc{REF,
  author       = {Chowdhury, Rajarshi},
  title        = {terms.txt: A Consent and Compensation Protocol for Agentic Web Access},
  year         = {2026},
  eprint       = {2609.11152},
  archivePrefix = {arXiv}
}""")
add("gdpr",
    "European Union. Regulation (EU) 2016/679 (General Data Protection Regulation). Official Journal of the European Union, L 119, 2016",
    """@misc{REF,
  author       = {{European Union}},
  title        = {Regulation ({EU}) 2016/679 (General Data Protection Regulation)},
  howpublished = {Official Journal of the European Union, L 119},
  year         = {2016}
}""")
add("edpb",
    "European Data Protection Board. AI: Effective Implementation of Data Subjects' Rights. EDPB document, 2025. https://www.edpb.europa.eu/system/files/2025-01/d2-ai-effective-implementation-of-data-subjects-rights_en.pdf (accessed 2026-10-16)",
    """@techreport{REF,
  author      = {{European Data Protection Board}},
  title       = {{AI}: Effective Implementation of Data Subjects' Rights},
  institution = {European Data Protection Board},
  year        = {2025},
  url         = {https://www.edpb.europa.eu/system/files/2025-01/d2-ai-effective-implementation-of-data-subjects-rights_en.pdf},
  note        = {Accessed 2026-10-16}
}""")
add("anthropic-privacy",
    "Anthropic. Is my data used for model training? Privacy FAQ, 2026. https://privacy.claude.com/en/articles/10023580-is-my-data-used-for-model-training (accessed 2026-10-16)",
    """@misc{REF,
  author       = {{Anthropic}},
  title        = {Is my data used for model training?},
  howpublished = {Privacy FAQ},
  year         = {2026},
  url          = {https://privacy.claude.com/en/articles/10023580-is-my-data-used-for-model-training},
  note         = {Accessed 2026-10-16}
}""")
add("reuters-reddit",
    "Reuters. Reddit has AI content licensing deal with Google, sources say. February 22, 2024. https://www.reuters.com/technology/reddit-ai-content-licensing-deal-with-google-sources-say-2024-02-22",
    """@misc{REF,
  author       = {{Reuters}},
  title        = {Reddit has {AI} content licensing deal with Google, sources say},
  howpublished = {Reuters},
  year         = {2024},
  url          = {https://www.reuters.com/technology/reddit-ai-content-licensing-deal-with-google-sources-say-2024-02-22},
  note         = {February 22, 2024}
}""")
add("latamgpt",
    "Latam-GPT Initiative. Latam-GPT: a regional public-good language model for Latin America. 2026. https://www.latamgpt.org/en (accessed 2026-10-16)",
    """@misc{REF,
  author       = {{Latam-GPT Initiative}},
  title        = {Latam-GPT: a regional public-good language model for {Latin America}},
  howpublished = {Official site},
  year         = {2026},
  url          = {https://www.latamgpt.org/en},
  note         = {Accessed 2026-10-16}
}""")
add("byrnes25",
    "S. Byrnes. 'The Era of Experience' has an unsolved technical alignment problem. Alignment Forum / LessWrong, April 24, 2025. https://www.alignmentforum.org/posts/TCGgiJAinGgcMEByt/the-era-of-experience-has-an-unsolved-technical-alignment",
    """@misc{REF,
  author       = {Byrnes, Steven},
  title        = {'The Era of Experience' has an unsolved technical alignment problem},
  howpublished = {Alignment Forum / LessWrong},
  year         = {2025},
  url          = {https://www.alignmentforum.org/posts/TCGgiJAinGgcMEByt/the-era-of-experience-has-an-unsolved-technical-alignment},
  note         = {April 24, 2025}
}""")
add("vallor24",
    "S. Vallor. The AI Mirror: How to Reclaim Our Humanity in an Age of Machine Thinking. Oxford University Press, 2024",
    """@book{REF,
  author    = {Vallor, Shannon},
  title     = {The AI Mirror: How to Reclaim Our Humanity in an Age of Machine Thinking},
  publisher = {Oxford University Press},
  year      = {2024}
}""")
add("paniego26",
    "S. Paniego. How frontier models train on outcomes in 2026. Hugging Face blog, August 2026. https://huggingface.co/blog/sergiopaniego/agentic-rl-2026 (accessed 2026-10-16)",
    """@misc{REF,
  author       = {Paniego, Sergio},
  title        = {How frontier models train on outcomes in 2026},
  howpublished = {Hugging Face blog},
  year         = {2026},
  url          = {https://huggingface.co/blog/sergiopaniego/agentic-rl-2026},
  note         = {August 2026; accessed 2026-10-16}
}""")
add("qwen38",
    "Qwen Team. Qwen3.8-Max. Official blog, August 3, 2026. https://qwen.ai/blog?id=qwen3.8 (accessed 2026-10-16)",
    """@misc{REF,
  author       = {{Qwen Team}},
  title        = {Qwen3.8-Max},
  howpublished = {Official blog},
  year         = {2026},
  url          = {https://qwen.ai/blog?id=qwen3.8},
  note         = {August 3, 2026; accessed 2026-10-16}
}""")

def main():
    text = io.open(MS, encoding="utf-8").read()

    # 1) merge adjacent tags: {{a}}{{b}} ... -> [na, nb, ...]
    run_re = re.compile(r'(?:\{\{[a-z0-9\-]+\}\})+')
    order = []          # tags in first-appearance order
    def run_sub(m):
        tags = re.findall(r'\{\{([a-z0-9\-]+)\}\}', m.group(0))
        nums = []
        for t in tags:
            if t not in R:
                print("UNKNOWN TAG:", t); sys.exit(1)
            if t not in order:
                order.append(t)
            nums.append(str(order.index(t) + 1))
        return "[" + ", ".join(nums) + "]"
    new_text = run_re.sub(run_sub, text)

    if "{{" in new_text:
        print("Leftover tags!"); sys.exit(1)

    # 2) build numbered reference list and bib
    ref_list = []
    bib_entries = []
    for i, t in enumerate(order, 1):
        disp, bib = R[t]
        ref_list.append("[%d] %s" % (i, disp))
        bib_entries.append(bib.replace("REF", "ref%d" % i))
        print("%3d  %s" % (i, t))

    new_text = new_text.replace("<!--REFS-->", "\n".join(ref_list) + "\n")
    io.open(MS, "w", encoding="utf-8").write(new_text)

    header = ("% Numbered in order of first citation; key refN corresponds to in-text [N].\n"
              "% Generated 2026-10-16 for: Fitting the Flow (04_manuscript.md).\n\n")
    io.open(BIB, "w", encoding="utf-8").write(header + "\n\n".join(bib_entries) + "\n")

    words = len(re.findall(r"\b[\w'-]+\b", re.sub(r'!\[.*?\]\(.*?\)', '', new_text)))
    print("\nTotal unique references:", len(order))
    print("Approx word count (whole file):", words)

if __name__ == "__main__":
    main()
