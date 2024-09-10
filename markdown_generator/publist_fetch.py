from scholarly import scholarly
from scholarly import ProxyGenerator

# Create proxy session to prevent being blocked by google scholar
pg = ProxyGenerator()
pg.FreeProxies()
scholarly.use_proxy(pg)

# Enter your Google Scholar profile name 
# handle case where multiple author share a name
author_name = "Gongbo Sun"

# Search for the author
search_query = scholarly.search_author(author_name)
author = next(search_query)

# Fill in the details of the author, including publications
author = scholarly.fill(author)

# Create or open the bib file for writing
with open('proceedings.bib', 'w', encoding='utf-8') as bibfile:
    for publication in author['publications']:
        title = publication['bib']['title']
        result = scholarly.search_pubs(title)
        pub_details = next(result)
        print(pub_details)
        pub_bib = scholarly.bibtex(pub_details)
        try:
            bibfile.write(pub_bib + '\n')
        except:
            print("Error writing to bib file")

print("BibTeX entries saved to proceedings.bib")
