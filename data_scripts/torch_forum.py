# import requests
# from bs4 import BeautifulSoup
# import json
# import time
# import logging
# import os

# # Configure logging
# logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# # Base URL for the forum
# base_url = 'https://discuss.pytorch.org'



# # List of categories and their URLs
# categories = [
#     {"name": "Uncategorized", "url": "/c/uncategorized"},
#     {"name": "vision", "url": "/c/vision"},
#     {"name": "projects", "url": "/c/projects"},
#     {"name": "autograd", "url": "/c/autograd"},
#     {"name": "data", "url": "/c/data"},
#     {"name": "reinforcement-learning", "url": "/c/reinforcement-learning"},
#     {"name": "nlp", "url": "/c/nlp"},
#     {"name": "distributed", "url": "/c/distributed"},
#     {"name": "quantization", "url": "/c/quantization"},
#     {"name": "deployment", "url": "/c/deployment"},
#     {"name": "PyTorch Live", "url": "/c/pytorch-live"},
#     {"name": "audio", "url": "/c/audio"},
#     {"name": "windows", "url": "/c/windows"},
#     {"name": "ExecuTorch", "url": "/c/executorch"},
#     {"name": "mixed-precision", "url": "/c/mixed-precision"},
#     {"name": "Memory Format", "url": "/c/memory-format"},
#     {"name": "jit", "url": "/c/jit"},
#     {"name": "Mobile", "url": "/c/mobile"},
#     {"name": "FAQ", "url": "/c/faq"},
#     {"name": "torch.package / torch::deploy", "url": "/c/torch-package-torch-deploy"},
#     {"name": "Mac OS X", "url": "/c/mac-os-x"},
#     {"name": "Opacus", "url": "/c/opacus"},
#     {"name": "Captum", "url": "/c/captum"},
#     {"name": "tensorboard", "url": "/c/tensorboard"},
#     {"name": "jobs", "url": "/c/jobs"},
#     {"name": "ignite", "url": "/c/ignite"},
#     {"name": "glow", "url": "/c/glow"},
#     {"name": "xla", "url": "/c/xla"},
#     {"name": "Site Feedback", "url": "/c/site-feedback"},
#     {"name": "hackathon", "url": "/c/hackathon"},
#     {"name": "complex", "url": "/c/complex"},
#     {"name": "torchx", "url": "/c/torchx"},
# ]

# # Function to fetch and parse a topic page
# def fetch_topic_data(topic_url):
#     try:
#         logging.debug(f"Fetching topic data from {topic_url}")
#         topic_response = requests.get(topic_url)
#         topic_response.raise_for_status()  # Raise an HTTPError for bad responses
#         topic_soup = BeautifulSoup(topic_response.text, 'html.parser')
        
#         # Extract the question
#         question = topic_soup.find('div', class_='post').text.strip() if topic_soup.find('div', class_='post') else 'N/A'
        
#         # Extract all answers
#         answers = topic_soup.find_all('div', class_='post')
#         all_answers = [answer.text.strip() for answer in answers[1:]]  # Skip the first post as it's the question
        
#         # Concatenate all answers with '//' separator
        
#         return {
#             'question': question,
#             'all_answers': all_answers
#         }
#     except requests.exceptions.RequestException as e:
#         logging.error(f"Error fetching {topic_url}: {e}")
#         return None

# # Function to fetch topics from a specific category page
# def fetch_category_topics(category_url):
#     try:
#         logging.debug(f"Fetching topics from category {category_url}")
#         category_response = requests.get(base_url + category_url)
#         category_response.raise_for_status()
#         category_soup = BeautifulSoup(category_response.text, 'html.parser')
#         topics = category_soup.find_all('a', class_='title raw-link raw-topic-link')
#         return topics
#     except requests.exceptions.RequestException as e:
#         logging.error(f"Error fetching {category_url}: {e}")
#         return []

# # Main script to fetch data from all categories and topics
# def main():
#     # Initialize a list to store data
#     data = []

#     # Loop through each category and extract topics
#     for category in categories:
#         category_name = category["name"]
#         category_url = category["url"]
        
#         # Fetch topics in the category
#         topics = fetch_category_topics(category_url)
        
#         for topic in topics:
#             topic_title = topic.text.strip()
#             topic_path = topic['href']
            
#             # Check if the topic_path is a full URL or a relative path
#             if topic_path.startswith('http'):
#                 topic_url = topic_path
#             else:
#                 topic_url = base_url + topic_path
            
#             # Fetch and parse the topic data
#             topic_data = fetch_topic_data(topic_url)
            
#             if topic_data:
#                 # Store the extracted data in a dictionary
#                 topic_entry = {
#                     'category': category_name,
#                     'title': topic_title,
#                     'question': topic_data['question'],
#                     'all_answers': topic_data['all_answers']
#                 }
                
