# Project Zathras: My first ML project. 

## Overview
This is my project to learn how to set up local LLMs and how to use GitHub. I used Gemini to help brainstorm and to help with coding as I am not good enoough yet to write an entire projects worth of code by myself. This tool allows users to connect to a local LLM server (via LM Studio), generate creative text, and benchmark the hardware's performance by measuring Tokens Per Second (TPS). It demonstrates the integration of Python with local AI API endpoints.

## Features
- **Local API Connection:** Connects to localhost endpoints (mimicking OpenAI's API structure).
- **Performance Metrics:** Real-time calculation of token generation speed.
- **File I/O:** Automatically captures and saves generated content to a local text file.

## Requirements
- Python 3.x
- LM Studio (running a local server)
- `openai` python library

## Installation
1. Install the required library:
   ```bash
   pip install -r requirements.txt
   
