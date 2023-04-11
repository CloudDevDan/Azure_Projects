# Private networking with PaaS resources

- Author: [CloudDevDanUK](https://www.reddit.com/user/CloudDevDanUK)
- Category: Networking

---

Consider a really simply N-tier architecture, with a web front-end, an API, and a back-end.

Your brief for this project is to have a public facing website, but all other resources need to be totally offline - no public access whatsoever.

Demonstrate displaying data on the website that is pulled from the back-end via the API (with the back-end and the API set so that they are not accessible over public internet).

Provide evidence that the API and a back-end cannot be resolved over public internet, and ensure that the web front-end has best-practice secure connectivity to the API only - not the back-end. The same goes for the API connectivity to the back-end.

Consider deployment - for example, if you use Bicep or Terraform for IaC, and deploy this infra via GitHub Actions or Azure Pipelines, how will the pipeline handle the private resources? Can you build, deploy and provide consequent updates to this project via CI/CD?

By completing this project, you will be able to demonstrate knowledge of the private networking aspects of Azure (which often crop up in penetration test reports) as well as knowledge on linking various resources together in a secure and private way.