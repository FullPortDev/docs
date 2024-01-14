```py
# 1. Filtering
class Filter:
    """
    gets the CollectionRetrievers, DocumentRetrievers 
    """


# 2. Retriever
class ResultDoc:
    page_content: str
    metadata: Any

class SearchResultDoc(ResultDoc)
    score: float

class Retriever:
    def __init__(self, filter):
        pass

    def search(self):
        for doc in self.filter.documents:
            # search this doc
            # return the 
        return List[SearchResultDoc]

    def scan(self):
        return List[ResultDoc]


    def get(self):
        """
        depending on the form.retriever.type, call either scan or search
        """

class DocumentRetriever(Retriever):
    ...

# 3. Method

class QAMethod:
    def __init__(self, form: QAMethodForm):
        pass

    def run(self, retriever):
        docs = retriever.get()

        # group the context blocks by the max llm context size


        # get questions
        questions = self.form.questions

        # call openai with the prompt / questions

        """
        docs = [
            Document(A)
            Document(B)
            Document(C)
        ]
        groups = [
            [
                Document(A)
                Document(B)
            ],
            [
                Document(C)
            ]
        ]
        outputs = []
        for group in groups:
            input_text = group.join('\n')
            output = call_llm(input_text + prompt_template)
            outputs.append(output)


        outputs = [
            "Document A and B talk about this ... ",
            "Document C talks about ... "
        ]

        # option 1: return a single string
        - using an LLM
        - check if the output is shrinking 
            - if it is, combine using LLM recursively
        - knn

        # option 2: 
        - provide aggregation capabilities
            - single answer
            - collection
            - document

        # option 3:
        - don't aggregate, simply return all of the answers joined together

        """


```