# Wildlifeguard

**Wildlifeguard** is an AI-powered safety tool designed to detect animals encroaching on human habitats and deter them by playing repellent sounds. It enhances human–wildlife coexistence while ensuring safety for both parties.

> 🏆 Submitted to the CapeGemini's Tech for Positive future Competition and awarded a prize!

## Features

* **Real-time animal detection** using computer vision models
* **Automatic repellent sound playback** when animals are detected
* Configurable detection zones and sound profiles
* Lightweight and easy-to-run via Streamlit interface

## Getting Started

Follow these steps to set up the environment and run the application:

1. **Clone the repository**

   ```bash
   git clone https://github.com/yourusername/wildlifeguard.git
   cd wildlifeguard
   ```

2. **Create a Python virtual environment**

   ```bash
   python3 -m venv venv
   ```

3. **Activate the virtual environment**

   * On **Windows**:

     ```bash
     venv\Scripts\activate
     ```
   * On **Linux/macOS**:

     ```bash
     source venv/bin/activate
     ```

4. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

5. **Run the application**

   ```bash
   streamlit run './scripts/final.py'
   ```

## Usage

1. Point your camera toward the area you want to monitor.
2. The app will display the live feed and highlight detected animals.
3. Upon detection, a configurable repellent sound will play automatically.
4. Use the sidebar controls to adjust detection sensitivity and sound volume.

## Project Structure

```plaintext
wildlifeguard/
├── .dvc/                 # Data version control configurations
├── .streamlit/           # Streamlit app settings
├── config/               # Config files for detection thresholds and sound profiles
├── data/                 # Datasets, test media, and input data
├── demo/                 # Demonstration scripts and example outputs
├── logs/                 # Application and detection logs
├── notebooks/            # Jupyter notebooks for experiments and analysis
├── runs/                 # Model training and inference output (e.g., runs/detect)
│   └── detect/
├── scripts/              # Main Streamlit application and utility scripts
│   └── final.py          # Entry point to launch the app
├── sound/                # Repellent audio files
├── test/                 # Unit and integration tests
├── venv/                 # Python virtual environment (excluded from VCS)
├── .dvcignore            # Files/directories ignored by DVC
├── .gitignore            # Files/directories ignored by Git
├── requirements.txt      # Python dependencies
├── README.md             # Project documentation
├── "Frequencies affecting animals research papers ..."  # Research resources
├── "Research Papers"     # Additional literature
└── "articles regarding the animal intrusions"  # Related articles
```

```

## Configuration

- **Detection Model**: Replace or fine-tune models in `/models`
- **Sound Profiles**: Add or swap audio files in `/sounds`
- **Parameters**: Modify thresholds and settings in `scripts/final.py`

## Contributing

Contributions are welcome! Please open issues or submit pull requests for bug fixes, enhancements, or new features.

---

*Developed by Sameer*

```
