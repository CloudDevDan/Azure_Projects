# Send a Tweet whenever a new blog post is published

- Author: [CloudDevDanUK](https://www.reddit.com/user/CloudDevDanUK)
- Category: Random Fun!

---

Using whatever Azure based resources you see fit, regularly poll an RSS feed for new articles, and if found, send a Tweet about it.

The Tweet should contain the article's title, URL and should have logic to ensure the entire Tweet content does not breach the maximum character limited (imposed by Twitter).

Ensure that you have monitoring in place to capture and alert upon any errors that may occur,

Added challenges:

* Shorten the URL and post that in place of the original *&lt;- this is a good one!*
* Make a record of this action in a database, and do a lookup on said database before Tweeting to avoid any duplicates Tweets.
* Build this entire project as code and deploy via automated means.