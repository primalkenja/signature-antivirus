import tkinter as tk
from tkinter import filedialog, messagebox
from scanner import load_signatures, scan_directory

class AntivirusApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Signature-based Antivirus")
        self.root.geometry("800x600")
        
        # Initialize variables
        self.signatures = []
        
        # Title Label
        tk.Label(root, text="Simple Antivirus", font=("Arial", 20)).pack(pady=10)
        
        # Buttons
        tk.Button(root, text="Load Signatures", command=self.load_signatures, width=20).pack(pady=5)
        tk.Button(root, text="Scan Directory", command=self.scan_directory, width=20).pack(pady=5)
        
        # Output Text Area
        self.text_area = tk.Text(root, height=25, width=100)
        self.text_area.pack(pady=10)
        self.text_area.insert(tk.END, "Status: Please load signatures to begin.\n")
    
    def load_signatures(self):
        """Load signatures from signatures.txt"""
        try:
            self.signatures = load_signatures("signatures.txt")
            if self.signatures:
                self.text_area.insert(tk.END, f"Loaded {len(self.signatures)} signatures.\n")
            else:
                self.text_area.insert(tk.END, "No signatures found in signatures.txt.\n")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load signatures: {e}")
    
    def scan_directory(self):
        """Scan a user-selected directory"""
        if not self.signatures:
            messagebox.showwarning("Warning", "Please load signatures before scanning.")
            return
        
        # Let the user select a directory
        directory = filedialog.askdirectory(title="Select Directory to Scan")
        if directory:
            self.text_area.insert(tk.END, f"Scanning directory: {directory}\n")
            self.text_area.update()
            
            # Redirect scan results to the text area
            def custom_scan_file(filepath, signatures):
                # Adapted scan_file to display results in the text area
                from scanner import calculate_hash
                if filepath.endswith('.txt'):
                    modified_filepath = filepath[:-4] + '.exe'
                else:
                    modified_filepath = filepath
                
                file_hash = calculate_hash(filepath)
                if file_hash in signatures:
                    self.text_area.insert(tk.END, f"[ALERT] Malware detected in {modified_filepath}\n")
                else:
                    self.text_area.insert(tk.END, f"[SAFE] {modified_filepath} is clean.\n")
            
            # Call the directory scan function with the custom scan logic
            from scanner import os
            for root, _, files in os.walk(directory):
                for file in files:
                    filepath = os.path.join(root, file)
                    custom_scan_file(filepath, self.signatures)

# Run the app
if __name__ == "__main__":
    root = tk.Tk()
    app = AntivirusApp(root)
    root.mainloop()
