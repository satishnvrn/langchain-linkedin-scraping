from langchain.chains import LLMChain
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

from third_parties.linkedin import scrape_linkedin_profile
from agents.linkedin_lookup_agent import lookup as linkedin_lookup_agent


def ice_breaker_with(name: str) -> str:
    linkedin_url = linkedin_lookup_agent(name)
    linkedin_data = scrape_linkedin_profile(linkedin_url)

    summary_template = """
    given the Linkedin information {information} about a person from I want you to create:
    1. a short summary
    2. two interesting facts about them
    """

    summary_prompt_template = PromptTemplate(
        input_variables=["information"], template=summary_template
    )

    llm = ChatOpenAI(temperature=0, model="gpt-3.5-turbo")

    chain = summary_prompt_template | llm
    linkedin_data = scrape_linkedin_profile(
        "https://www.linkedin.com/in/eden-marco-866555128/",
        mock=True
    )
    res = chain.invoke({"information": linkedin_data})

    print(res)
    return "res"


if __name__ == "__main__":
    load_dotenv()

    print("Ice Breaker Enter")
    ice_breaker_with(name="Eden Marco Udemy")
