import os
import sys
from dotenv import load_dotenv
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from src.extractor import detect_architecture, extract_strings
from src.classifier import classify_strings
from src.reporter import generate_html_report
load_dotenv()
console = Console()

def main():
    console.print(Panel.fit(
        "[bold green]Static String Extractor & Classifier[/bold green]\n"
        "[bold blue]BGT210 Reverse Engineering Final Project[/bold blue]",
        title="[bold white]System Boot[/bold white]"
    ))

    target_path = os.getenv("TARGET_FILE_PATH")
    min_length = int(os.getenv("MIN_STRING_LENGTH", 4))
    entropy_thresh = float(os.getenv("ENTROPY_THRESHOLD", 4.5))
    output_dir = os.getenv("OUTPUT_DIR", "/app/reports")

    if not target_path or not os.path.exists(target_path):
        console.print("[bold red][!] Operational Failure: Target file could not be resolved.[/bold red]")
        sys.exit(1)

    console.print("[bold blue][*][/bold blue] Processing target file stream...")
    
    raw_strings, file_format, metadata = extract_strings(target_path, min_length)
    console.print(f"[bold yellow][+] Target Architecture Identified: {file_format}[/bold yellow]\n")
    
    classified_results = classify_strings(raw_strings, entropy_thresh)

    table = Table(title="Classification Summary Metrics", title_style="bold magenta")
    table.add_column("Category", style="cyan", justify="left")
    table.add_column("Detected Count", style="green", justify="right")

    for category, items in classified_results.items():
        if category != "General_Strings":
            table.add_row(category.replace("_", " "), str(len(items)))

    console.print(table)

    if classified_results["High_Risk_Alerts"]:
        console.print("\n[bold red][!!!] HIGH RISK ALERT LIST [!!!][/bold red]")
        for alert in classified_results["High_Risk_Alerts"]:
            console.print(f"[bold red]──► [Entropy: {alert['entropy']}] [/bold red][yellow]{alert['string']}[/yellow]")
    else:
        console.print("\n[bold green][+] No high-risk string anomalies detected.[/bold green]")

    report_file = save_report(classified_results, output_dir)
    html_report_file = save_html_report(classified_results, file_format, metadata, os.path.basename(target_path), output_dir)
    
    console.print(f"\n[bold green][+] Structured JSON report successfully exported to: [yaml]{report_file}[/yaml][/bold green]")
    console.print(f"[bold green][+] Visual HTML Dashboard successfully generated to: [cyan]{html_report_file}[/cyan][/bold green]")

if __name__ == "__main__":
    main()
