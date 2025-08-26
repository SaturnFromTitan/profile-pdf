#!/usr/bin/env python3
"""
Script to generate PDF from HTML template using WeasyPrint
"""

import os
import pathlib
import sys
from typing import Union
from pathlib import Path
from weasyprint import HTML, CSS
from weasyprint.text.fonts import FontConfiguration

PACKAGE_DIR = pathlib.Path(__file__).parent
TEMPLATES_DIR = PACKAGE_DIR / "templates"
STYLES_DIR = PACKAGE_DIR / "styles"
REPO_ROOT = PACKAGE_DIR.parent.parent
OUTPUT_DIR = REPO_ROOT / "output"

def generate_pdf(html_file: Union[str, Path], css_file: Union[str, Path], output_file: Union[str, Path]) -> bool:
    """Generate PDF from HTML and CSS files"""
    try:
        # Read HTML file
        with open(html_file, 'r', encoding='utf-8') as f:
            html_content = f.read()
        
        # Read CSS file
        with open(css_file, 'r', encoding='utf-8') as f:
            css_content = f.read()
        
        # Configure fonts
        font_config = FontConfiguration()
        
        # Create HTML object
        html_doc = HTML(string=html_content, base_url=os.getcwd())
        
        # Create CSS object
        css_doc = CSS(string=css_content, font_config=font_config)
        
        # Generate PDF
        print(f"Generating PDF from {html_file}...")
        html_doc.write_pdf(output_file, stylesheets=[css_doc], font_config=font_config)
        
        print(f"PDF generated successfully: {output_file}")
        return True
        
    except Exception as e:
        print(f"Error generating PDF: {e}", file=sys.stderr)
        return False

def main() -> None:
    """Main function"""
    # File paths
    html_file = TEMPLATES_DIR / "template.html"
    css_file = STYLES_DIR / "tailwind.css"
    output_file = OUTPUT_DIR / "profile.pdf"
    
    # Check if input files exist
    if not os.path.exists(html_file):
        print(f"Error: HTML file '{html_file}' not found", file=sys.stderr)
        sys.exit(1)
    
    if not os.path.exists(css_file):
        print(f"Error: CSS file '{css_file}' not found", file=sys.stderr)
        sys.exit(1)
    
    # Create output directory if it doesn't exist
    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    
    # Generate PDF
    success = generate_pdf(html_file, css_file, output_file)
    
    if success:
        print(f"PDF saved to: {output_file}")
        sys.exit(0)
    else:
        print("Failed to generate PDF", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
