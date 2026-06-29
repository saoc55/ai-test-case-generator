import click
import sys
from pathlib import Path
from generator.pipeline import generate
from knowledge_base.ingest import ingest


@click.group()
def cli():
    """AI-powered test case generator using LangChain + Claude + RAG."""
    pass


@cli.command("generate")
@click.argument("feature")
@click.option("--format", "output_format", type=click.Choice(["bdd", "table"]), default="bdd", show_default=True)
@click.option("--output", "output_path", type=click.Path(), default=None, help="Save output to file instead of stdout")
@click.option("--model", default=None, help="LLM model override (default: from .env)")
def generate_cmd(feature, output_format, output_path, model):
    """Generate test cases from a FEATURE description."""
    if not feature.strip():
        click.echo("Error: feature description cannot be empty.", err=True)
        sys.exit(1)

    result = generate(feature, output_format=output_format, model=model)

    if output_path:
        Path(output_path).parent.mkdir(parents=True, exist_ok=True)
        Path(output_path).write_text(result, encoding="utf-8")
        click.echo(f"Test cases saved to {output_path}")
    else:
        click.echo(result)


@cli.command("ingest")
def ingest_cmd():
    """Seed the ChromaDB knowledge base from seed_data/."""
    ingest()


if __name__ == "__main__":
    cli()