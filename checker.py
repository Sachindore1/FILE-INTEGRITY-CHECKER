import hashlib
import os

def calculate_hash(file_path):
    sha256 = hashlib.sha256()
    try:
        with open(file_path, 'rb') as f:
            while chunk := f.read(4096):
                sha256.update(chunk)
        return sha256.hexdigest()
    except FileNotFoundError:
        return None

def main():
    file_path = "test_files/sample.txt"

    # Step 1: Calculate initial hash
    original_hash = calculate_hash(file_path)
    if original_hash is None:
        print("❌ File not found!")
        return

    print(f"Original Hash: {original_hash}")

    # Step 2: Ask user to press Enter when ready to check again
    input("\n🔄 Modify the file (if you want) and press Enter to recheck...")

    new_hash = calculate_hash(file_path)
    print(f"New Hash: {new_hash}")

    if original_hash == new_hash:
        print("✅ File is intact.")
    else:
        print("⚠️ File has been modified!")

if __name__ == "__main__":
    main()
