from ragas import evaluate
from datasets import Dataset

# Load expert-curated ground truth data
test_data = Dataset.from_json("evaluation/test-sets/compliance_cases.json")

def evaluate_domain_accuracy(agent_outputs):
    # Specialized 2026 metrics for domain faithfulness
    result = evaluate(
        test_data,
        metrics=["faithfulness", "answer_relevancy", "context_precision"]
    )
    print(f"Domain Expertise Score: {result}")
  
