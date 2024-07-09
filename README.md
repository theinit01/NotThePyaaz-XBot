
# NotThePyaaz Twitter Bot 🤖
<p align="center">
<img src="/assets/diagram.png">
</p>


NotThePyaaz is a Twitter bot that fetches the funniest and weirdest headlines from the r/notthepyaaz subreddit and tweets them in a humorous way. It's a parody bot inspired by the NotTheOnion subreddit, delivering daily doses of humor and satire.

## Features

-   🤖 Fetches top rising posts from the r/notthepyaaz subreddit.
-   😂 Converts headlines into humorous tweets using a Google Gemini.
-   🐦 Automatically posts the tweets to Twitter.
-   📝 Logs all activities for tracking.


## Prerequisites

-   Python 3.x
-   Reddit API credentials
-   Twitter API credentials

## Installation 

1. Clone the repository:
  ```bash
  git clone https://github.com/theinit01/NotThePyaaz-XBot.git 
  cd NotThePyaaz-XBot
  ```
2. Install the dependencies
`pip install -r requirements.txt`

3. Set up environment variables:
	- Create a `.env` file in the root directory.
	- Add your Reddit, Google Gemini and X (Twitter) API credentials to the `.env` file:
	
  ```makefile
	REDDIT_USERNAME=your_reddit_username
	REDDIT_PASSWORD=your_reddit_password
	REDDIT_CLIENT_ID=your_reddit_client_id
	REDDIT_CLIENT_SECRET=your_reddit_client_secret
	GEMINI_API_KEY=your_gemini_api_key
	TWITTER_API_KEY=your_twitter_api_key
	TWITTER_API_SECRET=your_twitter_api_secret
	BEARER_TOKEN=your_twitter_bearer_token
	ACCESS_TOKEN=your_twitter_access_token
	ACCESS_TOKEN_SECRET=your_twitter_access_token_secret
  ```

4. Run the main file
`python3 bot.py`



## Contributing 
Contributions are welcome! If you have any ideas, suggestions, or improvements, feel free to open an issue or submit a pull request. 
## License 
This project is licensed under the [MIT License](LICENSE).
