import firecrawl # 2026 standard for high-fidelity web-to-markdown conversion

def crawl_and_index(url_list):
    crawler = firecrawl.FirecrawlApp(api_key=os.getenv("FIRECRAWL_KEY"))
    
    for url in url_list:
        # Convert domain site to LLM-ready Markdown
        markdown_content = crawler.scrape_url(url, params={'formats': ['markdown']})
        
        # Save to processed folder for RAG indexing
        filename = url.split("/")[-1] + ".md"
        with open(f"data/processed/{filename}", "w") as f:
            f.write(markdown_content)

if __name__ == "__main__":
    crawl_and_index(["official-regulation-site.gov"])
  
