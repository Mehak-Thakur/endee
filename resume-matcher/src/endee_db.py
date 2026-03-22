# Simulated Endee Vector Database Layer

class EndeeDB:
    def __init__(self):
        self.storage = []

    def insert(self, id, vector, metadata):
        self.storage.append({
            "id": id,
            "vector": vector,
            "metadata": metadata
        })

    def search(self):
        # Simulated retrieval
        return self.storage