set fallback := true
set shell := ["bash", "-c"]

@clean:
  rm -rf dist
  rm -rf deps
  rm -rf build
  rm -rf **/*.egg-info
  rm -rf .eggs
  rm -rf .pytest_cache
  rm -rf **/*/__pycache__
  rm -rf **/__pycache__
  rm -rf **/.mypy_cache
  rm -rf htmlcov
  rm -f docker/requirements.txt
  rm -f .coverage
  rm -f .coverage.xml
  rm -f .junit.xml

# run pre-commit linters on all files
@lint:
  uv run pre-commit run --all-files

@test *ARGS:
  uv run pytest {{ ARGS }}

# build minified tailwind.css
build-css:
    # TODO: make this work without input.css
    npx @tailwindcss/cli -i ./input.css -o ./tailwind.css --minify

# generate PDF from HTML template using Docker
generate-pdf:
    docker build -t pdf-generator .
    docker run --rm -v "$(pwd)/output:/app/output" pdf-generator
    @echo "PDF generation complete! Check the output/ directory for your PDF file."
