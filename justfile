# build minified tailwind.css
build-css:
    # TODO: make this work without input.css
    npx @tailwindcss/cli -i ./input.css -o ./tailwind.css --minify

# generate PDF from HTML template using Docker
generate-pdf:
    docker build -t pdf-generator .
    docker run --rm -v "$(pwd)/output:/app/output" pdf-generator
    @echo "PDF generation complete! Check the output/ directory for your PDF file."
