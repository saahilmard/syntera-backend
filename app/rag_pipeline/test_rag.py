from query_rag_context import get_relevant_context

def test_rag_query(query: str):
    print("\nQuery:", query)
    print("\nRelevant Context:")
    print("=" * 80)
    context = get_relevant_context(query)
    print(context)
    print("=" * 80)

if __name__ == "__main__":
    # Test queries
    test_queries = [
        "What are the key components of a well-child visit for a 2-year-old?",
        "What are common developmental milestones for a 30-month-old child?",
        "How should you document growth measurements in pediatric visits?"
    ]
    
    for query in test_queries:
        test_rag_query(query) 