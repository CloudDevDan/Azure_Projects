# Deploy updated workload without downtime

- Author: [AutoSysOps](https://www.reddit.com/user/AutoSysOps)
- Category: Business Continuity

---

You are a Azure Platform Engineer who's job it is to make sure the workloads running on your platform don't experience any downtime.  
One of the developers from one of your workloads comes to you with a questions.  
The next update of there software will require some reconfigurations during the deployment. Some DNS stuff and database stuff needs to be changed so during the deployment the workload could experience some downtime.  
Your job as platform engineer is to design a solution so that the application won't experience any downtime.  
For simplicity sake you can go with one of these scenario's:  
\- Have a azure webapp (AppService) with a simple webpage (can be a basic html hello world page).  
\- Have a VM running IIS with a simple webpage (can be the welcome page)  


You can use a tool like the azure availibity monitor to monitor the availability of your webapp:  
[https://learn.microsoft.com/en-us/azure/azure-monitor/app/monitor-web-app-availability](https://learn.microsoft.com/en-us/azure/azure-monitor/app/monitor-web-app-availability)  


Now create a automated solution to redeploy your solution without it generating downtime.  


For Bonuspoint:  
Think about how this solution would change once databases get involved and how can you design a solution to update the workload without losing data and still allow for any kind of reconfiguration which could cause downtime. (Hint: this would probably involve some kind of messaging or event service)