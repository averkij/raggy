import json

from datasets import Dataset


#mocked dataset
def get_dataset():
    
    data = [{"caption": f"some caption ({i})", "text": f"some text with many words ({i})"} for i in range(100)]
    ds = Dataset.from_dict({
        "caption": [item["caption"] for item in data],
        "text": [item["text"] for item in data]
    })
    
    return ds