import os

from dotenv import load_dotenv

from agents import NewsletterAgents
from tasks import NewsletterTasks
from crewai import Crew, Process

from langchain_openai import ChatOpenAI

from tools.save_file import save_file

agents = NewsletterAgents()
tasks = NewsletterTasks()

load_dotenv()

OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")

llm = ChatOpenAI(temperature=0, model="gpt-4", api_key=OPENAI_API_KEY)

editor = agents.editor_agent()
get_news_agents = agents.get_news_agent()
news_analyzer = agents.analyze_news()
compiler = agents.newsletter_compiler()

get_news_task = tasks.get_news_task(get_news_agents)
analyze_news_task = tasks.analyze_news_task(news_analyzer, [get_news_task])
compile_newsletter_task = tasks.compile_newsletter(
    compiler, [analyze_news_task], callback_function=save_file
)


crew = Crew(
    agents=[editor, get_news_agents, news_analyzer, compiler],
    tasks=[get_news_task, analyze_news_task, compile_newsletter_task],
    process=Process.hierarchical,
    manager_llm=llm,
)

results = crew.kickoff()

print(results)
