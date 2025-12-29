##CREW LOGIC MODULE
import os
import json
import random
from dotenv import load_dotenv
from crewai import Agent, Task, Crew, Process, LLM
from crewai_tools import SerperDevTool
from PIL import Image, ImageDraw, ImageFont, ImageFilter # <--- ADDED ImageFilter

# IMPORT THE NEW CONFIGURATION
from theme_config import THEMES
