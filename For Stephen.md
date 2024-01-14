# Goal
to write out what stephen will need in the next week to continue work on the SDK

## Auth
- GET /user/me


## Collections
### GET /collections/{cid}
```ts
interface Collection{
    name: string
    type: 'search'|'text'|'image'|''
    model?: 'instruct-xl' | 'openai-ada-v2'
    createdAt: string
    updatedAt: string
    wid: string
    id: string
}
```

### GET /collections
```ts
type output = Collection[]
```
```ts
ezllm.collections


```

## Documents
### GET /documents/{did}
```ts
interface Document {
    name: string
    type: 'pdf'|'transcript'|'image' // based off of this, generate a different Document class
    errorMessage?: string
    state: 'unprocessed'|'processing'|'active'|'error'
    createdAt: string
    updatedAt: string
    did: string
    cid: string
    wid: string
    id: string
}
```

```py
doc = Document("did")


col.documents

col.filter(page=1).get()


```

## Sub Documents
### GET /documents/{did}/subdocs
```ts 
interface subdoc {
    content: string
}

type output = subdoc[]
```


## Filter


```ts
interface Filter {
    collections: string[] // array of collection ids
    documents: string[] // array of document ids
    subdocs: string[] // array of subdoc ids
    metadata: {
        [metadata_key: string]: {
            eq?: (number|string)
            gte?: number
            lte?: number
            gt?: number
            lt?: number
            in: (number|string)[]
        }
    }
}

type input = Filter

interface output {
    docs: Document[]
}
```


```py
ezllm.filter(documents=["did"], page=1)

[
    Document("did") # subdocs would only be from page 1
]

# these two things are identical
doc = Document("did")
doc.filter(page=1).scan()

doc.filter(page=1).search("")

class Method:
    pass

class QA(Method):
    def json(self):
        return {
            "type" : "qa",
            ...
        }

class Action:
    def run(self, method):
        pass

    def get(self, method):
        pass

class Scan(Action):
    def run(self, method):
        # make the call, including the filter + method info
        body = {
            "method" : method.json(),
            "filter" : self.filter.json()
        }

        requests.post('/scan', body=body)

class ResponseDocument(Document):
    pass

class Response:
    def __init__(self, docs: List[ResponseDocument], output: T):
        self.docs = docs
        self.output = output
        # will also have to include info on token usage & cost

class ExtractionResponse(Response[ExtractionBody]):
    pass

class Filter(Action):
    def __init__(self, documents: List[Document], collections: List[Collection], ...):
        self.documents = documents
        self.collections = collections
    
    def get(self):
        requests.post(
            f'{self.client.url}/filter/{self.wid}',
            headers=self.client.headers,
            body=json.dumps(self.json())
        )

    def json(self):
        return {
            "collections" : [x.id for x in self.collections],
            "documents" : [x.id for x in self.documents],
            ...
        }

    def scan(self):
        return Scan(filter=self)
    
    def search(self):
        return Search(filter=self)


class Document:
    def filter(self, *args, **kwargs):
        return Filter(documents=[self], *args, **kwargs)

    def scan(self, *args, **kwargs):
        return self.filter().scan(*args, **kwargs)

    def search(self, *args, **kwargs):
        return self.filter().search(*args, **kwargs)

class Collection:
    def filter(self, *args, **kwargs):
        return Filter(collections=[self], *args, **kwargs)

    def scan(self, *args, **kwargs):
        return self.filter().scan(*args, **kwargs)

    def search(self, *args, **kwargs):
        return self.filter().search(*args, **kwargs)


# __init__.py
def filter(*args, **kwargs):
    return Filter(*args, **kwargs)

# SDK user

import ezllm

ezllm.filter(
    documents=[Document("did")]
)

from ezllm import Filter

f = Filter(
    documents=[Document("did")]
)


```

## Search
```ts
interface input {
    filter: Filter
    n: number // number of documents to include in search
}

interface output {
    docs: Document[]
}
```

## Scan
```ts
interface input {
    filter: Filter
}

interface output {
    docs: Document[]
}
```

## Methods
for actually running an LLM method you can make the following call


```ts

interface input {
    filter: Filter
    model: 'gpt-4' // LLM model to use
    method: {
        type: 'Extraction',
        data: any // ExtractionModelJSON
    }
    include_docs: boolean // whether to include docs in the output
}

interface output {
    docs?: Document[]
    output: any // could be JSON
}
```




# Defining Documents

```py
doc = Document("did")

doc.search("")


pdf_doc = PDFDocument("did")

pdf_doc.pages

transcript_doc = TranscriptDocument("did")

transcript_doc.duration


col.scan
doc.scan
ezllm.scan

Filter(documents=["did"])

```


# uploading
```py
ezllm.upload(file)

col.upload(file)
```


# Response
- be able to get the output of previous responses




# Calls

## 1. GET /filter 
- return the filtered documents 
```ts
interface input{
    filter: Filter
}
```

```py
class Filter:
    def search(self):
        return Search()
```

## 2. GET /search or GET /scan
- return the documents and relevant subdocuments from the search

```ts
interface SearchMetadata {
    query: string
    n: number
}
interface ScanMetadata {
    // TODO
}

interface input{
    filter: Filter
    retrieval: {
        type: 'search'|'scan',
        metadata: SearchMetadata|ScanMetadata
    }
}
```

```py
class Search:
    def run(self, method):
        output = method.run()
        return output
```

## 3. GET /run
```ts
interface input{
    filter: Filter
    retrieval: {
        type: 'search'|'scan',
        metadata: SearchMetadata|ScanMetadata

    },
    method: {
        type: 'extraction',
        metadata: {
            schema: JSON,
        }
    }
}
```

```py
class Method:
    pass

class ExtractionMethod:
    def run(self):
        # makes a call to the api with the above interface




class Action:
    # can't do this because it isn't strict enough on what methods can be run and when
    def __init__(self, filter, retrieval, method):
        pass

    def get(self):
        # makes the call to get the data based off of the filter / retrieval / method provided

    def search(self):
        pass

    def scan(self):
        pass

    def run(self):
        pass
```




# December 20th

```py

class DocGrouping:
    type: 'collection' | 'document' | 'all' = 'all'
    id: str # id of the resource grouped by
    docs: List[Document]

class Document:
    subdocs: List[Subdoc]

class Subdoc:
    content: string
    score: float


# 1. Filter
class Filter:
    def get() -> List[Document]:

# 2. Retrieval
class Search:
    def search() -> List[DocGrouping]:
        pass

# 3. Method
class RunOutput:
    docs: List[DocGrouping] = None # optional
    total_cost: float
    costs: List[Cost] # not too important to include in the SDK rn
    output: Any # different depending on the Method, could be a string, array, dict ... 

```
