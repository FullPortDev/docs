# Collection

## Collection
The default collection saves the parsed documents as plain text.

## Search Collection
Search Collections save each sub document in a vector database for semantic search, enabling semantic search on the documents within the collection.


## Data Collection (WIP)
Is used for tabular data. Data Collections provide different methods leveraging the LLM to generate queries on your data.



- ttl=1
- type
- model




# SubDocs
## Retrieving a Sub Document Directly
```py
subdoc = SubDocument("id")
```

# I WOULD LIKE
- ttl
- to be able to filter by metadata as easily as 
```py
filter(page=1)
#instead of 
filter(metadata={'page' : 1})
```



# Filter
## Filter Between Metadata Values
```py
documents = await doc.filter(page=(1, 5))
```

### Range
alternatively if you want to specify inclusive / exclusive constaints you can use
```py
from ezllm import Filter

await doc.filter(page=Filter(gt=1, lte=5))
# can't do this cause in is protected keyword
# await doc.filter(page=Filter(in=[1, 3, 5]))


# or

from ezllm import Range, In

await doc.filter(page=Range(gt=1, lte=5))
await doc.filter(page=In([1, 3, 5]))

```

## 

## Advanced Filtering Methods
```py
table_document = await doc.filter(page=1, type="table").first()

# gets the context previous to the table document
# as this free text may be useful in deducing information of the table
docs = [
  ...doc.subdocs[table_document.index - 3: table_document.index - 1],
  table_document
]

ezllm.scan(docs).run(QA(["Who was the invoice for?", "What was the invoices payment terms?"]))
```




# Use Cases
## QA
```py
from ezllm import Document, Collection
from ezllm.methods import QA

# QA The Entirety of an Individual Document
doc = Document("doc_id")
doc.scan().run(QA("User Query"))


# QA Semantically Similar Context of an Individual Document
doc.search("User Query").run(QA())


# Collection of Documents
col = Collection("Collection Name")
collection.search("User Question").run(QA())


# A List Of Documents
doc1 = Document("doc1")
doc2 = Document("doc2")
ezllm.search([doc1, doc2], "User Query").run(QA())


# Specific Sub Document
table_sub_doc = doc.subdocs.filter(page=1, type='table')
ezllm.scan(table_sub_doc).run(QA("User Query"))


# A Slice of Sub Documents
subdocs = doc.subdocs[0:10]
ezllm.scan(subdocs).run(QA("User Query"))
```