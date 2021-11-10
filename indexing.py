import heapq

# indexing: token, priority queue of documents
indexes = {}

# calculates to document score
# NOTE: THIS IS TEMPORARY CODE, should include weights of the document itself
def calculate_doc_score(document):
    return ord(document[0])

# adds the document to the token index's priority queue
def add_index(token, document):
    # higher score means greater priority
    priority = calculate_doc_score(document) * -1

    # if the token doesn't exist, add the token in, initializing its priority queue
    if(not token in indexes):
        indexes[token] = []

    # adds the document into the respective token's priority queue
    heapq.heappush(indexes[token], (priority, document))

# prints the top n documents from the respective token
# SIDE EFFECT: it removes the top n documents as well
# BUG: doesn't check for if n > len(indexes[token])
def print_top_documents(token, n = 1):
    print("TOP " + str(n) + " DOCUMENTS IN TOKEN \"" + token + "\"")
    for i in range(n):
        print(heapq.heappop(indexes[token])[1])
    print()



# test functions
add_index("23","3document")
add_index("23","5document")
add_index("23","1document")
add_index("2","6document")
print_top_documents("2")
print_top_documents("23", 2)
print_top_documents("23")