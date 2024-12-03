from scanner import load_signatures, scan_directory
import hashlib

def main():
    # COMMENTED OUT DEBUGGING STUFF
    # content = "password"  # Expected content
    # calculated_hash = hashlib.sha256(content.encode()).hexdigest()
    # print("Calculated hash:", calculated_hash)

    # Expected hash for "password" (matches the signature database)
    # print("Expected hash:", "5f4dcc3b5aa765d61d8327deb882cf99")
    # Specify paths
    signature_file = "signatures.txt"
    directory_to_scan = "test_files"

    # Load signatures
    print("Loading malware signatures...")
    signatures = load_signatures(signature_file)

    if not signatures:
        print("No signatures loaded. Ensure signatures.txt exists and contains valid hashes.")
        return

    # Scan directory
    print(f"Scanning directory: {directory_to_scan}")
    scan_directory(directory_to_scan, signatures)

if __name__ == "__main__":
    main()
