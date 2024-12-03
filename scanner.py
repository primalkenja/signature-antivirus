import os
import hashlib

def calculate_hash(filepath):
    """
    Calculate the SHA-256 hash of a file.
    :param filepath: Path to the file to hash.
    :return: The hexadecimal hash of the file.
    """
    sha256_hash = hashlib.sha256()
    try:
        with open(filepath, "rb") as f:
            for byte_block in iter(lambda: f.read(4096), b""):
                sha256_hash.update(byte_block)
        return sha256_hash.hexdigest()
    except Exception as e:
        print(f"Error reading file {filepath}: {e}")
        return None

def load_signatures(signature_file):
    """
    Load known malware signatures from a file.
    :param signature_file: Path to the signature file.
    :return: A list of malware signatures.
    """
    try:
        with open(signature_file, "r") as f:
            return [line.strip() for line in f if line.strip()]
    except Exception as e:
        print(f"Error loading signatures: {e}")
        return []

def scan_file(filepath, signatures):
    """
    Scan a single file for malware.
    :param filepath: Path to the file to scan.
    :param signatures: List of known malware signatures.
    :return: Boolean indicating if malware was found.
    """
    mod_filepath = filepath[:-4] + '.exe'
    file_hash = calculate_hash(filepath)
    # print(f"Debug: Calculated hash for {filepath}: {file_hash}")  # Debugging
    # print(f"Debug: Signature list: {signatures}")  # Debugging
    if file_hash in signatures:
        print(f"[ALERT] Malware detected in {mod_filepath}")
        return True
    else:
        print(f"[SAFE] {mod_filepath} is clean.")
        return False

def scan_directory(directory, signatures):
    """
    Scan all files in a directory for malware.
    :param directory: Path to the directory to scan.
    :param signatures: List of known malware signatures.
    """
    for root, _, files in os.walk(directory):
        for file in files:
            filepath = os.path.join(root, file)
            scan_file(filepath, signatures)
