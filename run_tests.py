import subprocess
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor, as_completed
import argparse
import os

# Define test files
current_dir = os.path.dirname(os.path.abspath(__file__))
test_cases_dir = os.path.join(current_dir, 'test_cases')
career_paths_dir = os.path.join(test_cases_dir, 'career_paths')
print(os.listdir('/Users/shharutyunyan/kube/heroco-qa-automation/heroco-qa-automation/test_cases/career_paths'))
test_files = [os.path.join(career_paths_dir, f) for f in os.listdir(career_paths_dir) if f.endswith('.py')]
print(test_files)
# Define the function to run a test
def run_test(test_file):
    try:
        result = subprocess.run(['python', test_file], capture_output=True, text=True, check=True)
        return f"Test {test_file} passed:\n{result.stdout}"
    except subprocess.CalledProcessError as e:
        return f"Test {test_file} failed with exit code {e.returncode}:\n{e.stderr}"

# Function to run tests concurrently using threads
def run_tests_with_threads(test_files, max_workers=4):
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        future_to_test = {executor.submit(run_test, test_file): test_file for test_file in test_files}
        for future in as_completed(future_to_test):
            test_file = future_to_test[future]
            try:
                result = future.result()
                print(result)
            except Exception as e:
                print(f"Test {test_file} generated an exception: {e}")

# Function to run tests concurrently using processes
def run_tests_with_processes(test_files, max_workers=4):
    with ProcessPoolExecutor(max_workers=max_workers) as executor:
        future_to_test = {executor.submit(run_test, test_file): test_file for test_file in test_files}
        for future in as_completed(future_to_test):
            test_file = future_to_test[future]
            try:
                result = future.result()
                print(result)
            except Exception as e:
                print(f"Test {test_file} generated an exception: {e}")

# Main function to handle argument parsing and execution
def main():
    parser = argparse.ArgumentParser(description="Run tests concurrently")
    parser.add_argument('--mode', choices=['threads', 'processes'], default='threads', help="Concurrency mode")
    parser.add_argument('--workers', type=int, default=4, help="Number of workers")
    args = parser.parse_args()

    if args.mode == 'threads':
        run_tests_with_threads(test_files, args.workers)
    elif args.mode == 'processes':
        run_tests_with_processes(test_files, args.workers) 
    print(f"Concurrency mode: {args.mode}")
    print(f"Number of workers: {args.workers}")

#run_tests_with_threads(test_files)
if __name__ == "__main__":
    main()