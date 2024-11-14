# test state change
# pip install -U langchain langchain-openai
# # !pip install -qU langchain-openai
# # !pip install -qU "langchain-community>=0.2.11" tavily-python

import os
os.environ["OPENAI_API_KEY"] = 'Enter OpenAI API Key Here'

from langchain_openai import ChatOpenAI

# model = ChatOpenAI(model="gpt-3.5-turbo")
model = ChatOpenAI(model="gpt-4o-mini")

import os

if not os.environ.get("TAVILY_API_KEY"):
    os.environ["TAVILY_API_KEY"] = 'Enter Tavily API Key Here'

# +
from langchain_community.tools import TavilySearchResults

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

import datetime
from pprint import pprint
import datetime

from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnableConfig, chain

today = datetime.datetime.today().strftime("%D")

# Prompt setup with combined information
prompt = ChatPromptTemplate(
    [
        ("system", "You are a helpful writing assistant to improve information for customers of ConsumersEnergy.com. "
                   "You clean up rough drafts and make them friendly and professional for customers to read. "
                   "You NEVER alter URLs from the rough drafts you receive."),
        ("human", "{combined_input}"),  # Combined user and tool input
    ]
)

# Assuming `llm` and `tool` have been initialized
llm_with_tools = model.bind_tools([tool])
llm_chain = prompt | llm_with_tools

@chain
def tool_chain(user_input: str, config: RunnableConfig):
    try:
        # Step 1: Use the tool first to get initial information
        tool_response = tool.invoke({"query": user_input}, config=config)
        tool_content = tool_response.content if hasattr(tool_response, 'content') else tool_response
        print("Tool Response:")
        pprint(tool_content)  # Display tool response for clarity

        # Step 2: Combine user input and tool response into a single input
        combined_input = f"User's question: {user_input}\n\nTool provided information:\n{tool_content}"

        # Final invocation with combined context
        final_output = llm_chain.invoke({"combined_input": combined_input}, config=config)
        final_content = getattr(final_output, 'content', "")
        print("\nFinal Revised Output:")
        pprint(final_content)  # Display the final LLM response

        return final_content  # Return only the final revised content
    except Exception as e:
        print(f"An error occurred: {e}")
        return None