# Brain Tumor Segmentation (Using Dataset)

This project performs brain tumor segmentation using the COCO dataset format. The repository includes scripts for generating segmentation masks and visualizing them.

## Project Structure
```
brain-tumor-segmentation(Using Dataset)/
│── data/
│   ├── train/  # Contains images
│   ├── train/masks/  # Output folder for masks
│   ├── _annotations.coco.json  # COCO annotations file
│── src/
│   ├── generate_masks.py  # Script to generate masks
│   ├── visualize_masks.py  # Script to overlay masks on images
│── requirements.txt  # Dependencies for the project
│── README.md  # Documentation for GitHub
│── .gitignore  # Ignore unnecessary files
```

## Setup Instructions

### 1. Install Git and Python
Ensure you have Git and Python installed. Check versions:
```sh
git --version
python --version
```

### 2. Clone the Repository
To get a local copy of this project, run:
```sh
git clone https://github.com/Anupam2090/brain-tumor-segmentation.git
cd brain-tumor-segmentation
```

### 3. Set Up a Virtual Environment (Recommended)
```sh
python -m venv venv
source venv/bin/activate  # On Mac/Linux
venv\Scripts\activate    # On Windows
```

### 4. Install Dependencies
```sh
pip install -r requirements.txt
```

### 5. Generate Tumor Segmentation Masks
```sh
python src/generate_masks.py
```

### 6. Visualize the Masks
```sh
python src/visualize_masks.py
```

## Uploading the Project to GitHub
### 1. Initialize Git Repository
```sh
git init
git add .
git commit -m "Initial commit"
```

### 2. Create a GitHub Repository
1. Go to [GitHub](https://github.com/) and create a new repository.
2. Copy the repository URL.

### 3. Link Local Repository to GitHub
```sh
git branch -M main
git remote add origin https://github.com/Anupam2090/brain-tumor-segmentation.git
git push -u origin main
```

## Running the Project in VS Code
1. Open VS Code and navigate to the project folder.
2. Open the terminal in VS Code (`Ctrl + ~`).
3. Activate the virtual environment.
4. Run the required scripts as mentioned above.

## Contributing
If you'd like to contribute, feel free to submit a pull request.

## License
This project is licensed under the MIT License.
