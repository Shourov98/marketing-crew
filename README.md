# Marketing Crew AI

An AI-powered marketing team built with CrewAI that automates content creation, SEO optimization, and marketing strategy development.

## Overview

Marketing Crew AI is a comprehensive solution that leverages AI agents to handle various aspects of marketing, from market research to content creation and SEO optimization. The system uses a crew of specialized AI agents, each with specific roles and responsibilities, to create a complete marketing pipeline.

## Tech Stack

- **Python 3.12+**
- **CrewAI**: Framework for creating and orchestrating AI agent workflows
- **CrewAI Tools**: Additional tools for web scraping, file operations, etc.
- **OpenAI**: GPT models for agent intelligence
- **Pydantic**: Data validation and settings management
- **Python-dotenv**: Environment variable management

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd marketing-crew
```

2. Set up a virtual environment:
```bash
python -m venv .venv
# On Windows
.venv\Scripts\activate
# On macOS/Linux
source .venv/bin/activate
```

3. Install dependencies:
```bash
pip install -e .
# or using uv
uv pip install -e .
```

4. Create a `.env` file with your API keys (see Environment Variables section)

## Environment Variables

Create a `.env` file in the root directory with the following variables:

```
OPENAI_API_KEY=your_openai_api_key_here
SERPER_API_KEY=your_serper_api_key_here
```

## Project Structure

```
marketing-crew/
├── config/
│   ├── agents.yaml    # Agent definitions and roles
│   └── tasks.yaml     # Task definitions and expected outputs
├── resources/
│   └── drafts/        # Output directory for generated content
│       ├── content_calendar.md
│       ├── marketing_strategy.md
│       ├── posts/
│       └── reels/
├── .env               # Environment variables
├── crew.py            # Main crew definition and agent interactions
├── main.py            # Entry point for running the application
└── README.md          # This file
```

## Agents

The marketing crew consists of the following specialized agents:

1. **Head of Marketing**
   - Role: Lead the marketing team to achieve strategic goals
   - Responsibilities: Develop marketing strategies, coordinate team efforts
   - Goal: Drive brand growth through effective marketing planning

2. **Content Creator for Social Media**
   - Role: Create engaging social media content
   - Responsibilities: Develop reels, posts, and email campaigns
   - Goal: Produce content that resonates with the target audience

3. **Content Writer for Blogs**
   - Role: Write compelling blog content
   - Responsibilities: Create informative and engaging blog posts
   - Goal: Produce high-quality blogs that drive traffic and engagement

4. **SEO Specialist**
   - Role: Optimize content for search engines
   - Responsibilities: Improve content visibility and drive organic traffic
   - Goal: Enhance search engine rankings through effective SEO strategies

## Task Pipeline

The marketing crew follows this workflow:

1. **Market Research**
   - Conduct comprehensive market research
   - Analyze trends, competitors, and customer needs
   - Output: Detailed market research report

2. **Prepare Marketing Strategy**
   - Develop a marketing strategy based on research
   - Define target audience, budget, and channels
   - Output: Marketing strategy document stored in `resources/drafts/marketing_strategy.md`

3. **Create Content Calendar**
   - Plan content topics and publishing schedule
   - Align with marketing strategy
   - Output: Content calendar stored in `resources/drafts/content_calendar.md`

4. **Prepare Post Drafts**
   - Create drafts for social media posts
   - Follow content calendar guidelines
   - Output: Post drafts stored in `resources/drafts/posts/`

5. **Write Blog Content**
   - Develop detailed blog articles
   - Follow content calendar and marketing strategy
   - Output: Blog content stored as text files

6. **Optimize Content for SEO**
   - Enhance content with SEO best practices
   - Improve visibility and search rankings
   - Output: SEO-optimized content

## Usage

Run the marketing crew with:

```bash
python main.py
# or using uv
uv run main.py
```

You can also run specific components:

```bash
python crew.py
# or using uv
uv run crew.py
```

## Customization

- Modify agent roles and behaviors in `config/agents.yaml`
- Adjust task descriptions and outputs in `config/tasks.yaml`
- Extend the crew with additional agents or tasks in `crew.py`

## Troubleshooting

- **API Rate Limits**: If you encounter rate limit errors, consider:
  - Using a different model (e.g., gpt-3.5-turbo instead of gpt-4o-mini)
  - Adding a payment method to your OpenAI account to increase limits
  - Implementing rate limiting in your code

- **Model Availability**: Ensure you're using available models for your API key