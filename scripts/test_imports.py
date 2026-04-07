import pkgutil
import langchain

print("langchain version", langchain.__version__)
print("modules:", [m[1] for m in pkgutil.iter_modules(langchain.__path__)])

for mod in ['langchain.text_splitter', 'langchain.text_splitters', 'langchain_text_splitters']:
    try:
        __import__(mod)
        print(mod, "import succeeded")
    except Exception as e:
        print(mod, "import failed", type(e), e)

for pkg in ['langchain.text_splitters', 'langchain_text_splitters']:
    try:
        from langchain.text_splitters import RecursiveCharacterTextSplitter
        print('text_splitters class import ok')
    except Exception as e:
        print('text_splitters class import failed', type(e), e)
    try:
        from langchain_text_splitters import RecursiveCharacterTextSplitter
        print('langchain_text_splitters class import ok')
    except Exception as e:
        print('langchain_text_splitters class import failed', type(e), e)
