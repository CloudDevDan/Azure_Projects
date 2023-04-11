# Azure Durable Functions - parallel image download and recognition

- Author: [CloudDevDanUK](https://www.reddit.com/user/CloudDevDanUK)
- Category: PaaS

---

I've had this video bookmarked for a while, and I've always wanted to have a go myself, so I figured I would share it here as a fun project to have a go at.

Here is the video: [Durable functions in Python for Azure Functions | Azure Friday](https://www.youtube.com/watch?v=HZgjmb9Y_IM) with Scott Hanselman and David Justo.

If you skip to approx [13 mins in](https://youtu.be/HZgjmb9Y_IM?t=809), you'll see an awesome example by David Justo that uses a Python based Durable Function with the fan out/fan in pattern. The Durable Function downloads a given number of images from the internet and determines if they are of dogs or cats - all in parallel. The results are displayed on a simple web page.

I think this would be a really fun to re-create, either in Python or whatever language you choose. 

The only thing I'm not sure about here is how the images are classified. I believe David mentions [Tensorflow](https://www.tensorflow.org/tutorials/images/classification) image classification. You could possibly use [Azure Computer Vision](https://azure.microsoft.com/en-gb/products/cognitive-services/computer-vision/) or [Custom Vision](https://azure.microsoft.com/en-gb/products/cognitive-services/custom-vision-service/).

Completing this project would expose you to Durable Functions and Azure Web Apps (or Static Web Apps) whilst getting your hands dirty with writing some code, particularly if you chose a language you're not overly familiar with. The image recognition would expose you some machine learning in Azure. The latter part could be a bit tricky if it's a new concept for you, but what better way to learn!

To further expand this project - deploy it to Azure rather than running it locally. Consider the error handling aspect and how you can report/alert on that. How much would a project like this cost to run?

Save your work in a GitHub repo and include it in your portfolio of project work. Report back here on your progress and to get input.

Have fun!