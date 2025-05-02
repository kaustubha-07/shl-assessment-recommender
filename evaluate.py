from recommend import recommend_assessments

def recall_at_k(preds, ground_truth, k=3):
    return len([p for p in preds[:k] if p['name'] in ground_truth]) / len(ground_truth)

def average_precision_at_k(preds, ground_truth, k=3):
    hits, score = 0, 0.0
    for i, pred in enumerate(preds[:k], 1):
        if pred['name'] in ground_truth:
            hits += 1
            score += hits / i
    return score / min(len(ground_truth), k)

def evaluate():
    benchmark = [
        ("I am hiring for Java developers who can also collaborate effectively with my business teams. Looking for an assessment(s) that can be completed in 40 minutes.",
         {"Automata - Fix (New)", "Core Java (Entry Level) (New)", "Core Java (Advanced Level) (New)", "Java 8 (New)", "Agile Software Development"})
        # Add more benchmark queries here...
    ]
    recalls, maps = [], []
    for query, ground in benchmark:
        preds = recommend_assessments(query)
        recalls.append(recall_at_k(preds, ground))
        maps.append(average_precision_at_k(preds, ground))
    print("Mean Recall@3:", sum(recalls)/len(recalls))
    print("MAP@3:", sum(maps)/len(maps))

if __name__ == "__main__":
    evaluate()