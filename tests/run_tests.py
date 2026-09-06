import os
import sys
import time
import unittest

# Ensure project root is in sys.path
ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if ROOT_DIR not in sys.path:
    sys.path.insert(0, ROOT_DIR)


def main():
    print("\n" + "=" * 75)
    print("      SANSKRIT MORPHOLOGICAL CLASSIFIER: AUTOMATED TEST SUITE")
    print("=" * 75 + "\n")

    loader = unittest.TestLoader()
    suite = loader.discover("tests", pattern="test_*.py")

    runner = unittest.TextTestRunner(verbosity=2)
    start_time = time.time()
    result = runner.run(suite)
    elapsed = time.time() - start_time

    print("\n" + "=" * 75)
    print("  MODULAR TEST EXECUTION SUMMARY:")
    print(f"  • Total Test Suites Run : {result.testsRun}")
    print(f"  • Total Passed          : {result.testsRun - len(result.failures) - len(result.errors)}")
    print(f"  • Failures              : {len(result.failures)}")
    print(f"  • Errors                : {len(result.errors)}")
    print(f"  • Total Execution Time  : {elapsed:.2f} seconds")
    print("=" * 75 + "\n")

    if not result.wasSuccessful():
        print("❌ Some regression tests failed! Check output above.\n")
        sys.exit(1)
    else:
        print("✅ All regression and unit test suites passed successfully!\n")


if __name__ == "__main__":
    main()
