# Securing a vulnerable webapp with Azure

- Author: [AutoSysOps](https://www.reddit.com/user/AutoSysOps)
- Category: Security & Compliance

---

Your job is to run OWASP WebGoat in a azure environment (NOTE: make sure it's not network connected to any other service you are using as this webapp really is vulnerable).  
You can find the app here:  
[https://github.com/WebGoat/WebGoat](https://github.com/WebGoat/WebGoat)  
How you host the webapp is all up to you.  
Your job as Azure Security specialist is to design a solution to make sure this webapp is secured to as many vulnerabilities as possible without altering the code itself. So use different azure security techniques to prevent these attacks.  
Once you are setup run through some of the tasks in the WebGoat and see which ones are still exploitable and which ones are not. (You can look at the solutions here: [https://github.com/WebGoat/WebGoat/wiki/Main-Exploits](https://github.com/WebGoat/WebGoat/wiki/Main-Exploits) if you don't want to figure out how to do the exploits).  
For bonus points you can start by setting up the security solutions in a auditing/reporting way where you will get notified if vulnerabilites are exploited and only afterward block them.