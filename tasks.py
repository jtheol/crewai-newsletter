from crewai import Task
from datetime import datetime


class NewsletterTasks:
    def get_news_task(self, agent):
        return Task(
            description=f"Get the latest AI news stories from the last 24 hours. The current time is {datetime.now()}",
            agent=agent,
            async_execution=True,
            expected_output="""A list of the top AI news stories with their titles, URLS, and a brief summary.
            
            Example Output:
            [
                {
                    'title': '',
                    'url': 'https://example.com/',
                    'summary': '',
                },
                {{...}}
            ]

            """,
        )

    def analyze_news_task(self, agent, context):
        return Task(
            description="Analyze each news story and ensure that there are 5 well-formatted articles.",
            agent=agent,
            async_execution=True,
            context=context,
            expected_output="""A summary of the news story and 5 key points as a bulleted list under the summary in markdown.
            """,
        )

    def compile_newsletter(self, agent, context, callback_function):
        return Task(
            description="Compile the newsletter in a well formatted way using markdown.",
            agent=agent,
            context=context,
            callback=callback_function,
            expected_output="""A well formated markdown report of the 5 news articles.
            """,
        )
