# Abstract
Nowadays, more and more fields can be described as graph data. A pivotal idea in network science and marketing research is that a small group of nodes, called influencers, have the largest impact on social contagion and epidemic processes in networks. For viral marketing, with given budget, we hope to maximize the outreach by word-of-mouth effect and to realize it, we need to target initial ’seed’ nodes with biggest impact. In our project, we chose Twitch gamersdataset and the task is to spread a product news with certain budget - the number of initial seed nodes, K. Seed set selection for Information Maximization Problem (IMP) is an NP-hard problem. We implemented centrality-based methods including K-core number, PageRank, ViralRank, and etc.,vanilla greedy algorithm and its variant, CELF algorithm.
Meanwhile, we tried degree discount heuristics method. Evaluated by the impact (the simulated number of infected nodes) and time complexity(how many iterations it takes for converge), CELF significantly outperformed all state-of-art centrality measures in simulated impact with slightly more time complexity. 

# Dataset
https://snap.stanford.edu/data/twitch_gamers.html

# Conclusion
In terms of diffusion models, we found that Independent Cascade model works best in terms of time complexity. For centrality measure, actually there still lacks agreement on which metric best quantifies the spreading ability of the nodes. Most proposed centrality measures are based on analytical arguments which are valid for certain types of networks and spreading parameters. So the choice of centrality measures depends on which type of networks we will bedealing with.
To summarize, our highlights of work are mainly twofold.
First is on the centrality measurement. Apart from all state-of-art centrality measures, we implemented ViralRank-the first one that builds a centrality measure on analytic estimates of random-walk hitting times[6]. Second is on the selection method. The Influence Maxi-mization problem is a NP-hard problem. The most prevalent method is Greedy algorithm, which is synonym to computation burden, and to tackle this, we implemented CELF(’Cost-Effective Lazy Forward’), an optimized version of Greedy algorithm. The CELF optimization uses the submodularity property of the influence maximization objective to greatlyreduce the number of evaluations on the influence spread of
vertices [ 2 ].Our experiment results demonstrate that CELF optimization has almost the same influence spread as theoriginal greedy algorithm but could achieve 66.67% speedup, which is a very impressive result.
One step further, instead of using Greedy algorithm, we experimented with degree discount heuristics. Still there are several points that we can work further on.

In our project, we didn’t take node features into consideration but rather focus only on their connectivity, however the features like recency, seniority are informative indicators for gauging a gamer’s activity, which should be decisive if we should shortlist a node. We can further develop our project by involving them and adopt UAC Rank algorithm.
Meanwhile, there are plenty of variants of greedy algorithm in this particular topic, we should be able to touch on few more others.
Furthermore, we only look at identifying individual influencers, while in real life, a collection of nodes with lowercentrality score can propagate more collectively. Collective influence maximization can be another topic we dig deeper into.

