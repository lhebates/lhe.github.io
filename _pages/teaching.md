---
layout: archive
title: "Teaching"
permalink: /teaching/
author_profile: true
---


## Courses

* ECON 103 - Principles of Macroeconomics
* ECON 260 - Intermediate Microeconomics [(Github repo)](https://github.com/lhebates/BatesEcon260)
* ECON 306 - Games and Strategies in Firms and Markets [(Github repo)](https://github.com/lhebates/BatesEcon306)
* ECON 339 - Industrial Organization [(Github repo)](https://github.com/lhebates/BatesEcon339)
* ECON 456 - Senior Thesis Seminar


<!-- To include blog style pages, add .md files to folder: _teaching  -->
{% include base_path %}

{% for post in site.teaching reversed %}
  {% include archive-single.html %}
{% endfor %}
