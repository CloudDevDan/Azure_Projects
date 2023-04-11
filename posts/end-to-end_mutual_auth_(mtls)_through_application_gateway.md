# End-to-End Mutual Auth (mTLS) Through Application Gateway

- Author: [Dus-Dee](https://www.reddit.com/user/Dus-Dee)
- Category: Networking

---

Imagine you've just implemented Mutual Auth on your Application such as on an App Service.  Mutual Auth (mTLS) is where not only the server authenticates itself during the TLS handshake, but the client also must provide a certificate to authenticate themselves.  You now want to place this App Service behind an Azure Application Gateway but this presents a few issues.

Application Gateway V2 does support mTLS, but it's a reverse proxy and cannot authenticate to the backend itself.  How can you implement this?  The solution you want is that your clients present a certificate to authenticate to the App Gateway, and then this certificate is passed to the App Service in case you might need data from it such as the user's name, email, or department.

HINT: the client certificate data is stored in a variable you can have the App Gateway pass to the backend, but not in a way that your App Service might expect.  Think of the types of data that can be "Rewritten" in Application Gateway V2 and think of ways to recode your App Service to verify certificates based on this data.