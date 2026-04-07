from app.config import Config


def retrieve_context(vector_db, question):

    docs = vector_db.similarity_search(
        question,
        k=Config.TOP_K_RESULTS
    )

    context = "\n\n".join([d.page_content for d in docs])

    return context