#                 # Append the dictionary to the data list
#                 data.append(topic_entry)
            
#             # To avoid hitting the server too frequently in seconds
#             time.sleep(1)

#     # Save the extracted data to a JSON file
#     with open('/Users/moutasemhome/Human-vs.-Synthetic-Datasets-Advancing-Niche-Model-Training-for-qa/data/forum_qas.json', 'w') as json_file:
#         json.dump(data, json_file, indent=4)

#     # Print the data to verify the output
#     logging.info("Data extraction complete. Check the JSON file for results.")
#     logging.debug(json.dumps(data, indent=4))

# # Run the main script
# if __name__ == '__main__':
#     main()



### V2

# import requests
# from bs4 import BeautifulSoup
# import json
# import time
# import logging

# # Configure logging
# logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# # Base URL for the forum
# base_url = 'https://discuss.pytorch.org'

# # List of categories and their URLs
# categories = [
#     {"name": "Uncategorized", "url": "/c/uncategorized"},
#     {"name": "vision", "url": "/c/vision"},
#     {"name": "projects", "url": "/c/projects"},
#     {"name": "autograd", "url": "/c/autograd"},
#     {"name": "data", "url": "/c/data"},
#     {"name": "reinforcement-learning", "url": "/c/reinforcement-learning"},
#     {"name": "nlp", "url": "/c/nlp"},
#     {"name": "distributed", "url": "/c/distributed"},
#     {"name": "quantization", "url": "/c/quantization"},
#     {"name": "deployment", "url": "/c/deployment"},
#     {"name": "PyTorch Live", "url": "/c/pytorch-live"},
#     {"name": "audio", "url": "/c/audio"},
#     {"name": "windows", "url": "/c/windows"},
#     {"name": "ExecuTorch", "url": "/c/executorch"},
#     {"name": "mixed-precision", "url": "/c/mixed-precision"},
#     {"name": "Memory Format", "url": "/c/memory-format"},
#     {"name": "jit", "url": "/c/jit"},
#     {"name": "Mobile", "url": "/c/mobile"},
#     {"name": "FAQ", "url": "/c/faq"},
#     {"name": "torch.package / torch::deploy", "url": "/c/torch-package-torch-deploy"},
#     {"name": "Mac OS X", "url": "/c/mac-os-x"},
#     {"name": "Opacus", "url": "/c/opacus"},
#     {"name": "Captum", "url": "/c/captum"},
#     {"name": "tensorboard", "url": "/c/tensorboard"},
#     {"name": "jobs", "url": "/c/jobs"},
#     {"name": "ignite", "url": "/c/ignite"},
#     {"name": "glow", "url": "/c/glow"},
#     {"name": "xla", "url": "/c/xla"},
#     {"name": "Site Feedback", "url": "/c/site-feedback"},
#     {"name": "hackathon", "url": "/c/hackathon"},
#     {"name": "complex", "url": "/c/complex"},
#     {"name": "torchx", "url": "/c/torchx"},
# ]

# # Function to fetch and parse a topic page
# def fetch_topic_data(topic_url):
#     try:
#         logging.debug(f"Fetching topic data from {topic_url}")
#         topic_response = requests.get(topic_url)
#         topic_response.raise_for_status()  # Raise an HTTPError for bad responses
#         topic_soup = BeautifulSoup(topic_response.text, 'html.parser')
        
#         # Extract the question
#         question = topic_soup.find('div', class_='post').text.strip() if topic_soup.find('div', class_='post') else 'N/A'
        
#         # Extract all answers
#         answers = topic_soup.find_all('div', class_='post')
#         all_answers = [answer.text.strip() for answer in answers[1:]]  # Skip the first post as it's the question
        
#         return {
#             'question': question,
#             'all_answers': all_answers
#         }
#     except requests.exceptions.RequestException as e:
#         logging.error(f"Error fetching {topic_url}: {e}")
#         return None

# # Function to fetch topics from a specific category page
# def fetch_category_topics(category_url):
#     all_topics = []
#     page = 1
#     while True:
#         logging.debug(f"Fetching topics from category {category_url} page {page}")
#         category_response = requests.get(f'{base_url}{category_url}?page={page}')
#         if category_response.status_code != 200:
#             break  # Stop if no more pages or other error
#         category_soup = BeautifulSoup(category_response.text, 'html.parser')
#         topics = category_soup.find_all('a', class_='title raw-link raw-topic-link')
#         if not topics:
#             break  # Stop if no more topics
#         all_topics.extend(topics)
#         page += 1  # Move to the next page
#     return all_topics

# # Main script to fetch data from all categories and topics
# def main():
#     # Initialize a list to store data
#     data = []

