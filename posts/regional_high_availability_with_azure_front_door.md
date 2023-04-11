# Regional High Availability with Azure Front Door

- Author: [mattallford](https://www.reddit.com/user/mattallford)
- Category: Business Continuity

---

Imagine you have a simple web application that runs inside an Azure App Service (or a function app, either is OK for this project).

Your focus is to start ensuring the application is production ready, and one area you need to address is to ensure availability of the application in the event of Azure regional issues.

Your task is to create the same web application in two separate Azure Regions, and then use Azure Front door to route traffic to the app services. Consider the following scenarios to implement different configurations based on requirements of each bullet point:

* Always route traffic to one region unless that region is unavailable, then automatically route traffic to the second region
* Always route traffic to either region to load balance and make use of both resources
* Create a custom domain name for your web application which resolves to front door, and ensure end users have a secure connection to the web application
* Restrict direct access to the web applications to force all traffic to route through front door

&amp;#x200B;

As an extension of this project if you want an extra challenge, change your web application to something that requires a database such as Azure SQL or Cosmos DB. Consider the following additional points:

* Ensure the web application connects to the database on a private network and the database is not publicly accessible
* How will you handle connectivity between the web application and the database? Hint: There are better methods than using connection strings and passwords :)
* How will you handle regional availability of the database?
* Should you route traffic from front door to the web application in the secondary region under normal circumstances? Why or why not?