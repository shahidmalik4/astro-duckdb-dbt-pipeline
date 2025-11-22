FROM astrocrpublic.azurecr.io/runtime:3.0-6

# Create a venv and install dbt-postgres inside it.
RUN python -m venv dbt_venv && \
    source dbt_venv/bin/activate && \
    pip install --no-cache-dir dbt-duckdb && \
    deactivate
