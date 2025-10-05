from typing import List
from crewai import Agent, Task, Crew, Process, LLM
from crewai.project import CrewBase, agent, crew, task

from crewai_tools import SerperDevTool, ScrapeWebsiteTool, DirectoryReadTool, FileReadTool, FileWriterTool
from pydantic import BaseModel, Field
from dotenv import load_dotenv
