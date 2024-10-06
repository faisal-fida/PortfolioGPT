# PortfolioGPT

PortfolioGPT is an advanced portfolio analysis AI assistant designed to help users analyze and understand portfolio data. It uses specialized tools to access and interpret data from Faisal's portfolio, providing insights into skills, types of works, and resume information.

## Features

- **Skills Analysis**: Retrieves detailed information about skills, including languages, frameworks, and tools.
- **Work Categorization**: Analyzes and categorizes types of work based on skills.
- **Resume Retrieval**: Provides the resume URL for quick access.
- **Contextual Understanding**: Offers detailed explanations and insights on the portfolio data.

## Setup

1. Clone the repository:
   ```sh
   git clone https://github.com/faisal-fida/PortfolioGPT.git
   cd PortfolioGPT
   ```

2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```

3. Set up environment variables:
   ```sh
   cp .env.example .env
   # Update .env with your API keys and configuration
   ```

## Usage

Run the main script to analyze the portfolio data:
```sh
python main.py
```

## Components

### `main.py`
Orchestrates the overall process of querying and analyzing portfolio data using the defined tools and prompts.

### `app/config.py`
Handles configuration settings and environment variables.

### `app/toolkit.py`
Defines the `PortfolioToolkit` class, which manages the tools used for data retrieval and analysis.

### `app/portfolio_agent/tools.py`
Contains the `SkillsData` tool that interacts with the Portfolio API to fetch and process skills data.

### `app/portfolio_agent/cleaning.py`
Provides functions to clean and format the retrieved portfolio data.

### `app/portfolio_agent/api_wrapper.py`
Implements the `PortfolioAPIWrapper` class to interact with the Portfolio API and retrieve data.

## Challenges and Solutions

- **Data Integration**: Integrating multiple data sources and ensuring consistency was challenging. We resolved this by implementing robust data cleaning and formatting functions.
- **API Interaction**: Ensuring reliable communication with the Portfolio API required careful handling of requests and responses.
- **Complex Prompt Handling**: Creating effective prompts for the language model involved fine-tuning and iterative testing to achieve accurate and relevant responses.

## Contributing

Contributions are welcome! Please submit issues or pull requests to improve the project.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
