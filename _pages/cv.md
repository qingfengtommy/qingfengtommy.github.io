---
layout: archive
title: "CV"
permalink: /cv/
author_profile: true
redirect_from:
  - /resume
---

{% include base_path %}

Education
======
* B.S, UW-Madison in Computer Sciences, 2023-onging

Work experience
======
* TEG Platform, Tencent (2023.09-2024.01)
  * Conducted research on fine-tuning LLMs using LoRA for SQL code generation.
  * Combined datasets and developed a comprehensive pipeline for fine-tuning, pruning, and evaluating LLMs on SQL tasks.
  * Analyzed the effectiveness of the fine-tuning method (LoRA) and both unstructured and structured pruning methods (Wanda, SparseGPT) for generating SQL code.
  * Explored the impact of model size and pruning percentage on the performance of the model in SQL code generation tasks.

  
Skills
======
* Used to play violin lol...
* Coding: Java, Python, Javascript, SQL .... 

Publications
======
  <ul>{% for post in site.publications reversed %}
    {% include archive-single-cv.html %}
  {% endfor %}</ul>
  
<Talks>
  <ul>{% for post in site.talks reversed %}
    {% include archive-single-talk-cv.html  %}
  {% endfor %}</ul>
  
<Teaching>
  <ul>{% for post in site.teaching reversed %}
    {% include archive-single-cv.html %}
  {% endfor %}</ul>
  
<Service and leadership>