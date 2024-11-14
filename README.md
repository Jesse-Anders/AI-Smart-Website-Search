## AI Smart Website Search Tool
_Agentic System - Built with LangChain - Utilizing GPT4o-mini and TAVILY search tool_

This smart search tool searches a defined website and return results with pertinent URLs from the website. It is currently setup to demonstrate on the ConsumersEnergy.com website. (I have no professional affiliation with Consumers Energy. This is just a demo)

### DOCUMENTATION
#### Clone the Repository:
Obtain the project files by cloning the repository.<br>

```bash
git clone https://github.com/Jesse-Anders/AI-Smart-Website-Search.git

cd AI-Smart-Website-Search/lang_search_bot
```

🚨OpenAI and Tavily API Keys Required🚨<br>
Enter your API Keys where labeled in the lang_bot_build.py file and save the file.

### Setting up and running the Web UI as is:
> Install Docker Desktop App - https://www.docker.com <br>
> Create Environment in VS Studio with included Files (file structure)
> Enter 

- __From Terminal in VS Code Run:__
```docker build -t lang_search_bot .```  
- __From Terminal in VS Code Run:__
```docker run -p 6002:6000 lang_search_bot```
- __In Web Browser Navigate to:__
```http://localhost:6002```
- __Input Test Search to See Results:__
"How can I save money on my electric bill?"

### Making Basic Alterations
Changes to the AI agentic sytem and search functionality can all be made in the lang_bot_build.py<br>
The Tavily search tool's current setup allows it to search ConsumersEnergy.com and can be easily changed.
```python
tool = TavilySearchResults(
    max_results=5,
    search_depth="advanced",
    include_answer=True,
    include_raw_content=True,
    include_images=False,
    include_domains=["https://www.consumersenergy.com/"],
    # exclude_domains=[...],
    # name="...",            # overwrite default tool name
    # description="...",     # overwrite default tool description
    # args_schema=...,       # overwrite default args_schema: BaseModel
)
```

The Prompt Agent can also be changed to match the desired company information. Right now the system is acting as a writing assistant for ConsumersEnergy.com.
```python
prompt = ChatPromptTemplate(
    [
        ("system", "You are a helpful writing assistant to improve information for customers of ConsumersEnergy.com. "
                   "You clean up rough drafts and make them friendly and professional for customers to read. "
                   "You NEVER alter URLs from the rough drafts you receive."),
        ("human", "{combined_input}"),  # Combined user and tool input
    ]
)
```

### Understanding the Agent Flow in lang_bot_build.py
This is a simple 2 part Langnchain agentic system. _(llm_chain = prompt | llm_with_tools)_ wherin the Tavily search tool (llm_with_tools) runs a search based on the user inquiry and outputs its search results formatted with URLs. This result/output is then handed off to the 'prompt' which cleans up the content and generates a 'cutomer service styled' final response. In the current setup both the prompt and the llm_with_tools utilize gtp4o-mini, but each can utilize their own models if need be.

<img width="938" alt="Screenshot 2024-11-13 at 9 22 09 PM" src="https://github.com/user-attachments/assets/07e15100-6047-412b-90ae-c262692a0d1c">

