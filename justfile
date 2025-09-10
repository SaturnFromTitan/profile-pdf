set fallback := true
set shell := ["bash", "-c"]

# remove files created by tooling and packaging
@clean:
  rm -rf output
  rm -rf dist
  rm -rf deps
  rm -rf build
  rm -rf **/*.egg-info
  rm -rf .eggs
  rm -rf .pytest_cache
  rm -rf **/*/__pycache__
  rm -rf **/__pycache__
  rm -rf .mypy_cache
  rm -rf **/.mypy_cache
  rm -rf .ruff_cache
  rm -rf **/.ruff_cache
  rm -rf htmlcov
  rm -f docker/requirements.txt
  rm -f .coverage
  rm -f .coverage.xml
  rm -f .junit.xml

# run pre-commit linters on all files
@lint:
  uv run pre-commit run --all-files

# run python tests
@test *ARGS:
  uv run pytest {{ ARGS }}

# generate PDF from HTML template using Docker
@generate-pdf OPEN='1':
  docker build -t pdf-generator .
  docker run --rm -v "$(pwd)/public:/app/public" pdf-generator
  @echo "PDF generation complete! Check the public/ directory for your PDF file."
  if [ "{{OPEN}}" = "1" ]; then just open; fi

# open the generated PDF
@open:
  open public/profile.pdf
