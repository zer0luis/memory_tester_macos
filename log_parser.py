import time

def parse_logs(file_path):
    print(f"[INFO] Starting analytics engine on {file_path}...")
    try:
        with open(file_path, 'r') as file:
            for line in file:
                # Simulating heavy parsing workload
                pass
        print("[INFO] Parsing complete.")
    except FileNotFoundError:
        print("[ERROR] Log file not found. Please generate test data first.")

if __name__ == "__main__":
    parse_logs("server_test.log")
