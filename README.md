
# Static Site Generator
# introduction.

This is a simple Python script for generating a static website from Markdown files. It takes a folder containing Markdown pages and produces a website with support for a homepage, articles, an about page, and error pages.

## Usage

1. Ensure you have Python installed on your system.
2. Install the required libraries using pip:
    ```
    pip install markdown
    ```
3. Clone or download this repository to your local machine.
    ```
    git clone git@github.com:christinamuthoni/pesapal.git
    cd pesapal

    ```
4. Place your Markdown files in the `input` folder. Each Markdown file will be converted to an HTML page.
5. Run the `generator.py` script to generate the website:
    ```
    python3 generator.py
    ```
   This will generate the HTML files in the `output` folder.
6. You can then host the generated HTML files using any web server or view them locally in your browser.

## Structure

- `generator.py`: The Python script responsible for generating the website.
- `input/`: Folder containing Markdown files.
- `output/`: Output folder for generated HTML files.
- `README.md`: Documentation file.

## Dependencies

- `markdown`: Library for converting Markdown to HTML.

## About Us

This static site generator is created with the aim of simplifying the process of creating static websites from Markdown content. It allows users to focus on content creation while automating the generation of HTML files.

We hope you find this tool useful for your projects. Feel free to contribute or provide feedback!

## Author.

This Project was contributed by: Christine Muriungi.

## License.

This project is licensed under the MIT License - see the LICENSE.md file for details.