#     # Loop through each category and extract topics
#     for category in categories:
#         category_name = category["name"]
#         category_url = category["url"]
        
#         # Fetch topics in the category
#         topics = fetch_category_topics(category_url)
        
#         for topic in topics:
#             topic_title = topic.text.strip()
#             topic_path = topic['href']
            
#             # Check if the topic_path is a full URL or a relative path
#             if topic_path.startswith('http'):
#                 topic_url = topic_path
#             else:
#                 topic_url = base_url + topic_path
            
#             # Fetch and parse the topic data
#             topic_data = fetch_topic_data(topic_url)
            
#             if topic_data:
#                 # Store the extracted data in a dictionary
#                 topic_entry = {
#                     'category': category_name,
#                     'title': topic_title,
#                     'question': topic_data['question'],
#                     'all_answers': topic_data['all_answers']
#                 }
                
#                 # Append the dictionary to the data list
#                 data.append(topic_entry)
            
#             # To avoid hitting the server too frequently
#             #time.sleep(0.2)

#     # Save the extracted data to a JSON file
#     with open('/Users/moutasemhome/Human-vs.-Synthetic-Datasets-Advancing-Niche-Model-Training-for-qa/data/forum_qas_v3.json', 'w') as json_file:
#         json.dump(data, json_file, indent=4)

#     # Print the data to verify the output
#     logging.info("Data extraction complete. Check the JSON file for results.")
#     logging.debug(json.dumps(data, indent=4))

# # Run the main script
# if __name__ == '__main__':
#     main()




### V3

import requests
from bs4 import BeautifulSoup
import json
import logging
import time
import random
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

# Function to load progress from a checkpoint file
def load_progress(file_path):
    if os.path.exists(file_path):
        with open(file_path, 'r') as f:
            return json.load(f)
    return {'category': None, 'page': 1}

# Function to save progress to a checkpoint file
def save_progress(file_path, category, page):
    progress = {'category': category, 'page': page}
    with open(file_path, 'w') as f:
        json.dump(progress, f)

# Function to fetch and parse a topic page
def fetch_topic_data(topic_url):
    try:
        logging.debug(f"Fetching topic data from {topic_url}")
        response = requests.get(topic_url, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        
        question_post = soup.find('div', class_='post')
        question = question_post.text.strip() if question_post else 'N/A'
        
        answers = soup.find_all('div', class_='post')
        all_answers = [answer.text.strip() for answer in answers[1:]]
        
        logging.debug(f"Fetched topic data from {topic_url}")
        return {
            'question': question,
            'all_answers': all_answers
        }
    except requests.exceptions.RequestException as e:
        logging.error(f"Error fetching {topic_url}: {e}")
    return None

# Function to fetch topics from a specific category page
def fetch_category_topics(category_url, page):
    logging.debug(f"Fetching topics from category {category_url} page {page}")
    try:
        response = requests.get(f'{base_url}{category_url}?page={page}', timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        topics = soup.find_all('a', class_='title raw-link raw-topic-link')
        if not topics:
            logging.info(f"No more topics found in category {category_url} at page {page}")
            return None
        return topics
    except requests.exceptions.RequestException as e:
        logging.error(f"Error fetching page {page} of {category_url}: {e}")
    return None

# Main script to fetch data from all categories and topics
def main():
    checkpoint_file = 'progress_checkpoint_append.json'
    data_file = '/Users/moutasemhome/Human-vs.-Synthetic-Datasets-Advancing-Niche-Model-Training-for-qa/data/forum_qas_v3_append.json'
    progress = load_progress(checkpoint_file)

    for category in categories:
        category_name = category["name"]
        category_url = category["url"]
        start_page = progress['page'] if progress['category'] == category_name else 1

        page = start_page
        while True:  # Continue fetching until no more topics are found
            topics = fetch_category_topics(category_url, page)
            if topics is None:
                logging.info(f"No more topics found in category {category_name} at page {page}")
                break

            topic_urls = [base_url + topic['href'] if not topic['href'].startswith('http') else topic['href'] for topic in topics]
            for topic_url in topic_urls:
                topic_data = fetch_topic_data(topic_url)
                if topic_data:
                    topic_entry = {
                        'category': category_name,
                        'title': topic_url,  # Assuming title is in the URL path as the unique identifier
                        'question': topic_data['question'],
                        'all_answers': topic_data['all_answers']
                    }
                    with open(data_file, 'a') as json_file:
                        json.dump(topic_entry, json_file)
                        json_file.write("\n")

            # Save progress after processing the page
            save_progress(checkpoint_file, category_name, page)
            page += 1  # Move to the next page

    logging.info(f"Data extraction complete.")

if __name__ == '__main__':
    main()
