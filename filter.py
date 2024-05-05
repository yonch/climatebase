import json
import pprint
from groq import AsyncGroq
from groq.types.chat.completion_create_params import Message
import os
from pydantic import BaseModel, Field
from typing import Literal
import asyncio

DATA_FILE = "jobs_data.json"

# models
MIXTRAL = "mixtral-8x7b-32768"
LLAMA3_70B = "llama3-70b-8192"

class JobScore(BaseModel):
    summary: str = Field(description="Brief description of the job and company")
    reason: str = Field(
        description="Clear and concise explanation of why this job is a match"
    )
    score: Literal["Not Likely", "Neutral", "Likely", "Very Likely"] = Field(
        description="How good of a match this job is to the candidate's skills, experience, and priorities"
    )


async def main():

    # instantiate groq client
    groq = AsyncGroq(
        api_key=os.environ.get("GROQ_API_KEY"),
    )

    # read the json from the file 
    with open(DATA_FILE, "r") as f:
        raw_jobs = json.load(f)

    # get the list of jobs, under the key "hits"
    jobs = raw_jobs["hits"]

    response_schema = json.dumps(JobScore.model_json_schema(), indent=2)

    chat_completion_promises = []
    # for each jobs
    for job in jobs[:1]:


        messages=[
            Message(role="system",
                    content="You are an employment consultant, whose goal is to find the most suitable jobs for a candidate.\n"
                # Pass the json schema to the model. Pretty printing improves results.
                f"You MUST generate output in JSON. The JSON object must use the schema: {response_schema}\n\n"
                "Create a single JSON object for the talk, NOT for each speaker.\n\n"
                "As a reminder, the JSON schema specifies the properties expected, but the root of the resulting object should not have a 'properties' key\n"
                'For example, the JSON will look like {"summary": "", "reason": "", "score": ""}',
            ),
            Message(role="user",
                    content="The job hunter is looking for a job in Product management or data science in a company that pursues environmental sustainability, natural resource management, or green house gas emission reduction through nature based solutions.\n\n"
                "Please evaluate the relevance and potential value of engaging with the listed company.\n\n"
                # f"Examples:\n{example_message}\n"
                f"Input:\n{json.dumps(job, indent=2)}\n"
                "Output:\n",
            ),
        ]

        pprint.pp(messages)


        chat_completion = groq.chat.completions.create(
            messages=messages,
            model=LLAMA3_70B,
            # Streaming is not supported in JSON mode
            stream=False,
            # Enable JSON mode by setting the response format
            response_format={"type": "json_object"},
            # lower temperature to reduce hallucinations
            temperature=0.0,
        )
        
        chat_completion_promises.append(chat_completion)

    chat_completions = await asyncio.gather(
        *chat_completion_promises, return_exceptions=True
    )

    pprint.pp(chat_completions)


asyncio.run(main())
