from sentence_transformers import SentenceTransformer, util
import json
import torch

model = SentenceTransformer('all-MiniLM-L6-v2')

with open("assessments.json", "r") as f:
    assessments = json.load(f)

descriptions = [f"{a['name']} {a.get('test_type', '')}" for a in assessments]
embeddings = model.encode(descriptions, convert_to_tensor=True)

def recommend_assessments(query, top_k=10):
    query_embedding = model.encode(query, convert_to_tensor=True)
    hits = util.semantic_search(query_embedding, embeddings, top_k=top_k)[0]
    return [assessments[hit['corpus_id']] for hit in hits]