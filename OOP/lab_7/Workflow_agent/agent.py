from google.adk.agents import Agent, SequentialAgent, ParallelAgent, LoopAgent

def fetch_from_wikipedia(topic: str) -> dict:
    if not topic.strip():
        return {"status": "error", "error": "Порожня тема"}

    return {
        "status": "success",
        "source": "wikipedia",
        "data": f"Основна інформація про {topic}"
    }


def fetch_from_blog(topic: str) -> dict:
    return {
        "status": "success",
        "source": "blog",
        "data": f"Практичне використання {topic}"
    }


def analyze_data(data: str) -> dict:
    """
    Аналізує зібрані дані.

    Args:
        data: текст з даними

    Returns:
        dict
    """
    if not data.strip():
        return {"status": "error", "error": "Немає даних"}

    return {
        "status": "success",
        "analysis": f"Аналіз: {data}"
    }


def generate_report(analysis: str) -> dict:
    return {
        "status": "success",
        "report": f"Звіт:\n{analysis}"
    }


def improve_report(report: str) -> dict:
    if len(report) < 50:
        return {
            "status": "retry",
            "report": report + "\n(додано більше деталей...)"
        }

    return {
        "status": "done",
        "report": report + "\n(звіт оптимізовано)"
    }

parallel_agent = ParallelAgent(
    name="data_collection",
    sub_agents=[
        Agent(
            model="gemini-3.1-flash-lite",
            name="wiki_agent",
            instruction="Отримай інформацію про тему користувача",
            tools=[fetch_from_wikipedia],
        ),
        Agent(
            model="gemini-3.1-flash-lite",
            name="blog_agent",
            instruction="Отримай практичну інформацію про тему",
            tools=[fetch_from_blog],
        ),
    ]
)

sequential_agent = SequentialAgent(
    name="processing_pipeline",
    sub_agents=[
        Agent(
            model="gemini-3.1-flash-lite",
            name="analysis_agent",
            instruction="Проаналізуй отримані дані",
            tools=[analyze_data],
        ),
        Agent(
            model="gemini-3.1-flash-lite",
            name="report_agent",
            instruction="Створи звіт",
            tools=[generate_report],
        ),
    ]
)

loop_agent = LoopAgent(
    name="improvement_loop",
    sub_agents=[
        Agent(
            model="gemini-3.1-flash-lite",
            name="improver",
            instruction="""
            Покращуй звіт поки він не стане достатньо детальним.
            Якщо звіт хороший — завершуй.
            """,
            tools=[improve_report],
        )
    ],
    max_iterations=5
)

root_agent = SequentialAgent(
    name="full_workflow",
    sub_agents=[
        parallel_agent,
        sequential_agent,
        loop_agent
    ]
)