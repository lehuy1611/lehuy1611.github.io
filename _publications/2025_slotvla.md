---
title: "SlotVLA: Towards Relation-Centric Robotic Manipulation"
image: "/images/publications/slotvla_2025.jpg"
arxiv: 
github: 
authors: 
    - nhatchung
    - huyle
    - taiseih
    - khoavo
    - tungkieu
    - anhnguyen
    - nganle
collection: publications
permalink: /publication/uno
type: "under review"
publication: "Under Review"
year: "2025"
date: 2025-01-05
---
<!-- <button class="btn btn-round btn-sm btn-ghost-blue" onclick="location.href='https://arxiv.org/abs/2312.09507'">arXiv</button> -->

## Abstract
Humans can naturally conceptualize their surroundings in terms of a small number of objects and their spatial relationships, enabling them to perform manipulation tasks effectively. 
However, typical visuomotor control models in robotics rely on dense embeddings that entangle object positions, affordances, and backgrounds, making interpretability and efficiency a concern.
In line with the challenge, we aim to mimic human reasoning by investigating a novel problem of how to construct a compact, yet highly semantic set of visual representations for multitask robotic manipulation.
The core challenge lies in understanding object entities that are relevant to the manipulation tasks, while obtaining the contextual features that are necessary for action decoding.
To address this, we propose \model, a framework that leverages slot attention not only to extract objects from the scene, but also to encode their interactions with the robotic gripper as task-relevant features, forming relation-centric representations for action decoding. \model comprises of three main components: (i) Slot-based visual tokenizer to transform the visual input into relation-centric visual tokens; 
(ii) Task-centric multimodal decoder to determine task-centric tokens; and (iii) LLM action decoder
to convert the multimodal representations into precise control parameters for robot execution.
Our findings highlight the importance of relational understanding in object-centric robotic systems.
In particular, our experiments, conducted under a low-token vision setting, demonstrate that these relation-centric slot representations efficiently support different manipulation tasks while using as few as four slots. We validate our approach in different environments, offering a novel pathway toward efficient and interpretable visuomotor modeling in robotics.
