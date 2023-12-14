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
    documents: string[] // array of document ids
    subdocs: string[] // array of subdoc ids
    collections: string[] // array of collection ids
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

class Filter(Action):
    def scan(self):
        return Scan(filter=self)


class ResponseDocument(Document):
    pass

class Response:
    def __init__(self, docs: List[ResponseDocument], output: T):
        self.docs = docs
        self.output = output
        # will also have to include info on token usage & cost

class ExtractionResponse(Response[ExtractionBody]):
    pass
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