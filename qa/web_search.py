from ddgs import DDGS

def search_web(query, max_results=3):

    results = []

    with DDGS() as ddgs:

        search_results = ddgs.text(query, max_results=max_results)

        for r in search_results:

            results.append(r["body"])

    return "\n".join(results)