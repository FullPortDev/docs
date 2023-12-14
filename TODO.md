## TODO SDK DESIGN - December 12th 2023
- [ ] logging
- [ ] combining upload and processing
- [ ] Batch Operations
- [ ] explain pydantic extraction better
- [ ] get doc content
- [ ] sub-doc, subdocument, sub document ... 
- [ ] specify which LLM model to run with
- [ ] pulling historical runs data

### How do images / Image Collections work?
- should they work identically?
  - may screw up searching

# Documentation TODO Nov 28th 2023
- [ ] authentication
- [ ] async vs sync interface
- [ ] improve the FastAPI openapi documentation to be able to auto-import it
- [ ] about section
- [ ] quick start

## 
- [ ] upload
- [ ] supported file types
- [ ] storage
  - [ ] embedding
  - [ ] ttl
  - [ ] plain text
  - [ ] markdown
- [ ] retrieval
  - [ ] scan
  - [ ] search
- [ ] LLM Methods
  - [ ] Extraction
  - [ ] Q&A
  - [ ] Summarization
- [ ] Streaming
- [ ] Agents


# Document Types
## PDF
## HTML
## txt
## Markdown
## Image


# Sub Doc Slicing 

```py
table_document = await doc.subdocs.find_one(page=1, type="table")

# gets the context previous to the table document
# as this free text may be useful in deducing information of the table
docs = [
  ...doc.subdocs[table_document.index - 3: table_document.index - 1],
  table_document
]

ezllm.scan(docs).run(QA(["Who was the invoice for?", "What was the invoices payment terms?"]))


```


# Examples
## Search
- embedded search
- image search
- Q&A

## Scan
- classification
- image classification
- extraction
- summarization

- brail code translator for brail keyboards
  - perhaps even use it to parse relevant information from a website and be able to display it to the user

# Use Cases
- [ ] frame by frame comparison
- [ ] image
  - [ ] e-commerce (and all its varients) image classification questions
    - [ ] fashion
    - [ ] electronics
    - [ ] robotic object classification
  - [ ] text generation
    - [ ] sports journalism
    - [ ] 
    - [ ] 
- [ ] web scraping
- [ ] token contract analyzer for eth
- [ ] table extraction
- [ ] pauls vision stuff
- [ ] fashion categorization



# Pauls Notes - December 6th 2023
## introduction
- the use cases are a little too much at once
  - perhaps simplify the snippets and link to full code snippets elsewhere
  - showcase the tools not individual use cases
- tools
- rather than go directly into use cases
- only show one line

1. documentation needs to read linearly
2. goal section is good, but jumped straight into actions - but should have taught objects and then taught actions
3. explain what type of documents you can work with


## Quick Start
- describe the Collection and Document before the upload / actions

## uses Cases
- organize use cases into hierarchy
  - Image
  - Semantic Search

## Organization
- organize it into document pre
- and run

## Steps
1. upload
2. parsing
3. storage
4. retrieval
5. aggregation
6. method




# Stephens Notes - December 7th 2023

- a collection is
- What is the return of -> related_documents = c.search("User Query")
  - Is it the documents uploaded'
  - Is it the response of the LLM from the search
  - Am I searching upon all files or just one, or the ones just uploaded?
- Provide examples of outputs after code
- explain pydantic, explain the descriptions, separate the inline comments into a heading



## Quick Start
- explain score




## Thoughts on Aggregation
- no need to right now as you can achieve this with separate calls in a for loop
- lower priority