## AI Smart Website Search Tool
_Agentic System - Built with LangChain - Utilizing GPT4o-mini and TAVILY search tool_

This smart search tool searches a defined website and return results with pertinent URLs from the website. It is currently setup to demonstrate on the ConsumersEnergy.com website. 
(There is no professional affiliation with Consumers Energy) 

### DOCUMENTATION

git clone https://github.com/jesseanders/opengpts.git
cd opengpts

🚨OpenAI and Tavily API Keys Required🚨<br>
Enter your API Keys where labeled in the lang_bot_build.py file and save the file.

### Setting up and running the Web UI as is:
> Install Docker Desktop App - https://www.docker.com <br>
> Create Environment in VS Studio with included Files (file structure)
> Enter 

- __From Terminal in VS Code Run:__
docker build -t lang_search_bot .  
- __From Terminal in VS Code Run:__
docker run -p 6002:6000 lang_search_bot
- __In Web Browser Navigate to:__
http://localhost:6002
-__Input Test Search to See Results:__
How can I save money on my electric bill

### "Und
