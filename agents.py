from crewai import Agent
from tools.search_tools import SearchTool


class NewsletterAgents:
    def editor_agent(self):
        return Agent(
            role="Editor",
            goal="Ensures the quality of the AI newsletter",
            backstory="""You ensure the newsletter is engaging and informative for viewers""",
            allow_delegation=True,
            verbose=True,
            max_iter=5,
        )

    def get_news_agent(self):
        return Agent(
            role="Automated News Fetcher",
            goal="You will retrieve the top AI news stories for the day.",
            backstory="""You will look for the most impactful articles about AI and cutting edge research of large language models""",
            tools=[SearchTool.search_google],
            verbose=True,
            allow_delegation=True,
        )

    def analyze_news(self):
        return Agent(
            role="AI News Analyst",
            goal="You will analyze the AI news stories making them engaging and explain them in a way that is accessible to nontechnical audiences formatted in markdown.",
            backstory="""
                        Your role is to analyze the research,
					analysis, and strategic insights.
                    """,
            tools=[SearchTool.search_google],
            verbose=True,
            allow_delegation=True,
        )

    def newsletter_compiler(self):
        return Agent(
            role="Newsletter Compiler",
            goal="Compile the simplified news stories into a final newsletter format.",
            backstory="""Arrange the stories in a visually appealing newsletter format.""",
            verbose=True,
            allow_delegation=True,
        )
