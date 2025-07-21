# Extending AnalyticsAI

## How to Add Data Sources

- Edit `app/services/data_adapter.py` to add support for new databases or APIs.
- Use environment variables in `.env` for secure secrets/config.
- Example:
  ```python
  # Add new method to DataAdapter for Google Analytics
  def fetch_google_analytics(self, query_params):
      # Use settings.GOOGLE_ANALYTICS_API_KEY for auth
      pass
  ```

## How to Add LLM Providers

- Edit `app/agents/agent.py` and expand `get_llm()` with new providers (e.g., Gemini, Anthropic).
- Update `.env` and config for new provider API keys.

## How to Add Tools (Agent Skills)

- Add new `Tool` objects to the `tools` list in `agent.py`.
- Each tool can wrap a function that queries a source, analyzes data, or executes an action.

## How to Extend the Frontend

- Add new React components in `src/components`.
- Use the chat interface (`ChatInterface.tsx`) for natural language Q&A.
- Add visualizations to `DashboardSkeleton.tsx` (e.g., with Plotly or Chart.js).

## Documentation

- See `docs/agentic-ai-example.md` for agentic AI background.
- Use `docs/architecture.md` for system overview.
- Update this file (`extensibility.md`) as you add new features!