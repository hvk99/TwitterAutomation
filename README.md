# Automated Twitter Content Posting with Generative AI

This project automates the posting of content to Twitter using Python's Selenium library and Google's Gemini AI for content generation.

## Motivation:

While Twitter's API offers powerful features, obtaining access can be challenging. This project provides an alternative solution for developers who may not have been granted API access.

## Functionality:

**Login Automation:** The script logs into your Twitter account using Selenium.\
**Content Generation:** The script leverages Google's Gemini AI to generate unique and engaging content for your tweets.\
**Posting Automation:** The script interacts with Twitter's interface to post the generated content directly to your account.

## Installation / Usage:

Clone this git repo using the below command:
`git clone https://github.com/hvk99/TwitterAutomation-Posting.git`

Use this command to install all the required python libraries.
`pip install -r requirements.txt`

Create a .env file inside the cloned directory. You can use the TEMPLATE_ENV to create you own .env file.

Place a chrome driver at the path you mentioned in the .env file.\
You can download the chrome driver from [this](https://googlechromelabs.github.io/chrome-for-testing/) location.\
Note: Use the chrome driver which matches the chrome version on your setup.

## Benefits:

**Save Time:** Automate content creation and posting to streamline your social media presence.\
**Enhance Creativity:** Explore new content ideas with the help of generative AI.\
**API Alternative:** Provides a solution for developers who haven't received Twitter API access.

## Please Note:

- This project utilizes a browser automation approach.
- Twitter may view automated activity as a violation of their terms of service.
- Use this script responsibly and at your own risk.
- Consider exploring alternative content moderation techniques to ensure the generated content aligns with your brand voice and avoids any potential issues.

## Disclaimer:

- This project is for educational purposes only. The author is not responsible for any misuse or consequences arising from its use.
