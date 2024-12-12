##  🔎 Horizon Data Wave Tools
[![Python](https://img.shields.io/badge/Python-3.12%20|%203.13-blue)](https://github.com/horizondatawave/hdw_tools)
[![PyPI](https://img.shields.io/pypi/v/hdw_tools?label=hdw_tools&color=blue)](https://pypi.org/project/hdw-tools/)
[![License](https://img.shields.io/badge/License-MIT-green)](https://github.com/horizondatawave/hdw-tools/blob/main/LICENSE)

**Horizon Data Wave Tools** is a library designed for seamless integration with [`llamaindex`](https://www.llamaindex.ai) and [`crewai`](https://www.crewai.com).  

This library provides robust tools and endpoints to fetch data directly from LinkedIn via the [`HorizonDataWave`](https://www.horizondatawave.ai/) data provider. With [`hdw_tools`](https://pypi.org/project/hdw-tools/), you can simplify and automate the process of integrating LinkedIn data queries into projects that utilize [`llamaindex`](https://www.llamaindex.ai) or [`crewai`](https://www.crewai.com).  


## Python Version Requirement
HDW tools requires Python 3.12 or higher.

## Installation

Install using pip:

```bash
pip install hdw_tools
```
##  Environment Variables
To use this project, you need to set the following environment variables:

**HDW_API_KEY**: The API key required for authentication. You can obtain this key by visiting [Horizon Data Wave](https://www.horizondatawave.ai/).

Make sure to add these variables to your environment configuration before running the project.

## Examples

Using with LlamaIndex
```python
from hdw_tools.tools.llama_linkedin import LinkedInToolSpec
from llama_index.agent.openai import OpenAIAgent
from llama_index.llms.openai import OpenAI

agent = OpenAIAgent.from_tools(
    [tool for sublist in [LinkedInToolSpec().to_tool_list()] for tool in sublist],
    llm=OpenAI(model="gpt-4", temperature=0.1),
    verbose=True,
    system_prompt="You are an AI assistant helping users with LinkedIn searches",
)
```
Using with CrewAI
```python
from crewai import Task
from hdw_tools.tools import crewai_linkedin

find_user_data = Task(
    description=(
        "Analyze {user_request}. Define provided data and tasks. Create plan to use existing tools to find information "
        "in requred sources based on provided information and tasks. And execute this plan."
    ),
    expected_output="Provide results in markdown format.",
    tools=[
        crewai_linkedin.GetLinkedInCompany(),
        crewai_linkedin.GetLinkedInUser(),
        crewai_linkedin.GetLinkedInPost()
    ]
)
```

##  License
This project is licensed under the MIT License. See the [LICENSE](https://github.com/horizondatawave/hdw-tools/blob/main/LICENSE) file for more information.