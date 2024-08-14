import requests
from bs4 import BeautifulSoup
import json
import time
import logging
import os

# Configure logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# Base URL for the forum
base_url = 'https://discuss.pytorch.org'



# List of categories and their URLs
categories = [
    {"name": "Uncategorized", "url": "/c/uncategorized"},
    {"name": "vision", "url": "/c/vision"},
    {"name": "projects", "url": "/c/projects"},
    {"name": "autograd", "url": "/c/autograd"},
    {"name": "data", "url": "/c/data"},
    {"name": "reinforcement-learning", "url": "/c/reinforcement-learning"},
    {"name": "nlp", "url": "/c/nlp"},
    {"name": "distributed", "url": "/c/distributed"},
    {"name": "quantization", "url": "/c/quantization"},
    {"name": "deployment", "url": "/c/deployment"},
    {"name": "PyTorch Live", "url": "/c/pytorch-live"},
    {"name": "audio", "url": "/c/audio"},
    {"name": "windows", "url": "/c/windows"},
    {"name": "ExecuTorch", "url": "/c/executorch"},
    {"name": "mixed-precision", "url": "/c/mixed-precision"},
    {"name": "Memory Format", "url": "/c/memory-format"},
    {"name": "jit", "url": "/c/jit"},
    {"name": "Mobile", "url": "/c/mobile"},
    {"name": "FAQ", "url": "/c/faq"},
    {"name": "torch.package / torch::deploy", "url": "/c/torch-package-torch-deploy"},
    {"name": "Mac OS X", "url": "/c/mac-os-x"},
    {"name": "Opacus", "url": "/c/opacus"},
    {"name": "Captum", "url": "/c/captum"},
    {"name": "tensorboard", "url": "/c/tensorboard"},
    {"name": "jobs", "url": "/c/jobs"},
    {"name": "ignite", "url": "/c/ignite"},
    {"name": "glow", "url": "/c/glow"},
    {"name": "xla", "url": "/c/xla"},
    {"name": "Site Feedback", "url": "/c/site-feedback"},
    {"name": "hackathon", "url": "/c/hackathon"},
    {"name": "complex", "url": "/c/complex"},
    {"name": "torchx", "url": "/c/torchx"},
]

# Function to fetch and parse a topic page
def fetch_topic_data(topic_url):
    try:
        logging.debug(f"Fetching topic data from {topic_url}")
        topic_response = requests.get(topic_url)
        topic_response.raise_for_status()  # Raise an HTTPError for bad responses
        topic_soup = BeautifulSoup(topic_response.text, 'html.parser')
        
        # Extract the question
        question = topic_soup.find('div', class_='post').text.strip() if topic_soup.find('div', class_='post') else 'N/A'
        
        # Extract all answers
        answers = topic_soup.find_all('div', class_='post')
        all_answers = [answer.text.strip() for answer in answers[1:]]  # Skip the first post as it's the question
        
        # Concatenate all answers with '//' separator
        
        return {
            'question': question,
            'all_answers': all_answers
        }
    except requests.exceptions.RequestException as e:
        logging.error(f"Error fetching {topic_url}: {e}")
        return None

# Function to fetch topics from a specific category page
def fetch_category_topics(category_url):
    try:
        logging.debug(f"Fetching topics from category {category_url}")
        category_response = requests.get(base_url + category_url)
        category_response.raise_for_status()
        category_soup = BeautifulSoup(category_response.text, 'html.parser')
        topics = category_soup.find_all('a', class_='title raw-link raw-topic-link')
        return topics
    except requests.exceptions.RequestException as e:
        logging.error(f"Error fetching {category_url}: {e}")
        return []

# Main script to fetch data from all categories and topics
def main():
    # Initialize a list to store data
    data = []

    # Loop through each category and extract topics
    for category in categories:
        category_name = category["name"]
        category_url = category["url"]
        
        # Fetch topics in the category
        topics = fetch_category_topics(category_url)
        
        for topic in topics:
            topic_title = topic.text.strip()
            topic_path = topic['href']
            
            # Check if the topic_path is a full URL or a relative path
            if topic_path.startswith('http'):
                topic_url = topic_path
            else:
                topic_url = base_url + topic_path
            
            # Fetch and parse the topic data
            topic_data = fetch_topic_data(topic_url)
            
            if topic_data:
                # Store the extracted data in a dictionary
                topic_entry = {
                    'category': category_name,
                    'title': topic_title,
                    'question': topic_data['question'],
                    'all_answers': topic_data['all_answers']
                }
                
                # Append the dictionary to the data list
                data.append(topic_entry)
            
            # To avoid hitting the server too frequently
            time.sleep(1)

    # Save the extracted data to a JSON file
    with open('/Users/moutasemhome/Human-vs.-Synthetic-Datasets-Advancing-Niche-Model-Training-for-qa/data/forum_qas.json', 'w') as json_file:
        json.dump(data, json_file, indent=4)

    # Print the data to verify the output
    logging.info("Data extraction complete. Check the JSON file for results.")
    logging.debug(json.dumps(data, indent=4))

# Run the main script
if __name__ == '__main__':
    main()