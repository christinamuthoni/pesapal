import os
import markdown

def generate_index(output_dir):
    homepage_content = """
    # Welcome to My Website!

    This is the homepage of my awesome website. Enjoy your stay!
    """
    write_html_file(output_dir, "index.html", homepage_content)

def generate_articles(output_dir):
    articles = [
        {"title": "Article 1", "content": "Content of Article 1"},
        {"title": "Article 2", "content": "Content of Article 2"}
    ]
    for article in articles:
        article_content = f"# {article['title']}\n\n{article['content']}"
        write_html_file(output_dir, f"{article['title'].lower().replace(' ', '_')}.html", article_content)

def generate_about_page(output_dir):
    about_content = """
    # About Us

    This is the about page of our website. We are a team dedicated to creating awesome content.
    """
    write_html_file(output_dir, "about.html", about_content)

def generate_error_pages(output_dir):
    error_404_content = """
    # 404 Error

    Page not found! Please go back to the homepage.
    """
    write_html_file(output_dir, "404.html", error_404_content)

def write_html_file(output_dir, file_name, content):
    os.makedirs(output_dir, exist_ok=True)  # Create the output directory if it doesn't exist
    with open(os.path.join(output_dir, file_name), 'w') as file:
        file.write(markdown.markdown(content))

def generate_site(output_dir):
    generate_index(output_dir)
    generate_articles(output_dir)
    generate_about_page(output_dir)
    generate_error_pages(output_dir)

if __name__ == "__main__":
    output_dir = "output"
    generate_site(output_dir)
