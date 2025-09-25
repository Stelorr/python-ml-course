# test_learning_tracker.py
"""
Test file for learning_tracker.py functions
Run this file to test all functionality
"""

# Import your functions
from learning_tracker import learning_session, weekly_analyzer

def test_learning_session():
    """Test the learning_session function with various inputs"""
    print("=== Testing learning_session function ===")
    
    # Test 1: Valid input
    print("\n1. Testing valid input:")
    result = learning_session(2, "Python basics", 3, "Great session!")
    print(f"Result: {result}")
    
    # Test 2: Invalid hours (too high)
    print("\n2. Testing invalid hours (too high):")
    result = learning_session(10, "Too long", 3, "Should fail")
    print(f"Result: {result}")
    
    # Test 3: Invalid difficulty
    print("\n3. Testing invalid difficulty:")
    result = learning_session(1.5, "Valid topic", 7, "Should fail")
    print(f"Result: {result}")
    
    # Test 4: Default parameters
    print("\n4. Testing default parameters:")
    result = learning_session(1.0, "Quick study")
    print(f"Result: {result}")

def test_weekly_analyzer():
    """Test the weekly_analyzer function"""
    print("\n=== Testing weekly_analyzer function ===")
    
    # Create test data
    test_sessions = [
        {'hours': 1.5, 'topic': 'Python basics', 'difficulty': 2, 'notes': 'Good start'},
        {'hours': 2.0, 'topic': 'Functions', 'difficulty': 3, 'notes': 'Challenging'},
        {'hours': 1.0, 'topic': 'Python basics', 'difficulty': 2, 'notes': 'Review'},
        {'hours': 2.5, 'topic': 'Control flow', 'difficulty': 4, 'notes': 'Hard but useful'}
    ]
    
    result = weekly_analyzer(test_sessions)
    print(f"Weekly analysis: {result}")

def run_all_tests():
    """Run all test functions"""
    print("🧪 Running all tests for learning_tracker.py")
    print("=" * 50)
    
    test_learning_session()
    test_weekly_analyzer()
    
    print("\n✅ All tests completed!")

# Run tests when this file is executed directly
if __name__ == "__main__":
    run_all_tests()