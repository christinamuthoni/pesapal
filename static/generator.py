import os
import markdown

def generate_index(output_dir):
    homepage_content = """
   "Welcome to Jaba site!

    We're thrilled to have you here on our platform. Feel free to explore and make 
    yourself at home as you discover the wonderful content we have to offer. Enjoy your visit!"
    """
    write_html_file(output_dir, "index.html", homepage_content)

def generate_articles(output_dir):
    articles = [
        {"title": "Article 1", 
        "content": "Unlocking Creativity: A Journey into the Art of Innovation"},

        {"title":"Article 2" , 
        "content": "The Quest for the Perfect Cup of Coffee: A Comedy of Caffeine"}
    ]
    for article in articles:
        article_content = f"# {article['title']}\n\n{article['content']}"
        write_html_file(output_dir, f"{article['title'].lower().replace(' ', '_')}.html", article_content)

def generate_about_page(output_dir):
    about_content = """
    About Us

    Welcome to Jaba site, where curiosity meets creativity, and inspiration knows no bounds. We're a passionate team of storytellers, 
    thinkers, and dreamers dedicated to bringing you engaging content that ignites your imagination and enriches your journey through life.

    Come curious, leave inspired. 
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
