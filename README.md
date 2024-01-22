## Inspiration
The project was inspired by the themes of rosehack, and empowering women in stem. 
Rosehack stands as a beacon of transformative empowerment for women in STEM, fearlessly tackling the challenges that often besiege their journey to success. 
Through cutting-edge initiatives and a visionary approach, Rosehack transcends obstacles, sculpting a future where women not only thrive but redefine the very essence of excellence in science and technology. 

## What it does
The project EqualEye is a chrome extension, which uses a fine-tuned Large Language model to find and classify misogynistic content on your twitter page.

## How we built it
We first took an open source transformer model from Huggingface called distilBERT and trained it to identify and classify misogynist and/or sexist online social posts using datasets of posts from reddit by academic researchers. On our test data, it achieve 94% accuracy.

We made a chrome extension which finds and extracts the text from all the tweets in your twitter feed, and then sends them to a backend server which return whether or not each tweet is misogynist. 

Our backend server uses FastAPI and hosts our LLM.


## Challenges we ran into
The biggest challenge we ran into was getting the backend work. Our first major problem was that we were using a specially defined class of distilBERT, which pytorch was not able to load properly. After that, we spent over 6 hours trying to get our backend server up so it could be queried by our browser extension. 

## Accomplishments that we're proud of
We are most proud of our achievements with the large language model, including the process of training the model despite little public data, trouble shooting the abnormal issue we had loading the model into our server, and the models 95% accuracy rate.
On top of that, we are also very happy with the reliability of the extension. We have seen it work across twitter.


