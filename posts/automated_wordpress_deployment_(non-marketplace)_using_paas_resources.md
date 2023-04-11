# Automated WordPress deployment (non-marketplace) using PaaS resources

- Author: [CloudDevDanUK](https://www.reddit.com/user/CloudDevDanUK)
- Category: IaC & DevOps

---

Using only IaC and DevOps pipelines, deploy a WordPress site **without using the marketplace offering** \- only using PaaS resources.

Consider: 

* How to securely link the various PaaS resources together, following best-practice.
* Security of the individual PaaS components - such as access over public internet and authentication.
* Monitoring and alerting of the pipeline runs.
* Monitoring and alerting of the application.
* Resource utilisation and scale. What SKUs are the best fit for the job, and how can you handle scale (e.g. traffic spikes).
* Resiliency - what would happen if a data centre, or even a region went down? How can the application handle events such as this?
* Costs - how much will it cost to host this application?
* How would you give the application a custom domain and SSL certificate?

There are a lot of good learning outcomes from this project. Hosting applications in Azure is a common scenario, as is deploying and updating them via automated means. Completing this project would show a competence in these areas.